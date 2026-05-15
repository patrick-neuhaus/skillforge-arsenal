# Pattern: Button press compress + spring back

> **Source:** DR-D Pattern 07 (CRITICAL — gap principal site-consultoria/JRG Corp)
> **Categoria:** button / micro-interactions canonical UI
> **Pilar:** 1 (funcional/estrutural — extension Wave 9.1)
> **Quando usar:** TODO botão clicável funcional. Frequência altíssima por sessão. Diferença A vs B+: A tem compress real (`scale(0.97)`) + spring back; B só tem `translateY(-2px)` no hover.
> **Quando NÃO usar:** ícone-only buttons sem hit target dedicado (use osmo-button-pack Variant 1 lift + shadow).

---

## ⚠️ Anti-pattern literal site-consultoria/JRG Corp

```css
/* ❌ ANTI-PATTERN — apenas hover, ZERO press feedback */
.btn:hover { transform: translateY(-2px); }
.btn:active { transform: translateY(0); }
```

**Por quê falha:**
- Zero confirmação tátil ao clicar (só hover decorativo)
- Em touch device, hover não dispara → user não tem feedback algum
- Site sente "plástico" — frequência altíssima amplifica fricção
- DR-D Pattern 07 explicit: "Apenas `translateY(-2px)` no hover sem feedback de press" = anti-pattern #1

## ✅ Snippet canonical

```html
<button class="btn">Salvar</button>
```

```css
.btn {
  background: #3b82f6; color: white;
  padding: 10px 20px; border: none; border-radius: 8px;
  font-size: 14px; font-weight: 500; cursor: pointer;
  transition: transform 200ms cubic-bezier(0.34, 1.56, 0.64, 1),
              background-color 150ms ease-out;
  will-change: transform;
}
.btn:hover { background: #2563eb; }
.btn:active {
  transform: scale(0.97);
  transition-duration: 100ms;
}
.btn:focus-visible {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn { transition: background-color 150ms; }
  .btn:active { transform: none; }
}
```

**Curva `cubic-bezier(0.34, 1.56, 0.64, 1)`** = "easeOutBack" — overshoot leve no release (CTA lúdico). Pra critically-damped (sem overshoot, botão funcional sério): use `cubic-bezier(0.2, 0, 0, 1)` (Material standard).

## Spec técnico

| Trigger | Duração | Easing | Propriedades |
|---|---|---|---|
| `:active` press | 100ms (in) | ease-out | `transform: scale(0.97)` |
| Release | 200-250ms | spring overdamped (`cubic-bezier(0.34, 1.56, 0.64, 1)` ou critically-damped) | `transform: scale(1)` |

**Emil Kowalski guideline:** scale 0.95-0.98 é range tátil. Abaixo 0.95 vira cartoon. Critically-damped (sem overshoot) pra botões funcionais; underdamped (overshoot 1.02 → 1) pra CTAs lúdicos.

## React adapter (Framer Motion springs)

Springs autênticos com física — preservam velocidade se interrompidos:

```jsx
import { motion } from "framer-motion";

<motion.button
  whileTap={{ scale: 0.97 }}
  transition={{ type: "spring", stiffness: 400, damping: 17 }}
  className="bg-blue-500 text-white px-5 py-2.5 rounded-lg">
  Salvar
</motion.button>
```

User tira o dedo mid-press → animação continua naturalmente sem reset. Diferença vs CSS: CSS transitions não preservam velocity.

## React adapter (vanilla CSS — preferido pra forms B2B)

CSS-only é suficiente em 95% dos casos. Use React/Framer apenas se:
- Botão é toggle complexo com múltiplos estados (loading + success + error em sequência)
- Spring physics é parte da identidade brand
- Composição com outras animações (hover card open, scroll trigger)

## Reduced motion

- Apenas `background-color` change no hover
- Sem `scale` no active
- Feedback funcional preservado (cor muda = user sabe que clicou)

## A11y crítico

- **`<button>` semântico** — NUNCA `<div onclick>` (não focusable, não keyboard-accessible)
- `:focus-visible` outline preservado, **NUNCA** animar o anel
- `aria-pressed` se botão é toggle (mute/unmute, like/unlike)
- Tap target ≥ 44×44px (Apple HIG, WCAG 2.5.5) — padding faz o trabalho mesmo se ícone é 16px
- Keyboard activation (Enter/Space) — `<button>` resolve nativo

## Anti-patterns

1. **Apenas `translateY(-2px)` no hover sem feedback de press** — ZERO confirmação de clique. **Anti-pattern #1 site-consultoria/JRG Corp.**
2. **`scale(0.85)` ou abaixo** — cartoon, não tátil
3. **`transition: all`** — anima props imprevisíveis (background-image, etc), causa jank
4. **Sem reduced-motion fallback** — vestibular trigger
5. **Animar `box-shadow` no press** — paint cost > value (compositor-only é law)
6. **Springs com damping < 10** — botão ricocheteia, parece bug

## Edge cases

- **Touch devices:** `:active` dispara mas hover persiste após tap (sticky hover) — use `@media (hover: hover)` pra hover state
- **Disabled state:** remover `transform` + `cursor`; cor 38% opacity (Material). `pointer-events: none` + `aria-disabled="true"`
- **Loading state:** ver `patterns/button-loading-async.md` (pattern dedicado)
- **Long press / double click:** spring acumula velocity → pode parecer ricochete. Cap via `duration` máximo OR cancelar via JS

## Performance

- `transform: scale()` = compositor-only, GPU-friendly
- `will-change: transform` apenas em botões com motion frequente (não em todos)
- 60fps universal mesmo em mobile médio

## Browser baseline

- CSS transitions/transforms: universal
- `cubic-bezier()` overshoot (valores > 1): universal moderno
- Framer Motion springs: requer React + `framer-motion` lib (~30KB gzipped)

## Boundary

- Reference 13 sec 3 (button patterns canonical)
- Reference 06-theoretical-foundations sec 4 (easing semantics — overshoot vs critically-damped semantics)
- patterns/osmo-button-pack.md Variant 6 (legacy press, **superseded por este pattern** — Variant 6 não tinha cubic-bezier overshoot canonical)
- patterns/button-loading-async.md (loading state)
- ui-design-system Phase 4 motion tokens (durations 100ms = "fast")
- component-architect Button anatomy (não absorver — só motion spec aqui)
