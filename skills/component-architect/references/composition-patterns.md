# Composition Patterns — Complete Reference

Consulte este arquivo no **Phase 2** quando for planejar a árvore de componentes e no **Phase 3** para design de interfaces.

---

## Atomic Design — Detailed Classification

### Atoms (primitivos visuais)

Menor unidade, sem dependência de outros componentes. Pura apresentação.

```
Button, Input, Label, Badge, Avatar, Icon, Spinner,
Separator, Skeleton, Tooltip, Switch, Checkbox, Radio
```

**Regras:**
- Zero business logic
- Aceita `className` para customização externa
- Variantes via prop discriminada (`variant="primary" | "secondary" | "ghost"`)
- Forwarded ref quando necessário (inputs, buttons)

### Molecules (combinações simples)

2-3 átomos combinados com propósito claro. Estado mínimo.

```
FormField (Label + Input + ErrorMessage)
SearchBar (Input + Button)
UserChip (Avatar + Name)
NavLink (Icon + Label + Badge)
StatCard (Icon + Number + Label)
```

**Regras:**
- Composição de átomos, não duplicação
- Se precisa de >3 átomos, provavelmente é organismo
- Estado local mínimo (ex: controlled input value)

### Organisms (seções complexas)

Múltiplas moléculas e átomos. Pode ter estado e data fetching.

```
Header (Logo + NavLinks + UserMenu)
DataTable (SearchBar + Table + Pagination)
CommentThread (CommentForm + CommentList)
Sidebar (NavGroup + UserProfile + Footer)
```

**Regras:**
- Pode usar hooks de estado e data fetching
- Deve ter responsabilidade clara (1 seção da UI)
- Se ultrapassa 200 linhas, decomponha

### Templates (layouts com slots)

Estrutura da página sem dados reais. Define onde os organismos ficam.

```tsx
function DashboardLayout({ sidebar, header, children }) {
  return (
    <div className="grid grid-cols-[250px_1fr]">
      <aside>{sidebar}</aside>
      <main>
        <header>{header}</header>
        <section>{children}</section>
      </main>
    </div>
  )
}
```

**Regras:**
- Zero data fetching — só estrutura
- Usa slots (children, named slots via props)
- Responsivo (grid/flex com breakpoints)

### Pages (templates + dados reais)

Conectam templates com dados. Geralmente são route handlers (Next.js `page.tsx`).

```tsx
// app/dashboard/page.tsx
export default async function DashboardPage() {
  const stats = await getStats()
  const recent = await getRecentActivity()

  return (
    <DashboardLayout
      sidebar={<Sidebar />}
      header={<DashboardHeader stats={stats} />}
    >
      <ActivityFeed items={recent} />
    </DashboardLayout>
  )
}
```

---

## Composition Patterns

### 1. Compound Components

Componentes que funcionam juntos com contexto implícito:

```tsx
<Select value={v} onValueChange={setV}>
  <SelectTrigger>
    <SelectValue placeholder="Choose..." />
  </SelectTrigger>
  <SelectContent>
    <SelectItem value="a">Option A</SelectItem>
    <SelectItem value="b">Option B</SelectItem>
  </SelectContent>
</Select>
```

**Quando usar:** Componentes com múltiplas partes que compartilham estado (tabs, select, accordion, dialog).

### 2. Render Props / Children as Function

```tsx
<DataFetcher url="/api/users">
  {({ data, loading, error }) => (
    loading ? <Spinner /> : <UserList users={data} />
  )}
</DataFetcher>
```

**Quando usar:** Raramente em React moderno. Prefira hooks.

### 3. Slot Pattern (named children)

```tsx
<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
    <CardAction><Button>Edit</Button></CardAction>
  </CardHeader>
  <CardBody>Content here</CardBody>
  <CardFooter>Footer</CardFooter>
</Card>
```

**Quando usar:** Quando o layout é flexível — o consumidor decide o que vai em cada slot.

### 4. HOC → Hook Migration

```tsx
// ❌ HOC (legacy)
const EnhancedComponent = withAuth(withTheme(MyComponent))

// ✅ Hook (modern)
function MyComponent() {
  const { user } = useAuth()
  const { theme } = useTheme()
  // ...
}
```

### 5. Polymorphic Components

```tsx
<Button as="a" href="/login">Login</Button>
<Button as="button" type="submit">Submit</Button>
```

**Quando usar:** Componente que precisa renderizar como diferentes elementos HTML mantendo o mesmo estilo.

---

## Component Health Metrics (para --audit)

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Props count | ≤5 | 6-7 | >7 |
| Component lines | ≤100 | 100-200 | >200 |
| Nesting depth | ≤3 | 4 | >4 |
| Direct dependencies | ≤5 | 6-8 | >8 |
| Reuse count | ≥3 | 2 | 1 (one-off) |
| Boolean props | 0-1 | 2 | >2 |

### Audit Report Format

```markdown
## Component Health Report

### Summary
- Total components: X
- Healthy: Y | Warning: Z | Critical: W

### Critical Issues
| Component | Metric | Value | Threshold | Action |
|-----------|--------|-------|-----------|--------|

### Reuse Opportunities
| Pattern | Components | Suggestion |
```

---

## shadcn/ui Integration Notes

shadcn/ui is copy-paste, not npm install. Key patterns:

1. **Components live in your codebase** — `components/ui/` is yours to modify
2. **Radix primitives underneath** — accessible by default
3. **Tailwind for styling** — use `cn()` utility for conditional classes
4. **Variants via `cva()`** — class-variance-authority for variant management

```tsx
// Typical shadcn pattern
import { cn } from "@/lib/utils"
import { cva, type VariantProps } from "class-variance-authority"

const buttonVariants = cva("inline-flex items-center justify-center rounded-md", {
  variants: {
    variant: {
      default: "bg-primary text-primary-foreground hover:bg-primary/90",
      destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
      outline: "border border-input bg-background hover:bg-accent",
      ghost: "hover:bg-accent hover:text-accent-foreground",
    },
    size: {
      default: "h-10 px-4 py-2",
      sm: "h-9 rounded-md px-3",
      lg: "h-11 rounded-md px-8",
    },
  },
  defaultVariants: { variant: "default", size: "default" },
})
```

**Rule:** Don't fight shadcn patterns. If the project uses shadcn, follow its conventions (cva, cn, Radix primitives). Don't mix with MUI/Chakra patterns.
