from clean import is_authorized

# Casos reais da planilha 23_02_2026: das 4 respostas com Entry_Status="Incomplete"
# (linhas 6, 7, 23, 24), só 23 e 24 têm autorização em branco — 6 e 7 confirmaram "Sim"
# e devem ENTRAR no dataset público apesar do status "Incomplete".
LINHAS_INCOMPLETE = {
    6: "Sim",
    7: "Sim",
    23: None,
    24: None,
}


def test_incomplete_rows_with_confirmed_authorization_are_included():
    assert is_authorized(LINHAS_INCOMPLETE[6]) is True
    assert is_authorized(LINHAS_INCOMPLETE[7]) is True


def test_incomplete_rows_without_authorization_are_excluded():
    assert is_authorized(LINHAS_INCOMPLETE[23]) is False
    assert is_authorized(LINHAS_INCOMPLETE[24]) is False


def test_explicit_no_is_not_authorized():
    assert is_authorized("Não") is False


def test_criterion_is_authorization_not_entry_status():
    # Regra do pipeline: inclusão pública == autorizacao == "Sim", nunca Entry_Status.
    # Este teste documenta a intenção; a aplicação real está em aggregate.py.
    submitted_but_hypothetically_unauthorized = is_authorized(None)
    assert submitted_but_hypothetically_unauthorized is False
