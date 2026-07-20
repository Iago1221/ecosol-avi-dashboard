import { StatTile } from "@/components/StatTile";
import type { AggregatePovoTradicional } from "@/lib/types";

export function PovoTradicionalCard({ aggregate }: { aggregate: AggregatePovoTradicional }) {
  return (
    <div className="flex flex-col gap-3">
      <div className="grid grid-cols-2 gap-3">
        <StatTile valor={aggregate.quantidade_sim} rotulo="Pertencem a povo/comunidade tradicional" destaque />
        <StatTile valor={aggregate.quantidade_nao} rotulo="Não pertencem" />
      </div>
      {aggregate.povos_citados.length > 0 ? (
        <div>
          <p className="mb-1 text-xs font-medium text-zinc-500 dark:text-zinc-400">Povos/comunidades citados</p>
          <div className="flex flex-wrap gap-1.5">
            {aggregate.povos_citados.map((povo) => (
              <span
                key={povo}
                className="rounded-full bg-teal-50 px-2.5 py-1 text-xs text-teal-800 dark:bg-teal-950 dark:text-teal-200"
              >
                {povo}
              </span>
            ))}
          </div>
        </div>
      ) : null}
    </div>
  );
}
