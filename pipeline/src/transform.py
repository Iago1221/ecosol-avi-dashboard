"""Monta os registros "core" (limpos, achatados) a partir do DataFrame principal bruto.

Cobre só os campos de identificação + os 8 campos do MVP — o restante das 251 colunas
fica disponível em `full_raw` (ver `build.py`) para uso interno, sem passar por estas
transformações.
"""
from __future__ import annotations

from typing import Any, Optional

import pandas as pd

import columns as C
from clean import (
    MunicipioLookup,
    coerce_nullable_int,
    derive_area_atuacao,
    is_authorized,
    normalize_estado,
    parse_multiselect,
    reconcile_total,
    _fold,
)


def _str_or_none(value: Any) -> Optional[str]:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    text = str(value).strip()
    return text or None


def _bool_sim_nao_or_none(value: Any) -> Optional[bool]:
    text = _str_or_none(value)
    if text is None:
        return None
    return _fold(text) == "sim"


def build_core_records(
    main_df: pd.DataFrame, municipio_lookup: MunicipioLookup
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []

    for idx, row in main_df.iterrows():
        linha_origem_planilha = int(idx) + 2  # cabeçalho ocupa a linha 1 do Excel

        municipio_raw = _str_or_none(row[C.MUNICIPIO])
        estado_raw = _str_or_none(row[C.ESTADO])
        municipio = municipio_lookup.normalize(municipio_raw) if municipio_raw else None
        estado = normalize_estado(estado_raw) if estado_raw else None

        atua_rural, atua_urbana = derive_area_atuacao(row[C.AREA_ATUACAO])

        mulheres = coerce_nullable_int(row[C.SOCIOS_MULHERES])
        homens = coerce_nullable_int(row[C.SOCIOS_HOMENS])
        total_declarado = coerce_nullable_int(row[C.SOCIOS_TOTAL_DECLARADO])
        totais = reconcile_total(mulheres, homens, total_declarado)

        redes_tipos = []
        redes_detalhes: dict[str, str] = {}
        for label, col in C.REDES_TIPOS_QUAL.items():
            texto = _str_or_none(row[col])
            if texto:
                redes_tipos.append(label)
                redes_detalhes[label] = texto

        record = {
            "id": int(row[C.ID]),
            "linha_origem_planilha": linha_origem_planilha,
            "nome_empreendimento": _str_or_none(row[C.NOME_EMPREENDIMENTO]),
            "municipio": municipio,
            "estado": estado,
            "situacao_atual": _str_or_none(row[C.SITUACAO_ATUAL]),
            "atua_rural": atua_rural,
            "atua_urbana": atua_urbana,
            "socios_mulheres": mulheres,
            "socios_homens": homens,
            "socios_total": totais.total_calculado,
            "socios_total_declarado": totais.total_declarado,
            "socios_total_divergente": totais.divergente,
            "cor_branca": coerce_nullable_int(row[C.COR_BRANCA]),
            "cor_preta": coerce_nullable_int(row[C.COR_PRETA]),
            "cor_amarela": coerce_nullable_int(row[C.COR_AMARELA]),
            "cor_parda": coerce_nullable_int(row[C.COR_PARDA]),
            "cor_indigena": coerce_nullable_int(row[C.COR_INDIGENA]),
            "cor_total_declarado": coerce_nullable_int(row[C.COR_TOTAL_DECLARADO]),
            "pertence_povo_tradicional": _bool_sim_nao_or_none(row[C.POVO_TRADICIONAL]),
            "povo_tradicional_qual": _str_or_none(row[C.POVO_TRADICIONAL_QUAL]),
            "forma_organizacao": _str_or_none(row[C.FORMA_ORGANIZACAO]),
            "participa_rede": _bool_sim_nao_or_none(row[C.PARTICIPA_REDE]),
            "redes_tipos": redes_tipos,
            "redes_detalhes": redes_detalhes,
            "atividades_coletivas": parse_multiselect(_str_or_none(row[C.ATIVIDADES_COLETIVAS])),
            "atividade_principal": _str_or_none(row[C.ATIVIDADE_PRINCIPAL]),
            "entry_status": _str_or_none(row[C.ENTRY_STATUS]),
            "incluido_no_publico": is_authorized(_str_or_none(row[C.AUTORIZACAO])),
        }
        records.append(record)

    return records


def build_full_raw_records(main_df: pd.DataFrame) -> list[dict[str, Any]]:
    """Cópia bruta completa (251 colunas), sem transformação — uso interno apenas."""
    df = main_df.where(pd.notnull(main_df), None)
    return df.to_dict(orient="records")
