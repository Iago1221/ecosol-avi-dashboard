# Como atualizar os dados

Runbook para quando uma nova exportação da planilha de respostas chegar. O site é estático
— não há atualização automática; siga estes passos manualmente.

## 1. Substituir a planilha de entrada

Copie a nova planilha `.xlsx` para `inputs/`, mantendo o nome descritivo (ex.:
`Respostas - Pesquisa Economia Solidária - DD_MM_AAAA.xlsx`). O arquivo antigo pode ser
removido ou mantido para histórico local (não é versionado no git de qualquer forma).

## 2. Rodar o pipeline

```bash
cd pipeline
./.venv/bin/python -m pytest -q          # confere que nada quebrou
./.venv/bin/python src/build.py "../inputs/Respostas - Pesquisa Economia Solidária - NOVA.xlsx"
```

Se o pipeline falhar com um erro de "Município não reconhecido", é sinal de um valor novo
não presente em `pipeline/reference_data/municipios_alto_vale.csv` — verifique se é erro de
digitação (corrija na fonte se possível) ou um município novo legítimo (adicione à lista).

## 3. Revisar o relatório de qualidade

Abra `pipeline/output/quality_report.md` e confira:

- Quantas linhas foram incluídas vs. excluídas do público, e por quê.
- Se surgiram novas divergências de "Total de sócios/as declarado vs. calculado".

## 4. Copiar os dados para o site

```bash
cp pipeline/output/core.json web/data/core.json
cp pipeline/output/dataset_meta.json web/data/dataset_meta.json
cp pipeline/output/aggregates/*.json web/data/aggregates/
```

**Nunca copie `pipeline/output/full_raw.json` para `web/data/`** — contém PII e não deve
chegar ao site público.

## 5. Rebuildar e testar o site localmente

```bash
cd web
npm run build
npx serve -s out
```

Abra `http://localhost:3000` (ou a porta indicada) e confira visualmente os 8 gráficos,
a página `/metodologia` e os filtros cruzados.

## 6. Reimplantar

Se hospedado em Vercel/Netlify: um novo deploy a partir do repositório atualizado já resolve
(a plataforma roda `npm run build` automaticamente). Se hospedado em servidor próprio da
UNIDAVI: copiar o conteúdo de `web/out/` para o diretório servido.

## 7. Conferência final

Compare manualmente 2–3 números do painel (ex. contagem por município, total de mulheres e
homens) contra a planilha nova aberta em uma ferramenta de planilhas, antes de anunciar a
atualização aos stakeholders.
