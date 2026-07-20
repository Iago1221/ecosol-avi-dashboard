"use client";

import type { Filtros } from "@/lib/aggregate-client";

const OPCOES_AREA: { value: NonNullable<Filtros["areaAtuacao"]>; label: string }[] = [
  { value: "rural", label: "Somente rural" },
  { value: "urbana", label: "Somente urbana" },
  { value: "ambas", label: "Rural e urbana" },
];

export function FilterBar({
  filtros,
  municipios,
  formasOrganizacao,
  onChange,
  onLimpar,
}: {
  filtros: Filtros;
  municipios: string[];
  formasOrganizacao: string[];
  onChange: (novo: Partial<Filtros>) => void;
  onLimpar: () => void;
}) {
  const ativo = filtros.municipio || filtros.areaAtuacao || filtros.formaOrganizacao;

  return (
    <div className="flex flex-wrap items-center gap-3 rounded-xl border border-black/10 bg-white p-4 dark:border-white/10 dark:bg-zinc-900">
      <label className="flex flex-col gap-1 text-xs text-zinc-500 dark:text-zinc-400">
        Município
        <select
          className="rounded-md border border-black/10 bg-white px-2 py-1.5 text-sm text-zinc-900 dark:border-white/10 dark:bg-zinc-800 dark:text-zinc-100"
          value={filtros.municipio ?? ""}
          onChange={(e) => onChange({ municipio: e.target.value || null })}
        >
          <option value="">Todos</option>
          {municipios.map((m) => (
            <option key={m} value={m}>
              {m}
            </option>
          ))}
        </select>
      </label>

      <label className="flex flex-col gap-1 text-xs text-zinc-500 dark:text-zinc-400">
        Área de atuação
        <select
          className="rounded-md border border-black/10 bg-white px-2 py-1.5 text-sm text-zinc-900 dark:border-white/10 dark:bg-zinc-800 dark:text-zinc-100"
          value={filtros.areaAtuacao ?? ""}
          onChange={(e) =>
            onChange({ areaAtuacao: (e.target.value || null) as Filtros["areaAtuacao"] })
          }
        >
          <option value="">Todas</option>
          {OPCOES_AREA.map((o) => (
            <option key={o.value} value={o.value}>
              {o.label}
            </option>
          ))}
        </select>
      </label>

      <label className="flex flex-col gap-1 text-xs text-zinc-500 dark:text-zinc-400">
        Forma de organização
        <select
          className="rounded-md border border-black/10 bg-white px-2 py-1.5 text-sm text-zinc-900 dark:border-white/10 dark:bg-zinc-800 dark:text-zinc-100"
          value={filtros.formaOrganizacao ?? ""}
          onChange={(e) => onChange({ formaOrganizacao: e.target.value || null })}
        >
          <option value="">Todas</option>
          {formasOrganizacao.map((f) => (
            <option key={f} value={f}>
              {f}
            </option>
          ))}
        </select>
      </label>

      {ativo ? (
        <button
          onClick={onLimpar}
          className="ml-auto rounded-md border border-black/10 px-3 py-1.5 text-xs text-zinc-600 hover:bg-zinc-50 dark:border-white/10 dark:text-zinc-300 dark:hover:bg-zinc-800"
        >
          Limpar filtros
        </button>
      ) : null}
    </div>
  );
}
