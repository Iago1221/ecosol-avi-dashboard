// Tipos fortes só para o dataset "core" (público) — o restante das 251 colunas da
// planilha bruta fica em full_raw.json, uso interno, nunca chega ao frontend.

export type CoreRecord = {
  id: number;
  linha_origem_planilha: number;
  nome_empreendimento: string | null;
  municipio: string | null;
  estado: string | null;
  situacao_atual: string | null;
  atua_rural: boolean;
  atua_urbana: boolean;
  socios_mulheres: number | null;
  socios_homens: number | null;
  socios_total: number | null;
  socios_total_declarado: number | null;
  socios_total_divergente: boolean;
  cor_branca: number | null;
  cor_preta: number | null;
  cor_amarela: number | null;
  cor_parda: number | null;
  cor_indigena: number | null;
  cor_total_declarado: number | null;
  pertence_povo_tradicional: boolean | null;
  povo_tradicional_qual: string | null;
  forma_organizacao: string | null;
  participa_rede: boolean | null;
  redes_tipos: string[];
  redes_detalhes: Record<string, string>;
  atividades_coletivas: string[];
  atividade_principal: string | null;
  entry_status: string | null;
  incluido_no_publico: boolean;
};

export type DatasetMeta = {
  gerado_em: string;
  arquivo_fonte: string;
  total_linhas_coletadas: number;
  total_linhas_incluidas_no_publico: number;
  criterio_inclusao: string;
};

export type ContagemCategoria = { categoria: string; quantidade: number };

export type AggregateMunicipio = {
  campo: "municipio";
  n_total_incluido: number;
  n_respostas_com_dado: number;
  contagens: { municipio: string; quantidade: number }[];
};

export type AggregateAreaAtuacao = {
  campo: "area_atuacao";
  n_total_incluido: number;
  n_respostas_com_dado: number;
  contagens: ContagemCategoria[];
};

export type AggregateGenero = {
  campo: "genero";
  n_total_incluido: number;
  n_respostas_com_dado: number;
  total_mulheres: number;
  total_homens: number;
  percentual_feminino: number | null;
  por_municipio: { municipio: string; mulheres: number; homens: number }[];
};

export type AggregateCor = {
  campo: "cor";
  n_total_incluido: number;
  n_respostas_com_dado: number;
  contagens: ContagemCategoria[];
};

export type AggregatePovoTradicional = {
  campo: "povo_tradicional";
  n_total_incluido: number;
  n_respostas_com_dado: number;
  quantidade_sim: number;
  quantidade_nao: number;
  povos_citados: string[];
};

export type AggregateFormaOrganizacao = {
  campo: "forma_organizacao";
  n_total_incluido: number;
  n_respostas_com_dado: number;
  contagens: { forma: string; quantidade: number }[];
};

export type AggregateParticipaRede = {
  campo: "participa_rede";
  n_total_incluido: number;
  n_respostas_com_dado: number;
  quantidade_sim: number;
  quantidade_nao: number;
  tipos_de_rede: { tipo: string; quantidade: number }[];
};

export type AggregateAtividadesColetivas = {
  campo: "atividades_coletivas";
  n_total_incluido: number;
  n_respostas_com_dado: number;
  nota: string;
  contagens: { atividade: string; quantidade: number }[];
};
