"use client";

import { Bar, BarChart, CartesianGrid, Cell, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { hueUnica } from "@/lib/palette";

export type BarRankingDatum = { label: string; value: number };

export function BarRanking({
  data,
  color = hueUnica,
  height,
}: {
  data: BarRankingDatum[];
  color?: string;
  height?: number;
}) {
  const chartHeight = height ?? Math.max(120, data.length * 32);

  if (data.length === 0) {
    return <p className="text-sm text-zinc-500 dark:text-zinc-400">Sem dados para exibir.</p>;
  }

  return (
    <ResponsiveContainer width="100%" height={chartHeight}>
      <BarChart data={data} layout="vertical" margin={{ top: 4, right: 24, bottom: 4, left: 8 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="var(--chart-grid)" horizontal={false} />
        <XAxis type="number" allowDecimals={false} tick={{ fill: "var(--chart-text)", fontSize: 12 }} />
        <YAxis
          type="category"
          dataKey="label"
          width={180}
          tick={{ fill: "var(--chart-text)", fontSize: 12 }}
        />
        <Tooltip contentStyle={{ fontSize: 12 }} formatter={(value) => [value ?? "", "Quantidade"]} />
        <Bar dataKey="value" radius={[0, 4, 4, 0]}>
          {data.map((d) => (
            <Cell key={d.label} fill={color} />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}
