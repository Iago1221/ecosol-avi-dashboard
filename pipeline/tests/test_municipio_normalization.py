import pytest

from clean import MunicipioLookup, normalize_estado


@pytest.fixture(scope="module")
def lookup() -> MunicipioLookup:
    return MunicipioLookup.load()


# Casos reais observados na planilha 23_02_2026 (coluna Endereço_City)
@pytest.mark.parametrize(
    "raw, esperado",
    [
        ("Rio do Sul", "Rio do Sul"),
        ("RIO DO SUL", "Rio do Sul"),
        ("IBIRAMA", "Ibirama"),
        ("Ibirama", "Ibirama"),
        ("Chapadao do Lageado", "Chapadão do Lageado"),  # sem til, erro de digitação
        ("Chapadão do Lageado", "Chapadão do Lageado"),
        ("Vítor Meireles", "Vitor Meireles"),  # grafia oficial AMAVI não usa acento
        ("Vitor Meireles", "Vitor Meireles"),
        ("Alfredo Wagner", "Alfredo Wagner"),  # fora da lista AMAVI, mas resposta válida
        ("  ituporanga  ", "Ituporanga"),
    ],
)
def test_normalize_known_variants(lookup: MunicipioLookup, raw: str, esperado: str):
    assert lookup.normalize(raw) == esperado


def test_unknown_municipio_raises(lookup: MunicipioLookup):
    with pytest.raises(ValueError):
        lookup.normalize("Cidade Que Não Existe")


def test_blank_raises(lookup: MunicipioLookup):
    with pytest.raises(ValueError):
        lookup.normalize(None)
    with pytest.raises(ValueError):
        lookup.normalize("")


# Casos reais observados na planilha 23_02_2026 (coluna Endereço_State)
@pytest.mark.parametrize(
    "raw",
    ["Santa Catarina", "SC", "Sc", "SC - SANTA CATARINA", "Santa Catarna"],
)
def test_normalize_estado_variants(raw: str):
    assert normalize_estado(raw) == "SC"


def test_normalize_estado_unknown_raises():
    with pytest.raises(ValueError):
        normalize_estado("Paraná")
