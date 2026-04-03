# AGENTS.md — Guia Completo

Referência para quando o usuário quiser gerar ou otimizar um AGENTS.md.

---

## O que é AGENTS.md

AGENTS.md é um formato aberto mantido pela Linux Foundation (Agentic AI Foundation) que serve como single source of truth pra AI coding tools. Adotado em 60.000+ projetos open-source.

### Tools que leem AGENTS.md
- Lovable
- Cursor
- Windsurf
- Kilo Code
- OpenAI Codex
- Factory
- Amp
- Jules (Google)

### O que Lovable especificamente lê

1. Project Knowledge (prioridade 1)
2. Workspace Knowledge (prioridade 2)
3. Código do projeto
4. Integration Knowledge
5. **AGENTS.md** e **CLAUDE.md** no root do repo

Se Project Knowledge e AGENTS.md conflitam, Project Knowledge vence.

---

## Estrutura recomendada

```markdown
# AGENTS.md

## Project Context
[1-2 frases sobre o projeto]

## Tech Stack
[Lista de tecnologias com versões quando relevante]

## Build & Test Commands
[Comandos exatos — a parte mais importante pra AI tools]

## Project Structure
[Árvore de diretórios simplificada]

## Architecture Decisions
[Decisões que a IA não consegue inferir do código]

## Domain Terminology
[Glossário de termos do negócio]

## Database Schema
[Tabelas principais com campos e tipos]

## Coding Conventions
[Padrões que o linter não cobre]

## DO NOT
[Lista de proibições explícitas]
```

---

## Princípio dos ~300 linhas

Frontier LLMs seguem ~150-200 instruções de forma confiável. Além disso, as instruções competem por atenção e as últimas são ignoradas.

### Prioridade de conteúdo (do mais ao menos importante)

1. **Comandos de build/test** — AI tools PRECISAM disso pra funcionar
2. **Decisões de arquitetura** — impossível inferir do código
3. **Terminologia de domínio** — evita confusão semântica
4. **Proibições (DO NOT)** — evita danos irreversíveis
5. **Schema resumido** — ajuda a gerar queries corretas
6. **Coding conventions** — apenas o que linter não cobre

### O que NÃO incluir

- Regras de estilo que o ESLint/Prettier já enforçam
- Documentação de API (use links externos)
- Histórico do projeto ou changelogs
- Instruções pra humanos (o arquivo é pra AI tools)

---

## Estratégia multi-tool

### Quando usar cada arquivo

| Cenário | Arquivo |
|---------|---------|
| Projeto com 1 tool (só Lovable) | Project Knowledge + Workspace Knowledge |
| Projeto multi-tool | AGENTS.md (universal) como base |
| Precisa de features Claude-específicas | AGENTS.md + CLAUDE.md |
| Cursor com regras por contexto | AGENTS.md + .cursor/rules/*.mdc |
| GitHub Copilot | AGENTS.md + .github/copilot-instructions.md |

### Hierarquia de leitura do Claude Code

1. `~/.claude/CLAUDE.md` (pessoal, global)
2. `./CLAUDE.md` (root do projeto, compartilhado via git)
3. Subdiretório CLAUDE.md (escopo local)

O mais próximo tem prioridade.

### Cursor .mdc files

Cursor suporta arquivos `.mdc` em `.cursor/rules/` com:
- **Always**: sempre ativo
- **Auto Attached**: ativado quando arquivos matching são abertos
- **Agent Requested**: ativado quando o agente pede
- **Manual**: ativado por @ mention

Útil pra regras por contexto (ex: regras diferentes pra testes vs componentes).

---

## Template mínimo pra projetos Lovable + Supabase

```markdown
# AGENTS.md

## Project Context
[App name] — [1 frase do que faz]

## Tech Stack
- React 18 + TypeScript (strict mode)
- Vite
- Tailwind CSS + shadcn/ui
- Supabase (PostgreSQL + Auth + Edge Functions)
- Zod (validation)
- TanStack Query (server state)

## Build Commands
npm run dev     # local dev
npm run build   # production build
npm run lint    # ESLint check

## Project Structure
src/
  components/ui/   # shadcn/ui components (do not modify)
  components/       # app components
  hooks/            # custom hooks
  integrations/     # Supabase client, API calls
  pages/            # route pages
  types/            # TypeScript types

## Architecture
- API calls via integrations/ layer, NEVER in components
- Supabase client from integrations/supabase/client.ts
- Server state: TanStack Query (useQuery/useMutation)
- Client state: React useState/useReducer (minimal)
- Form validation: Zod schemas in types/
- Money: cents as integer, display with formatter

## Auth
- Supabase Auth (email + password)
- RLS enabled on all tables
- Always use (select auth.uid()) in policies

## Key Tables
- profiles (id UUID PK → auth.users, full_name, avatar_url)
- [table2] (campos essenciais)
- [table3] (campos essenciais)

## Domain Terms
- [Termo 1]: [definição]
- [Termo 2]: [definição]

## DO NOT
- Install new dependencies without approval
- Modify files in components/ui/ (shadcn managed)
- Change auth flow without explicit instruction
- Use 'any' type — use 'unknown' with narrowing
- Store secrets in client code
- Disable RLS on any table
```

---

## Quando gerar AGENTS.md vs usar só Knowledge

| Situação | Recomendação |
|----------|--------------|
| Projeto solo no Lovable, <10k chars de contexto | Workspace + Project Knowledge basta |
| Projeto multi-tool ou time > 1 pessoa | AGENTS.md no repo |
| Contexto > 10k chars | AGENTS.md (sem limite) + resumo no Knowledge |
| Projeto com Lovable + Claude Code | AGENTS.md + CLAUDE.md referenciando ele |
| Open source | AGENTS.md obrigatório |
