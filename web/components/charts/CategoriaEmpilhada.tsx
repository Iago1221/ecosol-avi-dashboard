"use client";

import { Bar, BarChart, CartesianGrid, Legend, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { categorica, naoInformado } from "@/lib/palette";

export type CategoriaDatum = { categoria: string; quantidade: number };

/** Barra horizontal única empilhada — para campos categóricos de parte-todo com poucas
 * categorias (ex. área de atuação). A última categoria ("Não informado") sempre recebe
 * a cor neutra, as demais seguem a paleta categórica na ordem recebida. */
export function CategoriaEmpilhada({ data, linha = "Total" }: { data: CategoriaDatum[]; linha?: string }) {
  const semZero = data.filter((d) => d.quantidade > 0);
  if (semZero.length === 0) {
    return <p className="text-sm text-zinc-500 dark:text-zinc-400">Sem dados para exibir.</p>;
  }

  const row: Record<string, string | number> = { linha };
  for (const d of data) row[d.categoria] = d.quantidade;

  return (
    <ResponsiveContainer width="100%" height={120}>
      <BarChart data={[row]} layout="vertical" margin={{ top: 4, right: 16, bottom: 4, left: 8 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="var(--chart-grid)" horizontal={false} />
        <XAxis type="number" allowDecimals={false} tick={{ fill: "var(--chart-text)", fontSize: 12 }} />
        <YAxis type="category" dataKey="linha" width={0} tick={false} axisLine={false} />
        <Tooltip contentStyle={{ fontSize: 12 }} />
        <Legend wrapperStyle={{ fontSize: 12 }} />
        {data.map((d, i) => (
          <Bar
            key={d.categoria}
            dataKey={d.categoria}
            stackId="unica"
            fill={d.categoria === "Não informado" ? naoInformado : categorica[i % categorica.length]}
            radius={i === data.length - 1 ? [0, 4, 4, 0] : i === 0 ? [4, 0, 0, 4] : undefined}
          />
        ))}
      </BarChart>
    </ResponsiveContainer>
  );
}
