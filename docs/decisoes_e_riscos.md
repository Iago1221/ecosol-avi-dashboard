# Decisões e riscos

Registro vivo das decisões tomadas durante a implementação do dashboard e dos riscos
identificados que precisam de validação contínua com o NUPESER. Atualizar sempre que uma
decisão mudar ou um novo risco for identificado.

## Decisões tomadas

1. **Critério de inclusão pública = autorização confirmada, não status de preenchimento.**
   Um formulário entra em `core.json` quando a coluna de autorização de uso do SIES está
   `"Sim"`, independentemente de `Entry_Status` ser `Submitted` ou `Incomplete`. Na carga
   23/02/2026 isso incluiu 22 das 24 linhas (as 2 excluídas são as únicas sem confirmação).
2. **Total de sócios/as é sempre recalculado** (`mulheres + homens`), nunca lido do campo
   declarado — 5 das 24 linhas da carga atual tinham o campo declarado incorreto (0 quando
   deveria ser a soma). O valor declarado é mantido só como campo de auditoria interna.
3. **Escopo de exposição pública limitado aos 8 campos do MVP.** O pipeline processa e
   estrutura internamente as 251 colunas do questionário (`full_raw.json`), mas só os campos
   de identificação + os 8 campos priorizados pelos stakeholders vão para `core.json` e para
   o site. O termo de autorização do SIES consente divulgação de identificação + atividades
   econômicas — não estender a exposição pública além disso sem revisitar essa decisão.
4. **Site 100% estático, sem backend/banco de dados.** Dados são gerados uma vez pelo
   pipeline Python e servidos como JSON estático. Atualizar os dados é um processo manual
   (rodar o pipeline de novo e reimplantar o site) — ver `docs/como_atualizar_os_dados.md`.
5. **Paleta de cores é um placeholder neutro** (ver `web/lib/palette.ts` e
   `web/app/globals.css`) — nenhuma cor institucional da UNIDAVI/NUPESER foi confirmada.
6. **Repositório e hospedagem: GitHub público + GitHub Pages.** Código em
   `github.com/Iago1221/ecosol-avi-dashboard`, deploy automático via GitHub Actions
   (`.github/workflows/deploy.yml`) a cada push em `web/**` na branch `main`. Site publicado
   em `https://iago1221.github.io/ecosol-avi-dashboard/`. `next.config.ts` usa `basePath`
   fixo com esse nome de repositório — renomear o repo exige atualizar essa constante.

## Riscos abertos (precisam de validação com o NUPESER)

1. **PII no arquivo bruto** (telefone/e-mail/CNPJ do empreendimento, nome/telefone/cargo da
   pessoa entrevistada — ver `pipeline/reference_data/pii_columns.yaml`). O `.xlsx` bruto e
   `pipeline/output/full_raw.json` nunca devem ser publicados nem versionados (já cobertos
   pelo `.gitignore`); confirmar que a cópia mestra do `.xlsx` fica em local de acesso
   controlado fora deste repositório.
2. **Duas respostas "Incomplete" (linhas 6 e 7) estão incluídas no público** por terem
   autorização confirmada e dados demográficos parciais preenchidos — confirmar que isso é
   aceitável, já que outras seções do formulário dessas duas linhas podem estar vazias.
3. **"Total de sócios/as" declarado está incorreto em 5 linhas da carga atual** — vale
   reportar ao NUPESER para investigar se é erro de digitação no formulário original ou bug
   sistemático do instrumento de coleta.
4. **Não-resposta parcial elevada no campo "Cor"** — o N efetivo desse gráfico é menor que o
   dos demais campos do MVP; o painel já exibe o N ao lado de cada gráfico, mas vale
   considerar se isso merece destaque adicional na leitura dos dados.
5. **"Rural, Urbana" vs "Rural e Urbana"** tratados como equivalentes na normalização —
   confirmar com quem aplicou o formulário que ambas as grafias significam a mesma coisa.
6. **Lista canônica de municípios** (`pipeline/reference_data/municipios_alto_vale.csv`)
   inclui "Alfredo Wagner", que não é município associado à AMAVI mas apareceu como resposta
   válida na carga atual — confirmar se isso é esperado (área de abrangência da pesquisa pode
   ir além dos municípios formalmente associados à AMAVI).
7. **Risco de reidentificação por cruzamento de filtros em N pequeno** (ex. filtrar por um
   município com um único empreendimento respondente, cruzado com forma de organização) —
   considerado aceitável por serem organizações (não indivíduos) com consentimento explícito
   de divulgação, mas é uma decisão consciente, não um efeito colateral não discutido.
8. **Mapa geográfico dos municípios** (visual mais rico que a barra ranking atual) requer
   GeoJSON dos limites municipais — não obtido ainda; adiado para uma fase futura.
