# AGENTS.md — Referência pra AI Coding Tools

Última atualização: 2026-03-27

Consulte este arquivo quando o usuário pedir instruções pra Lovable, Cursor, Claude Code, Copilot, Codex, ou qualquer AI coding tool.

---

## O que é AGENTS.md

AGENTS.md é um arquivo Markdown colocado na raiz do projeto que contém instruções pra AI coding assistants. É o padrão universal, mantido pela Linux Foundation (Agentic AI Foundation), adotado por 60K+ repos no GitHub, e lido nativamente por Claude Code, Cursor, Copilot, Codex CLI, Jules (Google), e Gemini.

Dar contexto de projeto ao agente é a ação de maior leverage pra melhorar qualidade de output em coding tools.

## Estrutura recomendada

```markdown
# AGENTS.md

## Project Overview
[1-2 frases: o que é o projeto e qual stack usa]

## Tech Stack
- Frontend: [framework, versão]
- Backend: [framework, versão]
- Database: [tipo, versão]
- Key libraries: [lista com versões pinadas]

## Project Structure
```
src/
├── components/   # UI components (shadcn/ui)
├── pages/        # Route pages
├── hooks/        # Custom React hooks
├── lib/          # Utility functions
├── types/        # TypeScript types
└── integrations/ # External service connectors
```

## Build & Test Commands
```bash
npm run dev          # Start dev server
npm run build        # Production build
npm run test         # Run tests
npm run lint         # Run linter
```

## Code Conventions
[Apenas o que a AI erraria SEM este arquivo]
- [Convenção 1 — com exemplo]
- [Convenção 2 — com exemplo]

## Domain Glossary
[Termos domain-specific que a AI não conheceria]
- **[Termo]**: [definição]

## Common Patterns
[Padrões que o projeto usa e a AI deve seguir]

## Do NOT
[Lista explícita do que a AI NÃO deve fazer]
- Não edite [arquivo crítico]
- Não use [lib proibida]
- Não altere [padrão estabelecido]
```

## Regras de ouro

1. **Máximo ~300 linhas.** Claude Code já tem ~50 instruções no system prompt. Cada instrução adicional compete por atenção. Seja cirúrgico.

2. **Foque no que a AI erraria SEM o arquivo.** Não repita o que linters fazem. Não ensine TypeScript ao modelo. Documente as decisões ESPECÍFICAS do seu projeto.

3. **Comandos exatos com argumentos.** Previne flags alucinadas:
   - Bom: `npm run test -- --watchAll=false`
   - Ruim: "rode os testes"

4. **Versões pinadas.** A AI pode sugerir versões incompatíveis sem isso:
   - Bom: `React 18.3, Vite 5.4, shadcn/ui 2.1`
   - Ruim: "usa React e Vite"

5. **Jargão domain-specific.** Se o projeto tem termos próprios ("tenant" = empresa cliente, "flow" = workflow de automação), documente.

6. **NÃO inclua:**
   - Guidelines de code style → use linters (ESLint, Prettier, Biome)
   - Instruções óbvias → "use TypeScript" quando o projeto já é TS
   - Documentação extensa → mantenha conciso, reference docs externas

## Estratégia multi-tool

Diferentes AI tools leem diferentes arquivos. Pra cobertura máxima:

| Arquivo | Quem lê | Quando usar |
|---|---|---|
| `AGENTS.md` | Claude Code, Cursor, Copilot, Codex, Jules, Gemini | **Sempre** — é o universal |
| `CLAUDE.md` | Claude Code | Instrucões Claude-specific (pode referenciar AGENTS.md) |
| `.github/copilot-instructions.md` | GitHub Copilot | Só se usa Copilot além do Claude |
| `.cursor/rules/` | Cursor | Regras específicas do Cursor (pode importar AGENTS.md) |

Recomendação: mantenha AGENTS.md como single source of truth. Outros arquivos referenciam ele.

## Lovable-specific

Lovable não lê AGENTS.md do repo — usa Workspace Knowledge e Project Knowledge. Mas os princípios são os mesmos:

- **Plan mode 60-70% do tempo** — deixar o Lovable analisar antes de agir
- **Front-end first** — construir UI com mock data ANTES de conectar DB
- **Prompts incrementais** — uma tarefa por vez, não "faz o app inteiro"
- **Guardrails explícitos** — "Não edite /shared/Layout.tsx"
- **Pin versions** após cada feature funcional — permite rollback

## Template minimal (copiar e adaptar)

```markdown
# AGENTS.md

## Overview
[Nome do projeto] — [descrição em 1 frase]. Built with [stack principal].

## Stack
- React 18.3 + TypeScript 5.5
- Vite 5.4
- Supabase (auth, database, storage)
- shadcn/ui + Tailwind CSS 3.4
- React Query (TanStack Query v5)

## Structure
src/components/ → UI components
src/pages/ → Route pages
src/hooks/ → Custom hooks
src/lib/ → Utilities
src/integrations/supabase/ → Supabase client and types

## Commands
npm run dev → dev server (port 8080)
npm run build → production build (must pass before deploy)

## Conventions
- All API calls through React Query hooks in src/hooks/
- Supabase client from src/integrations/supabase/client.ts (never create new instances)
- Toast notifications via sonner (already configured)
- Forms with react-hook-form + zod validation

## Do NOT
- Edit src/integrations/supabase/client.ts
- Add new npm packages without asking
- Use localStorage for auth (Supabase handles it)
- Create new Supabase client instances
```

## Fontes

- agents.md (site oficial) — especificação e exemplos
- Anthropic: "Prompting best practices" — project instructions guidance
- OpenAI Codex docs — AGENTS.md integration
- Pesquisa InfoQ mar/2026 — análise de valor de AGENTS.md files
