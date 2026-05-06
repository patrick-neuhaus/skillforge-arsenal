# Pattern: Tooltip position-aware (Radix/Floating UI canonical)

> **Source:** DR-D Pattern 18
> **Categoria:** overlay / micro-interactions canonical UI
> **Pilar:** 1 (funcional/estrutural — extension Wave 9.1)
> **Quando usar:** hint hover/focus em ícone-only buttons, abreviações, info auxiliar. Frequência altíssima em dashboards. Critical: edge detection (não vazar viewport), delay calibrado.
> **Quando NÃO usar:** info crítica única (touch + screen reader perdem), interactive elements internos (use HoverCard ou Popover), explicação extensa (> 1 frase = use Popover).

---

## Recomendação canonical: USE Radix Tooltip OR Floating UI

Reimplementar edge detection (flip top↔bottom, shift mantém in-viewport) corretamente é não-trivial. Radix + Floating UI battle-tested.

```bash
npm install @radix-ui/react-tooltip
# OU vanilla:
npm install @floating-ui/dom
```

## Snippet canonical (Radix React)

```jsx
import * as Tooltip from "@radix-ui/react-tooltip";

<Tooltip.Provider delayDuration={700} skipDelayDuration={300}>
  <Tooltip.Root>
    <Tooltip.Trigger asChild>
      <button aria-label="Settings"><GearIcon/></button>
    </Tooltip.Trigger>
    <Tooltip.Portal>
      <Tooltip.Content
        className="tooltip"
        sideOffset={6}
        collisionPadding={8}>
        Settings
        <Tooltip.Arrow/>
      </Tooltip.Content>
    </Tooltip.Portal>
  </Tooltip.Root>
</Tooltip.Provider>
```

```css
.tooltip {
  background: #18181b;
  color: white;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 12px;
  animation: tooltip-in 150ms ease-out;
}

@keyframes tooltip-in {
  from { opacity: 0; transform: translateY(4px); }
  to   { opacity: 1; transform: translateY(0); }
}

.tooltip[data-state="closed"] {
  animation: tooltip-out 100ms ease-in;
}

@keyframes tooltip-out {
  to { opacity: 0; transform: translateY(4px); }
}

@media (prefers-reduced-motion: reduce) {
  .tooltip {
    animation: tooltip-fade 100ms ease-out;
  }
  @keyframes tooltip-fade {
    from { opacity: 0 }
  }
}
```

**Direção translate ajusta com `data-side`:**
- top → `translateY(-4px)` initial
- bottom → `translateY(4px)` initial

## Spec técnico

| Aspect | Value |
|---|---|
| Open delay | 700ms (Radix default; React Aria "warmup") |
| Subsequent open delay | 0ms (cooldown < 1500ms via `skipDelayDuration={300}`) |
| Close delay | 100-300ms |
| Animation | 120-180ms fade + translate 4px ease-out |
| Easing | ease-out (in), ease-in (out) |
| Edge detection | flip (top↔bottom), shift (mantém in-viewport) |

**WAI-ARIA APG:** "small delay 1-5s". 700ms é sweet spot Radix/React Aria.

## Vanilla snippet (Floating UI)

```js
import { computePosition, flip, shift, offset } from "@floating-ui/dom";

let showTimer;

trigger.addEventListener("mouseenter", () => {
  showTimer = setTimeout(async () => {
    tooltip.dataset.show = "true";
    const { x, y } = await computePosition(trigger, tooltip, {
      placement: "top",
      middleware: [
        offset(6),
        flip(),
        shift({ padding: 8 })
      ]
    });
    tooltip.style.transform = `translate(${x}px, ${y}px)`;
  }, 700);
});

trigger.addEventListener("mouseleave", () => {
  clearTimeout(showTimer);
  setTimeout(() => tooltip.dataset.show = "false", 100);
});

trigger.addEventListener("focus", () => {
  // Same logic — tooltip aparece on focus, NÃO só hover
});
```

## Reduced motion

Fade-only sem translate. Delay timing preservado (preventiveness > motion).

## A11y crítico

- `role="tooltip"` (Radix faz auto)
- Trigger tem `aria-describedby={tooltipId}` (Radix faz auto)
- **NUNCA** colocar interactive elements no tooltip (use HoverCard ou Popover)
- Esc fecha (Radix faz)
- Aparece on focus, **não só hover** (keyboard users dependem disso)
- Touch devices: tooltip não dispara — info crítica precisa fallback (visible text)
- **Tooltip NUNCA é o accessible name** — use `aria-label` no trigger

## Anti-patterns

1. **Open delay 0ms** — flash em pass-through, distrai
2. **Tooltip com link/button interno** — viola APG (não focusable inside tooltip)
3. **`title` attr como tooltip styled** — keyboard inacessível
4. **Tooltip com info crítica única** — touch e screen reader perdem
5. **Sem `flip()` em viewport edge** — vaza fora da tela, conteúdo cortado
6. **Trigger sem `aria-label`** — screen reader não tem nome (tooltip não substitui)
7. **Tooltip permanente sem close button** — bloqueia interação se posicionado mal

## Edge cases

- **Long content:** max-width 240-300px, wrap — mas considere virar Popover
- **Multiple tooltips simultâneos:** limitar a 1 ativo (Provider gerencia)
- **RTL:** Radix `side="start"`/`"end"` é logical (não left/right)
- **Inside scrollable container:** `autoUpdate` (Floating UI) reposiciona on scroll
- **Modal scroll-lock:** tooltip dentro de Dialog precisa Portal correto
- **Touch devices:** Radix Tooltip não dispara — considere fallback visible info OR Popover tap-to-show

## Performance

- Open delay 700ms = baixíssimo overhead (timeout simples)
- `computePosition` Floating UI: ~1ms
- CSS animation = compositor-only

## Browser baseline

- Radix Tooltip: React 18+, universal browsers
- Floating UI: universal modern (ES modules)
- CSS animation: universal

## Diferença Tooltip vs HoverCard vs Popover

| Component | Conteúdo | Trigger | Quando |
|---|---|---|---|
| **Tooltip** | Texto curto descritivo | Hover/focus | Hint, label, abbreviation |
| **HoverCard** | Conteúdo rich (avatar, bio, button) | Hover/focus | Profile preview, link preview |
| **Popover** | Conteúdo interativo, form | Click/tap | Settings, share menu, color picker |

## Boundary

- Reference 13 sec 5 (overlay patterns canonical)
- patterns/button-press-compress.md (botão trigger do tooltip)
- ui-design-system Phase 4 motion tokens (durations 150ms = "fast")
- component-architect Tooltip anatomy (não absorver, só motion + behavior)
- React Aria Tooltip (alternativa headless: react-spectrum.adobe.com/react-aria/Tooltip.html)
