"""Funções puras de limpeza/normalização usadas pelo pipeline.

Cada função aqui resolve um problema real encontrado na planilha
"Respostas - Pesquisa Economia Solidária - 23_02_2026.xlsx" (ver docs/decisoes_e_riscos.md
e o plano de implementação). Mantidas isoladas de I/O para serem fáceis de testar.
"""
from __future__ import annotations

import csv
import io
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml

REFERENCE_DATA_DIR = Path(__file__).resolve().parent.parent / "reference_data"


# ---------------------------------------------------------------------------
# Múltipla escolha
# ---------------------------------------------------------------------------

def parse_multiselect(raw: Optional[str]) -> list[str]:
    """Separa uma célula de resposta múltipla em uma lista de opções.

    As respostas são concatenadas por vírgula, mas pelo menos uma opção do
    questionário ("Poupança, crédito ou finanças solidárias") contém uma
    vírgula dentro do próprio texto e vem entre aspas — um `str.split(',')`
    ingênuo quebraria essa opção em duas. `csv.reader` já resolve isso
    corretamente pois respeita aspas.
    """
    if raw is None:
        return []
    text = str(raw).strip()
    if not text:
        return []
    reader = csv.reader(io.StringIO(text), skipinitialspace=True)
    row = next(reader, [])
    return [item.strip() for item in row if item.strip()]


# ---------------------------------------------------------------------------
# Município / Estado
# ---------------------------------------------------------------------------

def _fold(value: str) -> str:
    """Remove acentos, baixa a caixa, colapsa espaços — chave de comparação."""
    decomposed = unicodedata.normalize("NFKD", value)
    without_accents = "".join(c for c in decomposed if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", without_accents.strip().lower())


@dataclass(frozen=True)
class MunicipioLookup:
    canonical_by_fold: dict[str, str]
    aliases: dict[str, str]

    @classmethod
    def load(cls, reference_dir: Path = REFERENCE_DATA_DIR) -> "MunicipioLookup":
        import pandas as pd

        municipios_csv = pd.read_csv(reference_dir / "municipios_alto_vale.csv")
        canonical_by_fold = {
            _fold(nome): nome for nome in municipios_csv["municipio_canonico"]
        }
        aliases_path = reference_dir / "aliases_geograficos.yaml"
        aliases_raw = yaml.safe_load(aliases_path.read_text(encoding="utf-8")) or {}
        return cls(canonical_by_fold=canonical_by_fold, aliases=aliases_raw.get("municipio", {}))

    def normalize(self, raw: Optional[str]) -> str:
        if raw is None or not str(raw).strip():
            raise ValueError("Município em branco não pode ser normalizado")
        folded = _fold(str(raw))
        if folded in self.aliases:
            return self.aliases[folded]
        if folded in self.canonical_by_fold:
            return self.canonical_by_fold[folded]
        raise ValueError(
            f"Município {raw!r} não reconhecido na lista canônica "
            f"(pipeline/reference_data/municipios_alto_vale.csv). "
            "Verifique se é erro de digitação ou um município novo a incluir."
        )


_ESTADO_ALIASES_CACHE: Optional[dict[str, str]] = None


def _load_estado_aliases(reference_dir: Path = REFERENCE_DATA_DIR) -> dict[str, str]:
    aliases_path = reference_dir / "aliases_geograficos.yaml"
    aliases_raw = yaml.safe_load(aliases_path.read_text(encoding="utf-8")) or {}
    return aliases_raw.get("estado", {})


def normalize_estado(raw: Optional[str], reference_dir: Path = REFERENCE_DATA_DIR) -> str:
    """Normaliza o campo Estado para a sigla canônica ``"SC"``.

    Valores observados na planilha: "Santa Catarina", "SC", "Sc",
    "SC - SANTA CATARINA", e o erro de digitação "Santa Catarna" (falta o "i").
    O erro de digitação não é resolvido por dobra de acento/caixa — precisa de
    alias explícito em ``aliases_geograficos.yaml``.
    """
    if raw is None or not str(raw).strip():
        raise ValueError("Estado em branco não pode ser normalizado")
    folded = _fold(str(raw))
    aliases = _load_estado_aliases(reference_dir)
    if folded in aliases:
        return aliases[folded]
    if folded == "sc" or "catarina" in folded:
        return "SC"
    raise ValueError(f"Estado {raw!r} não reconhecido — adicione um alias se for válido")


# ---------------------------------------------------------------------------
# Área de atuação
# ---------------------------------------------------------------------------

def derive_area_atuacao(raw: Optional[str]) -> tuple[bool, bool]:
    """Deriva (atua_rural, atua_urbana) a partir do texto livre do formulário.

    O instrumento registrou "ambas as áreas" de duas formas distintas
    ("Rural e Urbana" e "Rural, Urbana") — em vez de modelar como categoria de
    texto única, derivamos dois booleanos por substring, robustos a qualquer
    separador.
    """
    if raw is None:
        return (False, False)
    folded = _fold(str(raw))
    return ("rural" in folded, "urbana" in folded)


# ---------------------------------------------------------------------------
# Numérico: None vs 0
# ---------------------------------------------------------------------------

def coerce_nullable_int(raw: object) -> Optional[int]:
    """Converte para ``int`` preservando a distinção entre ausente e zero.

    Campos demográficos (mulheres/homens/cor) costumam vir em branco quando a
    pergunta não foi respondida — isso é semanticamente diferente de uma
    resposta explícita de zero, e não deve ser tratado com `fillna(0)`.
    """
    if raw is None:
        return None
    if isinstance(raw, float) and raw != raw:  # NaN
        return None
    if isinstance(raw, str) and not raw.strip():
        return None
    return int(raw)


# ---------------------------------------------------------------------------
# Total de sócios/as: o campo declarado não é confiável
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class TotalReconciliation:
    total_calculado: Optional[int]
    total_declarado: Optional[int]
    divergente: bool


def reconcile_total(
    mulheres: Optional[int], homens: Optional[int], total_declarado: Optional[int]
) -> TotalReconciliation:
    """Deriva o total de sócios/as a partir de mulheres+homens.

    Encontramos 5 linhas (das 24) na planilha 23/02/2026 em que o campo
    "Total" declarado é 0 mesmo com mulheres/homens preenchidos e não-zero
    (ex.: mulheres=62, homens=76, total declarado=0) — o pipeline nunca deve
    confiar nesse campo bruto; ele é mantido só como auditoria.
    """
    if mulheres is None and homens is None:
        total_calculado = None
    else:
        total_calculado = (mulheres or 0) + (homens or 0)
    divergente = (
        total_declarado is not None
        and total_calculado is not None
        and total_declarado != total_calculado
    )
    return TotalReconciliation(
        total_calculado=total_calculado,
        total_declarado=total_declarado,
        divergente=divergente,
    )


# ---------------------------------------------------------------------------
# Autorização de uso
# ---------------------------------------------------------------------------

def is_authorized(raw: Optional[str]) -> bool:
    """Critério de inclusão no dataset público: autorização confirmada.

    Note: isto é deliberadamente independente de `Entry_Status` — das 4
    respostas "Incomplete" na planilha 23/02/2026, duas (linhas 6 e 7) têm
    autorização "Sim" e dados demográficos parciais preenchidos; só as
    linhas sem essa confirmação (23 e 24, autorização em branco) devem ser
    excluídas da visão pública.
    """
    if raw is None:
        return False
    return _fold(str(raw)) == "sim"
