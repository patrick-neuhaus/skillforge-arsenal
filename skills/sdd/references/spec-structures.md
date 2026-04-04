# Spec Structures — Decomposicao e Agentes Especializados

Consulte este arquivo no **Phase 2 (Spec)** para features grandes ou full-stack.

---

## Estrutura Pagina / Componente / Comportamento

Para projetos com UI, a spec deve seguir esta hierarquia (Video 2):

```
Pagina
├── Componente A
│   ├── Comportamento 1 (ex: filtrar lista)
│   └── Comportamento 2 (ex: ordenar por data)
├── Componente B
│   ├── Comportamento 3 (ex: submit form)
│   └── Comportamento 4 (ex: validacao inline)
└── Componente C (shared/reusavel)
```

### Template de Spec por Pagina

```markdown
# Spec: [Nome da Pagina]

## Layout
- **Rota:** /[path]
- **Componentes:** [lista com hierarquia]
- **Dados necessarios:** [queries, server actions]

## Componentes

### [ComponenteA]
**Tipo:** Feature component (page-specific)
**Path:** src/components/features/[page]/ComponenteA.tsx
**Props:** { data: Type[], onAction: (id) => void }

#### Comportamento 1: [Nome]
**Trigger:** [evento do usuario]
**Acao:** [o que acontece]
**Edge cases:** [cenarios nao-obvios]

#### Comportamento 2: [Nome]
...
```

## Decomposicao em Issues Atomicas

Quando a feature e grande (>15 mudancas estimadas), quebre em issues:

### Regra: Prototipos Primeiro, Funcionalidade Depois

1. **Issues de prototipo:** So UI, sem funcionalidade. Cada pagina = 1 issue de prototipo.
   - Resultado: usuario pode ver e aprovar o layout antes de investir em logica
   - "Design first" adaptado pra IA

2. **Issues de funcionalidade:** 1 issue = 1 comportamento.
   - Cada comportamento e implementavel e testavel independentemente
   - Ordem definida por dependencias (ex: criar schema antes de query)

### Template de Issue

```markdown
## Issue [N]: [Nome do comportamento]

**Tipo:** Prototipo / Funcionalidade
**Pagina:** [pagina]
**Componente:** [componente]
**Dependencias:** [issues que devem ser feitas antes]

### Mudancas
[path] → [create/modify] → [o que fazer]

### Critérios de Aceite
- [ ] [criterio verificavel]
- [ ] [criterio verificavel]

### Testes
- [ ] [cenario de teste]
```

### Ordem de Issues

```
Issue 1: Prototipo pagina A (so layout, dados mock)
Issue 2: Prototipo pagina B
Issue 3: Schema + migrations (banco)
Issue 4: Queries + server actions (data layer)
Issue 5: Comportamento A1 (conectar prototipo com dados reais)
Issue 6: Comportamento A2
Issue 7: Comportamento B1
...
```

## Agentes Especializados por Camada

Para features full-stack, considere dividir a implementacao em sub-agents por camada (Video 2):

| Agente | Camada | Responsabilidade |
|--------|--------|-----------------|
| **Model Writer** | Database | Schemas, migrations, RLS, seeds, queries |
| **Component Writer** | Frontend | Componentes seguindo design system, atomic design |
| **API Writer** | Backend | Server actions, API routes, middleware, validacao |
| **Test Writer** | Testing | Testes unitarios, integracao, e2e |

### Como Funciona na Pratica

Nao e necessario ter 4 conversas separadas. O conceito e **mentalidade de camada**:

1. Na spec, agrupe mudancas por camada
2. Na implementacao, implemente uma camada por vez
3. Teste cada camada antes de passar pra proxima

```markdown
# Spec: [Feature] — Agrupado por Camada

## Camada 1: Database (Model Writer)
### 1. supabase/migrations/001_create_invoices.sql — create
### 2. src/lib/supabase/queries/invoices.ts — create

## Camada 2: API (API Writer)
### 3. src/app/api/invoices/route.ts — create
### 4. src/lib/validations/invoice.ts — create

## Camada 3: UI (Component Writer)
### 5. src/components/features/invoices/InvoiceTable.tsx — create
### 6. src/components/features/invoices/InvoiceForm.tsx — create

## Camada 4: Testes (Test Writer)
### 7. src/__tests__/invoices.test.ts — create
```

## Context Window e Specs Grandes

Se a spec tem >20 mudancas:
1. Divida em `spec-part1.md`, `spec-part2.md`
2. Cada parte deve ser implementavel independentemente
3. Execute `/clear` entre partes
4. A regra dos 40-50% se aplica POR PARTE, nao no total

## Anti-Patterns

- **Spec monolitica:** 30+ mudancas num unico spec.md → dividir em partes
- **Issues nao-atomicas:** "Implementar toda a pagina de settings" → quebrar por comportamento
- **Pular prototipos:** Ir direto pra funcionalidade sem validar UI = retrabalho visual
- **Ignorar camadas:** Implementar tudo junto = conflitos e efeito cobertor de pobre
- **Spec sem paths:** "Adicionar autenticacao" nao e spec. "src/app/(auth)/login/page.tsx → create" e spec
