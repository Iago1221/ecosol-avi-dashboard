from dictionary import build_dictionary, parse_column_name, _load_section_labels, REFERENCE_DATA_DIR


def test_parse_column_name_with_question_number_and_suffix():
    section_labels = _load_section_labels(REFERENCE_DATA_DIR)
    prefix, meta, subgroups, qnum, campo = parse_column_name(
        "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO__28IndiqueQuaisAtividadesEconômicas",
        section_labels,
    )
    assert prefix == "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO"
    assert meta["ordem"] == 3
    assert qnum == "28"
    assert campo == "IndiqueQuaisAtividadesEconômicas"


def test_parse_column_name_conditional_block_prefix():
    section_labels = _load_section_labels(REFERENCE_DATA_DIR)
    prefix, meta, subgroups, qnum, campo = parse_column_name(
        "_35A55__35QuantosTiposDeProdutos", section_labels
    )
    assert prefix == "_35A55"
    assert qnum == "35"


def test_pii_column_flagged():
    entries = build_dictionary(["SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__11CNPJ"])
    assert entries[0].pii is True


def test_non_pii_column_not_flagged():
    entries = build_dictionary(["SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__1NomeDoEmpreendimento"])
    assert entries[0].pii is False


def test_override_applied():
    entries = build_dictionary(["SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__1NomeDoEmpreendimento"])
    assert entries[0].tipo_inferido == "text"


def test_multiselect_suffix_detected():
    entries = build_dictionary(
        ["SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO__26XrespostaMúltipla"]
    )
    assert entries[0].tipo_inferido == "multi_select"


def test_single_select_suffix_detected():
    entries = build_dictionary(
        ["SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO__26XrespostaÚnica"]
    )
    assert entries[0].tipo_inferido == "single_select"
