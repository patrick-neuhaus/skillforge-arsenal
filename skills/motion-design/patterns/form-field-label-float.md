# Pattern: Form field label float (Material canonical)

> **Source:** DR-D Pattern 01
> **Categoria:** form / micro-interactions canonical UI
> **Pilar:** 1 (funcional/estrutural — extension Wave 9.1)
> **Quando usar:** forms operacionais B2B/SaaS (signup, settings, checkout, contact). Frequência altíssima por sessão. Material Design canonical (Stripe Elements `labels: 'floating'` API, Material 3 mwc-textfield, Vercel signup, Supabase dashboard).
> **Quando NÃO usar:** forms editorial single-input (email-only newsletter), search bar (placeholder ok), forms onde label sempre visível acima já cobre.

---

## Por quê (anti-placeholder-only)

Placeholder-only viola WCAG 1.3.1 (info perdida ao começar digitar) + WCAG 3.3.2 (sem label visível). Affordance cai. Site B+ vs A: A tem label que sobe + state visual claro.

## Snippet canonical (CSS-only via :placeholder-shown)

```html
<div class="field">
  <input id="email" type="email" placeholder=" " required>
  <label for="email">Email</label>
</div>
```

```css
.field { position: relative; padding-top: 16px; }
.field input {
  width: 100%; height: 40px; padding: 0 12px;
  border: 1px solid #cbd5e1; border-radius: 6px;
  font-size: 16px; background: transparent;
  transition: border-color 150ms cubic-bezier(0.2, 0, 0, 1);
}
.field label {
  position: absolute; left: 12px; top: 24px;
  font-size: 16px; color: #64748b;
  pointer-events: none;
  transform-origin: 0 0;
  transition: transform 150ms cubic-bezier(0.2, 0, 0, 1),
              color 150ms cubic-bezier(0.2, 0, 0, 1);
  background: white; padding: 0 4px;
}
.field input:focus { border-color: #3b82f6; outline: none; }
.field input:focus ~ label,
.field input:not(:placeholder-shown) ~ label {
  transform: translateY(-22px) scale(0.85);
  color: #3b82f6;
}

@media (prefers-reduced-motion: reduce) {
  .field label, .field input { transition: none; }
}
```

**Trick:** `placeholder=" "` (espaço) habilita `:placeholder-shown` pra detectar empty state sem JS.

## Spec técnico

| Trigger | Duração | Easing | Propriedades | Browser |
|---|---|---|---|---|
| `:focus` ou `:not(:placeholder-shown)` | 150ms | `cubic-bezier(0.2, 0, 0, 1)` (Material standard) | `transform`, `font-size`, `color` | Baseline 2020+ |

iOS HIG variant: 200ms suaviza com leve overshoot. Material 3 token "short4" (200ms) pra text-field motion.

## React adapter (Framer Motion)

CSS já resolve. Use Framer Motion APENAS se label tem layout shared com erro/helper (AnimatePresence).

```jsx
import { motion } from "framer-motion";

function Field({ label, ...props }) {
  const [focused, setFocused] = useState(false);
  const [value, setValue] = useState("");
  const float = focused || value.length > 0;

  return (
    <div className="relative pt-4">
      <input {...props} value={value}
        onChange={e => setValue(e.target.value)}
        onFocus={() => setFocused(true)}
        onBlur={() => setFocused(false)}
        className="w-full h-10 px-3 border rounded outline-none"/>
      <motion.label
        animate={{
          y: float ? -22 : 0,
          scale: float ? 0.85 : 1,
          color: focused ? "#3b82f6" : "#64748b"
        }}
        transition={{ duration: 0.15, ease: [0.2, 0, 0, 1] }}
        className="absolute left-3 top-6 origin-top-left bg-white px-1 pointer-events-none">
        {label}
      </motion.label>
    </div>
  );
}
```

## Reduced motion

`transition: none`; label salta direto ao estado final. Funcional preservado, motion timing some.

## A11y

- `<label for="id">` ou `<label>` envolvendo input — affordance + screen reader
- `:focus-visible` outline preservado, NUNCA animar o anel
- Required marker via `aria-required="true"` ou `*` visual + `aria-describedby` apontando pra hint
- Autofill: navegadores preenchem sem disparar `focus`; selector `input:-webkit-autofill ~ label` precisa do mesmo float treatment
- Tap target ≥ 44×44px (Apple HIG, WCAG 2.5.5) — input height 40px + padding ok

## Anti-patterns

1. **Placeholder-only sem label** — viola WCAG 1.3.1 e 3.3.2; perde affordance ao começar digitar (gap site-consultoria literal)
2. **Animar `top`/`left` em vez de `transform`** — força layout, não usa GPU
3. **Label dentro do input com cor low-contrast** — confunde com valor preenchido. Smashing Magazine 2021 (Adam Silver) documentou falha em testes de usabilidade
4. **`scale(0)` em label hidden** — screen readers ainda anunciam, mas reduzir `font-size` abaixo de 11px viola legibilidade
5. **`transition: all`** — anima props imprevisíveis (background-image autofill amarelo Chrome), causa jank

## Edge cases

- **Viewport pequeno:** garantir `font-size: 16px` no input pra evitar zoom iOS
- **RTL:** `transform-origin: 100% 0` e `right: 12px`
- **Dark mode:** `background` do label precisa match container (ou `background: var(--surface)`)
- **Password field:** ícone show/hide à direita não pode sobrepor label flutuante
- **Autofill (Chrome):** força background amarelo; workaround `transition: background-color 5000s`
- **Long labels (> 30 chars):** truncate com ellipsis OU considere conventional label acima do input

## Performance

CSS-only = zero JS overhead. Compositor-only (`transform`, `color`). Universal browser baseline.

## Boundary

- Reference 13 sec 1 (form patterns canonical)
- Reference 06-theoretical-foundations sec 4 (easing semantics — Material standard `cubic-bezier(0.2, 0, 0, 1)` source)
- ui-design-system Phase 4 (motion tokens — durations 150ms = "short" token)
- component-architect (anatomia FormField — não absorver, só motion spec aqui)
