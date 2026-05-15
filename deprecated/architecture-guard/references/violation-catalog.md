# Violation Catalog — Catalogo Completo de Violacoes

Consulte este arquivo no **Phase 2** como referencia de todas as violacoes possiveis.

---

## Indice por Rule ID

### Thin Client (TC-xxx)

| ID | Nome | Severity | Descricao |
|----|------|:--------:|-----------|
| TC-001 | no-business-logic-in-client | P0 | Logica de negocio (calculo, regra, state machine) em 'use client' |
| TC-002 | no-server-env-in-client | P0 | process.env sem NEXT_PUBLIC em client component |
| TC-003 | no-direct-db-in-client | P0 | Supabase/DB queries com logica de negocio em client |
| TC-004 | no-api-keys-in-client | P0 | API keys hardcoded ou expostas em client bundle |
| TC-005 | no-auth-decisions-in-client | P0 | Decisoes de acesso (role check, permission) apenas no client |

### Layer Separation (LS-xxx)

| ID | Nome | Severity | Descricao |
|----|------|:--------:|-----------|
| LS-001 | no-db-import-in-component | P1 | Component importa diretamente camada de dados |
| LS-002 | no-jsx-in-server-action | P1 | Server action retorna JSX ou manipula DOM |
| LS-003 | no-side-effects-in-utils | P1 | Funcao em utils/ faz fetch, write, ou mutation |
| LS-004 | no-circular-deps | P1 | Imports circulares (A→B→A) |
| LS-005 | no-mixed-concerns | P1 | Arquivo mistura UI + business logic + data access |

### Behavior Organization (BO-xxx)

| ID | Nome | Severity | Descricao |
|----|------|:--------:|-----------|
| BO-001 | organize-by-feature | P2 | Arquivos organizados por tipo em vez de por feature |
| BO-002 | no-feature-in-shared | P2 | Componente feature-specific em pasta shared/ |
| BO-003 | no-flat-directories | P2 | Diretorio com 20+ arquivos sem subdivisao |

### Convention Compliance (CC-xxx)

| ID | Nome | Severity | Descricao |
|----|------|:--------:|-----------|
| CC-001 | consistent-naming | P2 | Mix de convencoes de naming no mesmo diretorio |
| CC-002 | use-path-aliases | P2 | Imports relativos profundos (../../..) em vez de @/ |
| CC-003 | follow-project-patterns | P2 | Implementacao diverge dos padroes ja estabelecidos |

---

## Formato de Report

Cada violacao reportada deve seguir este formato:

```markdown
#### [ID] Nome da Violacao
**Severity:** P[0-2]
**File:** caminho/exato/arquivo.ext:linha
**Evidence:** `trecho de codigo que viola`
**Rule:** [descricao da regra violada]
**Fix:** [acao especifica para corrigir]
**Why:** [por que essa regra existe — consequencia de ignorar]
```

## Exemplos de Violacoes Reais

### TC-001 — Business Logic Leak
```typescript
// src/components/features/cart/CartTotal.tsx:15
'use client'
// VIOLACAO: calculo de preco com desconto no client
const finalPrice = items.reduce((sum, item) => {
  const discount = item.qty > 10 ? 0.15 : item.qty > 5 ? 0.10 : 0
  return sum + item.price * item.qty * (1 - discount)
}, 0)
```
**Fix:** Mover calculo para server action `calculateCartTotal(items)`.
**Why:** Regra de desconto e logica de negocio. No client, usuario pode manipular.

### LS-001 — DB Import in Component
```typescript
// src/components/features/users/UserList.tsx:3
'use client'
import { supabase } from '@/lib/supabase/client'
// Component faz query diretamente
const { data } = await supabase.from('users').select('*')
```
**Fix:** Criar query em `src/lib/supabase/queries/users.ts`, usar via server component ou server action.
**Why:** Componente nao deve conhecer a estrutura do banco. Camada de dados isolada facilita mudancas.

### BO-002 — Feature Code in Shared
```
src/components/shared/InvoiceStatusBadge.tsx  # So usado em src/features/invoices/
```
**Fix:** Mover para `src/components/features/invoices/InvoiceStatusBadge.tsx`.
**Why:** Se so 1 feature usa, nao e shared. Polui o namespace compartilhado.
