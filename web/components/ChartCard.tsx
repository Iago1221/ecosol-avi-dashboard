import type { ReactNode } from "react";

type ChartCardProps = {
  titulo: string;
  nRespostasComDado: number;
  nTotalIncluido: number;
  nota?: string;
  children: ReactNode;
};

export function ChartCard({
  titulo,
  nRespostasComDado,
  nTotalIncluido,
  nota,
  children,
}: ChartCardProps) {
  return (
    <section className="flex flex-col gap-3 rounded-xl border border-black/10 bg-white p-5 shadow-sm dark:border-white/10 dark:bg-zinc-900">
      <header className="flex flex-wrap items-baseline justify-between gap-2">
        <h2 className="text-base font-semibold text-zinc-900 dark:text-zinc-50">{titulo}</h2>
        <span className="text-xs text-zinc-500 dark:text-zinc-400">
          N = {nRespostasComDado} de {nTotalIncluido}
        </span>
      </header>
      {children}
      {nota ? <p className="text-xs text-zinc-500 dark:text-zinc-400">{nota}</p> : null}
    </section>
  );
}
