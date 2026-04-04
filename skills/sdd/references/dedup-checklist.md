# Dedup Checklist — Buscar Reutilizaveis Antes de Criar

Consulte este arquivo no **Phase 1, Step 2** antes de criar qualquer codigo novo.

---

## Principio

"Cria outro botao e agora voce tem manutencao dobrada" (Video 4). O maior desperdicio no vibe coding e reinventar o que ja existe. Este checklist previne isso.

## Checklist de Busca

### 1. Componentes UI
- [ ] Buscar no diretorio de componentes (`src/components/`, `components/`, `ui/`)
- [ ] Buscar por nome similar (Button, Modal, Card, Form, Table, List...)
- [ ] Checar se shadcn/ui ja tem o componente (antes de criar custom)
- [ ] Buscar variants existentes que podem ser estendidas (ex: Button ja tem variant="outline"?)

### 2. Funcoes e Utilitarios
- [ ] Buscar em `utils/`, `lib/`, `helpers/`
- [ ] Grep por nome da operacao (formatDate, parseJSON, validateEmail...)
- [ ] Checar se alguma dependencia instalada ja resolve (lodash, date-fns, zod...)
- [ ] Buscar custom hooks que encapsulam logica similar

### 3. Queries e Data Access
- [ ] Buscar queries existentes pro mesmo recurso (users, products, orders...)
- [ ] Checar se ja existe RPC/function no Supabase pra essa operacao
- [ ] Buscar server actions ou API routes existentes pra o mesmo dominio

### 4. Padroes e Convencoes
- [ ] Como features similares foram implementadas no projeto?
- [ ] Existe um padrao de composicao ja estabelecido? (ex: form pattern, list+detail pattern)
- [ ] Que libs o projeto ja usa pra resolver problemas similares?

## Como Buscar

```bash
# Buscar por nome de componente/funcao
grep -r "Button\|Modal\|Card" src/components/ --include="*.tsx"

# Buscar por operacao
grep -r "format.*Date\|parse.*JSON" src/ --include="*.ts" --include="*.tsx"

# Buscar por imports (o que ja e usado)
grep -r "from.*@/components" src/ --include="*.tsx" | sort | uniq -c | sort -rn

# Buscar por exports (o que existe disponivel)
grep -r "export.*function\|export.*const\|export.*default" src/lib/ src/utils/
```

## Decisao: Reuse, Extend, ou Create

| Cenario | Acao |
|---------|------|
| Componente identico ja existe | **Reuse** — importar direto |
| Componente similar mas falta variant | **Extend** — adicionar prop/variant |
| Funcao parecida mas dominio diferente | **Extract** — generalizar em util |
| Nada similar existe | **Create** — documentar no spec |

## Reportar no prd.md

Adicione uma secao "Reusables Found" no prd.md:

```markdown
## Reusables Found
- `src/components/ui/Button.tsx` — pode ser reutilizado com nova variant
- `src/lib/supabase/queries/users.ts` — query de usuario ja existe, estender
- `shadcn/ui Dialog` — usar em vez de criar modal custom

## New Code Needed
- `src/components/features/InvoiceTable.tsx` — nao encontrado similar
- `src/lib/supabase/queries/invoices.ts` — dominio novo, criar
```
