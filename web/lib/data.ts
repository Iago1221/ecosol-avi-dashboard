import coreJson from "@/data/core.json";
import datasetMetaJson from "@/data/dataset_meta.json";
import municipioJson from "@/data/aggregates/municipio.json";
import areaAtuacaoJson from "@/data/aggregates/area_atuacao.json";
import generoJson from "@/data/aggregates/genero.json";
import corJson from "@/data/aggregates/cor.json";
import povoTradicionalJson from "@/data/aggregates/povo_tradicional.json";
import formaOrganizacaoJson from "@/data/aggregates/forma_organizacao.json";
import participaRedeJson from "@/data/aggregates/participa_rede.json";
import atividadesColetivasJson from "@/data/aggregates/atividades_coletivas.json";

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
  DatasetMeta,
} from "@/lib/types";

// `as unknown as X`: os JSONs importados têm formas estruturais levemente distintas
// por objeto (TS infere um tipo por item quando algumas chaves opcionais variam), então
// o cast direto para o tipo nominal falha por "não overlap suficiente" — o dado em si
// está correto (gerado e validado pelo pipeline Python), só o TS é conservador aqui.
export const coreRecords = coreJson as unknown as CoreRecord[];
export const datasetMeta = datasetMetaJson as unknown as DatasetMeta;

export const aggregates = {
  municipio: municipioJson as unknown as AggregateMunicipio,
  areaAtuacao: areaAtuacaoJson as unknown as AggregateAreaAtuacao,
  genero: generoJson as unknown as AggregateGenero,
  cor: corJson as unknown as AggregateCor,
  povoTradicional: povoTradicionalJson as unknown as AggregatePovoTradicional,
  formaOrganizacao: formaOrganizacaoJson as unknown as AggregateFormaOrganizacao,
  participaRede: participaRedeJson as unknown as AggregateParticipaRede,
  atividadesColetivas: atividadesColetivasJson as unknown as AggregateAtividadesColetivas,
};
