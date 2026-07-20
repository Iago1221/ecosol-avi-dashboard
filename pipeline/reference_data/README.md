# Dados de referência

## `municipios_alto_vale.csv`

Lista canônica de municípios usada por `clean.normalize_municipio` para validar/normalizar o
campo de município das respostas.

- Fonte dos 28 municípios com `membro_amavi=true`: [AMAVI — Municípios associados](https://amavi.org.br/municipios-associados/perfil)
  (Associação dos Municípios do Alto Vale do Itajaí), consultado em 2026-07-12.
- `Alfredo Wagner` foi incluído com `membro_amavi=false` porque apareceu como resposta válida
  na coleta de 23/02/2026 (linha 4) apesar de não ser município associado à AMAVI — está na
  divisa da região e pode estar dentro da área de abrangência da pesquisa do NUPESER mesmo
  sem integrar formalmente a associação. **Confirmar com o NUPESER se isso é esperado** (risco
  nº 6 do plano) antes de tratar futuras respostas fora da lista AMAVI como erro de digitação.
- A coluna `observado_na_pesquisa_23_02_2026` é só um registro do snapshot atual, não afeta a
  validação — serve para saber rapidamente quais municípios já têm dado.
- Não inclui código IBGE (seria necessário para um mapa geográfico no futuro — ver risco nº 10
  do plano); buscar de fonte oficial (IBGE) quando essa funcionalidade for priorizada.

Qualquer valor de município que não normalizar para uma linha desta lista faz o pipeline
**falhar** (`validate.py`), não descartar silenciosamente — isso é intencional: nomes de
município são poucos e um valor não reconhecido quase sempre é erro de digitação novo que
merece revisão humana, não uma correção automática silenciosa.

## `aliases_geograficos.yaml`

Correções pontuais que não são resolvidas por dobra de acento/caixa (ex.: erros de digitação
que removem uma letra, como "Santa Catarna" em vez de "Santa Catarina"). Novos casos
encontrados em futuras cargas devem ser adicionados aqui.
