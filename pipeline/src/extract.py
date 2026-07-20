"""Leitura da planilha bruta de respostas para DataFrames do pandas.

A planilha exportada tem uma aba principal (uma linha por empreendimento) e 7 abas
"filhas" de grupos de repetição (listas de produtos/serviços), ligadas à principal
pela coluna `PesquisaEconomiaSolidária_Id`. Hoje essas abas filhas estão praticamente
vazias (só a FK/Id preenchidos), mas o join é montado mesmo assim para não exigir
retrabalho quando a coleta passar a preencher esses dados.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

MAIN_SHEET = "PesquisaEconomiaSolidária"
# Nomes reais das 7 abas filhas na planilha 23_02_2026 (sem aba para o bloco
# Clube de Trocas — esse bloco não tem grupo de repetição no instrumento).
CHILD_SHEETS = [
    "_35A55.SemTítulo",
    "_35A55.SemTítulo2",
    "_56A74.SemTítulo",
    "_75A93.SemTítulo",
    "_75A93.SemTítulo2",
    "_94A110.SemTítulo",
    "_111A121.SemTítulo",
]


@dataclass(frozen=True)
class RawWorkbook:
    main: pd.DataFrame
    children: dict[str, pd.DataFrame]


def extract(xlsx_path: Path) -> RawWorkbook:
    all_sheets = pd.read_excel(xlsx_path, sheet_name=None, engine="openpyxl")
    main = all_sheets[MAIN_SHEET]
    children = {name: df for name, df in all_sheets.items() if name != MAIN_SHEET}
    return RawWorkbook(main=main, children=children)
