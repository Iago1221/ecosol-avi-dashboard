"""Agregados pré-computados para os 8 campos do MVP.

Cada agregado inclui `n_respostas_com_dado` (quantos registros incluídos tinham valor
não-nulo para aquele campo especificamente) e `n_total_incluido` (quantos registros
entraram no dataset público no total) — o N efetivo varia por campo (ex.: "Cor" tem
não-resposta parcial bem maior que "Forma de organização").
"""
from __future__ import annotations

from collections import Counter
from typing import Any


def _public_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [r for r in records if r["incluido_no_publico"]]


def aggregate_municipio(records: list[dict[str, Any]]) -> dict[str, Any]:
    publicos = _public_records(records)
    com_dado = [r for r in publicos if r["municipio"]]
    counts = Counter(r["municipio"] for r in com_dado)
    return {
        "campo": "municipio",
        "n_total_incluido": len(publicos),
        "n_respostas_com_dado": len(com_dado),
        "contagens": [
            {"municipio": nome, "quantidade": qtd}
            for nome, qtd in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        ],
    }


def aggregate_area_atuacao(records: list[dict[str, Any]]) -> dict[str, Any]:
    publicos = _public_records(records)
    rural_e_urbana = sum(1 for r in publicos if r["atua_rural"] and r["atua_urbana"])
    so_rural = sum(1 for r in publicos if r["atua_rural"] and not r["atua_urbana"])
    so_urbana = sum(1 for r in publicos if r["atua_urbana"] and not r["atua_rural"])
    nenhuma = sum(1 for r in publicos if not r["atua_rural"] and not r["atua_urbana"])
    return {
        "campo": "area_atuacao",
        "n_total_incluido": len(publicos),
        "n_respostas_com_dado": len(publicos) - nenhuma,
        "contagens": [
            {"categoria": "Somente rural", "quantidade": so_rural},
            {"categoria": "Somente urbana", "quantidade": so_urbana},
            {"categoria": "Rural e urbana", "quantidade": rural_e_urbana},
            {"categoria": "Não informado", "quantidade": nenhuma},
        ],
    }


def aggregate_genero(records: list[dict[str, Any]]) -> dict[str, Any]:
    publicos = _public_records(records)
    com_dado = [r for r in publicos if r["socios_total"] is not None]
    total_mulheres = sum(r["socios_mulheres"] or 0 for r in com_dado)
    total_homens = sum(r["socios_homens"] or 0 for r in com_dado)
    total_geral = total_mulheres + total_homens
    # Somado por município (não por empreendimento): vários empreendimentos podem
    # compartilhar o mesmo município — um rótulo por empreendimento com nomes longos
    # sobrepõe/ilegível num gráfico de barras; a soma por município é o nível de
    # granularidade que o campo do MVP pede.
    por_municipio_map: dict[str, dict[str, int]] = {}
    for r in com_dado:
        if r["municipio"]:
            bucket = por_municipio_map.setdefault(r["municipio"], {"mulheres": 0, "homens": 0})
            bucket["mulheres"] += r["socios_mulheres"] or 0
            bucket["homens"] += r["socios_homens"] or 0
    por_municipio = [
        {"municipio": municipio, **valores} for municipio, valores in por_municipio_map.items()
    ]
    return {
        "campo": "genero",
        "n_total_incluido": len(publicos),
        "n_respostas_com_dado": len(com_dado),
        "total_mulheres": total_mulheres,
        "total_homens": total_homens,
        "percentual_feminino": round(100 * total_mulheres / total_geral, 1) if total_geral else None,
        "por_municipio": sorted(por_municipio, key=lambda d: d["municipio"]),
    }


_COR_CAMPOS = {
    "Branca": "cor_branca",
    "Preta": "cor_preta",
    "Amarela": "cor_amarela",
    "Parda": "cor_parda",
    "Indígena": "cor_indigena",
}


def aggregate_cor(records: list[dict[str, Any]]) -> dict[str, Any]:
    publicos = _public_records(records)
    com_dado = [r for r in publicos if any(r[campo] is not None for campo in _COR_CAMPOS.values())]
    contagens = [
        {"categoria": categoria, "quantidade": sum(r[campo] or 0 for r in com_dado)}
        for categoria, campo in _COR_CAMPOS.items()
    ]
    return {
        "campo": "cor",
        "n_total_incluido": len(publicos),
        "n_respostas_com_dado": len(com_dado),
        "contagens": contagens,
    }


def aggregate_povo_tradicional(records: list[dict[str, Any]]) -> dict[str, Any]:
    publicos = _public_records(records)
    com_dado = [r for r in publicos if r["pertence_povo_tradicional"] is not None]
    sim = [r for r in com_dado if r["pertence_povo_tradicional"]]
    povos_citados = sorted({r["povo_tradicional_qual"] for r in sim if r["povo_tradicional_qual"]})
    return {
        "campo": "povo_tradicional",
        "n_total_incluido": len(publicos),
        "n_respostas_com_dado": len(com_dado),
        "quantidade_sim": len(sim),
        "quantidade_nao": len(com_dado) - len(sim),
        "povos_citados": povos_citados,
    }


def aggregate_forma_organizacao(records: list[dict[str, Any]]) -> dict[str, Any]:
    publicos = _public_records(records)
    com_dado = [r for r in publicos if r["forma_organizacao"]]
    counts = Counter(r["forma_organizacao"] for r in com_dado)
    return {
        "campo": "forma_organizacao",
        "n_total_incluido": len(publicos),
        "n_respostas_com_dado": len(com_dado),
        "contagens": [
            {"forma": nome, "quantidade": qtd}
            for nome, qtd in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        ],
    }


def aggregate_participa_rede(records: list[dict[str, Any]]) -> dict[str, Any]:
    publicos = _public_records(records)
    com_dado = [r for r in publicos if r["participa_rede"] is not None]
    sim = [r for r in com_dado if r["participa_rede"]]
    tipos_counter: Counter[str] = Counter()
    for r in sim:
        tipos_counter.update(r["redes_tipos"])
    return {
        "campo": "participa_rede",
        "n_total_incluido": len(publicos),
        "n_respostas_com_dado": len(com_dado),
        "quantidade_sim": len(sim),
        "quantidade_nao": len(com_dado) - len(sim),
        "tipos_de_rede": [
            {"tipo": tipo, "quantidade": qtd}
            for tipo, qtd in sorted(tipos_counter.items(), key=lambda kv: (-kv[1], kv[0]))
        ],
    }


def aggregate_atividades_coletivas(records: list[dict[str, Any]]) -> dict[str, Any]:
    publicos = _public_records(records)
    com_dado = [r for r in publicos if r["atividades_coletivas"]]
    counts: Counter[str] = Counter()
    for r in com_dado:
        counts.update(r["atividades_coletivas"])
    return {
        "campo": "atividades_coletivas",
        "n_total_incluido": len(publicos),
        "n_respostas_com_dado": len(com_dado),
        "nota": "Multiescolha: a soma das quantidades pode ultrapassar N.",
        "contagens": [
            {"atividade": nome, "quantidade": qtd}
            for nome, qtd in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        ],
    }


AGGREGATORS = {
    "municipio": aggregate_municipio,
    "area_atuacao": aggregate_area_atuacao,
    "genero": aggregate_genero,
    "cor": aggregate_cor,
    "povo_tradicional": aggregate_povo_tradicional,
    "forma_organizacao": aggregate_forma_organizacao,
    "participa_rede": aggregate_participa_rede,
    "atividades_coletivas": aggregate_atividades_coletivas,
}


def build_all_aggregates(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {nome: fn(records) for nome, fn in AGGREGATORS.items()}
