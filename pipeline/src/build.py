"""Entrypoint único do pipeline: lê a planilha bruta e gera todos os artefatos de saída.

Uso:
    python -m src.build [caminho/para/planilha.xlsx]

Se o caminho não for informado, usa `inputs/Respostas - Pesquisa Economia Solidária - 23_02_2026.xlsx`
relativo à raiz do projeto.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_XLSX = PROJECT_ROOT / "inputs" / "Respostas - Pesquisa Economia Solidária - 23_02_2026.xlsx"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
DOCS_DIR = PROJECT_ROOT / "docs"

# Chaves que NUNCA podem aparecer num registro "core" — guarda de regressão, mesmo que
# `transform.py` já só extraia campos permitidos (ver pipeline/reference_data/pii_columns.yaml).
PII_FORBIDDEN_SUBSTRINGS = [
    "telefone", "whatsapp", "email", "cnpj", "pessoa_contato",
    "cargo", "postal_code", "endereco_line1", "nome_entrevistad",
]


def _assert_core_record_has_no_pii(record: dict) -> None:
    for key in record.keys():
        lowered = key.lower()
        for forbidden in PII_FORBIDDEN_SUBSTRINGS:
            if forbidden in lowered:
                raise AssertionError(f"Chave suspeita de PII em registro core: {key!r}")


def run(xlsx_path: Path) -> None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from clean import MunicipioLookup
    from dictionary import build_dictionary, render_markdown
    from extract import extract
    from transform import build_core_records, build_full_raw_records
    from aggregate import build_all_aggregates
    from validate import validate_records, render_report

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "aggregates").mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Lendo planilha: {xlsx_path}")
    wb = extract(xlsx_path)
    print(f"  aba principal: {wb.main.shape[0]} linhas x {wb.main.shape[1]} colunas")
    print(f"  abas filhas: {len(wb.children)}")

    print("Gerando dicionário de dados...")
    dict_entries = build_dictionary(list(wb.main.columns), sample_frame=wb.main)
    (OUTPUT_DIR / "data_dictionary.json").write_text(
        json.dumps([e.to_dict() for e in dict_entries], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (DOCS_DIR / "dicionario_de_dados.md").write_text(
        render_markdown(dict_entries), encoding="utf-8"
    )

    print("Limpando e normalizando registros...")
    municipio_lookup = MunicipioLookup.load()
    core_records_all = build_core_records(wb.main, municipio_lookup)

    for record in core_records_all:
        _assert_core_record_has_no_pii(record)

    core_records_public = [r for r in core_records_all if r["incluido_no_publico"]]
    print(f"  {len(core_records_public)} de {len(core_records_all)} registros incluídos no público")

    print("Rodando validações de qualidade...")
    findings = validate_records(core_records_all)
    report = render_report(findings, total_linhas=len(core_records_all), incluidas=len(core_records_public))
    (OUTPUT_DIR / "quality_report.md").write_text(report, encoding="utf-8")

    print("Calculando agregados do MVP...")
    aggregates = build_all_aggregates(core_records_all)
    for nome, dados in aggregates.items():
        (OUTPUT_DIR / "aggregates" / f"{nome}.json").write_text(
            json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    print("Escrevendo core.json (público, sem PII, só linhas autorizadas)...")
    (OUTPUT_DIR / "core.json").write_text(
        json.dumps(core_records_public, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print("Escrevendo full_raw.json (uso interno, NÃO publicar)...")
    full_raw = build_full_raw_records(wb.main)
    (OUTPUT_DIR / "full_raw.json").write_text(
        json.dumps(full_raw, ensure_ascii=False, indent=2, default=str), encoding="utf-8"
    )

    dataset_meta = {
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "arquivo_fonte": xlsx_path.name,
        "total_linhas_coletadas": len(core_records_all),
        "total_linhas_incluidas_no_publico": len(core_records_public),
        "criterio_inclusao": "autorizacao_de_uso_confirmada (coluna 'AUTORIZAÇÃO PARA O USO DAS INFORMAÇÕES DO SIES...') == 'Sim'",
    }
    (OUTPUT_DIR / "dataset_meta.json").write_text(
        json.dumps(dataset_meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print("Concluído.")
    print(f"  Saídas em: {OUTPUT_DIR}")
    print(f"  Dicionário em: {DOCS_DIR / 'dicionario_de_dados.md'}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xlsx_path", nargs="?", default=str(DEFAULT_XLSX))
    args = parser.parse_args()
    run(Path(args.xlsx_path))


if __name__ == "__main__":
    main()
