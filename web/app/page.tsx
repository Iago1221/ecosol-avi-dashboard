import { Suspense } from "react";
import { Dashboard } from "@/components/Dashboard";

export default function Home() {
  return (
    <Suspense fallback={<p className="text-sm text-zinc-500">Carregando painel…</p>}>
      <Dashboard />
    </Suspense>
  );
}
