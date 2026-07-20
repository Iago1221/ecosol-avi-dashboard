"use client";

import { Bar, BarChart, CartesianGrid, Legend, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { categorica } from "@/lib/palette";
import type { AggregateGenero } from "@/lib/types";

export function GeneroChart({ aggregate }: { aggregate: AggregateGenero }) {
  const porMunicipio = [...aggregate.por_municipio].sort(
    (a, b) => b.mulheres + b.homens - (a.mulheres + a.homens)
  );

  return (
    <div className="flex flex-col gap-4">
      <div className="grid grid-cols-3 gap-3 text-center">
        <div className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800">
          <p className="text-2xl font-semibold text-zinc-900 dark:text-zinc-50">
            {aggregate.total_mulheres}
          </p>
          <p className="text-xs text-zinc-500 dark:text-zinc-400">Mulheres</p>
        </div>
        <div className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800">
          <p className="text-2xl font-semibold text-zinc-900 dark:text-zinc-50">
            {aggregate.total_homens}
          </p>
          <p className="text-xs text-zinc-500 dark:text-zinc-400">Homens</p>
        </div>
        <div className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800">
          <p className="text-2xl font-semibold text-zinc-900 dark:text-zinc-50">
            {aggregate.percentual_feminino ?? "—"}
            {aggregate.percentual_feminino !== null ? "%" : ""}
          </p>
          <p className="text-xs text-zinc-500 dark:text-zinc-400">% feminino</p>
        </div>
      </div>

      {porMunicipio.length > 0 ? (
        <ResponsiveContainer width="100%" height={Math.max(120, porMunicipio.length * 32)}>
          <BarChart
            data={porMunicipio}
            layout="vertical"
            margin={{ top: 4, right: 24, bottom: 4, left: 8 }}
          >
            <CartesianGrid strokeDasharray="3 3" stroke="var(--chart-grid)" horizontal={false} />
            <XAxis type="number" allowDecimals={false} tick={{ fill: "var(--chart-text)", fontSize: 12 }} />
            <YAxis
              type="category"
              dataKey="municipio"
              width={140}
              tick={{ fill: "var(--chart-text)", fontSize: 12 }}
            />
            <Tooltip contentStyle={{ fontSize: 12 }} />
            <Legend wrapperStyle={{ fontSize: 12 }} />
            <Bar dataKey="mulheres" name="Mulheres" stackId="genero" fill={categorica[0]} />
            <Bar
              dataKey="homens"
              name="Homens"
              stackId="genero"
              fill={categorica[1]}
              radius={[0, 4, 4, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      ) : null}
    </div>
  );
}
