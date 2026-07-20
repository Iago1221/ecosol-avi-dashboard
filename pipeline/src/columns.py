"""Nomes exatos das colunas brutas usadas pelo dataset "core" (os 8 campos do MVP +
campos de identificação/controle). Centralizado aqui para não espalhar strings gigantes
de nome de coluna por `transform.py`/`aggregate.py`.
"""

ID = "PesquisaEconomiaSolidária_Id"
NOME_EMPREENDIMENTO = "SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__1NomeDoEmpreendimento"
MUNICIPIO = "SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__3Endereço_City"
ESTADO = "SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__3Endereço_State"
SITUACAO_ATUAL = "SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__13SituaçãoAtualDoEmpreendimento"
AREA_ATUACAO = "SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__14QualAÁreaDeAtuaçãoDoEmpreendimento"

SOCIOS_MULHERES = "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS_Mulheresquantas"
SOCIOS_HOMENS = "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS_Homensquantos"
SOCIOS_TOTAL_DECLARADO = "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS_Totalquantas"

COR_BRANCA = "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18aBrancaquantas"
COR_PRETA = "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18bPretaquantas"
COR_AMARELA = "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18cAmarelaquantas"
COR_PARDA = "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18dPardaquantas"
COR_INDIGENA = "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18eIndígenaquantas"
COR_TOTAL_DECLARADO = "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18fTotalquantas"

POVO_TRADICIONAL = (
    "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS"
    "__19OsSóciosDoEmpreendimentoPertencemAAlgumPovoOuComunidadeTradicional"
)
POVO_TRADICIONAL_QUAL = (
    "SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__20AQualPovoOuComunidadeTradicional"
)

FORMA_ORGANIZACAO = "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO__25FormaDeOrganização"
PARTICIPA_REDE = (
    "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO"
    "__26OEmpreendimentoParticipaDeAlgumaRedeDeProduçãoComercializaçãoConsumoOuCrédito"
)

# Colunas "Qual" condicionais de tipo de rede (preenchida = participa daquele tipo)
REDES_TIPOS_QUAL: dict[str, str] = {
    "Rede de Produção": (
        "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27aRedeDeProduçãoQual"
    ),
    "Rede de Comercialização": (
        "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27bRedeDeComercializaçãoQual"
    ),
    "Cadeia Produtiva Solidária": (
        "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27cCadeiaProdutivaSolidáriaQual"
    ),
    "Complexo Cooperativo": (
        "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27dComplexoCooperativoQual"
    ),
    "Cooperativa Central": (
        "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27eCooperativaCentralQual"
    ),
    "Rede de Consumo": (
        "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27fRedeDeConsumoQual"
    ),
    "Rede de Crédito ou Finanças Solidárias": (
        "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27gRedeDeCréditoOuFinançasSolidáriasQual"
    ),
    "Rede ou Organização de Comércio Justo e Solidário": (
        "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27hRedeOuOrganizaçãoDeComércioJustoESolidárioQual"
    ),
}

ATIVIDADES_COLETIVAS = (
    "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO"
    "__28IndiqueQuaisAtividadesEconômicasSãoRealizadasDeFormaColetivaPelosasSóciosasDoEmpreendimento"
)
ATIVIDADE_PRINCIPAL = (
    "SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO"
    "__29DentreAsAtividadesEconômicasRealizadasPeloEmpreendimentoIndiqueQualAPrincipal"
)

AUTORIZACAO = (
    "AUTORIZAÇÃOPARAOUSODASINFORMAÇÕESDOSIESCONFORMEPORTARIAMINISTERIAL"
    "__171OEmpreendimentoAutorizaAUtilizaçãoDeInformaçõesRelativasÀIdentificaçãoEÀsAtividadesEconômicasComOObjetivoDeFortalecerEDivulgarAEconomiaSolidária"
)
ENTRY_STATUS = "Entry_Status"
