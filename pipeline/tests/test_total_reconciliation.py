from clean import reconcile_total

# Casos reais da planilha 23_02_2026 (colunas Mulheres/Homens/Total, seção II)
CASOS_SEM_DIVERGENCIA = [
    # (mulheres, homens, total_declarado)
    (15, 8, 23),   # linha 2
    (6, 19, 25),   # linha 3
    (42, 18, 60),  # linha 4 (total declarado bate)
]

CASOS_COM_DIVERGENCIA = [
    (5, 2, 0),     # linha 8: total declarado 0, correto seria 7
    (4, 6, 0),     # linha 9: total declarado 0, correto seria 10
    (14, 14, 0),   # linha 21: total declarado 0, correto seria 28
    (62, 76, 0),   # linha 22: total declarado 0, correto seria 138
    (10, 5, 0),    # linha 25: total declarado 0, correto seria 15
]


def test_no_divergence_when_declared_matches_sum():
    for mulheres, homens, total in CASOS_SEM_DIVERGENCIA:
        r = reconcile_total(mulheres, homens, total)
        assert r.total_calculado == mulheres + homens
        assert r.divergente is False


def test_known_divergent_rows_flagged():
    for mulheres, homens, total in CASOS_COM_DIVERGENCIA:
        r = reconcile_total(mulheres, homens, total)
        assert r.total_calculado == mulheres + homens
        assert r.total_calculado != total
        assert r.divergente is True


def test_missing_declared_total_is_not_a_divergence():
    # linha 7: mulheres=1, homens=2, total declarado ausente (None) -> calculado=3, sem alerta
    r = reconcile_total(1, 2, None)
    assert r.total_calculado == 3
    assert r.divergente is False


def test_both_counts_missing_yields_none():
    r = reconcile_total(None, None, None)
    assert r.total_calculado is None
    assert r.divergente is False


def test_one_count_missing_treated_as_zero_for_sum():
    r = reconcile_total(14, None, 14)
    assert r.total_calculado == 14
    assert r.divergente is False
