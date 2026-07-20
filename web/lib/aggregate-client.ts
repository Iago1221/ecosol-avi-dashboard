// Port das agregações de `pipeline/src/aggregate.py` para o cliente — usado só quando
// um filtro está ativo (a visão sem filtro usa os agregados pré-computados em
// `web/data/aggregates/*.json`, que são a referência oficial). As duas implementações
// devem produzir números idênticos na visão sem filtro; isso é verificado manualmente
// comparando a saída daqui com `aggregates.*` (ver docs/como_atualizar_os_dados.md).
import type {
  AggregateAreaAtuacao,
  AggregateAtividadesColetivas,
  AggregateCor,
  AggregateFormaOrganizacao,
  AggregateGenero,
  AggregateMunicipio,
  AggregateParticipaRede,
  AggregatePovoTradicional,
  CoreRecord,
} from "@/lib/types";

function sortedCounts<T extends string>(counts: Map<T, number>): { key: T; quantidade: number }[] {
  return Array.from(counts.entries())
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .map(([key, quantidade]) => ({ key, quantidade }));
}

function count<T extends string>(items: T[]): Map<T, number> {
  const m = new Map<T, number>();
  for (const item of items) m.set(item, (m.get(item) ?? 0) + 1);
  return m;
}

export function aggregateMunicipio(records: CoreRecord[]): AggregateMunicipio {
  const comDado = records.filter((r) => r.municipio);
  const counts = count(comDado.map((r) => r.municipio as string));
  return {
    campo: "municipio",
    n_total_incluido: records.length,
    n_respostas_com_dado: comDado.length,
    contagens: sortedCounts(counts).map(({ key, quantidade }) => ({ municipio: key, quantidade })),
  };
}

export function aggregateAreaAtuacao(records: CoreRecord[]): AggregateAreaAtuacao {
  const ruralEUrbana = records.filter((r) => r.atua_rural && r.atua_urbana).length;
  const soRural = records.filter((r) => r.atua_rural && !r.atua_urbana).length;
  const soUrbana = records.filter((r) => r.atua_urbana && !r.atua_rural).length;
  const nenhuma = records.filter((r) => !r.atua_rural && !r.atua_urbana).length;
  return {
    campo: "area_atuacao",
    n_total_incluido: records.length,
    n_respostas_com_dado: records.length - nenhuma,
    contagens: [
      { categoria: "Somente rural", quantidade: soRural },
      { categoria: "Somente urbana", quantidade: soUrbana },
      { categoria: "Rural e urbana", quantidade: ruralEUrbana },
      { categoria: "Não informado", quantidade: nenhuma },
    ],
  };
}

export function aggregateGenero(records: CoreRecord[]): AggregateGenero {
  const comDado = records.filter((r) => r.socios_total !== null);
  const totalMulheres = comDado.reduce((acc, r) => acc + (r.socios_mulheres ?? 0), 0);
  const totalHomens = comDado.reduce((acc, r) => acc + (r.socios_homens ?? 0), 0);
  const totalGeral = totalMulheres + totalHomens;
  // Somado por município — vários empreendimentos podem compartilhar o mesmo
  // município; um rótulo por empreendimento com nomes longos sobrepõe/ilegível.
  const porMunicipioMap = new Map<string, { mulheres: number; homens: number }>();
  for (const r of comDado) {
    if (!r.municipio) continue;
    const bucket = porMunicipioMap.get(r.municipio) ?? { mulheres: 0, homens: 0 };
    bucket.mulheres += r.socios_mulheres ?? 0;
    bucket.homens += r.socios_homens ?? 0;
    porMunicipioMap.set(r.municipio, bucket);
  }
  const porMunicipio = Array.from(porMunicipioMap.entries())
    .map(([municipio, valores]) => ({ municipio, ...valores }))
    .sort((a, b) => a.municipio.localeCompare(b.municipio));
  return {
    campo: "genero",
    n_total_incluido: records.length,
    n_respostas_com_dado: comDado.length,
    total_mulheres: totalMulheres,
    total_homens: totalHomens,
    percentual_feminino: totalGeral ? Math.round((1000 * totalMulheres) / totalGeral) / 10 : null,
    por_municipio: porMunicipio,
  };
}

const CAMPOS_COR: { categoria: string; campo: keyof CoreRecord }[] = [
  { categoria: "Branca", campo: "cor_branca" },
  { categoria: "Preta", campo: "cor_preta" },
  { categoria: "Amarela", campo: "cor_amarela" },
  { categoria: "Parda", campo: "cor_parda" },
  { categoria: "Indígena", campo: "cor_indigena" },
];

export function aggregateCor(records: CoreRecord[]): AggregateCor {
  const comDado = records.filter((r) =>
    CAMPOS_COR.some(({ campo }) => (r[campo] as number | null) !== null)
  );
  return {
    campo: "cor",
    n_total_incluido: records.length,
    n_respostas_com_dado: comDado.length,
    contagens: CAMPOS_COR.map(({ categoria, campo }) => ({
      categoria,
      quantidade: comDado.reduce((acc, r) => acc + ((r[campo] as number | null) ?? 0), 0),
    })),
  };
}

export function aggregatePovoTradicional(records: CoreRecord[]): AggregatePovoTradicional {
  const comDado = records.filter((r) => r.pertence_povo_tradicional !== null);
  const sim = comDado.filter((r) => r.pertence_povo_tradicional);
  const povosCitados = Array.from(
    new Set(sim.map((r) => r.povo_tradicional_qual).filter((v): v is string => !!v))
  ).sort();
  return {
    campo: "povo_tradicional",
    n_total_incluido: records.length,
    n_respostas_com_dado: comDado.length,
    quantidade_sim: sim.length,
    quantidade_nao: comDado.length - sim.length,
    povos_citados: povosCitados,
  };
}

export function aggregateFormaOrganizacao(records: CoreRecord[]): AggregateFormaOrganizacao {
  const comDado = records.filter((r) => r.forma_organizacao);
  const counts = count(comDado.map((r) => r.forma_organizacao as string));
  return {
    campo: "forma_organizacao",
    n_total_incluido: records.length,
    n_respostas_com_dado: comDado.length,
    contagens: sortedCounts(counts).map(({ key, quantidade }) => ({ forma: key, quantidade })),
  };
}

export function aggregateParticipaRede(records: CoreRecord[]): AggregateParticipaRede {
  const comDado = records.filter((r) => r.participa_rede !== null);
  const sim = comDado.filter((r) => r.participa_rede);
  const tiposCounts = count(sim.flatMap((r) => r.redes_tipos));
  return {
    campo: "participa_rede",
    n_total_incluido: records.length,
    n_respostas_com_dado: comDado.length,
    quantidade_sim: sim.length,
    quantidade_nao: comDado.length - sim.length,
    tipos_de_rede: sortedCounts(tiposCounts).map(({ key, quantidade }) => ({ tipo: key, quantidade })),
  };
}

export function aggregateAtividadesColetivas(records: CoreRecord[]): AggregateAtividadesColetivas {
  const comDado = records.filter((r) => r.atividades_coletivas.length > 0);
  const counts = count(comDado.flatMap((r) => r.atividades_coletivas));
  return {
    campo: "atividades_coletivas",
    n_total_incluido: records.length,
    n_respostas_com_dado: comDado.length,
    nota: "Multiescolha — a soma das quantidades pode ultrapassar n_respostas_com_dado.",
    contagens: sortedCounts(counts).map(({ key, quantidade }) => ({ atividade: key, quantidade })),
  };
}

export type Filtros = {
  municipio: string | null;
  areaAtuacao: "rural" | "urbana" | "ambas" | null;
  formaOrganizacao: string | null;
};

export const FILTROS_VAZIOS: Filtros = {
  municipio: null,
  areaAtuacao: null,
  formaOrganizacao: null,
};

export function temFiltroAtivo(filtros: Filtros): boolean {
  return Boolean(filtros.municipio || filtros.areaAtuacao || filtros.formaOrganizacao);
}

export function aplicarFiltros(records: CoreRecord[], filtros: Filtros): CoreRecord[] {
  return records.filter((r) => {
    if (filtros.municipio && r.municipio !== filtros.municipio) return false;
    if (filtros.formaOrganizacao && r.forma_organizacao !== filtros.formaOrganizacao) return false;
    if (filtros.areaAtuacao === "rural" && !(r.atua_rural && !r.atua_urbana)) return false;
    if (filtros.areaAtuacao === "urbana" && !(r.atua_urbana && !r.atua_rural)) return false;
    if (filtros.areaAtuacao === "ambas" && !(r.atua_rural && r.atua_urbana)) return false;
    return true;
  });
}
