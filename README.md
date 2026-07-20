# Dashboard Economia Solidária — Alto Vale do Itajaí

Dashboard estático para análise dos dados da pesquisa de campo sobre empreendimentos de
Economia Solidária (EES) conduzida pelo NUPESER/UNIDAVI na região do Alto Vale do Itajaí (SC).

## Estrutura

- `inputs/` — arquivos de entrada (planilha de respostas e ficha de necessidades). A planilha
  não é versionada (contém PII) — veja `inputs/README.md`.
- `pipeline/` — script Python que lê a planilha bruta, limpa/normaliza os dados e gera os
  arquivos JSON consumidos pelo site (`pipeline/output/`).
- `web/` — site Next.js (export estático) que consome os JSONs gerados pelo pipeline e
  renderiza o dashboard.
- `docs/` — dicionário de dados, registro de decisões/riscos e runbook de atualização.

## Como rodar

Veja `pipeline/README.md` e `web/README.md` para instruções específicas de cada parte, e
`docs/como_atualizar_os_dados.md` para o passo a passo completo de recarga de dados.
