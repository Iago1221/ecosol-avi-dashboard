import { StatTile } from "@/components/StatTile";
import { BarRanking } from "@/components/charts/BarRanking";
import { categorica } from "@/lib/palette";
import type { AggregateParticipaRede } from "@/lib/types";

export function ParticipaRedeCard({ aggregate }: { aggregate: AggregateParticipaRede }) {
  const dataTipos = aggregate.tipos_de_rede.map((t) => ({ label: t.tipo, value: t.quantidade }));
  return (
    <div className="flex flex-col gap-3">
      <div className="grid grid-cols-2 gap-3">
        <StatTile valor={aggregate.quantidade_sim} rotulo="Participam de alguma rede" destaque />
        <StatTile valor={aggregate.quantidade_nao} rotulo="Não participam" />
      </div>
      {dataTipos.length > 0 ? (
        <div>
          <p className="mb-1 text-xs font-medium text-zinc-500 dark:text-zinc-400">Tipos de rede citados</p>
          <BarRanking data={dataTipos} color={categorica[1]} height={Math.max(80, dataTipos.length * 28)} />
        </div>
      ) : null}
    </div>
  );
}
