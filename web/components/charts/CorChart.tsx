"use client";

import { Bar, BarChart, CartesianGrid, Cell, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { categorica } from "@/lib/palette";
import type { AggregateCor } from "@/lib/types";

/** Série categórica (5 cores/raças) — cores distintas, diferente da barra ranking de
 * série única (que usa um hue só). */
export function CorChart({ aggregate }: { aggregate: AggregateCor }) {
  const data = aggregate.contagens;
  const total = data.reduce((acc, d) => acc + d.quantidade, 0);
  if (total === 0) {
    return <p className="text-sm text-zinc-500 dark:text-zinc-400">Sem dados para exibir.</p>;
  }

  return (
    <ResponsiveContainer width="100%" height={Math.max(120, data.length * 32)}>
      <BarChart data={data} layout="vertical" margin={{ top: 4, right: 24, bottom: 4, left: 8 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="var(--chart-grid)" horizontal={false} />
        <XAxis type="number" allowDecimals={false} tick={{ fill: "var(--chart-text)", fontSize: 12 }} />
        <YAxis
          type="category"
          dataKey="categoria"
          width={90}
          tick={{ fill: "var(--chart-text)", fontSize: 12 }}
        />
        <Tooltip contentStyle={{ fontSize: 12 }} formatter={(value) => [value ?? "", "Pessoas"]} />
        <Bar dataKey="quantidade" radius={[0, 4, 4, 0]}>
          {data.map((d, i) => (
            <Cell key={d.categoria} fill={categorica[i % categorica.length]} />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}
