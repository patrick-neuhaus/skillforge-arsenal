# Architecture Template — Gerar architecture.md

Consulte este arquivo na operacao `--architecture`.

---

## Processo

1. Ler estrutura do projeto: `ls`, `package.json`, diretorio `src/`
2. Identificar stack (framework, styling, state, database, auth)
3. Identificar convencoes de organizacao (por feature? por tipo? hibrido?)
4. Gerar `architecture.md` na raiz do projeto

## Template

```markdown
# Architecture Rules — [Nome do Projeto]

## Core Principles
- **Thin Client, Fat Server:** Frontend captura intencoes e renderiza. Backend tem TODA logica.
- **Organizacao por Comportamento:** Pastas por feature, nao por tipo.
- **Layer Separation:** UI nao importa data layer. Server actions nao retornam JSX.

## Stack
- **Framework:** [detectado de package.json]
- **Styling:** [Tailwind/CSS Modules/styled-components]
- **State:** [Zustand/Context/Redux/React Query]
- **Database:** [Supabase/Prisma/Drizzle]
- **Auth:** [NextAuth/Supabase Auth/Clerk]

## Directory Structure
[Mapear estrutura real do projeto]

## Rules
| Rule ID | Description | Severity | Enabled |
|---------|-------------|:--------:|:-------:|
| TC-001 | No business logic in 'use client' | P0 | Yes |
| TC-002 | No server env in client | P0 | Yes |
| LS-001 | No direct DB imports in components | P1 | Yes |
| BO-001 | Features organized by behavior | P2 | Yes |
[Adicionar rules project-specific baseadas no que foi observado]
```

## Adaptacao

- Se projeto NAO usa React/Next.js, adaptar regras de thin client pro framework usado
- Se projeto e backend-only, focar em layer separation e convencoes
- Se projeto e MVP/prototipo, reduzir severity de P2 rules
- Sempre perguntar ao usuario antes de salvar: "Gerado. Quer ajustar alguma regra?"
