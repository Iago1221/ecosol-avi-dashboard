# Site (Next.js — export estático)

Dashboard público, consumindo os dados gerados pelo pipeline em `../pipeline/output/` (já
copiados para `web/data/`).

## Rodar localmente

```bash
npm install
npm run dev
```

Abra http://localhost:3000.

## Build estático

```bash
npm run build
npx serve -s out
```

Gera o site em `out/` — pasta de HTML/CSS/JS puro, sem servidor Node necessário em produção
(`next.config.ts` tem `output: "export"`).

## Estrutura

- `app/page.tsx` — painel principal (client component `Dashboard`, com filtros refletidos na URL).
- `app/metodologia/page.tsx` — ficha técnica e critérios de inclusão/exclusão.
- `components/charts/` — um componente por campo do MVP (Recharts).
- `lib/data.ts` — carrega os JSONs de `data/` com tipos fortes (`lib/types.ts`).
- `lib/aggregate-client.ts` — port das agregações do pipeline Python, usado só quando um
  filtro está ativo (a visão sem filtro usa os agregados pré-computados em `data/aggregates/`).
- `lib/palette.ts` + variáveis CSS em `app/globals.css` — paleta de cores (placeholder neutro,
  ver `docs/decisoes_e_riscos.md`).
- `data/` — cópia de `pipeline/output/core.json`, `dataset_meta.json` e `aggregates/*.json`.
  **Nunca copiar `full_raw.json` para cá** (tem PII).

Para atualizar os dados, veja `docs/como_atualizar_os_dados.md` na raiz do projeto.
