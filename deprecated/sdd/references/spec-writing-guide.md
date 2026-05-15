# Spec Writing Guide — Formato Path→Action

Consulte este arquivo no **Phase 2 (Spec)** quando for gerar spec.md.

---

## Princípio Central

A spec deve ser tão específica que uma conversa NOVA (sem contexto anterior) consiga implementar tudo apenas lendo spec.md. Se precisa de interpretação, está vago demais.

## Formato Path→Action

Cada mudança é um bloco com 4 campos obrigatórios:

```markdown
### [N]. [caminho/exato/do/arquivo.ext] — [create/modify/delete]

**What:** [Descrição específica OU pseudocódigo]

**Why:** [Razão — conecta com prd.md ou requisito]

**Dependencies:** [Outros arquivos que este precisa/afeta]
```

### Exemplo Real

```markdown
### 1. src/lib/supabase/queries/leads.ts — create

**What:**
- Export async function `upsertLead(lead: LeadInput): Promise<Lead>`
- Use `supabase.from('leads').upsert()` with `onConflict: 'email,organization_id'`
- Return the upserted row
- Throw `LeadUpsertError` on failure with original error attached

**Why:** Resolve race condition BUG-003 — current SELECT+INSERT has 50ms window for duplicates

**Dependencies:** Requires UNIQUE constraint on (email, organization_id) from change #2

### 2. supabase/migrations/20260403_add_lead_unique.sql — create

**What:**
- ALTER TABLE leads ADD CONSTRAINT leads_email_org_unique UNIQUE (email, organization_id)
- Add IF NOT EXISTS guard

**Why:** Database-level protection against duplicate leads (belt for the suspenders in #1)

**Dependencies:** None — run before deploying #1

### 3. src/app/api/webhooks/lead/route.ts — modify

**What:**
- Replace lines 45-62 (SELECT followed by INSERT) with call to `upsertLead()`
- Import `upsertLead` from `@/lib/supabase/queries/leads`
- Remove old `checkLeadExists()` function (now dead code)

**Why:** Migrate from racy read-then-write to atomic upsert

**Dependencies:** #1 must exist first
```

## Regras

### Ultra-específico significa:
- **Caminho exato** — `src/components/Dashboard/Stats.tsx`, não "o componente de stats"
- **Ação explícita** — create/modify/delete, não "ajustar" ou "melhorar"
- **Pseudocódigo quando complexo** — se a lógica não é óbvia, escreva pseudocódigo
- **Linhas quando modificar** — "Replace lines 45-62" ou "After line 30, add:"
- **Imports explícitos** — "Import X from Y" quando relevante

### Ordem importa:
- Numere as mudanças na ordem de implementação
- Dependencies determinam a ordem: se #3 depende de #1, #1 vem primeiro
- Migrations sempre antes do código que as usa

### Tamanho:
- Spec ideal: 5-15 mudanças
- Se >20 mudanças: quebre em 2 specs (spec-part1.md, spec-part2.md)
- Cada mudança: 5-15 linhas (não mais)

## Anti-Patterns de Spec

- **"Melhorar o componente X"** — vago. COMO melhorar? O que muda especificamente?
- **"Adicionar tratamento de erro"** — ONDE? Qual erro? Qual handler?
- **"Refatorar pra ficar melhor"** — não é spec, é desejo. Especifique as mudanças.
- **"Seguir o padrão do projeto"** — qual padrão? Cite o arquivo de referência.
- **"Criar testes"** — pra quê? Quais cenários? Quais assertions?

## Checklist de Qualidade da Spec

Antes de entregar spec.md:
- [ ] Cada mudança tem caminho exato de arquivo
- [ ] Cada mudança tem ação explícita (create/modify/delete)
- [ ] Mudanças complexas têm pseudocódigo
- [ ] Dependencies entre mudanças estão claras
- [ ] Ordem de implementação faz sentido
- [ ] Spec é implementável sem contexto adicional
- [ ] Total de mudanças entre 5-15 (ou quebrou em parts)

## Técnica .tmp (Video 4 — SDD)

Quando precisar aprender um padrão de outro projeto:

```bash
# 1. Clone o repo de referência em pasta temporária
git clone --depth 1 <repo-url> .tmp-reference

# 2. Analise o padrão
# Leia os arquivos relevantes, extraia o padrão

# 3. Documente o padrão no spec.md
# "Seguir padrão de .tmp-reference/src/auth/middleware.ts"

# 4. Delete a pasta temporária
rm -rf .tmp-reference
```

**Quando usar:** Implementando padrão que existe em outro projeto (auth, payments, etc.)
**Cuidado:** Não copie código — extraia o padrão e adapte ao seu contexto.
