"use client";

import { useCallback, useMemo } from "react";
import { usePathname, useRouter, useSearchParams } from "next/navigation";

import { ChartCard } from "@/components/ChartCard";
import { FilterBar } from "@/components/filters/FilterBar";
import { BarRanking } from "@/components/charts/BarRanking";
import { CategoriaEmpilhada } from "@/components/charts/CategoriaEmpilhada";
import { GeneroChart } from "@/components/charts/GeneroChart";
import { CorChart } from "@/components/charts/CorChart";
import { PovoTradicionalCard } from "@/components/charts/PovoTradicionalCard";
import { ParticipaRedeCard } from "@/components/charts/ParticipaRedeCard";
import { StatTile } from "@/components/StatTile";
import { aggregates, coreRecords, datasetMeta } from "@/lib/data";
import {
  aggregateAreaAtuacao,
  aggregateAtividadesColetivas,
  aggregateCor,
  aggregateFormaOrganizacao,
  aggregateGenero,
  aggregateMunicipio,
  aggregateParticipaRede,
  aggregatePovoTradicional,
  aplicarFiltros,
  temFiltroAtivo,
  type Filtros,
} from "@/lib/aggregate-client";

function useFiltros(): [Filtros, (novo: Partial<Filtros>) => void, () => void] {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const filtros: Filtros = {
    municipio: searchParams.get("municipio"),
    areaAtuacao: searchParams.get("area") as Filtros["areaAtuacao"],
    formaOrganizacao: searchParams.get("forma"),
  };

  const atualizar = useCallback(
    (novo: Partial<Filtros>) => {
      const params = new URLSearchParams(searchParams.toString());
      const mapeamento: [keyof Filtros, string][] = [
        ["municipio", "municipio"],
        ["areaAtuacao", "area"],
        ["formaOrganizacao", "forma"],
      ];
      const combinado = { ...filtros, ...novo };
      for (const [chave, param] of mapeamento) {
        const valor = combinado[chave];
        if (valor) params.set(param, valor);
        else params.delete(param);
      }
      router.push(`${pathname}?${params.toString()}`);
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [pathname, router, searchParams]
  );

  const limpar = useCallback(() => router.push(pathname), [pathname, router]);

  return [filtros, atualizar, limpar];
}

export function Dashboard() {
  const [filtros, atualizarFiltros, limparFiltros] = useFiltros();
  const filtroAtivo = temFiltroAtivo(filtros);

  const registrosFiltrados = useMemo(
    () => (filtroAtivo ? aplicarFiltros(coreRecords, filtros) : coreRecords),
    [filtroAtivo, filtros]
  );

  const dados = useMemo(() => {
    if (!filtroAtivo) return aggregates;
    return {
      municipio: aggregateMunicipio(registrosFiltrados),
      areaAtuacao: aggregateAreaAtuacao(registrosFiltrados),
      genero: aggregateGenero(registrosFiltrados),
      cor: aggregateCor(registrosFiltrados),
      povoTradicional: aggregatePovoTradicional(registrosFiltrados),
      formaOrganizacao: aggregateFormaOrganizacao(registrosFiltrados),
      participaRede: aggregateParticipaRede(registrosFiltrados),
      atividadesColetivas: aggregateAtividadesColetivas(registrosFiltrados),
    };
  }, [filtroAtivo, registrosFiltrados]);

  const municipiosDisponiveis = useMemo(
    () =>
      Array.from(new Set(coreRecords.map((r) => r.municipio).filter((m): m is string => !!m))).sort(),
    []
  );
  const formasDisponiveis = useMemo(
    () =>
      Array.from(
        new Set(coreRecords.map((r) => r.forma_organizacao).filter((f): f is string => !!f))
      ).sort(),
    []
  );

  return (
    <div className="flex flex-col gap-6">
      <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        <StatTile valor={datasetMeta.total_linhas_incluidas_no_publico} rotulo="Empreendimentos" destaque />
        <StatTile valor={municipiosDisponiveis.length} rotulo="Municípios cobertos" />
        <StatTile
          valor={`${datasetMeta.total_linhas_coletadas - datasetMeta.total_linhas_incluidas_no_publico}`}
          rotulo="Excluídos (sem autorização confirmada)"
        />
        <StatTile
          valor={registrosFiltrados.length}
          rotulo={filtroAtivo ? "Empreendimentos no filtro atual" : "Sem filtro aplicado"}
        />
      </div>

      <FilterBar
        filtros={filtros}
        municipios={municipiosDisponiveis}
        formasOrganizacao={formasDisponiveis}
        onChange={atualizarFiltros}
        onLimpar={limparFiltros}
      />

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <ChartCard
          titulo="Município"
          nRespostasComDado={dados.municipio.n_respostas_com_dado}
          nTotalIncluido={dados.municipio.n_total_incluido}
        >
          <BarRanking
            data={dados.municipio.contagens.map((c) => ({ label: c.municipio, value: c.quantidade }))}
          />
        </ChartCard>

        <ChartCard
          titulo="Área de atuação"
          nRespostasComDado={dados.areaAtuacao.n_respostas_com_dado}
          nTotalIncluido={dados.areaAtuacao.n_total_incluido}
        >
          <CategoriaEmpilhada data={dados.areaAtuacao.contagens} />
        </ChartCard>

        <ChartCard
          titulo="Mulheres e homens (sócios/as)"
          nRespostasComDado={dados.genero.n_respostas_com_dado}
          nTotalIncluido={dados.genero.n_total_incluido}
        >
          <GeneroChart aggregate={dados.genero} />
        </ChartCard>

        <ChartCard
          titulo="Cor/raça dos sócios/as"
          nRespostasComDado={dados.cor.n_respostas_com_dado}
          nTotalIncluido={dados.cor.n_total_incluido}
          nota="Nem todo empreendimento respondeu esta pergunta por completo; o N amostral é menor que o dos demais campos."
        >
          <CorChart aggregate={dados.cor} />
        </ChartCard>

        <ChartCard
          titulo="Povo ou comunidade tradicional"
          nRespostasComDado={dados.povoTradicional.n_respostas_com_dado}
          nTotalIncluido={dados.povoTradicional.n_total_incluido}
        >
          <PovoTradicionalCard aggregate={dados.povoTradicional} />
        </ChartCard>

        <ChartCard
          titulo="Forma de organização"
          nRespostasComDado={dados.formaOrganizacao.n_respostas_com_dado}
          nTotalIncluido={dados.formaOrganizacao.n_total_incluido}
        >
          <BarRanking
            data={dados.formaOrganizacao.contagens.map((c) => ({ label: c.forma, value: c.quantidade }))}
          />
        </ChartCard>

        <ChartCard
          titulo="Participação em rede de produção, comercialização, consumo ou crédito"
          nRespostasComDado={dados.participaRede.n_respostas_com_dado}
          nTotalIncluido={dados.participaRede.n_total_incluido}
        >
          <ParticipaRedeCard aggregate={dados.participaRede} />
        </ChartCard>

        <ChartCard
          titulo="Atividades econômicas coletivas"
          nRespostasComDado={dados.atividadesColetivas.n_respostas_com_dado}
          nTotalIncluido={dados.atividadesColetivas.n_total_incluido}
          nota={dados.atividadesColetivas.nota}
        >
          <BarRanking
            data={dados.atividadesColetivas.contagens.map((c) => ({
              label: c.atividade,
              value: c.quantidade,
            }))}
          />
        </ChartCard>
      </div>
    </div>
  );
}
