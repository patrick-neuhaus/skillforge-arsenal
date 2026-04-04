# Thin Client Rules — Regras de Escaneamento

Consulte este arquivo no **Phase 2** para os padroes de scan detalhados.

---

## Principio: Thin Client, Fat Server

"Tudo no frontend e acessivel com dois cliques no navegador" (Video 2). Se a logica esta no frontend, qualquer usuario pode:
- Ler a logica de negocio (desconto, precificacao, validacao)
- Burlar validacoes (bypassar frontend, mandar request direto)
- Acessar dados que deveriam ser protegidos

## Padroes de Violacao — O que Escanear

### P0: Business Logic Leak

**Indicadores em arquivos 'use client':**

```typescript
// VIOLACAO: fetch com logica de negocio
'use client'
const total = items.reduce((sum, i) => sum + i.price * i.qty * (1 - discount), 0)

// VIOLACAO: mutation com regra de negocio
'use client'
if (user.role === 'admin' && order.status === 'pending') {
  await approveOrder(order.id)
}

// VIOLACAO: state machine no client
'use client'
const [step, setStep] = useState('idle')
// ...complex state transitions with business rules

// OK: UI state (nao e violacao)
'use client'
const [isOpen, setIsOpen] = useState(false)    // modal toggle
const [tab, setTab] = useState('general')       // active tab
const [search, setSearch] = useState('')         // search input
```

**Grep patterns:**
```bash
# Buscar fetch/mutation em client components
grep -rn "'use client'" src/ --include="*.tsx" -l | xargs grep -l "fetch\|axios\|supabase\.\(from\|rpc\)"

# Buscar reduce/complex logic em client
grep -rn "'use client'" src/ --include="*.tsx" -l | xargs grep -l "\.reduce\|\.filter.*\.map\|switch.*case"

# Buscar process.env (non-public) em client
grep -rn "'use client'" src/ --include="*.tsx" -l | xargs grep -l "process\.env\." | xargs grep -v "NEXT_PUBLIC"
```

### P0: Security Placement

| Violacao | O que procurar |
|----------|---------------|
| Secrets no client | `process.env.` sem `NEXT_PUBLIC_` em arquivo 'use client' |
| Auth check no client | Decisao de acesso baseada apenas em state local |
| API key exposta | Chaves de API em codigo client-side |
| RLS bypass | Supabase client com `service_role` no frontend |

### P1: Layer Separation

| Violacao | Pattern |
|----------|---------|
| Component importa DB | `import { supabase } from` em arquivo de componente |
| Server action retorna JSX | `return <div>` em arquivo com "use server" |
| Util com side effect | Funcao em `utils/` que faz fetch, write, ou mutation |
| Circular dependency | A importa B, B importa A (direto ou transitivo) |

### P2: Organization

| Violacao | Como detectar |
|----------|--------------|
| Feature code em shared/ | Componente em `shared/` que so e usado em 1 feature |
| Tudo no mesmo nivel | Pasta `components/` com 50+ arquivos sem subpastas |
| Inconsistencia de naming | Mix de camelCase e PascalCase no mesmo diretorio |

## O que NAO e Violacao

| Padrao | Por que e OK |
|--------|-------------|
| `useState` para UI state | Toggle, modal, tab — nao e logica de negocio |
| `useEffect` para sync UI | Scroll, resize, animation — e concern de UI |
| `onChange` handlers simples | Input handling e responsabilidade do frontend |
| Validacao de UX | "Campo obrigatorio" no frontend e feedback, nao seguranca |
| Formatacao de display | `formatCurrency(value)` no client e apresentacao |
| Zustand/Context para UI state | Theme, sidebar, toast — UI concerns |

## Severidade

| Nivel | Significado | Acao |
|-------|------------|------|
| **P0** | Bloqueia merge. Risco de seguranca ou violacao fundamental | Fix obrigatorio |
| **P1** | Fix antes do merge se possivel. Debt arquitetural | Fix recomendado |
| **P2** | Fix ou cria follow-up issue. Convencao quebrada | Fix opcional |
