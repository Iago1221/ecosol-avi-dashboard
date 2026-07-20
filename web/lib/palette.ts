// Paleta neutra provisória (nenhuma cor institucional da UNIDAVI/NUPESER confirmada
// ainda — ver docs/decisoes_e_riscos.md, risco nº 9). As cores são definidas como
// variáveis CSS em app/globals.css (com override para dark mode via
// prefers-color-scheme) e referenciadas aqui só pelo nome da variável, para que os
// gráficos (Recharts) se adaptem ao tema sem lógica JS extra.
//
// Regra de uso: série única de contagens (ex. município, forma de organização,
// atividades coletivas) -> `hueUnica`. Múltiplas séries lado a lado ou partes de um
// todo (ex. mulheres x homens, área de atuação) -> `categorica`, na ordem.

export const hueUnica = "var(--chart-hue-unica)";

export const categorica = [
  "var(--chart-cat-1)",
  "var(--chart-cat-2)",
  "var(--chart-cat-3)",
  "var(--chart-cat-4)",
  "var(--chart-cat-5)",
] as const;

export const naoInformado = "var(--chart-neutro)";
