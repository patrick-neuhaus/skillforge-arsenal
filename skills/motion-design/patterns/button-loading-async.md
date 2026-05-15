# Pattern: Button loading state (async submit)

> **Source:** DR-D Pattern 10
> **Categoria:** button / micro-interactions canonical UI
> **Pilar:** 1 (funcional/estrutural — extension Wave 9.1)
> **Quando usar:** TODO submit assíncrono em forms B2B/SaaS. Frequência altíssima em apps. Critical: previne double-submit, indica progresso, mantém width (sem layout shift).
> **Quando NÃO usar:** botão sync (não disparing async — não precisa loading state).

---

## Por quê (anti-double-submit)

Sem loading state:
- Double-submit garantido (user clica 2x impaciente)
- Zero feedback de progresso (user não sabe se travou)
- Layout shift se texto vira "Loading…" sem width preserve
- Site-consultoria/JRG Corp gap: submit btn sem `aria-busy`/`disabled`/spinner

## Snippet canonical

```html
<button class="btn-async" data-loading="false">
  <span class="label">Save changes</span>
  <span class="spinner" aria-hidden="true"></span>
</button>
```

```css
.btn-async {
  position: relative;
  min-width: 120px; /* Width preserve — chave anti-layout-shift */
  padding: 10px 20px;
  background: #3b82f6; color: white;
  border: none; border-radius: 8px;
}

.btn-async .label {
  transition: opacity 150ms ease-out;
}

.btn-async .spinner {
  position: absolute; inset: 0; margin: auto;
  width: 16px; height: 16px;
  border: 2px solid rgba(255,255,255,0.3);
  border-top-color: white;
  border-radius: 50%;
  opacity: 0;
  animation: spin 600ms linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.btn-async[data-loading="true"] .label { opacity: 0; }
.btn-async[data-loading="true"] .spinner { opacity: 1; }
.btn-async[data-loading="true"] { pointer-events: none; }

@media (prefers-reduced-motion: reduce) {
  .btn-async .spinner {
    animation: spin 1.5s linear infinite;
    /* Spin lento ainda dá feedback funcional — NÃO eliminar */
  }
}
```

```js
btn.addEventListener("click", async () => {
  btn.dataset.loading = "true";
  btn.setAttribute("aria-busy", "true");
  btn.disabled = true;
  try {
    await save();
    // Optional: toast success
  } catch (err) {
    // Optional: shake + toast error
  } finally {
    btn.dataset.loading = "false";
    btn.setAttribute("aria-busy", "false");
    btn.disabled = false;
  }
});
```

## Spec técnico

| Trigger | Duração | Easing | Propriedades |
|---|---|---|---|
| `loading=true` | 150ms label fade | ease-out | `opacity` |
| Spinner | 600ms loop linear infinite | linear | `transform: rotate()` |

**Width preserve strategy:**
1. `min-width: 120px` (calculado pra label real)
2. OR medir `offsetWidth` antes de trocar conteúdo + lock via inline style
3. OR manter label invisível com `opacity: 0` (preserva width nativo) — **canonical**

## React adapter

```jsx
import { useState } from "react";

function SaveButton({ onSave }) {
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    try { await onSave(); }
    finally { setLoading(false); }
  };

  return (
    <button
      onClick={handleClick}
      disabled={loading}
      aria-busy={loading}
      className="relative min-w-[120px] px-5 py-2.5 bg-blue-500 text-white rounded-lg">
      <span className={loading ? "opacity-0" : "opacity-100"}>Save</span>
      {loading && <Spinner className="absolute inset-0 m-auto"/>}
    </button>
  );
}
```

## Reduced motion

- Spin lento (1.5-2s) ou substituir por dots pulsing
- **NÃO eliminar spinner** — é feedback funcional essencial
- Label fade em 0ms (toggle instantâneo)

## A11y crítico

- `aria-busy="true"` durante load — screen reader anuncia "busy"
- `disabled` previne click + hint visual (browser default cursor)
- `aria-live="polite"` em sibling pra anunciar "Saving…" / "Saved" — opcional mas premium
- Spinner com `aria-hidden="true"` — decorativo, não anuncia
- Considere `<span class="sr-only">Loading</span>` dentro do button quando loading

## Anti-patterns

1. **Texto vira "Loading…" sem width preserve** — layout shift, viola CLS Web Vital
2. **Spinner sozinho sem `aria-busy`** — screen reader não sabe que está esperando
3. **Disabled sem feedback visual de progresso** — user não sabe se travou OU se app crashou
4. **Permitir double-submit (não disabled)** — bug de transação, garbage in DB
5. **Spinner > 2s sem texto auxiliar** — user assume travado. Após 3s, mostrar "Ainda processando…"
6. **Animação loop sem `linear`** — spinner ease-in/out parece tropeçar

## Edge cases

- **Erro mid-load:** voltar ao estado normal + shake (link `patterns/form-validation-feedback.md` Sub-pattern A)
- **Long-running > 3s:** mostrar texto auxiliar "Ainda processando…" OR progress bar se possível
- **Optimistic UI:** state success ANTES do server resp; reverter se falhar
- **Mid-load route change:** cancel via `AbortController` + reset button
- **Multi-button form:** desabilitar TODOS botões durante save (não só o submit)

## Performance

- `transform: rotate()` no spinner = compositor-only, GPU-friendly
- `opacity` toggle = compositor-only
- Universal browser baseline

## Combinações canônicas

| Combo | Quando |
|---|---|
| Loading + Toast success | Form submit padrão (signup, settings, contact) |
| Loading + Shake on error | Validation server falhou (CVC inválido, email duplicate) |
| Loading + Optimistic UI | Like/follow/star — UI imediato, reverter se falha |
| Loading + Skeleton in next route | Save + navigate (checkout → confirmation page) |

## Boundary

- Reference 13 sec 3 (button patterns canonical)
- patterns/button-press-compress.md (press feedback combina com loading)
- patterns/toast-sonner-canonical.md (feedback pós-submit)
- patterns/form-validation-feedback.md Sub-pattern A (shake on server error)
- ui-design-system Phase 4 motion tokens (spinner duration 600ms = "decorative" token)
- component-architect Button anatomy + state contract (loading state declarado lá; motion spec aqui)
