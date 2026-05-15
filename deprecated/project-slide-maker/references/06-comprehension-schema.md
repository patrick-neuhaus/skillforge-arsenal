# Comprehension Schema (Phase 1)

> JSON output da Phase 1. Carrega na Phase 1 e Phase 3.

## Schema

```json
{
  "tipo": "crm | chat | viewer | dashboard | ecomm | data-tool | docs | landing | other",
  "stack": {
    "frontend": "react | vue | svelte | next | etc",
    "backend": "supabase | postgres | firebase | none | etc",
    "css": "tailwind | css-modules | styled | etc",
    "build": "vite | webpack | parcel | rsbuild"
  },
  "deps_chave": ["@radix-ui/*", "@tanstack/react-query", "..."],
  "entry_points": ["src/main.tsx", "src/App.tsx", "..."],
  "componentes_chave": [
    {
      "path": "src/components/X.tsx",
      "papel": "tabela CRUD principal",
      "uses_count": 5
    }
  ],
  "fluxos_inferidos": [
    "vendedor → /login → /dashboard → /clients/:id → editar deal"
  ],
  "rotas": ["/login", "/dashboard", "/clients/:id"],
  "evidencias": {
    "is_lovable_project": true,
    "has_supabase": true,
    "uses_charts": true
  }
}
```

## Heurísticas tipo

Detecção determinística primeiro, fallback LLM se ambíguo.

| Indicador concreto | tipo |
|---|---|
| `recharts` + `@tanstack/react-query` + `@radix-ui/react-dialog` + tabela CRUD | crm |
| `socket.io-client` ou `pusher-js` + componentes message/conversation | chat |
| `pdfjs` ou `@react-pdf/renderer` + canvas/zoom | viewer |
| `recharts` + KPI cards + filters (sem CRUD heavy) | dashboard |
| `stripe` + cart + product cards | ecomm |
| `papaparse` + table + import/export | data-tool |
| MDX + `next/mdx` ou `@mdx-js/react` | docs |
| `next/image` + hero + CTA + sem auth | landing |

Score: cada match = +1. Se 2+ tipos empatam, fallback LLM com `comprehension.evidencias` como contexto.

## Fluxos inferidos — heurística

1. Identificar routes via:
   - `react-router-dom` `<Route>` config
   - Next.js `app/` ou `pages/` layout
   - File-based routing (Astro, SvelteKit)
2. Sequenciar logical:
   - Entry point (`/`, `/login`, `/home`)
   - Main feature (rota mais profunda + mais imports)
   - Detail/edit (`:id` patterns)
   - Action/result (success/done)
3. Output: 3-5 fluxos críticos

## Exemplo (ia-da-plus)

```json
{
  "tipo": "crm",
  "stack": {
    "frontend": "react+vite",
    "backend": "supabase",
    "css": "tailwind",
    "build": "vite"
  },
  "deps_chave": [
    "@radix-ui/react-dialog",
    "@tanstack/react-query",
    "recharts",
    "papaparse",
    "@uiw/react-md-editor",
    "@supabase/supabase-js"
  ],
  "componentes_chave": [
    {"path": "src/components/ClientTable.tsx", "papel": "tabela CRUD principal"},
    {"path": "src/pages/Dashboard.tsx", "papel": "dashboard métricas"}
  ],
  "fluxos_inferidos": [
    "vendedor → /login → /dashboard → /clients/:id → editar",
    "admin → /import → upload CSV → /clients (lista atualizada)"
  ],
  "rotas": ["/login", "/dashboard", "/clients", "/clients/:id", "/import"],
  "evidencias": {"is_lovable_project": true, "has_supabase": true}
}
```
