# PRD Example — Modelo de prd.md

Consulte este arquivo no **Phase 1 (Research)** como referência de formato.

---

## Exemplo: Feature de Lead Deduplication

```markdown
# PRD: Lead Deduplication via Atomic Upsert

## Context
Webhooks de múltiplas fontes (Typeform, Calendly, manual) enviam leads para o sistema.
Quando 2 webhooks chegam simultaneamente para o mesmo email, o fluxo atual (SELECT + INSERT)
cria duplicatas. Estimativa: ~3% dos leads são duplicados (50-100/mês).

## Codebase Analysis
- **Stack:** Next.js 14 (App Router) + Supabase + TypeScript
- **Relevant files:**
  - `src/app/api/webhooks/lead/route.ts` — webhook handler (problema está aqui, L45-62)
  - `src/lib/supabase/queries/` — pattern de queries existente (upsert não existe ainda)
  - `supabase/migrations/` — 23 migrations existentes, formato: YYYYMMDD_description.sql
  - `src/types/lead.ts` — tipos existentes (Lead, LeadInput)
- **Conventions:**
  - Queries em `src/lib/supabase/queries/[entity].ts`
  - Migrations nomeadas com data
  - Error handling com classes custom (`src/lib/errors/`)
  - Tests em `__tests__/` co-located
- **Dependencies:**
  - webhook handler → queries → supabase client
  - Não tem UNIQUE constraint em (email, organization_id) — isso É o bug

## Constraints
- Não pode quebrar webhooks existentes durante deploy
- Migration precisa ser backwards-compatible (UNIQUE constraint é additive)
- Não pode usar advisory locks (Supabase free tier não suporta)
- Precisa manter idempotência (mesmo webhook pode chegar 2x)

## Scope
**IN scope:**
- Fix do race condition com upsert atômico
- UNIQUE constraint no banco
- Cleanup de duplicatas existentes

**OUT of scope:**
- Merge de dados de leads duplicados (feature separada)
- Webhook retry logic (já funciona)
- Dashboard de monitoramento de duplicatas (nice-to-have futuro)
```

## Anatomia de um Bom PRD

| Seção | O que incluir | O que NÃO incluir |
|-------|---------------|-------------------|
| **Context** | Problema, impacto, números se possível | Solução técnica (isso é pra spec) |
| **Codebase Analysis** | Stack, arquivos relevantes, conventions, dependencies | Código completo (cite paths + linhas) |
| **Constraints** | Limitações técnicas, backward compat, env constraints | Opiniões sobre como resolver |
| **Scope** | IN scope + OUT scope explícitos | Tudo — se não tem boundary, a spec vai inflar |

## Red Flags de PRD Ruim

- **Sem arquivos listados** — spec não vai saber onde mexer
- **Sem constraints** — spec vai over-engineer
- **Scope sem "OUT"** — feature vai crescer durante implement
- **Solução no PRD** — PRD documenta o PROBLEMA, spec define a SOLUÇÃO
- **Copy-paste de issue** — PRD precisa de análise de codebase, não só o pedido do usuário
