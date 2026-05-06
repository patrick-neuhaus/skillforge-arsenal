# `references/13-microinteractions-canonical.md` — Micro-interactions canonical UI (Wave 9.1)

> **Source:** DR-D MERGED (1614L) — Claude 18 patterns + ChatGPT apêndices semânticos. Gap real validado em site-consultoria/JRG Corp 2026-05-05.
> **Quando usar:** Phase 1 lookup do `--full` consulta esta ref pra patterns micro candidatos. `--quick` tb pode usar invocando `motion-design --spec micro-<pattern>`.
> **Boundary:** patterns canonical UI operacional repetida (form, button, toast, drawer, tooltip, etc). Recipes GSAP estruturais em `05-gsap-recipes.md`. Foundations theoretical em `06-theoretical-foundations.md`. Stack adapter React em `12-react-adapters.md`.

---

## 0. Princípios transversais (8 do DR-D)

1. **Easing assimétrico** — entrada usa ease-out (responsivo, "presente"); saída usa ease-in (some). Material 3 standard `cubic-bezier(0.2, 0, 0, 1)`, accelerate `cubic-bezier(0.3, 0, 1, 1)`, decelerate `cubic-bezier(0, 0, 0.2, 1)`.
2. **Duração por frequência** — o que user vê N vezes/sessão precisa ser ≤200ms. Press feedback 100-160ms; hover state 150-200ms; reveal pequeno 200-300ms; modal/drawer 300-500ms.
3. **Transitions > keyframes para interatividade** — keyframes não são interruptíveis; CSS transitions retargetam smooth ao mudar valor mid-flight. Springs (Framer Motion, react-spring) preservam velocidade.
4. **Compositor-only** — animar `transform`, `opacity`, `filter`. Evitar `width`, `height`, `top`, `left`, `margin` (layout reflow).
5. **Reduced-motion gate** — `@media (prefers-reduced-motion: reduce)` substitui transform por instant state-change preservando feedback funcional (cor, ícone, mensagem). Eliminar APENAS o motion timing — não o feedback.
6. **Focus preservado** — NUNCA animar `:focus-visible` outline; animar o elemento, não o anel. Modais/dialogs devolvem focus ao trigger.
7. **ARIA primeiro, animação depois** — status changes anunciam via `aria-live` antes/durante o transform; toasts usam `role="status"` (polite) ou `role="alert"` (assertive).
8. **Tokens de motion** — durations e easings em CSS variables / design tokens, nunca inline. Permite ajuste global e modo reduced-motion centralizado. Cross-ref: ui-design-system Phase 4 motion-and-interaction.md.

---

## 1. Form patterns

### 1.1 Floating label (Material/Stripe canonical)
**Pattern dedicado:** `patterns/form-field-label-float.md`
**Spec:** 150ms `cubic-bezier(0.2, 0, 0, 1)` translateY(-22px) scale(0.85)
**Quando:** TODO form B2B/SaaS com 2+ inputs. Anti-placeholder-only WCAG 1.3.1.

### 1.2 Underline reveal from center (variant minimal)
**Spec:** 250ms `cubic-bezier(0.2, 0, 0, 1)` `transform: scaleX(0)` → `scaleX(1)` from `transform-origin: center`
**Quando:** landing premium editorial (Stripe pricing, Apple). NÃO em forms B2B operacional.

```css
.field-underline .underline {
  position: absolute; bottom: 0; left: 0; right: 0;
  height: 2px; background: #3b82f6;
  transform: scaleX(0); transform-origin: center;
  transition: transform 250ms cubic-bezier(0.2, 0, 0, 1);
}
.field-underline input:focus ~ .underline { transform: scaleX(1); }
```

**Cross-ref:** site-consultoria nav links já usam variant `transform-origin: left` — válido pra nav, não pra form fields.

### 1.3 Validation feedback consolidated (shake + helper + error-clear + checkmark)
**Pattern dedicado:** `patterns/form-validation-feedback.md`
**Spec:**
- Shake: 400ms 4 oscillations 8px amplitude `cubic-bezier(0.36, 0.07, 0.19, 0.97)`
- Helper fade: 150-200ms ease-out `opacity` + `translateY(2px)`
- Error clear: 200ms ease-out `border-color` + `max-height` 0→40px
- Checkmark draw: 400-600ms `cubic-bezier(0.65, 0, 0.45, 1)` `stroke-dashoffset`
**Quando:** TODO form com validation server-side OR client-side rules.

---

## 2. Button patterns

### 2.1 Press compress + spring back (CRITICAL)
**Pattern dedicado:** `patterns/button-press-compress.md`
**Spec:** `:active` scale(0.97) 100ms ease-out + release 200-250ms `cubic-bezier(0.34, 1.56, 0.64, 1)` (overshoot) OU `cubic-bezier(0.2, 0, 0, 1)` (critically-damped)
**Quando:** TODO botão clicável funcional. Anti-pattern explícito: `translateY(-2px)` only.

### 2.2 Loading state (async submit)
**Pattern dedicado:** `patterns/button-loading-async.md`
**Spec:** label `opacity` 1→0 em 150ms ease-out + spinner `rotate` 600ms linear infinite + `aria-busy` + width preserve
**Quando:** TODO submit assíncrono. Critical: anti-double-submit + anti-layout-shift.

### 2.3 Magnetic pull (cursor follower)
**Cross-ref Wave 1:** `patterns/osmo-button-pack.md` Variant 2
**Quando:** CTA hero brand premium (1-2 max), landing premium aspiring. NÃO em SaaS operacional.
**ANTI-USE B2B:** distrai. Frequência amplifica fricção.

### 2.4 Border draw on hover
**Cross-ref Wave 1:** `patterns/osmo-button-pack.md` Variant 3
**Quando:** botões secondary/ghost de brand site editorial.

---

## 3. Feedback efêmero patterns

### 3.1 Toast notification (Sonner-style)
**Pattern dedicado:** `patterns/toast-sonner-canonical.md`
**Spec:** mount 400ms ease-out + dismiss 300ms ease-in + stack offset interruptível + auto-close 4000ms + swipe dismiss velocity-based
**Quando:** feedback efêmero pós-action (save, copy, error). Use Sonner direto (~5KB).

### 3.2 Drawer (Vaul-style bottom-sheet)
**Spec:** open easing iOS curve `cubic-bezier(0.32, 0.72, 0, 1)` 500ms + `closeThreshold: 0.25` + `VELOCITY_THRESHOLD: 0.4` + body scale 0.97 + backdrop opacity 0→0.4-0.6
**Quando:** mobile bottom-sheet (settings, filters, options). Use Vaul direto — drag tracking + dampening + scroll lock corretamente é não-trivial.

```jsx
import { Drawer } from "vaul";

<Drawer.Root shouldScaleBackground>
  <Drawer.Trigger>Open</Drawer.Trigger>
  <Drawer.Portal>
    <Drawer.Overlay className="fixed inset-0 bg-black/40"/>
    <Drawer.Content className="fixed bottom-0 left-0 right-0 bg-white rounded-t-2xl">
      <div className="mx-auto mt-2 h-1 w-12 rounded-full bg-zinc-300"/>
      …
    </Drawer.Content>
  </Drawer.Portal>
</Drawer.Root>
```

**A11y:** `role="dialog"` `aria-modal="true"` + focus trap + Esc fecha + restaura focus ao trigger (Vaul faz via Radix Dialog underneath).

### 3.3 Skeleton wave loading
**Spec shimmer:** `linear-gradient(90deg, #e5e7eb 25%, #f3f4f6 50%, #e5e7eb 75%)` 200% size + animate `background-position` 1.5s linear infinite
**Spec pulse:** `opacity 50%` em 1.5s ease-in-out infinite
**Spec content-aware:** match form real (avatar redondo, lines width 60%/80%/40%)
**Quando:** loading de layout conhecido. NÃO em empty state ou first paint hero.
**A11y:** container `aria-busy="true"` + `aria-live="polite"`. Reduced motion: `animation: none`.

```css
.skeleton {
  background: linear-gradient(90deg, #e5e7eb 25%, #f3f4f6 50%, #e5e7eb 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite linear;
}
@keyframes shimmer {
  from { background-position: 200% 0; }
  to   { background-position: -200% 0; }
}
```

**Lib alternative low-dep:** [`nullilac/skeleton-screen-css`](https://github.com/nullilac/skeleton-screen-css) (MIT, pure CSS, 107⭐, framework-agnostic). Útil pra projetos sem Tailwind.

---

## 4. Overlay/contextual patterns

### 4.1 Tooltip position-aware (Radix/Floating UI)
**Pattern dedicado:** `patterns/tooltip-floating-ui.md`
**Spec:** open delay 700ms + close delay 100-300ms + animation 120-180ms fade + translate 4px + edge detection (flip + shift)
**Quando:** ícone-only buttons, abreviações, info auxiliar. Use Radix/Floating UI direto.

### 4.2 Hover card with stagger children
**Cross-ref Wave 1:** `patterns/splittext-stagger.md` cobre stagger light. Pattern dedicado **NÃO criado** Wave 9.1 (frequência baixa em SaaS B2B Patrick).
**Spec:** open delay 700ms (Radix) + parent 150-200ms ease-out + children stagger 50-80ms each + close delay 300ms
**Quando:** profile preview, link preview rich (Twitter/X profile, Vercel team). Use Radix HoverCard.

```jsx
import * as HoverCard from "@radix-ui/react-hover-card";

<HoverCard.Root openDelay={700} closeDelay={300}>
  <HoverCard.Trigger asChild><a>@user</a></HoverCard.Trigger>
  <HoverCard.Portal>
    <HoverCard.Content sideOffset={8}>
      {/* children com stagger via CSS nth-child OR Framer Motion */}
    </HoverCard.Content>
  </HoverCard.Portal>
</HoverCard.Root>
```

**Diferença Tooltip vs HoverCard:** HoverCard pode ter conteúdo interativo (botão Follow), Tooltip não.

### 4.3 Tab shared-underline transition
**Spec:** FLIP via Framer Motion `layoutId` 250-350ms spring stiffness 400 damping 30 OR View Transitions API 250ms
**Quando:** dashboards SaaS (sidebar nav, settings tabs).

```jsx
{tabs.map(tab => (
  <button key={tab} onClick={() => setActive(tab)} className="relative">
    {tab}
    {active === tab && (
      <motion.div layoutId="tab-underline"
        className="absolute bottom-0 left-0 right-0 h-0.5 bg-blue-500"
        transition={{ type: "spring", stiffness: 400, damping: 30 }}/>
    )}
  </button>
))}
```

**View Transitions API baseline (Jan 2026):** Chrome 111+, Safari 18+, Firefox 146+ — Newly Available. Fallback: Framer Motion `layoutId`.

---

## 5. Interactive frequência média patterns

### 5.1 Copy-to-clipboard icon morph
**Spec:** click → icon swap (clipboard→check) 200-300ms ease-out scale + hold success 1500-2000ms + revert 200ms ease-in
**Quando:** copiar URL/snippet/token (dev tools, dashboards). Use `aria-live="polite"` em sibling pra anúncio "Copied".

```jsx
const [copied, setCopied] = useState(false);

const onCopy = async () => {
  await navigator.clipboard.writeText(text);
  setCopied(true);
  setTimeout(() => setCopied(false), 2000);
};

<button onClick={onCopy} aria-label="Copy">
  <AnimatePresence mode="wait" initial={false}>
    {copied ? (
      <motion.span key="c"
        initial={{ scale: 0.6, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.6, opacity: 0 }}
        transition={{ duration: 0.2 }}>
        <CheckIcon/>
      </motion.span>
    ) : (
      <motion.span key="d"
        initial={{ scale: 0.6, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.6, opacity: 0 }}
        transition={{ duration: 0.2 }}>
        <CopyIcon/>
      </motion.span>
    )}
  </AnimatePresence>
</button>
<span className="sr-only" aria-live="polite">{copied && "Copied"}</span>
```

---

## 6. Tabela A — Easings técnicas (curvas exatas)

| Nome | Curve | Sensação | Usar em |
|---|---|---|---|
| `linear` | `cubic-bezier(0, 0, 1, 1)` | Mecânico, robótico | Loops infinitos (spinner, marquee, shimmer) |
| Material standard | `cubic-bezier(0.2, 0, 0, 1)` | Ágil, propósito | Default UI moderno |
| Material decelerate | `cubic-bezier(0, 0, 0.2, 1)` | Aterrissar suave | Entradas (modal, toast in) |
| Material accelerate | `cubic-bezier(0.3, 0, 1, 1)` | Decolar | Saídas (modal, toast out) |
| Strong ease-out (Emil) | `cubic-bezier(0.23, 1, 0.32, 1)` | Snappy presente | UI premium |
| Strong ease-in-out (Emil) | `cubic-bezier(0.77, 0, 0.175, 1)` | Movimento on-screen | Layout shift, FLIP |
| iOS curve (Vaul) | `cubic-bezier(0.32, 0.72, 0, 1)` | Mobile feel | Drawers, sheets, page transitions mobile |
| easeOutBack (overshoot) | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Tátil, springy | Button release, like burst |
| Spring (FM) | stiffness 300-500, damping 25-35 | Físico interruptível | Gestos, drag, layout animations |
| Linear easing custom | `linear(0, 0.5, 1, 0.95, 1)` | Bounces multi-step | CSS-native bounces (CSS modern) |

**Cross-ref:** `06-theoretical-foundations.md` Section 4 cobre easing semantics theoretical (curves transmitem sensações). Esta tabela = curvas exatas pra implementação.

## 7. Tabela B — Easings semânticas (mapping alto-nível)

| Nome semântico | Modelo | Sensação | Melhor uso |
|---|---|---|---|
| Emphasized decelerate | `cubic-bezier(0.05, 0.7, 0.1, 1)` | Arrives confidently, soft landing | Field focus, helper reveal, underline reveal |
| Emphasized accelerate | `cubic-bezier(0.3, 0, 0.8, 0.15)` | Exits decisively | Blur-to-rest, dismissals |
| Soft out | `cubic-bezier(0.16, 1, 0.3, 1)` | Crisp but forgiving | Buttons, tabs, tooltips, hover cards |
| Vaul sheet ease | `cubic-bezier(0.32, 0.72, 0, 1)` | Heavier surface | Bottom sheets, drawers |
| Physics spring | stiffness/damping/mass | Reactive, velocity-aware | Press release, magnetic pull, shared underlines |
| Linear | `linear` | Mechanical / neutral | Shimmers, spinners, progress bars |
| Ease-out (UA default) | `cubic-bezier(0.25, 0.1, 0.25, 1)` | Simple and familiar | One-shot micro-confirmations |

---

## 8. Decision tree por contexto (qual pattern em qual site)

### B2B operacional (JRG Corp, dashboards comerciais simples, contact forms)
- **Easing default:** Material standard `cubic-bezier(0.2, 0, 0, 1)`
- **Durações:** 100-200ms presses, 200-300ms reveals
- **Patterns prioritários:** form-field-label-float, form-validation-feedback, button-press-compress, button-loading-async, toast-sonner-canonical
- **Patterns secundários:** tooltip-floating-ui (em ícone-only buttons)
- **EXCLUIR:** magnetic, custom cursor, like burst, hover card pesado, drawer (a menos que mobile-first)

### SaaS operacional (Linear, Vercel, Notion, dashboards interativos)
- **Easing default:** Material standard / Strong ease-out Emil
- **Durações:** 100-200ms presses, 200-300ms reveals
- **Patterns prioritários:** TODOS os 6 patterns Wave 9.1 + tab-shared-underline + copy-clipboard
- **EXCLUIR:** magnetic, custom cursor (B2B serioso)

### Landing premium (Stripe, framer.com)
- **Easing:** ease-out forte + springs
- **Durações:** 200-400ms; entradas hero 600-800ms
- **Patterns:** subset operacional + magnetic CTAs hero (1-2 max) + custom cursor subtle (mix-blend) + osmo-button-pack Variants 2/3 (Wave 1 cross-ref)
- **Foco:** encantamento controlado

### Brand site / portfolio (Awwwards SOTD)
- **Easing:** customizado por scene; springs lúdicos
- **Durações:** livres (1-3s page transitions)
- **Patterns:** custom cursor norma + magnetic norma + hover-card stagger pesado + osmo-text-effects (Wave 1 cross-ref)
- **Forms:** conservador mesmo aqui (form-field-label-float vale)

---

## 9. ANTI-USE em SaaS B2B (anti-bloat por subtração)

Patterns DR-D que NÃO entram em motion-design Wave 9.1 patterns/ porque são out-of-scope SaaS B2B Patrick:

| Pattern DR-D | Por quê NÃO entra |
|---|---|
| Custom cursor with lerp | "Brand site only / 0 em SaaS" (DR-D próprio confessa). Patrick contexto SaaS B2B operacional + landings B2B |
| Like/heart burst animation | "Tom errado em LinkedIn endorse" (DR-D próprio). Patrick faz B2B comércio internacional / SaaS operacional. Out of scope |
| Magnetic button pull | Wave 1 já tem `osmo-button-pack.md` Variant 2. Cross-ref, não pattern duplicado |
| Border draw on hover | Wave 1 já tem `osmo-button-pack.md` Variant 3. Cross-ref |
| Underline reveal from center | Wave 1 site-consultoria já usa variant `transform-origin: left` em nav. Inline em sec 1.2, não pattern dedicado |
| Hover card pesado (stagger 4 children) | Wave 1 splittext-stagger cobre. Inline em sec 4.2, não pattern dedicado |

**Knowledge negativo:** futuro Claude tentando reabrir esses patterns "porque tava no DR-D" → consultar esta section. Anti-drift.

---

## 10. Lessons cross-cutting (combinado Claude + ChatGPT DR-D)

### Lessons técnicas (8)

1. **Transitions > keyframes para state-dependent UI** — Sonner mudou pra CSS transitions porque keyframes não retargetam.
2. **Spring vs cubic-bezier para gestos** — drag/swipe/drawer = spring (preserva velocity). Hover/focus binário = cubic-bezier.
3. **Asymmetric ease-out vs ease-in** — entrada rápida + desacelera (responsivo); saída acelera + some (intencional).
4. **Reduced-motion não é "remover tudo"** — substituir transform por instant state-change preservando feedback funcional.
5. **ARIA precede ou acompanha o motion** — status changes anunciam via `aria-live` independente da animação.
6. **Compositor-only é law** — `transform` e `opacity` (e `filter` com cuidado).
7. **Tap target ≥ 44×44px** — mesmo se ícone 16px (padding faz trabalho).
8. **Delay opens, snappy closes** — tooltips/hover cards 700ms abrir, 100-300ms fechar. Cooldown reduz fricção.

### Lessons sistêmicas (6 prosa)

1. Cada "premium" micro-interaction vira mediocre quando aplicada indiscriminadamente. Magnetic pull, custom cursor, heart bursts pioram quando multiplicados em routine product surfaces.
2. Canonical micro-interactions reservam geometry antes de animar conteúdo: helper lines têm reserved height, loading buttons preserve width, shared underlines movem como single element.
3. Best production references publicam constraints comportamentais, não só visuais. Vercel documenta blur-first validation, tooltip delay, button loading delay. Sonner/Vaul publicam constants. Material publica token bands.
4. Reduced motion deve ser designed pattern-by-pattern, não global CSS reset. Drawer ainda precisa layering + focus management; tooltip ainda precisa delay; like burst não precisa particles; magnetic button não precisa mover.
5. Accessibility e motion são coupled. Tooltips afetam naming, drawers herdam dialog semantics, tabs herdam keyboard navigation. Motion decision NUNCA é puramente visual — é interaction contract.
6. Interruptions são o real test. Toast stacks reflowing, drawers reverse based on velocity, fields cuja errors clear during correction, buttons que mudam pra loading sem perder width/focus — solução canonical é a que sobrevive retargeting.

---

## 11. Auto-crítica + INVESTIGAR markers

**Cobertura técnica:**
- Patterns 11 (Toast Sonner) e 12 (Drawer Vaul) recomendam lib em vez de byte-perfect from scratch. Reimplementar drag-velocity-momentum corretamente excede 200 LoC. Source code Vaul `src/index.tsx` constants + `helpers.ts` cobrem velocity tracking algorithm caso evite dep.
- Pattern 17 (Tab shared underline) toca View Transitions API que pode aparecer em `12-react-adapters.md` page transitions. Mantido aqui só uso específico tab-underline.

**Easing/duração source-backed (strongest):**
Patterns 1, 4, 5, 7, 9, 10, 14, 15, 16, 18 usam timings com lastro direto (Material 3 tokens, Sonner/Vaul/Radix defaults, Emil Kowalski guidelines, React Aria).

**Easing/duração observados sem standard único (`[INVESTIGAR]`):**
- Pattern 2 (underline center) — valores observados em demos canonical (Codrops, Quackit), sem standard único
- Pattern 8 (magnetic strength 0.3-0.4) — corroborado Olivier Larose, Cassie Evans, Motion.page tutorials. Apple HIG não cobre magnetic. Source primária Awwwards/Apple = não há
- Pattern 13 (cursor lerp factor 0.15-0.2) — Olivier Larose + jQuery-cursor-magnetic plugin defaults. Heurística comunidade, não W3C standard
- Pattern 14 (hover-card child stagger 50-80ms) — observado Vercel/Twitter/Linear mas sem doc explícita

**Marca como recommended house defaults**, não authoritative vendor specs.

---

## 12. Sources

### Standards
- Material Design 3 Motion: https://m3.material.io/styles/motion/easing-and-duration/tokens-specs
- Apple HIG (motion, text fields, RTL)
- WAI-ARIA APG (Tooltip, Tabs, Dialog)
- WCAG 2.3.3 Animation from Interactions
- MDN: prefers-reduced-motion, focus-visible, View Transitions API, Pointer Events, Clipboard API

### Component libraries canonical
- Sonner: https://sonner.emilkowal.ski/ (Emil Kowalski)
- Vaul: https://vaul.emilkowal.ski/ (Emil Kowalski)
- Radix UI: https://www.radix-ui.com/primitives
- shadcn/ui: https://ui.shadcn.com/
- Floating UI: https://floating-ui.com/
- Framer Motion: https://www.framer.com/motion/
- Vercel Geist Design Guidelines

### Tutorials/articles
- Emil Kowalski — Building a Toast Component / Building a Drawer Component / Great Animations
- Codrops (text input effects, button styles)
- Josh Comeau — easing curves, button tactility, springs in CSS
- Adam Argyle — nerdy.dev / web.dev
- Olivier Larose — magnetic buttons, cursor patterns

### Skeleton lib alternative
- nullilac/skeleton-screen-css: https://github.com/nullilac/skeleton-screen-css (MIT, pure CSS, 107⭐)

---

## Boundary

- Reference 05-gsap-recipes.md: recipes GSAP estruturais (Lenis, ScrollTrigger, Flip, MorphSVG, SplitText). Esta ref = patterns canonical UI repetida.
- Reference 06-theoretical-foundations.md Section 4: easing semantics theoretical (curves transmitem sensações). Tabelas A/B aqui = curvas exatas pra implementação.
- Reference 12-react-adapters.md: useGSAP hook + R3F + Next.js SSR caveats. Esta ref = React adapters per-pattern (Framer Motion, Radix, Sonner, Vaul, Floating UI).
- ui-design-system Phase 4 motion-and-interaction.md: motion-as-system tokens (durations, easing curves). Esta ref consome tokens, não redefine.
- component-architect: anatomia de componentes + state contracts. Esta ref = motion specs aplicáveis aos componentes.
- ux-audit: audita se motion atrapalha tarefa observável. Esta ref = recipes pra IMPLEMENTAR motion certo desde início.
- design-system-audit: coverage motion em DS externo (raro overlap).
