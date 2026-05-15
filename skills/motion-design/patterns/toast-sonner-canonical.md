# Pattern: Toast notification (Sonner-style canonical)

> **Source:** DR-D Pattern 11. Emil Kowalski post "Building a Toast Component" documenta decisões.
> **Categoria:** feedback efêmero / micro-interactions canonical UI
> **Pilar:** 1 (funcional/estrutural — extension Wave 9.1)
> **Quando usar:** feedback efêmero non-blocking pós-action (save success, copy clipboard, error message). Frequência altíssima em apps. Sonner é canonical (sonner.emilkowal.ski).
> **Quando NÃO usar:** confirmação destructive (use Dialog), feedback que precisa decisão user (use Dialog), info crítica que user PRECISA ler (toasts auto-dismiss).

---

## Recomendação canonical: USE Sonner direto

Reimplementar drag-with-velocity-and-momentum + stack management corretamente excede 200 LoC. Sonner está battle-tested, MIT, ~5KB gzipped. shadcn/ui adopta direto.

```bash
npm install sonner
```

```jsx
import { Toaster, toast } from "sonner";

// Mount 1x no root layout
<Toaster position="bottom-right" expand={false} richColors closeButton />

// Use em qualquer lugar
toast.success("Salvo!", { duration: 4000 });
toast.error("Falha ao salvar", { description: "Tente novamente" });
toast.promise(save(), {
  loading: "Salvando…",
  success: "Salvo!",
  error: (err) => `Falha: ${err.message}`
});
```

## Spec técnico (referência caso DIY)

| Trigger | Duração | Easing | Propriedades |
|---|---|---|---|
| Mount | 400ms | ease-out | `transform: translateY(0)`, `opacity: 1` |
| Dismiss | 300ms | ease-in | reverse |
| Stack offset | 300ms (interruptível) | ease-out | `translateY` + `scale(0.95-0.9)` per back-toast |
| Auto-close | default 4000ms | timer pause on hover/focus | — |
| Swipe dismiss | velocity-based | momentum | `translateY` follows pointer |

## Por quê CSS transitions > keyframes (lesson Sonner)

Sonner abandonou keyframes porque **interruptíveis**:
- Novo toast entrando → antigos retargetam smooth pra nova posição
- Keyframes resetam para zero quando interrompidos = pular visual
- CSS transitions: `transform: var(--y-offset)` muda dinamicamente, browser interpola suave

## Snippet conceitual DIY (caso lib não cabe)

```css
.toast {
  position: fixed; bottom: 16px; right: 16px;
  background: white; padding: 16px; border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  transition: transform 400ms cubic-bezier(0.22, 1, 0.36, 1),
              opacity 400ms ease-out;
  --y-offset: 0px;
  --scale: 1;
  transform: translateY(var(--y-offset)) scale(var(--scale));
}
.toast[data-front="false"] { --scale: 0.94; }
.toast[data-mounted="false"] {
  transform: translateY(100%);
  opacity: 0;
}
.toast[data-removed="true"] {
  transform: translateY(100%) scale(0.9);
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .toast {
    transition: opacity 200ms;
    transform: none !important;
  }
}
```

JS calcula `--y-offset` por toast index dinamicamente. Stack mode: front toast altura real, back toasts forçados pra altura do front.

## Reduced motion

Sonner respeita automaticamente: substitui slide por opacity-only fade. Você pode override:

```css
@media (prefers-reduced-motion: reduce) {
  [data-sonner-toast] {
    transition: opacity 200ms;
    transform: none !important;
  }
}
```

## A11y

- `role="status"` (default polite, success/info)
- `role="alert"` (assertive, errors crítical)
- `aria-live` automático
- Pause on hover/focus dá tempo de leitura
- Close button com `aria-label="Dismiss notification"`
- Swipe dismiss não substitui keyboard close

**NÃO** colocar interactive elements críticos só em toast (não persiste). Ações tipo "Undo" devem aceitar keyboard via Tab antes do auto-close.

## Anti-patterns

1. **Auto-close < 3s** — user não consegue ler
2. **Toast com vários botões e form** — deve ser Dialog/Drawer
3. **Não pausar timer on hover** — dismissa enquanto user interage
4. **Stack ilimitada** — poluição visual; default 3 visíveis (Sonner `visibleToasts` prop)
5. **Toast pra info crítica única** — touch e screen reader podem perder
6. **Position centro do viewport** — bloqueia conteúdo. Use bottom-right (desktop) / top (mobile)
7. **Custom toast sem `aria-live`** — screen reader não anuncia

## Edge cases

- **Toast com long content:** max-height + scroll interno
- **Mobile:** position top é melhor (polegar não cobre)
- **Multiple categories simultâneo:** agrupar por type, não empilhar 10
- **Promise toast com loading > 5s:** considere progress bar dedicado em Dialog
- **Network offline:** toast persistente com retry button (não auto-close)

## Performance

Sonner ~5KB gzipped. CSS transitions = compositor-only. Stack management via React state.

## Browser baseline

- Sonner requires React 18+ (uses `useSyncExternalStore`)
- DIY snippet: universal CSS

## Combinações canônicas

| Combo | Pattern |
|---|---|
| `toast.promise(save())` | Pattern definitivo pra async submit feedback |
| Loading button + toast success | Combinação form B2B canonical |
| Form submit error + shake + toast error | Triple feedback (visual button + shake field + toast) |
| Optimistic UI + toast undo | Update imediato + toast com Undo action |

## Boundary

- Reference 13 sec 4 (feedback patterns canonical)
- patterns/button-loading-async.md (combina com toast success/error pós-submit)
- patterns/form-validation-feedback.md (toast pra erros server, shake pra erros client)
- ux-audit (audita se feedback chega ao user em fluxo real)
- component-architect (Toaster anatomy — não absorver, só motion + behavior)
