# Dicionário de Dados — Pesquisa Economia Solidária

Gerado automaticamente por `pipeline/src/dictionary.py`. Correções pontuais devem ir em `pipeline/reference_data/dictionary_overrides.yaml`, não direto neste arquivo (ele é sobrescrito a cada geração).

## Seção I — Identificação e Abrangência

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__1NomeDoEmpreendimento` | 1 | Nome Do Empreendimento | text |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__2NomeFantasiaSigla` | 2 | Nome Fantasia Sigla | text |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__3Endereço_Line1` | 3 | Endereço_Line1 | multi_select | ⚠️ SIM |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__3Endereço_City` | 3 | Endereço_City | text |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__3Endereço_State` | 3 | Endereço_State | text |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__3Endereço_PostalCode` | 3 | Endereço_Postal Code | text | ⚠️ SIM |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__3Endereço_Country` | 3 | Endereço_Country | text |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__3Endereço_CountryCode` | 3 | Endereço_Country Code | text |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__6Telefone` | 6 | Telefone | text | ⚠️ SIM |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA_Whatsapp` |  | Whatsapp | text | ⚠️ SIM |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__7Email` | 7 | Email | text | ⚠️ SIM |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__8PessoaParaContato` | 8 | Pessoa Para Contato | text | ⚠️ SIM |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__9ReferênciaParaLocalização` | 9 | Referência Para Localização | text |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__10PáginaNaInternet` | 10 | Página Na Internet | text |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__11CNPJ` | 11 | CNPJ | text | ⚠️ SIM |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__12QualOAnoDoInícioDoEmpreendimento` | 12 | Qual OAno Do Início Do Empreendimento | numeric |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__13SituaçãoAtualDoEmpreendimento` | 13 | Situação Atual Do Empreendimento | text |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__14QualAÁreaDeAtuaçãoDoEmpreendimento` | 14 | Qual AÁrea De Atuação Do Empreendimento | multi_select |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__15OEmpreendimentoTemAcessoAComputador` | 15 | OEmpreendimento Tem Acesso AComputador | boolean |  |
| `SeçãoIIDENTIFICAÇÃOEABRANGÊNCIA__16OEmpreendimentoTemAcessoÀInternet` | 16 | OEmpreendimento Tem Acesso ÀInternet | boolean |  |

## Seção II — Características Predominantes dos/as Sócios/as

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS_Mulheresquantas` |  | Mulheresquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS_Homensquantos` |  | Homensquantos | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS_Totalquantas` |  | Totalquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18aBrancaquantas` | 18a | Brancaquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18bPretaquantas` | 18b | Pretaquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18cAmarelaquantas` | 18c | Amarelaquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18dPardaquantas` | 18d | Pardaquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18eIndígenaquantas` | 18e | Indígenaquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__18fTotalquantas` | 18f | Totalquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__19OsSóciosDoEmpreendimentoPertencemAAlgumPovoOuComunidadeTradicional` | 19 | Os Sócios Do Empreendimento Pertencem AAlgum Povo Ou Comunidade Tradicional | boolean |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__20AQualPovoOuComunidadeTradicional` | 20 | AQual Povo Ou Comunidade Tradicional | text |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__21PodemosDizerQueNoEmpreendimentoOsasSóciosasPertencemOuJáPertenceramAQualDasSeguintesCategoriasSociais` | 21 | Podemos Dizer Que No Empreendimento Osas Sóciosas Pertencem Ou Já Pertenceram AQual Das Seguintes Categorias Sociais | text |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__22aPessoasComDeficiênciaFísicaOuMentalTotalquantas` | 22a | Pessoas Com Deficiência Física Ou Mental Totalquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__22bPessoasComTranstornosMentaisInclusiveQuandoDecorrentesDoUsoDeÁlcoolOuDeOutrasDrogas` | 22b | Pessoas Com Transtornos Mentais Inclusive Quando Decorrentes Do Uso De Álcool Ou De Outras Drogas | numeric |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__22cPresidiáriosOuEgressosDoSistemaPrisional` | 22c | Presidiários Ou Egressos Do Sistema Prisional | numeric |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__22dAposentadosasOuPensionistas` | 22d | Aposentadosas Ou Pensionistas | numeric |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__23EntreOsSóciosHáPredominânciaDePessoasBeneficiáriasDeProgramasDeTransferênciaDeRendaOuBenefíciosDaAssistênciaSocial` | 23 | Entre Os Sócios Há Predominância De Pessoas Beneficiárias De Programas De Transferência De Renda Ou Benefícios Da Assistência Social | boolean |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__23aQual` | 23a | Qual | conditional_text |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__24aJovensquantas` | 24a | Jovensquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__24bAdultosquantas` | 24b | Adultosquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__24cIdososquantas` | 24c | Idososquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__24dNãoSeAplicaOuNãoHáPredominânciaquantas` | 24d | Não Se Aplica Ou Não Há Predominânciaquantas | integer |  |
| `SeçãoIICARACTERÍSTICASPREDOMINANTESDOSASSÓCIOSAS__24eTotalquantas` | 24e | Totalquantas | integer |  |

## Seção III — Características Gerais do Empreendimento

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO__25FormaDeOrganização` | 25 | Forma De Organização | text |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO__26OEmpreendimentoParticipaDeAlgumaRedeDeProduçãoComercializaçãoConsumoOuCrédito` | 26 | OEmpreendimento Participa De Alguma Rede De Produção Comercialização Consumo Ou Crédito | boolean |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27aRedeDeProduçãoQual` | 27a | Rede De Produção Qual | conditional_text |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27bRedeDeComercializaçãoQual` | 27b | Rede De Comercialização Qual | conditional_text |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27cCadeiaProdutivaSolidáriaQual` | 27c | Cadeia Produtiva Solidária Qual | conditional_text |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27dComplexoCooperativoQual` | 27d | Complexo Cooperativo Qual | conditional_text |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27eCooperativaCentralQual` | 27e | Cooperativa Central Qual | conditional_text |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27fRedeDeConsumoQual` | 27f | Rede De Consumo Qual | conditional_text |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27gRedeDeCréditoOuFinançasSolidáriasQual` | 27g | Rede De Crédito Ou Finanças Solidárias Qual | conditional_text |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO_SemTítulo__27hRedeOuOrganizaçãoDeComércioJustoESolidárioQual` | 27h | Rede Ou Organização De Comércio Justo ESolidário Qual | conditional_text |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO__28IndiqueQuaisAtividadesEconômicasSãoRealizadasDeFormaColetivaPelosasSóciosasDoEmpreendimento` | 28 | Indique Quais Atividades Econômicas São Realizadas De Forma Coletiva Pelosas Sóciosas Do Empreendimento | multi_select |  |
| `SeçãoIIICARACTERÍSTICASGERAISDOEMPREENDIMENTO__29DentreAsAtividadesEconômicasRealizadasPeloEmpreendimentoIndiqueQualAPrincipal` | 29 | Dentre As Atividades Econômicas Realizadas Pelo Empreendimento Indique Qual APrincipal | multi_select |  |

## Bloco condicional — Clube de Trocas (perguntas 30–34)

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `_30A34__30OEmpreendimentoSeCaracterizaComoUmClubeDeTrocas` | 30 | OEmpreendimento Se Caracteriza Como Um Clube De Trocas | boolean |  |
| `_30A34__31OClubeDeTrocasUtilizaMoedaSocial` | 31 | OClube De Trocas Utiliza Moeda Social | boolean |  |
| `_30A34__32AMoedaSocialUtilizadaPossuiLastro` | 32 | AMoeda Social Utilizada Possui Lastro | boolean |  |
| `_30A34__33OsasSóciosasPagamAlgumaTaxaOuContribuiçãoParaOEmpreendimento` | 33 | Osas Sóciosas Pagam Alguma Taxa Ou Contribuição Para OEmpreendimento | boolean |  |
| `_30A34__34QualAFormaDeContribuiçãoDosParticipantesParaOEmpreendimento` | 34 | Qual AForma De Contribuição Dos Participantes Para OEmpreendimento | text |  |

## Bloco condicional — Produção (perguntas 35–55)

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `_35A55__35QuantosTiposDeProdutosSãoProduzidosColetivamentePeloEmpreendimento` | 35 | Quantos Tipos De Produtos São Produzidos Coletivamente Pelo Empreendimento | integer |  |
| `_35A55__37QualFoiOFaturamentoMensalDoEmpreendimentovalorMédioMensal` | 37 | Qual Foi OFaturamento Mensal Do Empreendimentovalor Médio Mensal | numeric_or_text |  |
| `_35A55__39QuantoOEmpreendimentoGastaMensalmenteComInsumos` | 39 | Quanto OEmpreendimento Gasta Mensalmente Com Insumos | numeric |  |
| `_35A55__40QualAOrigemDaMatériaprimaOuDoInsumorespostaMúltipla` | 40 | Qual AOrigem Da Matériaprima Ou Do Insumoresposta Múltipla | multi_select |  |
| `_35A55__41OsEquipamentosDoEmpreendimentoSãorespostaMúltipla` | 41 | Os Equipamentos Do Empreendimento Sãoresposta Múltipla | multi_select |  |
| `_35A55__42QualÉODestinoDosProdutosrespostaMúltipla` | 42 | Qual ÉODestino Dos Produtosresposta Múltipla | multi_select |  |
| `_35A55__43ParaQuemÉFeitaAComercializaçãoDeProdutosDoEmpreendimentorespostaMúltipla` | 43 | Para Quem ÉFeita AComercialização De Produtos Do Empreendimentoresposta Múltipla | multi_select |  |
| `_35A55__44AVendaEouTrocaDeProdutosRealizasePrincipalmenteNorespostaMúltipla` | 44 | AVenda Eou Troca De Produtos Realizase Principalmente Noresposta Múltipla | multi_select |  |
| `_35A55__45QuaisOsPrincipaisEspaçosDeComercializaçãorespostaMúltipla` | 45 | Quais Os Principais Espaços De Comercializaçãoresposta Múltipla | multi_select |  |
| `_35A55__46OEmpreendimentoTemEncontradoAlgumaDificuldadeNaComercializaçãoDeProdutosEouServiçosconsiderarTantoOsEmpreendimentosQueJáEstãoComercializandoQuantoOsQueTentamOuPretendemComercializarSeusProdutos` | 46 | OEmpreendimento Tem Encontrado Alguma Dificuldade Na Comercialização De Produtos Eou Serviçosconsiderar Tanto Os Empreendimentos Que Já Estão Comercializando Quanto Os Que Tentam Ou Pretendem Comercializar Seus Produtos | boolean |  |
| `_35A55__47QuaisAsPrincipaisDificuldadesNaComercializaçãoDosProdutosrespostaMúltipla` | 47 | Quais As Principais Dificuldades Na Comercialização Dos Produtosresposta Múltipla | multi_select |  |
| `_35A55_Mulheres` |  | Mulheres | numeric |  |
| `_35A55_Homens` |  | Homens | numeric |  |
| `_35A55__49OEmpreendimentoEstáConseguindoRemunerarOsasSóciosasQueTrabalham` | 49 | OEmpreendimento Está Conseguindo Remunerar Osas Sóciosas Que Trabalham | boolean |  |
| `_35A55__50QualOValorMédioDaRemuneraçãoretiradaMensalvalorMédioMensal` | 50 | Qual OValor Médio Da Remuneraçãoretirada Mensalvalor Médio Mensal | numeric_or_text |  |
| `_35A55__51DeManeiraPreponderanteARendaObtidaPelosasSóciosasNoEmpreendimentoÉrespostaÚnica` | 51 | De Maneira Preponderante ARenda Obtida Pelosas Sóciosas No Empreendimento ÉrespostaÚnica | single_select |  |
| `_35A55__52ComoÉFeitaARemuneraçãoOuRetiradaDosasSóciosasrespostaMúltipla` | 52 | Como ÉFeita ARemuneração Ou Retirada Dosas Sóciosasresposta Múltipla | multi_select |  |
| `_35A55__53QualOValorDaMenorRetiradaremuneraçãoDosasSóciosasDoEmpreendimento` | 53 | Qual OValor Da Menor Retiradaremuneração Dosas Sóciosas Do Empreendimento | numeric_or_text |  |
| `_35A55__55QuaisSãoOsBenefíciosAsGarantiasEOsDireitosDosasSóciosasQueTrabalhamNoEmpreendimentorespostaMúltipla` | 55 | Quais São Os Benefícios As Garantias EOs Direitos Dosas Sóciosas Que Trabalham No Empreendimentoresposta Múltipla | multi_select |  |

## Bloco condicional — Comercialização (perguntas 56–74)

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `_56A74__56QuaisAsPrincipaisFormasDeOrganizaçãoDaComercializaçãoUtilizadasPeloEmpreendimentorespostaMúltipla` | 56 | Quais As Principais Formas De Organização Da Comercialização Utilizadas Pelo Empreendimentoresposta Múltipla | multi_select |  |
| `_56A74__57QualAQuantidadeDeProdutositensComercializadosPeloEmpreendimento` | 57 | Qual AQuantidade De Produtositens Comercializados Pelo Empreendimento | numeric |  |
| `_56A74__59QualOFaturamentovolumeDeVendasMensalObtidoPeloEmpreendimentovalorMédioMensal` | 59 | Qual OFaturamentovolume De Vendas Mensal Obtido Pelo Empreendimentovalor Médio Mensal | numeric_or_text |  |
| `_56A74__60QualAOrigemDosProdutosComercializadosrespostaMúltipla` | 60 | Qual AOrigem Dos Produtos Comercializadosresposta Múltipla | multi_select |  |
| `_56A74__61ComoSãoFeitosOsPagamentosDosProdutosComercializadosrespostaMúltipla` | 61 | Como São Feitos Os Pagamentos Dos Produtos Comercializadosresposta Múltipla | multi_select |  |
| `_56A74__62QuantoOEmpreendimentoGastaMensalmenteComAAquisiçãoDosProdutosvalorMédioMensal` | 62 | Quanto OEmpreendimento Gasta Mensalmente Com AAquisição Dos Produtosvalor Médio Mensal | numeric_or_text |  |
| `_56A74__63OsasSóciosasPagamAlgumaTaxaOuContribuiçãoParaOEmpreendimento` | 63 | Osas Sóciosas Pagam Alguma Taxa Ou Contribuição Para OEmpreendimento | boolean |  |
| `_56A74__64QualAFormaDeContribuiçãoUtilizadarespostaMúltipla` | 64 | Qual AForma De Contribuição Utilizadaresposta Múltipla | multi_select |  |
| `_56A74__65DeManeiraPreponderanteARendaObtidaPelosasSóciosasComAComercializaçãoÉrespostaÚnica` | 65 | De Maneira Preponderante ARenda Obtida Pelosas Sóciosas Com AComercialização ÉrespostaÚnica | single_select |  |
| `_56A74__66ParaQuemÉFeitaAComercializaçãoDeProdutosDoEmpreendimentorespostaMúltipla` | 66 | Para Quem ÉFeita AComercialização De Produtos Do Empreendimentoresposta Múltipla | multi_select |  |
| `_56A74__67AVendaEouTrocaDeProdutosRealizasePrincipalmenteNorespostaMúltipla` | 67 | AVenda Eou Troca De Produtos Realizase Principalmente Noresposta Múltipla | multi_select |  |
| `_56A74__68OEmpreendimentoTemEncontradoAlgumaDificuldadeParaAComercialização` | 68 | OEmpreendimento Tem Encontrado Alguma Dificuldade Para AComercialização | boolean |  |
| `_56A74__69QuaisAsPrincipaisDificuldadesNaComercializaçãoDosProdutosrespostaMúltipla` | 69 | Quais As Principais Dificuldades Na Comercialização Dos Produtosresposta Múltipla | multi_select |  |
| `_56A74__70QuemÉResponsávelPelasVendasNoEmpreendimentorespostaMúltipla` | 70 | Quem ÉResponsável Pelas Vendas No Empreendimentoresposta Múltipla | multi_select |  |
| `_56A74_SemTítulo2_Mulheres` |  | Mulheres | text |  |
| `_56A74_SemTítulo2_Homens` |  | Homens | text |  |
| `_56A74_SemTítulo2_Total` |  | Total | text |  |
| `_56A74_SemTítulo2__72OEmpreendimentoEstáConseguindoRemunerarOsasSóciosasQueRealizamAsVendas` | 72 | OEmpreendimento Está Conseguindo Remunerar Osas Sóciosas Que Realizam As Vendas | text |  |
| `_56A74_SemTítulo2__73aRemuneraçãoFixaQualOValorMédioMensal` | 73a | Remuneração Fixa Qual OValor Médio Mensal | numeric_or_text |  |
| `_56A74_SemTítulo2__73bComissãoSobreValorDasVendascomissãoQualOPercentual` | 73b | Comissão Sobre Valor Das Vendascomissão Qual OPercentual | numeric_or_text |  |
| `_56A74_SemTítulo2__73cRemuneraçãoPorHorasTrabalhadasQualOValorMédioPorHora` | 73c | Remuneração Por Horas Trabalhadas Qual OValor Médio Por Hora | numeric_or_text |  |
| `_56A74_SemTítulo2__74QuaisSãoOsBenefíciosAsGarantiasEOsDireitosDosasSóciosasQueTrabalhamNoEmpreendimentorespostaMúltipla` | 74 | Quais São Os Benefícios As Garantias EOs Direitos Dosas Sóciosas Que Trabalham No Empreendimentoresposta Múltipla | multi_select |  |

## Bloco condicional — Prestação de Serviços (perguntas 75–93)

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `_75A93__75QuantosTiposDeServiçoSãoPrestadosPeloEmpreendimento` | 75 | Quantos Tipos De Serviço São Prestados Pelo Empreendimento | integer |  |
| `_75A93__77QualOFaturamentoMensalDoEmpreendimentovalorMédioMensal` | 77 | Qual OFaturamento Mensal Do Empreendimentovalor Médio Mensal | numeric_or_text |  |
| `_75A93__79QualAOrigemDosInsumosUtilizadosParaAPrestaçãoDeServiçosrespostaMúltipla` | 79 | Qual AOrigem Dos Insumos Utilizados Para APrestação De Serviçosresposta Múltipla | multi_select |  |
| `_75A93__80QuantoOEmpreendimentoGastaNaAquisiçãoDeTodosOsInsumosmatériasprimasUtilizadosvalorMédioMensal` | 80 | Quanto OEmpreendimento Gasta Na Aquisição De Todos Os Insumosmatériasprimas Utilizadosvalor Médio Mensal | numeric_or_text |  |
| `_75A93__81AQuemPertencemOsInstrumentosFerramentasOuEquipamentosUtilizadosPeloEESrespostaMúltipla` | 81 | AQuem Pertencem Os Instrumentos Ferramentas Ou Equipamentos Utilizados Pelo EESresposta Múltipla | multi_select |  |
| `_75A93__82ComoÉFeitaAPrestaçãoDeServiçosPeloEmpreendimentorespostaMúltipla` | 82 | Como ÉFeita APrestação De Serviços Pelo Empreendimentoresposta Múltipla | multi_select |  |
| `_75A93__83ParaQuemSeDestinaAPrestaçãoDeServiçosrespostaMúltipla` | 83 | Para Quem Se Destina APrestação De Serviçosresposta Múltipla | multi_select |  |
| `_75A93__84OEmpreendimentoTemEncontradoAlgumaDificuldadeNaVendaDosServiçosconsiderarTantoOsEmpreendimentosQueJáEstãoComercializandoQuantoOsQueTentamOuPretendemComercializarSeusServiços` | 84 | OEmpreendimento Tem Encontrado Alguma Dificuldade Na Venda Dos Serviçosconsiderar Tanto Os Empreendimentos Que Já Estão Comercializando Quanto Os Que Tentam Ou Pretendem Comercializar Seus Serviços | text |  |
| `_75A93__85QuaisAsPrincipaisDificuldadesNaComercializaçãoDosServiçosrespostaMúltipla` | 85 | Quais As Principais Dificuldades Na Comercialização Dos Serviçosresposta Múltipla | multi_select |  |
| `_75A93__86aMulheresquantas` | 86a | Mulheresquantas | integer |  |
| `_75A93__86bHomensquantos` | 86b | Homensquantos | integer |  |
| `_75A93__86cTotalquantos` | 86c | Totalquantos | integer |  |
| `_75A93__87OEmpreendimentoEstáConseguindoRemunerarOsasSóciosasQueTrabalham` | 87 | OEmpreendimento Está Conseguindo Remunerar Osas Sóciosas Que Trabalham | text |  |
| `_75A93_SemTítulo3__88QualOValorMédioDaRetiradaMensalvalorMédioMensal` | 88 | Qual OValor Médio Da Retirada Mensalvalor Médio Mensal | numeric_or_text |  |
| `_75A93_SemTítulo3__89DeManeiraPreponderanteARendaObtidaPelosasSóciosasNoEmpreendimentoÉrespostaÚnica` | 89 | De Maneira Preponderante ARenda Obtida Pelosas Sóciosas No Empreendimento ÉrespostaÚnica | single_select |  |
| `_75A93_SemTítulo3__90ComoÉFeitaARemuneraçãoOuRetiradaDosasSóciosasrespostaMúltipla` | 90 | Como ÉFeita ARemuneração Ou Retirada Dosas Sóciosasresposta Múltipla | multi_select |  |
| `_75A93_SemTítulo3__91QualOValorDaMenorRetiradaremuneraçãoDosasSóciosasDoEmpreendimento` | 91 | Qual OValor Da Menor Retiradaremuneração Dosas Sóciosas Do Empreendimento | numeric_or_text |  |
| `_75A93_SemTítulo3__92QualOValorDaMaiorRetiradaremuneraçãoDosasSóciosasDoEmpreendimento` | 92 | Qual OValor Da Maior Retiradaremuneração Dosas Sóciosas Do Empreendimento | numeric_or_text |  |
| `_75A93__93QuaisSãoOsBenefíciosAsGarantiasEOsDireitosDosasSóciosasQueTrabalhamNoEmpreendimentorespostaMúltipla` | 93 | Quais São Os Benefícios As Garantias EOs Direitos Dosas Sóciosas Que Trabalham No Empreendimentoresposta Múltipla | multi_select |  |

## Bloco condicional — Crédito/Finanças Solidárias (perguntas 94–110)

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `_94A110__94QualAFormaDeOrganizaçãorespostaÚnica` | 94 | Qual AForma De OrganizaçãorespostaÚnica | single_select |  |
| `_94A110__95QuantosTiposDeServiçosDeCréditoOuFinanceirosSãoFornecidos` | 95 | Quantos Tipos De Serviços De Crédito Ou Financeiros São Fornecidos | integer |  |
| `_94A110__97QualAOrigemDosRecursosOperadosPeloEmpreendimentorespostaMúltipla` | 97 | Qual AOrigem Dos Recursos Operados Pelo Empreendimentoresposta Múltipla | multi_select |  |
| `_94A110__98QualOVolumeDeRecursosQueCompõeOFundoDoEmpreendimento` | 98 | Qual OVolume De Recursos Que Compõe OFundo Do Empreendimento | text |  |
| `_94A110__99QualAQuantidadeDeRecursosContratadosOuRepassadosvalorMédioMensal` | 99 | Qual AQuantidade De Recursos Contratados Ou Repassadosvalor Médio Mensal | numeric_or_text |  |
| `_94A110__100ExisteAlgumaDefiniçãoQuantoAosLimitesMínimosEouMáximosParaOEmpréstimorepasseDeRecursos` | 100 | Existe Alguma Definição Quanto Aos Limites Mínimos Eou Máximos Para OEmpréstimorepasse De Recursos | text |  |
| `_94A110_SemTítulo2__101QualOValorMínimolimiteMínimo` | 101 | Qual OValor Mínimolimite Mínimo | numeric_or_text |  |
| `_94A110_SemTítulo2__102QualOValorMáximoteto` | 102 | Qual OValor Máximoteto | numeric_or_text |  |
| `_94A110__103OsRecursosRepassadosemprestadosSãoDevolvidosDeManeirarespostaMúltipla` | 103 | Os Recursos Repassadosemprestados São Devolvidos De Maneiraresposta Múltipla | multi_select |  |
| `_94A110_SemTítulo3__104ADevoluçãopagamentoDosEmpréstimosrepassesUtilizadosPeloEmpreendimentoOcorreSobFormaDerespostaMúltipla` | 104 | ADevoluçãopagamento Dos Empréstimosrepasses Utilizados Pelo Empreendimento Ocorre Sob Forma Deresposta Múltipla | multi_select |  |
| `_94A110_SemTítulo3__105QualONívelDeInadimplênciaDosContratosoperaçõesEfetuados` | 105 | Qual ONível De Inadimplência Dos Contratosoperações Efetuados | text |  |
| `_94A110__106QuaisSãoAsModalidadesDeGarantiaUtilizadasrespostaMúltipla` | 106 | Quais São As Modalidades De Garantia Utilizadasresposta Múltipla | multi_select |  |
| `_94A110__107ExistemSóciosasQueTrabalhamNoEmpreendimento` | 107 | Existem Sóciosas Que Trabalham No Empreendimento | text |  |
| `_94A110_SemTítulo4_Mulheresquantas` |  | Mulheresquantas | integer |  |
| `_94A110_SemTítulo4_Homensquantos` |  | Homensquantos | integer |  |
| `_94A110_SemTítulo4_Totalquantos` |  | Totalquantos | integer |  |
| `_94A110_SemTítulo4__109aRemuneraçãoFixaQualOValorMédioMensal` | 109a | Remuneração Fixa Qual OValor Médio Mensal | numeric_or_text |  |
| `_94A110_SemTítulo4__109bComissãoSobreOValorDasOperaçõesQualOPercentual` | 109b | Comissão Sobre OValor Das Operações Qual OPercentual | numeric_or_text |  |
| `_94A110_SemTítulo4__109cRemuneraçãoPorHorasTrabalhadasQualOValorMédioPorHora` | 109c | Remuneração Por Horas Trabalhadas Qual OValor Médio Por Hora | numeric_or_text |  |
| `_94A110_SemTítulo4__109d` | 109d | _94 A110_Sem Título4__109d | text |  |
| `_94A110_SemTítulo4__110QuaisSãoOsBenefíciosAsGarantiasEOsDireitosDosasSóciosasQueTrabalhamNoEmpreendimentorespostaMúltipla` | 110 | Quais São Os Benefícios As Garantias EOs Direitos Dosas Sóciosas Que Trabalham No Empreendimentoresposta Múltipla | multi_select |  |

## Bloco condicional — Consumo (perguntas 111–121)

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `_111A121__111QualÉOTipoDoEmpreendimentorespostaÚnica` | 111 | Qual ÉOTipo Do EmpreendimentorespostaÚnica | single_select |  |
| `_111A121__112QualAQuantidadeDeBensEouServiçosConsumidosPrestadosEouUtilizadosColetivamenteNoEmpreendimento` | 112 | Qual AQuantidade De Bens Eou Serviços Consumidos Prestados Eou Utilizados Coletivamente No Empreendimento | numeric |  |
| `_111A121__114QualAFormaDePagamentoPeloConsumoOuUsoDosBensEouServiçosrespostaMúltipla` | 114 | Qual AForma De Pagamento Pelo Consumo Ou Uso Dos Bens Eou Serviçosresposta Múltipla | multi_select |  |
| `_111A121__115QualAReceitaMensalObtidaPeloEmpreendimentovalorMédioMensal` | 115 | Qual AReceita Mensal Obtida Pelo Empreendimentovalor Médio Mensal | numeric_or_text |  |
| `_111A121__116QuantoOEmpreendimentoGastaMensalmenteComAAquisiçãoEouManutençãoDosBensEouServiçosvalorMédioMensal` | 116 | Quanto OEmpreendimento Gasta Mensalmente Com AAquisição Eou Manutenção Dos Bens Eou Serviçosvalor Médio Mensal | numeric_or_text |  |
| `_111A121__117QualAOrigemDosBensProdutosOuServiçosrespostaMúltipla` | 117 | Qual AOrigem Dos Bens Produtos Ou Serviçosresposta Múltipla | multi_select |  |
| `_111A121__118ExistemSóciosasResponsáveisPelasAtividadesqueTrabalhamNoEmpreendimento` | 118 | Existem Sóciosas Responsáveis Pelas Atividadesque Trabalham No Empreendimento | boolean |  |
| `_111A121_SemTítulo3__119aMulheresquantas` | 119a | Mulheresquantas | integer |  |
| `_111A121_SemTítulo3__119bHomensquantos` | 119b | Homensquantos | integer |  |
| `_111A121_SemTítulo3__119cTotalquantos` | 119c | Totalquantos | integer |  |
| `_111A121_SemTítulo3__120aRemuneraçãoFixaQualOValorMédioMensal` | 120a | Remuneração Fixa Qual OValor Médio Mensal | numeric_or_text |  |
| `_111A121_SemTítulo3__120bComissãoSobreValorDasVendascomissãoQualOPercentual` | 120b | Comissão Sobre Valor Das Vendascomissão Qual OPercentual | numeric_or_text |  |
| `_111A121_SemTítulo3__120c` | 120c | _111 A121_Sem Título3__120c | text |  |
| `_111A121_SemTítulo3__121QuaisDestesBenefíciosGarantiasEDireitosParaSóciosasQueTrabalhamNoEmpreendimentorespostaMúltipla` | 121 | Quais Destes Benefícios Garantias EDireitos Para Sóciosas Que Trabalham No Empreendimentoresposta Múltipla | multi_select |  |

## Seção V — Situação do Trabalho dos/as Não-Sócios/as

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS__122OEmpreendimentoContrataTrabalhadoresasNãosóciosas` | 122 | OEmpreendimento Contrata Trabalhadoresas Nãosóciosas | boolean |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2__123aMulheresquantas` | 123a | Mulheresquantas | integer |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2__123bHomensquantos` | 123b | Homensquantos | integer |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2__123cTotalquantos` | 123c | Totalquantos | integer |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2__124QualAFormaDeContrataçãoDosasTrabalhadoresasNãosóciosasrespostaMúltipla` | 124 | Qual AForma De Contratação Dosas Trabalhadoresas Nãosóciosasresposta Múltipla | multi_select |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126a` | 126a | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126a | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126b` | 126b | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126b | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126c` | 126c | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126c | multi_select |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126d` | 126d | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126d | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126f` | 126f | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126f | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126g` | 126g | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126g | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126h` | 126h | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126h | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126i` | 126i | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126i | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126j` | 126j | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126j | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126k` | 126k | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126k | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126l` | 126l | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126l | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2_SemTítulo__126m` | 126m | Seção VSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_Sem Título2_Sem Título__126m | text |  |
| `SeçãoVSITUAÇÃODOTRABALHODOSASNÃOSÓCIOSAS_SemTítulo2__127QuantoOEmpreendimentoGastaEmMédiaMensalmenteComOPagamentoDeTrabalhadoresasNãosóciosasvalorMédioMensal` | 127 | Quanto OEmpreendimento Gasta Em Média Mensalmente Com OPagamento De Trabalhadoresas Nãosóciosasvalor Médio Mensal | numeric_or_text |  |

## Seção VI — Investimentos, Acesso a Crédito e Apoios

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS__128QualAOrigemDosRecursosParaIniciarAsAtividadesDoEmpreendimentorespostaMúltipla` | 128 | Qual AOrigem Dos Recursos Para Iniciar As Atividades Do Empreendimentoresposta Múltipla | multi_select |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS__129ForamRealizadosInvestimentosNoEmpreendimentoNosÚltimos12Meses` | 129 | Foram Realizados Investimentos No Empreendimento NosÚltimos12 Meses | boolean |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo__130QualOTipoDeInvestimentoRealizadorespostaMúltipla` | 130 | Qual OTipo De Investimento Realizadoresposta Múltipla | multi_select |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo__131QualOValorDoInvestimentoRealizado` | 131 | Qual OValor Do Investimento Realizado | numeric_or_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS__132QuantoÀBuscaDeCréditoOuFinanciamentoNosÚltimos12MesesOEmpreendimentorespostaÚnica` | 132 | Quanto ÀBusca De Crédito Ou Financiamento NosÚltimos12 Meses OEmpreendimentorespostaÚnica | single_select |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS__133PorQueOEmpreendimentoNãoBuscouCréditoOuFinanciamentorespostaMúltipla` | 133 | Por Que OEmpreendimento Não Buscou Crédito Ou Financiamentoresposta Múltipla | multi_select |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS__134QualAFinalidadeDoCréditoOuFinanciamentorespostaMúltipla` | 134 | Qual AFinalidade Do Crédito Ou Financiamentoresposta Múltipla | multi_select |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo2__135aBancoPúblicoQual` | 135a | Banco Público Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo2__135bBancoPrivadoQual` | 135b | Banco Privado Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo2__135cBancoDoPovoOuSimilarQual` | 135c | Banco Do Povo Ou Similar Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo2__135dCooperativaDeCréditoQual` | 135d | Cooperativa De Crédito Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo2__135eOutraInstituiçãoFinanceiraPrivadaQual` | 135e | Outra Instituição Financeira Privada Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo2__135fONGOuOSCIPQual` | 135f | ONGOu OSCIPQual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo2__135gFundoSolidárioOuBancoComunitárioQual` | 135g | Fundo Solidário Ou Banco Comunitário Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo2__135hOutraQual` | 135h | Outra Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo2__136QualOValorTotalDoCréditoAoQualOEmpreendimentoTeveAcessoNosÚltimos12Meses` | 136 | Qual OValor Total Do Crédito Ao Qual OEmpreendimento Teve Acesso NosÚltimos12 Meses | numeric_or_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo2__137QualASituaçãoAtualDoPagamentoOuDevoluçãoDoCréditoOuFinanciamentorespostaÚnica` | 137 | Qual ASituação Atual Do Pagamento Ou Devolução Do Crédito Ou FinanciamentorespostaÚnica | single_select |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS__138AtualmenteExisteNecessidadeDeCréditoOuFinanciamento` | 138 | Atualmente Existe Necessidade De Crédito Ou Financiamento | boolean |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo3__139ParaQuêÉNecessárioOCréditoOuFinanciamentorespostaMúltipla` | 139 | Para Quê ÉNecessário OCrédito Ou Financiamentoresposta Múltipla | multi_select |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo3__140OEmpreendimentoEstáEnfrentandoDificuldadesParaAObtençãoDeCréditoOuFinanciamento` | 140 | OEmpreendimento Está Enfrentando Dificuldades Para AObtenção De Crédito Ou Financiamento | boolean |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo3__141QualaisDificuldadesrespostaMúltipla` | 141 | Qualais Dificuldadesresposta Múltipla | multi_select |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS__142OEmpreendimentoTeveAcessoAAlgumTipoDeAssessoriaAssistênciaOuCapacitação` | 142 | OEmpreendimento Teve Acesso AAlgum Tipo De Assessoria Assistência Ou Capacitação | boolean |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__143QueTipoDeApoioemAssessoriaAssistênciaOuCapacitaçãoOEmpreendimentoTeverespostaMúltipla` | 143 | Que Tipo De Apoioem Assessoria Assistência Ou Capacitação OEmpreendimento Teveresposta Múltipla | multi_select |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144aONGsOSCIPsQual` | 144a | ONGs OSCIPs Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144bIgrejasPastoraisEtcQual` | 144b | Igrejas Pastorais Etc Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144cAssociaçõesEConselhosComunitáriosEtcQual` | 144c | Associações EConselhos Comunitários Etc Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144dPrefeituraSecretariaÓrgão` | 144d | Prefeitura Secretaria Órgão | text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144eGovernoEstadualSecretariaÓrgão` | 144e | Governo Estadual Secretaria Órgão | text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144fGovernoFederalSecretariaÓrgão` | 144f | Governo Federal Secretaria Órgão | text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144gUniversidadesincubadorasUnitrabalhoQual` | 144g | Universidadesincubadoras Unitrabalho Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144hSistemaSSebraeSescoopEtcQual` | 144h | Sistema SSebrae Sescoop Etc Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144iCooperativasDeTécnicosasQual` | 144i | Cooperativas De Técnicosas Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144jMovimentoSindicalCentralSindicatoFederaçãoQual` | 144j | Movimento Sindical Central Sindicato Federação Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144kOutroEmpreendimentoOuEntidadeDeRepresentaçãoQual` | 144k | Outro Empreendimento Ou Entidade De Representação Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144lFornecedorOuCompradorparceriaQual` | 144l | Fornecedor Ou Compradorparceria Qual | conditional_text |  |
| `SeçãoVIINVESTIMENTOSACESSOACRÉDITOEAPOIOS_SemTítulo4__144mOutraQual` | 144m | Outra Qual | conditional_text |  |

## Seção VII — Gestão do Empreendimento

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `SeçãoVIIGESTÃODOEMPREENDIMENTO__145QuaisAsInstânciasDeDireçãoECoordenaçãoDoEmpreendimentorespostaMúltipla` | 145 | Quais As Instâncias De Direção ECoordenação Do Empreendimentoresposta Múltipla | multi_select |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO__146OQueÉDecididoEmAssembleiaGeralReuniãoDoColetivoDeSóciosasrespostaMúltipla` | 146 | OQue ÉDecidido Em Assembleia Geral Reunião Do Coletivo De Sóciosasresposta Múltipla | multi_select |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO__147QualAPeriodicidadeDeRealizaçãoDaAssembleiaGeralEouReuniãoColetivaDeSóciosasNoEmpreendimentorespostaÚnica` | 147 | Qual APeriodicidade De Realização Da Assembleia Geral Eou Reunião Coletiva De Sóciosas No EmpreendimentorespostaÚnica | single_select |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO_SemTítulo__148NaÚltimaAssembleiaGeralEouReuniãoColetivaDeSóciosasQuantosasSóciosasParticiparamrespostaÚnica` | 148 | NaÚltima Assembleia Geral Eou Reunião Coletiva De Sóciosas Quantosas Sóciosas ParticiparamrespostaÚnica | single_select |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO_SemTítulo__149QuaisOutrasFormasDeParticipaçãoDosasSóciosasrespostaMúltipla` | 149 | Quais Outras Formas De Participação Dosas Sóciosasresposta Múltipla | multi_select |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO_SemTítulo__150NoÚltimoAnoForamRealizadasAtividadesDeFormaçãoEouCampanhasDeSensibilizaçãoDosasSóciosas` | 150 | NoÚltimo Ano Foram Realizadas Atividades De Formação Eou Campanhas De Sensibilização Dosas Sóciosas | boolean |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO_SemTítulo__151QuaisForamOsTemasTratadosrespostaMúltipla` | 151 | Quais Foram Os Temas Tratadosresposta Múltipla | multi_select |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO__152HáQuantoTempoOAtualCoordenadorEouPresidenteExerceOCargoNoEmpreendimentorespostaÚnica` | 152 | Há Quanto Tempo OAtual Coordenador Eou Presidente Exerce OCargo No EmpreendimentorespostaÚnica | single_select |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO__153aMulheresquantas` | 153a | Mulheresquantas | integer |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO__153bHomensquantos` | 153b | Homensquantos | integer |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO__153cTotalquantos` | 153c | Totalquantos | integer |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO__154OsDirigentesRecebemRemuneraçãoOuGratificaçãoPeloExercícioDoCargoOuFunção` | 154 | Os Dirigentes Recebem Remuneração Ou Gratificação Pelo Exercício Do Cargo Ou Função | boolean |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO__155NoAnoAnteriorOsResultadosDaAtividadeEconômicaDoEmpreendimentoSemContarAsDoaçõesDeRecursosCasoExistamPermitiramrespostaÚnica` | 155 | No Ano Anterior Os Resultados Da Atividade Econômica Do Empreendimento Sem Contar As Doações De Recursos Caso Existam PermitiramrespostaÚnica | single_select |  |
| `SeçãoVIIGESTÃODOEMPREENDIMENTO__156SeHouveSobraexcedenteresposta1DaQuestãoAnteriorQualODestinorespostaMúltipla` | 156 | Se Houve Sobraexcedenteresposta1 Da Questão Anterior Qual ODestinoresposta Múltipla | multi_select |  |

## Seção VIII — Dimensão Sociopolítica e Ambiental

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL__157OEmpreendimentoParticipaDeAlgumFórumOuDeAlgumaRedeDeArticulaçãoOuRepresentação` | 157 | OEmpreendimento Participa De Algum Fórum Ou De Alguma Rede De Articulação Ou Representação | boolean |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL_SemTítulo__158aFórumOuRedeDeEconomiaSolidáriaQual` | 158a | Fórum Ou Rede De Economia Solidária Qual | conditional_text |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL_SemTítulo__158bUniãoOuAssociaçãoDeEESQual` | 158b | União Ou Associação De EESQual | conditional_text |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL_SemTítulo__158cFederaçõesDeCooperativasQual` | 158c | Federações De Cooperativas Qual | conditional_text |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL_SemTítulo__158dConselhosDeGestãoEFórunsDeParticipaçãoEmPolíticasPúblicas` | 158d | Conselhos De Gestão EFóruns De Participação Em Políticas Públicas | multi_select |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL_SemTítulo__158eOutrosFórunsRedesOuArticulaçõesQual` | 158e | Outros Fóruns Redes Ou Articulações Qual | conditional_text |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL__159OEmpreendimentoTemAlgumaRelaçãoOuParticipaDeMovimentosSociaisPopularesOuSindicais` | 159 | OEmpreendimento Tem Alguma Relação Ou Participa De Movimentos Sociais Populares Ou Sindicais | boolean |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL__160QualOTipoDeMovimentoOuLutaSocialrespostaMúltipla` | 160 | Qual OTipo De Movimento Ou Luta Socialresposta Múltipla | multi_select |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL__161OEmpreendimentoParticipaOuDesenvolveAlgumaAçãoSocialOuComunitária` | 161 | OEmpreendimento Participa Ou Desenvolve Alguma Ação Social Ou Comunitária | boolean |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL__162QualÁreaDeAtuaçãorespostaMúltipla` | 162 | Qual Área De Atuaçãoresposta Múltipla | multi_select |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL__163OQueOEmpreendimentoFazParaQualificarSeusProdutosEouServiçosNoIntuitoDeMelhorAtenderAosasConsumidoresasrespostaMúltipla` | 163 | OQue OEmpreendimento Faz Para Qualificar Seus Produtos Eou Serviços No Intuito De Melhor Atender Aosas Consumidoresasresposta Múltipla | multi_select |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL__164NoCasoDeProduçãoEOfertaDeProdutosOrgânicosOuLivresDeAgrotóxicosOsMesmosSãoCertificados` | 164 | No Caso De Produção EOferta De Produtos Orgânicos Ou Livres De Agrotóxicos Os Mesmos São Certificados | boolean |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL__165QualEntidadeFazACertificaçãoNomeDaEntidade` | 165 | Qual Entidade Faz ACertificação Nome Da Entidade | multi_select |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL__166OEmpreendimentoGeraAlgumTipoDeResíduolixoOuSobraDeMateriaisAPartirDaAtividadeProdutivaOuDaPrestaçãoDeServiços` | 166 | OEmpreendimento Gera Algum Tipo De Resíduolixo Ou Sobra De Materiais APartir Da Atividade Produtiva Ou Da Prestação De Serviços | boolean |  |
| `SeçãoVIIIDIMENSÃOSOCIOPOLÍTICAEAMBIENTAL__167QualOTratamentoEouDestinoDadoAosResíduosGeradosNoEmpreendimentorespostaMúltipla` | 167 | Qual OTratamento Eou Destino Dado Aos Resíduos Gerados No Empreendimentoresposta Múltipla | multi_select |  |

## Seção IX — Apreciações Subjetivas a Respeito do EES

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `SeçãoIXAPRECIAÇÕESSUBJETIVASARESPEITODOEES__168OQueMotivouACriaçãoDoEmpreendimentorespostaMúltipla` | 168 | OQue Motivou ACriação Do Empreendimentoresposta Múltipla | multi_select |  |
| `SeçãoIXAPRECIAÇÕESSUBJETIVASARESPEITODOEES__169QuaisAsPrincipaisConquistasObtidasPeloEmpreendimentorespostaMúltipla` | 169 | Quais As Principais Conquistas Obtidas Pelo Empreendimentoresposta Múltipla | multi_select |  |
| `SeçãoIXAPRECIAÇÕESSUBJETIVASARESPEITODOEES__170QuaisOsPrincipaisDesafiosDoEmpreendimentorespostaMúltipla` | 170 | Quais Os Principais Desafios Do Empreendimentoresposta Múltipla | multi_select |  |

## Autorização para Uso das Informações do SIES

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `AUTORIZAÇÃOPARAOUSODASINFORMAÇÕESDOSIESCONFORMEPORTARIAMINISTERIAL__171OEmpreendimentoAutorizaAUtilizaçãoDeInformaçõesRelativasÀIdentificaçãoEÀsAtividadesEconômicasComOObjetivoDeFortalecerEDivulgarAEconomiaSolidária` | 171 | OEmpreendimento Autoriza AUtilização De Informações Relativas ÀIdentificação EÀs Atividades Econômicas Com OObjetivo De Fortalecer EDivulgar AEconomia Solidária | boolean |  |

## Dados das Pessoas Entrevistadas (PII — não publicar)

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `DADOSDASPESSOASENTREVISTADAS_Nome` |  | Nome | text | ⚠️ SIM |
| `DADOSDASPESSOASENTREVISTADAS_CargoNoEmpreendimento` |  | Cargo No Empreendimento | text | ⚠️ SIM |
| `DADOSDASPESSOASENTREVISTADAS_TelefoneDeContato` |  | Telefone De Contato | text | ⚠️ SIM |
| `DADOSDASPESSOASENTREVISTADAS_Data` |  | Data | text | ⚠️ SIM |

## (sem seção — metadados/estrutura)

| Coluna bruta | Pergunta nº | Rótulo | Tipo | PII |
|---|---|---|---|---|
| `PesquisaEconomiaSolidária_Id` |  | Pesquisa Economia Solidária_Id | numeric |  |
| `Entry_Status` |  | Entry_Status | text |  |
| `Entry_DateCreated` |  | Entry_Date Created | text |  |
| `Entry_DateSubmitted` |  | Entry_Date Submitted | text |  |
| `Entry_DateUpdated` |  | Entry_Date Updated | text |  |
