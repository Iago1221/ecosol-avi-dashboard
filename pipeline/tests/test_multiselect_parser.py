from clean import parse_multiselect

# Valor real da linha 19, coluna 55 ("Indique quais atividades econômicas ...") da planilha
# 23_02_2026 — contém uma opção com vírgula interna, entre aspas.
LINHA_19_COL_55 = (
    'Produção, Comercialização ou organização da comercialização – venda, '
    'Prestação do serviço ou trabalho a terceiros, Troca de produtos ou serviços, '
    '"Poupança, crédito ou finanças solidárias", Consumo, Uso de infra-estrutura, '
    'Aquisição de matéria-prima e insumos, Obtenção de clientes ou serviços'
)


def test_quoted_comma_option_stays_as_single_item():
    result = parse_multiselect(LINHA_19_COL_55)
    assert "Poupança, crédito ou finanças solidárias" in result
    assert "Poupança" not in result
    assert "crédito ou finanças solidárias" not in result
    assert len(result) == 9


def test_simple_multiselect_without_quotes():
    result = parse_multiselect("Produção, Comercialização ou organização da comercialização – venda")
    assert result == ["Produção", "Comercialização ou organização da comercialização – venda"]


def test_single_option():
    assert parse_multiselect("Produção") == ["Produção"]


def test_none_and_blank():
    assert parse_multiselect(None) == []
    assert parse_multiselect("") == []
    assert parse_multiselect("   ") == []
