import type { Metadata } from "next";
import { datasetMeta } from "@/lib/data";

export const metadata: Metadata = {
  title: "Metodologia — Economia Solidária Alto Vale do Itajaí",
};

export default function MetodologiaPage() {
  const excluidos =
    datasetMeta.total_linhas_coletadas - datasetMeta.total_linhas_incluidas_no_publico;
  const geradoEm = new Date(datasetMeta.gerado_em).toLocaleDateString("pt-BR", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  return (
    <article className="flex max-w-3xl flex-col gap-1 rounded-xl border border-black/10 bg-white p-6 dark:border-white/10 dark:bg-zinc-900">
      <h1 className="text-2xl font-semibold">Metodologia</h1>

      <h2 className="mt-6 text-lg font-semibold">Ficha técnica</h2>
      <ul className="list-disc pl-5 text-sm leading-relaxed">
        <li>
          Total de formulários coletados na carga atual: <strong>{datasetMeta.total_linhas_coletadas}</strong>
        </li>
        <li>
          Incluídos nesta visão pública: <strong>{datasetMeta.total_linhas_incluidas_no_publico}</strong>
        </li>
        <li>
          Excluídos: <strong>{excluidos}</strong>
        </li>
        <li>Dados gerados em: {geradoEm}</li>
      </ul>

      <h2 className="mt-6 text-lg font-semibold">Critério de inclusão</h2>
      <p className="text-sm leading-relaxed">
        Um formulário entra nesta visão pública quando o empreendimento confirmou, no próprio
        instrumento de coleta, a autorização para uso das informações relativas à identificação e
        às atividades econômicas (conforme a Portaria Ministerial do SIES). Esse critério é
        independente do status de preenchimento do formulário — respostas marcadas como
        &quot;incompletas&quot; mas com autorização confirmada e dados demográficos preenchidos são
        incluídas; respostas sem essa confirmação são excluídas, mesmo quando parcialmente
        preenchidas.
      </p>

      <h2 className="mt-6 text-lg font-semibold">O que é exibido</h2>
      <p className="text-sm leading-relaxed">
        O instrumento de coleta cobre um questionário completo no padrão do Sistema de
        Informações em Economia Solidária (SIES), com mais de 250 perguntas. Esta primeira versão
        do painel exibe apenas os 8 campos priorizados pelos stakeholders: município, área de
        atuação, sexo dos sócios/as, cor/raça, pertencimento a povo ou comunidade tradicional,
        forma de organização, participação em redes e atividades econômicas coletivas. Os demais
        dados do questionário (comercialização, crédito, gestão, dimensão socioambiental etc.)
        já foram estruturados internamente e podem alimentar novas visualizações no futuro sem
        necessidade de reprocessar a coleta.
      </p>

      <h2 className="mt-6 text-lg font-semibold">Qualidade dos dados</h2>
      <p className="text-sm leading-relaxed">
        Município e estado são normalizados contra uma lista de referência para corrigir
        inconsistências de grafia (maiúsculas/minúsculas, acentuação). O total de sócios/as é
        sempre recalculado a partir da soma de mulheres e homens declarados — o campo de total
        preenchido diretamente no formulário não é usado como fonte, pois apresentou
        inconsistências em parte das respostas da carga atual. Campos de cor/raça têm uma taxa de
        não-resposta parcial maior que os demais campos — o N efetivo de cada gráfico é sempre
        exibido junto ao título.
      </p>
    </article>
  );
}
