"""Checks de qualidade sobre os registros já limpos (ver `transform.build_core_records`).

Produz uma lista de `Finding` (achados) que `build.py` grava em `quality_report.md`.
Nada aqui interrompe o pipeline por si só — falhas "duras" (município não reconhecido,
etc.) já acontecem antes, em `clean.py`, levantando `ValueError`.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Finding:
    nivel: str  # "info" | "atencao"
    linha_origem: int
    mensagem: str


def validate_records(records: list[dict[str, Any]]) -> list[Finding]:
    findings: list[Finding] = []

    for r in records:
        linha = r["linha_origem_planilha"]

        if r["socios_total_divergente"]:
            findings.append(
                Finding(
                    nivel="atencao",
                    linha_origem=linha,
                    mensagem=(
                        f"Total de sócios/as declarado ({r['socios_total_declarado']}) diverge "
                        f"da soma mulheres+homens ({r['socios_total']}) — usando o valor "
                        "calculado. Verificar na fonte (formulário original)."
                    ),
                )
            )

        cor_campos = [
            r.get("cor_branca"),
            r.get("cor_preta"),
            r.get("cor_amarela"),
            r.get("cor_parda"),
            r.get("cor_indigena"),
        ]
        if r["socios_total"] and all(v is None for v in cor_campos):
            findings.append(
                Finding(
                    nivel="info",
                    linha_origem=linha,
                    mensagem="Nenhum campo de cor/raça preenchido apesar de haver sócios/as declarados.",
                )
            )

        if not r["incluido_no_publico"]:
            findings.append(
                Finding(
                    nivel="info",
                    linha_origem=linha,
                    mensagem=(
                        f"Excluído do dataset público: autorização de uso não confirmada "
                        f"(entry_status={r['entry_status']!r})."
                    ),
                )
            )

    return findings


def render_report(findings: list[Finding], total_linhas: int, incluidas: int) -> str:
    lines = [
        "# Relatório de Qualidade dos Dados",
        "",
        f"Total de linhas na planilha: {total_linhas}. Incluídas no dataset público: {incluidas}.",
        "",
    ]
    atencao = [f for f in findings if f.nivel == "atencao"]
    info = [f for f in findings if f.nivel == "info"]

    lines.append(f"## Atenção ({len(atencao)})")
    lines.append("")
    for f in atencao:
        lines.append(f"- Linha {f.linha_origem}: {f.mensagem}")
    lines.append("")

    lines.append(f"## Informativo ({len(info)})")
    lines.append("")
    for f in info:
        lines.append(f"- Linha {f.linha_origem}: {f.mensagem}")
    lines.append("")

    return "\n".join(lines)


def assert_no_pii_leak(record_keys: set[str], pii_semantic_keys: set[str]) -> None:
    """Allowlist test: nenhuma chave de PII pode escapar para um registro público."""
    leaked = record_keys & pii_semantic_keys
    if leaked:
        raise AssertionError(f"Campos de PII vazando para artefato público: {leaked}")
