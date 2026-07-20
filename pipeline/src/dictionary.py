"""Gerador semi-automático do dicionário de dados das 251 colunas da planilha bruta.

Os nomes de coluna seguem um padrão decodificável:
  `SeçãoNome__NNTextoDaPergunta[respostaMúltipla|respostaÚnica]`
  `_NNaMM__NNTextoDaPergunta` (blocos condicionais por tipo de empreendimento)
  `Prefixo_Campo` (sem número de pergunta — subcampos estruturados, ex. endereço)

Este módulo faz o melhor esforço automático e deixa ganchos explícitos
(`dictionary_overrides.yaml`) para correções pontuais revisadas à mão — não tenta
adivinhar com perfeição as ~251 colunas.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

import pandas as pd
import yaml

REFERENCE_DATA_DIR = Path(__file__).resolve().parent.parent / "reference_data"

_SEM_TITULO_RE = re.compile(r"^_SemTítulo(\d*)")
_QNUM_RE = re.compile(r"^(\d+)([a-z])?(.*)$", re.DOTALL)
_PASCAL_SPLIT_RE = re.compile(r"(?<=[a-zà-öø-ÿ0-9])(?=[A-ZÀ-Ö])")

_TYPE_SUFFIX_RULES: list[tuple[str, str]] = [
    ("respostaMúltipla", "multi_select"),
    ("respostaÚnica", "single_select"),
]


@dataclass
class ColumnMeta:
    coluna_bruta: str
    prefixo: Optional[str]
    secao_label: Optional[str]
    ordem_secao: Optional[int]
    subgrupos: list[str]
    numero_pergunta: Optional[str]
    campo_texto: str
    rotulo: str
    tipo_inferido: str
    pii: bool
    valores_amostra: list[Any] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        d = {
            "coluna_bruta": self.coluna_bruta,
            "prefixo": self.prefixo,
            "secao_label": self.secao_label,
            "ordem_secao": self.ordem_secao,
            "subgrupos": self.subgrupos,
            "numero_pergunta": self.numero_pergunta,
            "rotulo": self.rotulo,
            "tipo_inferido": self.tipo_inferido,
            "pii": self.pii,
            "valores_amostra": self.valores_amostra,
        }
        return d


def _load_section_labels(reference_dir: Path) -> dict[str, dict[str, Any]]:
    return yaml.safe_load((reference_dir / "section_labels.yaml").read_text(encoding="utf-8")) or {}


def _load_pii_columns(reference_dir: Path) -> set[str]:
    raw = yaml.safe_load((reference_dir / "pii_columns.yaml").read_text(encoding="utf-8")) or []
    return {item["coluna"] for item in raw}


def _load_overrides(reference_dir: Path) -> dict[str, dict[str, Any]]:
    return yaml.safe_load((reference_dir / "dictionary_overrides.yaml").read_text(encoding="utf-8")) or {}


def _split_pascal_case(text: str) -> str:
    spaced = _PASCAL_SPLIT_RE.sub(" ", text)
    return spaced.strip()


def _infer_type(campo_texto: str, sample_values: list[Any]) -> str:
    for suffix, tipo in _TYPE_SUFFIX_RULES:
        if campo_texto.endswith(suffix):
            return tipo
    lowered = campo_texto.lower()
    if "quantas" in lowered or "quantos" in lowered or lowered.startswith("quantidade"):
        return "integer"
    if "valormédio" in lowered.replace(" ", "") or "valor" in lowered:
        return "numeric_or_text"
    if campo_texto.endswith("Qual"):
        return "conditional_text"

    non_null = [v for v in sample_values if v is not None and v == v]  # filtra NaN
    if non_null:
        as_str = {str(v).strip() for v in non_null}
        if as_str <= {"Sim", "Não"}:
            return "boolean"
        has_commas_multiple_tokens = any("," in str(v) for v in non_null)
        if has_commas_multiple_tokens:
            return "multi_select"
        if all(isinstance(v, (int, float)) for v in non_null):
            return "numeric"
    return "text"


def parse_column_name(
    name: str, section_labels: dict[str, dict[str, Any]]
) -> tuple[Optional[str], Optional[dict], list[str], Optional[str], str]:
    """Decompõe um nome de coluna bruto.

    Retorna (prefixo, meta_da_secao, subgrupos, numero_pergunta, campo_texto_restante).
    """
    remaining = name
    prefix = None
    section_meta = None
    for candidate in sorted(section_labels.keys(), key=len, reverse=True):
        if remaining.startswith(candidate):
            prefix = candidate
            section_meta = section_labels[candidate]
            remaining = remaining[len(candidate):]
            break

    subgroups: list[str] = []
    while True:
        m = _SEM_TITULO_RE.match(remaining)
        if not m:
            break
        subgroups.append("SemTítulo" + m.group(1))
        remaining = remaining[m.end():]

    qnum = None
    if remaining.startswith("__"):
        rest = remaining[2:]
        m = _QNUM_RE.match(rest)
        if m:
            qnum = m.group(1) + (m.group(2) or "")
            remaining = m.group(3)
        else:
            remaining = rest
    elif remaining.startswith("_"):
        remaining = remaining[1:]

    return prefix, section_meta, subgroups, qnum, remaining


def build_dictionary(
    columns: list[str],
    sample_frame: Optional[pd.DataFrame] = None,
    reference_dir: Path = REFERENCE_DATA_DIR,
) -> list[ColumnMeta]:
    section_labels = _load_section_labels(reference_dir)
    pii_columns = _load_pii_columns(reference_dir)
    overrides = _load_overrides(reference_dir)

    entries: list[ColumnMeta] = []
    for name in columns:
        prefix, section_meta, subgroups, qnum, campo_texto = parse_column_name(name, section_labels)
        rotulo = _split_pascal_case(campo_texto) or _split_pascal_case(name)

        sample_values: list[Any] = []
        if sample_frame is not None and name in sample_frame.columns:
            sample_values = sample_frame[name].dropna().unique().tolist()[:8]

        tipo = _infer_type(campo_texto, sample_values)

        meta = ColumnMeta(
            coluna_bruta=name,
            prefixo=prefix,
            secao_label=(section_meta or {}).get("label") if section_meta else None,
            ordem_secao=(section_meta or {}).get("ordem") if section_meta else None,
            subgrupos=subgroups,
            numero_pergunta=qnum,
            campo_texto=campo_texto,
            rotulo=rotulo,
            tipo_inferido=tipo,
            pii=name in pii_columns,
        )
        meta.valores_amostra = [str(v) for v in sample_values]

        if name in overrides:
            for key, value in overrides[name].items():
                setattr(meta, key, value)

        entries.append(meta)
    return entries


def render_markdown(entries: list[ColumnMeta]) -> str:
    lines = [
        "# Dicionário de Dados — Pesquisa Economia Solidária",
        "",
        "Gerado automaticamente por `pipeline/src/dictionary.py`. Correções pontuais devem ir "
        "em `pipeline/reference_data/dictionary_overrides.yaml`, não direto neste arquivo "
        "(ele é sobrescrito a cada geração).",
        "",
    ]
    by_section: dict[Optional[str], list[ColumnMeta]] = {}
    for e in entries:
        by_section.setdefault(e.secao_label, []).append(e)

    def sort_key(label: Optional[str]) -> int:
        for e in entries:
            if e.secao_label == label and e.ordem_secao is not None:
                return e.ordem_secao
        return 999

    for label in sorted(by_section.keys(), key=sort_key):
        lines.append(f"## {label or '(sem seção — metadados/estrutura)'}")
        lines.append("")
        lines.append("| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |")
        lines.append("|---|---|---|---|---|")
        for e in by_section[label]:
            pii_flag = "⚠️ SIM" if e.pii else ""
            lines.append(
                f"| `{e.coluna_bruta}` | {e.numero_pergunta or ''} | {e.rotulo} | "
                f"{e.tipo_inferido} | {pii_flag} |"
            )
        lines.append("")
    return "\n".join(lines)
