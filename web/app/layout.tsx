import type { Metadata } from "next";
import Link from "next/link";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Economia Solidária — Alto Vale do Itajaí",
  description:
    "Dashboard da pesquisa de Economia Solidária no Alto Vale do Itajaí (NUPESER/UNIDAVI).",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="pt-BR"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="flex min-h-full flex-col bg-zinc-50 text-zinc-900 dark:bg-zinc-950 dark:text-zinc-100">
        <header className="border-b border-black/10 bg-white dark:border-white/10 dark:bg-zinc-900">
          <div className="mx-auto flex max-w-6xl flex-wrap items-center justify-between gap-2 px-4 py-3 sm:px-6">
            <div>
              <p className="text-sm font-semibold">Economia Solidária — Alto Vale do Itajaí</p>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">NUPESER / UNIDAVI</p>
            </div>
            <nav className="flex gap-4 text-sm">
              <Link href="/" className="hover:underline">
                Painel
              </Link>
              <Link href="/metodologia" className="hover:underline">
                Metodologia
              </Link>
            </nav>
          </div>
        </header>
        <main className="mx-auto w-full max-w-6xl flex-1 px-4 py-6 sm:px-6">{children}</main>
        <footer className="border-t border-black/10 px-4 py-4 text-center text-xs text-zinc-500 dark:border-white/10 dark:text-zinc-400">
          Dados coletados pelo NUPESER/UNIDAVI — divulgados com autorização dos empreendimentos participantes.
        </footer>
      </body>
    </html>
  );
}
