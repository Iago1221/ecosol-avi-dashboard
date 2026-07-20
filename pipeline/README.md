# Pipeline de dados

Lê a planilha bruta de respostas, limpa/normaliza e gera os artefatos JSON consumidos
pelo site em `web/`.

## Setup

```bash
cd pipeline
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

## Rodar os testes

```bash
./.venv/bin/python -m pytest -q
```

## Gerar os dados

```bash
./.venv/bin/python src/build.py
# ou, para usar uma planilha diferente:
./.venv/bin/python src/build.py "../inputs/Respostas - Pesquisa Economia Solidária - NOVA.xlsx"
```

Saídas em `output/`:

- `core.json` — dataset público (sem PII), só respostas com autorização de uso confirmada.
- `full_raw.json` — **uso interno apenas** (tem PII, nunca é publicado nem copiado para `web/`).
- `aggregates/*.json` — um agregado pré-computado por campo do MVP.
- `data_dictionary.json` / `../docs/dicionario_de_dados.md` — dicionário de dados das 251 colunas.
- `quality_report.md` — divergências e exclusões encontradas na carga atual.
- `dataset_meta.json` — metadados da carga (data de geração, N incluído/total).

Veja `docs/como_atualizar_os_dados.md` (na raiz do projeto) para o passo a passo completo
de recarga quando uma nova planilha chegar.
