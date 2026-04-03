# React / Next.js Pattern Guide — Complete Reference

Consulte este arquivo no **Phase 2** quando for auditar padrões.

---

## Server vs Client Components (Next.js App Router)

### Decision Matrix

| Need | Component Type | Why |
|------|---------------|-----|
| Fetch data | Server | Direct DB/API access, no waterfall |
| Read files/env | Server | Access to server-only resources |
| Render static content | Server | Zero JS bundle impact |
| Use useState/useReducer | Client | Needs React state |
| Use useEffect | Client | Needs lifecycle/side effects |
| Use browser APIs | Client | window, localStorage, navigator |
| Add event handlers | Client | onClick, onChange, onSubmit |
| Use React Context | Client | Context requires client-side re-render |

### Push Client Boundaries Down

```tsx
// ❌ Entire page is client
'use client'
export default function Dashboard({ }) {
  const [tab, setTab] = useState('overview')
  const data = useQuery(...) // client-side fetch
  return (
    <div>
      <Stats data={data.stats} />        {/* static */}
      <TabBar value={tab} onChange={setTab} />  {/* interactive */}
      <Content tab={tab} data={data} />   {/* mixed */}
    </div>
  )
}

// ✅ Only interactive parts are client
// app/dashboard/page.tsx (Server Component)
export default async function Dashboard() {
  const data = await getStats()  // server-side fetch
  return (
    <div>
      <Stats data={data.stats} />        {/* Server: zero JS */}
      <DashboardTabs data={data} />      {/* Client: only this ships JS */}
    </div>
  )
}

// components/DashboardTabs.tsx
'use client'
export function DashboardTabs({ data }) {
  const [tab, setTab] = useState('overview')
  return (...)
}
```

---

## Data Fetching Patterns

### Pattern 1: Server Component (preferred)

```tsx
// app/users/page.tsx — Server Component
export default async function UsersPage() {
  const users = await db.user.findMany()  // Direct DB access
  return <UserList users={users} />
}
```

### Pattern 2: Server Actions (mutations)

```tsx
// app/actions.ts
'use server'
export async function createUser(formData: FormData) {
  const name = formData.get('name')
  await db.user.create({ data: { name } })
  revalidatePath('/users')
}

// components/CreateUserForm.tsx
'use client'
import { createUser } from '@/app/actions'

export function CreateUserForm() {
  return (
    <form action={createUser}>
      <input name="name" />
      <button type="submit">Create</button>
    </form>
  )
}
```

### Pattern 3: Route Handlers (API endpoints)

Use ONLY for external consumers (webhooks, mobile apps, third-party integrations).

```tsx
// app/api/users/route.ts
export async function GET() {
  const users = await db.user.findMany()
  return Response.json(users)
}
```

**Do NOT** create Route Handlers for internal data fetching — use Server Components or Server Actions instead.

### Pattern 4: React Query/SWR (real-time client data)

Use ONLY when you need:
- Real-time updates (polling, WebSocket)
- Optimistic updates
- Client-side cache with automatic revalidation

```tsx
'use client'
import { useQuery } from '@tanstack/react-query'

export function LiveNotifications() {
  const { data } = useQuery({
    queryKey: ['notifications'],
    queryFn: () => fetch('/api/notifications').then(r => r.json()),
    refetchInterval: 5000,  // Poll every 5s
  })
  return <NotificationList items={data} />
}
```

---

## Loading & Error Patterns

### Route-Level (file convention)

```
app/dashboard/
├── page.tsx       # Main content
├── loading.tsx    # Shown while page loads (Suspense boundary)
├── error.tsx      # Shown on error (Error boundary)
└── not-found.tsx  # Shown for 404
```

### Component-Level (explicit Suspense)

```tsx
export default async function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Suspense fallback={<StatsSkeleton />}>
        <Stats />  {/* Streams in when ready */}
      </Suspense>
      <Suspense fallback={<ActivitySkeleton />}>
        <RecentActivity />  {/* Independent loading */}
      </Suspense>
    </div>
  )
}
```

### Error Boundary Pattern

```tsx
// app/dashboard/error.tsx
'use client'
export default function DashboardError({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div>
      <h2>Something went wrong</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  )
}
```

---

## Anti-Pattern → Pattern Migration Table

| Anti-Pattern | Fix | Example |
|-------------|-----|---------|
| `useEffect` + `fetch` | Server Component async | `const data = await getData()` |
| `'use client'` on page | Push boundary down | Extract interactive parts only |
| API route for internal use | Server Component or Action | Remove `/api/` middleman |
| Prop drilling 3+ levels | Composition or Context | Pass components, not data |
| `useEffect` for derived state | Compute during render | `const total = items.reduce(...)` |
| `React.memo` everywhere | Profile first | Only memo measured bottlenecks |
| Global state for server data | React Query or Server Component | Fetch where needed |
| Manual form handling | Server Action + `useActionState` | Progressive enhancement |
| Client-side redirects | `redirect()` in Server Component | Server-side redirect |
| `typeof window !== 'undefined'` | Separate client component | Don't check environment in render |

---

## Performance Patterns

### Code Splitting

```tsx
import dynamic from 'next/dynamic'

// Heavy client-only component — load on demand
const Chart = dynamic(() => import('@/components/Chart'), {
  loading: () => <ChartSkeleton />,
  ssr: false,  // Only if truly client-only (canvas, WebGL)
})
```

### Image Optimization

```tsx
import Image from 'next/image'

// Always use next/image — auto webp, lazy load, blur placeholder
<Image
  src="/hero.jpg"
  alt="Hero"
  width={1200}
  height={600}
  priority  // Only for above-the-fold images
  placeholder="blur"
  blurDataURL={blurDataUrl}
/>
```

### Parallel Data Fetching

```tsx
// ❌ Sequential — slow
const users = await getUsers()
const stats = await getStats()

// ✅ Parallel — fast
const [users, stats] = await Promise.all([
  getUsers(),
  getStats(),
])
```

---

## Next.js App Router File Conventions

| File | Purpose |
|------|---------|
| `page.tsx` | Route UI (required for route to exist) |
| `layout.tsx` | Shared layout (persists across navigation) |
| `loading.tsx` | Loading UI (Suspense boundary) |
| `error.tsx` | Error UI (Error boundary) |
| `not-found.tsx` | 404 UI |
| `route.ts` | API endpoint (GET, POST, etc.) |
| `template.tsx` | Like layout but re-renders on navigation |
| `default.tsx` | Fallback for parallel routes |

### Route Groups

```
app/
├── (auth)/          # Group: shared auth layout
│   ├── login/
│   └── register/
├── (dashboard)/     # Group: shared dashboard layout
│   ├── overview/
│   └── settings/
```

Parentheses `()` create groups WITHOUT affecting the URL path.

### Parallel Routes

```
app/dashboard/
├── @analytics/page.tsx   # Rendered in parallel
├── @feed/page.tsx        # Rendered in parallel
├── layout.tsx            # Receives both as props
└── page.tsx
```

```tsx
// layout.tsx
export default function Layout({ analytics, feed, children }) {
  return (
    <div className="grid grid-cols-2">
      <div>{children}</div>
      <div>{analytics}</div>
      <div>{feed}</div>
    </div>
  )
}
```
