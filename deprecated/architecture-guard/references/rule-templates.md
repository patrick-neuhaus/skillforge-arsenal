# Rule Templates — Gerar architecture.md

Consulte este arquivo no **Phase 1** quando `architecture.md` nao existir e o usuario pedir `--init`.

---

## Template Base

```markdown
# Architecture Rules — [Nome do Projeto]

## Core Principles

### Thin Client, Fat Server
- Frontend apenas captura intencoes e renderiza respostas
- TODA logica de negocio fica no backend (server actions, API routes, RPC)
- Validacao no frontend e apenas UX (feedback imediato) — validacao real no server
- Regra de ouro: tudo no frontend e acessivel "com dois cliques no navegador"

### Organizacao por Comportamento
- Estrutura de pastas por feature/comportamento, nao por tipo de arquivo
- Cada feature contem seus componentes, hooks, utils, e testes
- Componentes compartilhados ficam em `components/ui/` ou `components/shared/`

### Layer Separation
- UI nao importa data layer diretamente
- Server actions nao retornam JSX
- Utils nao tem side effects
- Circular dependencies sao proibidas

## Stack

- **Framework:** [Next.js 14+ / React / etc.]
- **Styling:** [Tailwind + shadcn/ui / CSS Modules / etc.]
- **State:** [Zustand / Context / Server State com React Query]
- **Database:** [Supabase / Prisma / etc.]
- **Auth:** [NextAuth / Supabase Auth / Clerk]

## Directory Structure

```
src/
├── app/                    # Next.js App Router pages + layouts
├── components/
│   ├── ui/                 # Primitives (shadcn/ui, design tokens)
│   ├── shared/             # Cross-feature shared components
│   └── features/           # Feature-specific components
│       └── [feature]/      # Organized by behavior
├── lib/                    # Business logic, utils, configs
│   ├── supabase/           # Database queries, RPC
│   └── validations/        # Zod schemas
├── hooks/                  # Custom hooks (shared)
├── actions/                # Server actions
└── types/                  # TypeScript type definitions
```

## Rules (customize per project)

| Rule ID | Description | Severity | Enabled |
|---------|-------------|:--------:|:-------:|
| TC-001 | No fetch/mutation in 'use client' files | P0 | Yes |
| TC-002 | No process.env (non-NEXT_PUBLIC) in client | P0 | Yes |
| TC-003 | No Supabase client with business logic in client | P0 | Yes |
| LS-001 | No direct DB imports in components | P1 | Yes |
| LS-002 | No JSX in server actions | P1 | Yes |
| LS-003 | No circular dependencies | P1 | Yes |
| BO-001 | Features organized by behavior | P2 | Yes |
| BO-002 | No mixing feature code in shared/ | P2 | Yes |
| CC-001 | Naming follows project convention | P2 | Yes |
| CC-002 | Imports use path aliases (@/) | P2 | Yes |
```

## Customizacao

Instrua o usuario:
1. Copiar o template acima
2. Preencher Stack e Directory Structure
3. Ajustar regras: desabilitar as que nao aplicam, adicionar project-specific
4. Salvar como `architecture.md` na raiz do projeto

A skill respeita o `Enabled` de cada regra — se `No`, nao escaneia.
