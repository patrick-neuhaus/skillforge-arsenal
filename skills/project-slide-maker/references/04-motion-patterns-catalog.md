# Motion Patterns Catalog (10)

> Carrega na Phase 5. Snippets TSX prontos. Compilado de DR03 (`outputs/motion-03-pattern-inventory-gemini-2026-05-04.md`).

## 1. Kanban moving (Framer layoutId)

Slide.type=demo + drag/move

```tsx
import { motion, AnimatePresence } from 'framer-motion';

<AnimatePresence>
  {cards.filter(c => c.col === col).map(c => (
    <motion.div key={c.id} layoutId={c.id}
      initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
      transition={{ type: 'spring', stiffness: 280, damping: 28 }}>
      {c.title}
    </motion.div>
  ))}
</AnimatePresence>
```

Duration: spring (~400ms equiv) | Reduced-motion: snap final state sem transition.

## 2. Chat stagger reveal (Framer variants)

Slide.type=demo + typing sequence

```tsx
const variants = { hidden: { opacity: 0, y: 10 }, show: { opacity: 1, y: 0 } };

<motion.div initial="hidden" animate="show"
  variants={{ show: { transition: { staggerChildren: 0.3 } } }}>
  {messages.map(m => <motion.div key={m.id} variants={variants}>{m.text}</motion.div>)}
</motion.div>
```

Duration: 300ms stagger | Reduced-motion: all visible immediate.

## 3. Form auto-fill (Framer filter blur)

```tsx
<motion.input
  initial={{ filter: 'blur(8px)' }}
  animate={{ filter: 'blur(0)' }}
  transition={{ delay: 0.5, duration: 0.4 }}
  value={typed} readOnly />
```

Duration: 400ms | Reduced-motion: no blur, value direto.

## 4. Dashboard counter (useMotionValue + useTransform)

```tsx
import { useMotionValue, useTransform, animate } from 'framer-motion';

const count = useMotionValue(0);
const rounded = useTransform(count, latest => Math.round(latest));
useEffect(() => animate(count, 1234, { duration: 2 }), []);

return <motion.span>{rounded}</motion.span>;
```

Duration: 2s | Reduced-motion: render final value direto.

## 5. Cursor + click ghost

```tsx
<motion.div
  animate={{ x: cursor.x, y: cursor.y }}
  transition={{ type: 'spring', damping: 30 }}>
  <CursorIcon />
</motion.div>
```

## 6. Modal/sidebar slide (CSS-only)

```tsx
<div className={isOpen ? 'translate-x-0' : '-translate-x-full'}
  style={{ transition: 'transform 280ms ease-out' }}>
  <Sidebar />
</div>
```

Duration: 280ms | Reduced-motion: snap state.

## 7. Page transitions (AnimatePresence)

```tsx
<AnimatePresence mode="wait">
  <motion.div key={pageKey}
    initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
    {pageContent}
  </motion.div>
</AnimatePresence>
```

Pode usar View Transitions API nativa também (CSS `view-transition-name`).

## 8. Stagger reveal lists (Framer hierarchical)

Mesma shape do #2 mas pra lists/grids — staggerChildren em parent.

## 9. Hover micro-interactions (Tailwind)

```tsx
<button className="transition-transform hover:scale-105 hover:shadow-lg">
  Click
</button>
```

Duration: 150ms (Tailwind default) | Reduced-motion: scale stays 1.

## 10. PDF region select (DOM puro)

```tsx
const [region, setRegion] = useState(null);
const onPointerDown = (e) => setRegion({ x0: e.clientX, y0: e.clientY });
// PointerEvents + getBoundingClientRect, sem libs externas
```

## Reduced-motion wrapper (IL2 gate)

```tsx
import { useReducedMotion } from 'framer-motion';

function useMotionProps(props) {
  const reduce = useReducedMotion();
  return reduce
    ? { initial: false, animate: props.animate, transition: { duration: 0 } }
    : props;
}
```

Aplicar em CADA pattern com motion. Sem isso = WCAG 2.3.3 violation + IL2 fail.
