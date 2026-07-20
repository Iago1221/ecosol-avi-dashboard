export function StatTile({
  valor,
  rotulo,
  destaque = false,
}: {
  valor: string | number;
  rotulo: string;
  destaque?: boolean;
}) {
  return (
    <div className="rounded-lg bg-zinc-50 p-4 text-center dark:bg-zinc-800">
      <p
        className={
          destaque
            ? "text-3xl font-bold text-teal-600 dark:text-teal-400"
            : "text-2xl font-semibold text-zinc-900 dark:text-zinc-50"
        }
      >
        {valor}
      </p>
      <p className="text-xs text-zinc-500 dark:text-zinc-400">{rotulo}</p>
    </div>
  );
}
