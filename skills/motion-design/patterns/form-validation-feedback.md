# Pattern: Form validation feedback (consolidated)

> **Source:** DR-D Pattern 03 (shake) + 04 (checkmark) + 05 (helper) + 06 (real-time clear)
> **Categoria:** form / micro-interactions canonical UI
> **Pilar:** 1 (funcional/estrutural — extension Wave 9.1)
> **Quando usar:** forms B2B/SaaS com validation (signup, checkout, contact, settings). Critical: shake + helper text + error clear + success checkmark cobrem 80% dos cenários form feedback.
> **Quando NÃO usar:** forms 1-field simples (search), forms onde validation é só on submit sem feedback inline.

---

## Por quê consolidar 4 patterns em 1 arquivo

Os 4 patterns DR-D (shake, helper, error-clear, checkmark) compartilham ARIA + state machine + reduced-motion strategy. Em produção, raramente um sem os outros. Arquivo único = consult mais rápido durante implementação. Cada sub-pattern abaixo é independente porém coordenado.

---

## Sub-pattern A — Shake on error (submit fail)

### Spec

| Trigger | Duração | Easing | Propriedades |
|---|---|---|---|
| Submit fail / `:invalid` ativo | 400ms total | linear sequence (4 oscillations) | `transform: translateX()` |

Amplitude 8-10px, oscilações 4-6, duration total 300-500ms. Mais que isso = irritante; menos = imperceptível.

### Snippet

```html
<input id="email" type="email" required aria-describedby="email-error">
<p id="email-error" role="alert" class="error" hidden>Email inválido</p>
```

```css
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  20% { transform: translateX(-8px); }
  40% { transform: translateX(8px); }
  60% { transform: translateX(-4px); }
  80% { transform: translateX(4px); }
}
.shake { animation: shake 400ms cubic-bezier(0.36, 0.07, 0.19, 0.97); }
input.error { border-color: #ef4444; }

@media (prefers-reduced-motion: reduce) {
  .shake { animation: none; }
  input.error { box-shadow: 0 0 0 3px rgba(239,68,68,0.25); }
}
```

```js
form.addEventListener("submit", e => {
  if (!emailInput.checkValidity()) {
    e.preventDefault();
    emailInput.classList.add("error", "shake");
    document.getElementById("email-error").hidden = false;
    emailInput.addEventListener("animationend",
      () => emailInput.classList.remove("shake"), { once: true });
    emailInput.focus();
  }
});
```

### Anti-patterns shake

- **Shake em cada keystroke inválido** — agressivo, dispara vestibular. APENAS em submit attempt
- **Amplitude > 12px** — parece bug de layout, não feedback
- **Shake sem `role="alert"`** — screen reader não sabe que houve erro
- **Animação > 600ms** — bloqueia retomada da edição

---

## Sub-pattern B — Checkmark draw on success (async validation)

### Spec

| Trigger | Duração | Easing | Propriedades |
|---|---|---|---|
| Server validation success | 400-600ms | `cubic-bezier(0.65, 0, 0.45, 1)` (out-cubic) | `stroke-dashoffset` |

### Snippet

```html
<div class="field-success">
  <input type="text" id="username">
  <svg class="check" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
    <path d="M5 12 L10 17 L20 7" stroke="#10b981" stroke-width="2.5"
          fill="none" stroke-linecap="round" stroke-linejoin="round"
          pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
  </svg>
</div>
```

```css
.check { opacity: 0; transition: opacity 150ms; }
.check path {
  transition: stroke-dashoffset 500ms cubic-bezier(0.65, 0, 0.45, 1);
}
.field-success.is-valid .check { opacity: 1; }
.field-success.is-valid .check path { stroke-dashoffset: 0; }

@media (prefers-reduced-motion: reduce) {
  .check path { transition: none; stroke-dashoffset: 0; }
}
```

**`pathLength="1"`** normaliza path: dasharray/dashoffset trabalham em [0,1] sem precisar `getTotalLength()`.

### Anti-patterns checkmark

- **Animação > 800ms** — user vai pro próximo campo, perde feedback
- **Apenas o draw, sem mensagem textual** — viola WCAG 1.4.1 (use of color)
- **Sem `aria-live="polite"` em sibling pra anunciar status** — screen reader perde

---

## Sub-pattern C — Helper text fade

### Spec

| Trigger | Duração | Easing | Propriedades |
|---|---|---|---|
| `:focus`/blur | 150-200ms | ease-out (in), ease-in (out) | `opacity`, `transform: translateY(2px)` |

### Snippet

```html
<div class="field">
  <input id="pwd" type="password" aria-describedby="pwd-help">
  <label for="pwd">Senha</label>
  <p id="pwd-help" class="helper">Mínimo 8 caracteres, 1 número</p>
</div>
```

```css
.helper {
  font-size: 12px; color: #64748b; margin-top: 4px;
  opacity: 0; transform: translateY(-2px);
  transition: opacity 150ms ease-out, transform 150ms ease-out;
}
.field:focus-within .helper {
  opacity: 1; transform: translateY(0);
}
.field.has-error .helper { color: #ef4444; opacity: 1; transform: translateY(0); }

@media (prefers-reduced-motion: reduce) {
  .helper { transition: opacity 0ms; transform: none; }
}
```

### Anti-patterns helper

- **`display: none` ao esconder** — quebra `aria-describedby`. Use `opacity: 0` (mantém DOM)
- **Helper text como tooltip** — exige hover, screen reader pode perder
- **Texto de erro via `aria-describedby` sem `aria-live`** — erro precisa anúncio ativo

---

## Sub-pattern D — Real-time error clear

### Spec

| Trigger | Duração | Easing | Propriedades |
|---|---|---|---|
| `input` event quando valor passa a ser válido | 200ms | ease-out | `border-color`, `opacity` mensagem |

### Snippet

```css
.field input { border: 1px solid #cbd5e1; transition: border-color 200ms ease-out; }
.field.has-error input { border-color: #ef4444; }
.err {
  color: #ef4444; font-size: 12px;
  opacity: 0; max-height: 0; overflow: hidden;
  transition: opacity 200ms ease-out,
              max-height 200ms ease-out,
              margin-top 200ms ease-out;
  margin-top: 0;
}
.field.has-error .err { opacity: 1; max-height: 40px; margin-top: 4px; }
```

```js
input.addEventListener("input", e => {
  if (e.target.checkValidity()) {
    e.target.closest(".field").classList.remove("has-error");
  }
});
input.addEventListener("blur", e => {
  if (!e.target.checkValidity() && e.target.value) {
    e.target.closest(".field").classList.add("has-error");
  }
});
```

### Anti-patterns error-clear

- **Validar on `input` antes de blur inicial** — erro aparece antes do user terminar digitar
- **Animar `height: auto` puro CSS** — não anima. Use `max-height` workaround OR `grid-template-rows: 0fr → 1fr` (CSS moderno)
- **Manter `aria-invalid="true"` quando já válido** — confunde screen reader

---

## React adapter (Framer Motion + AnimatePresence)

```jsx
const [touched, setTouched] = useState(false);
const isInvalid = touched && !value.match(/^[^@]+@[^@]+\.[^@]+$/);

<motion.input
  animate={isInvalid ? { x: [0, -8, 8, -4, 4, 0] } : { x: 0 }}
  transition={{ duration: 0.4 }}
  value={value}
  onChange={e => setValue(e.target.value)}
  onBlur={() => setTouched(true)}
  aria-invalid={isInvalid} aria-describedby="email-err"
  className={isInvalid ? "border-red-500" : ""}/>

<AnimatePresence>
  {isInvalid && (
    <motion.p id="email-err" role="alert"
      initial={{ opacity: 0, height: 0 }}
      animate={{ opacity: 1, height: "auto" }}
      exit={{ opacity: 0, height: 0 }}
      transition={{ duration: 0.2 }}>
      Email inválido
    </motion.p>
  )}
</AnimatePresence>
```

## A11y consolidada

- `aria-invalid="true"` no input quando inválido
- `aria-describedby` aponta pra mensagem (helper OR error)
- Mensagem de erro `role="alert"` (assertive live region) — anunciada imediatamente
- Mensagem de helper sem `role="alert"` — só descrição
- Async success: `<span class="sr-only" aria-live="polite">{status}</span>` recebe "Disponível" / "Verificando…"
- Focus retorna ao primeiro campo inválido (`emailInput.focus()`)
- **NUNCA** confiar só em cor — texto + ícone + animação combinados (WCAG 1.4.1)

## Reduced motion strategy (todas sub-patterns)

| Sub-pattern | Reduced motion fallback |
|---|---|
| Shake | `animation: none` + `box-shadow` ring vermelho persistente. Mensagem `role="alert"` continua aparecendo |
| Checkmark | `transition: none` + `stroke-dashoffset: 0` (snap). Texto "Disponível" via `aria-live="polite"` |
| Helper | `transition: opacity 0ms` (toggle instantâneo, sem translate) |
| Error clear | Remove transition opacity/max-height (toggle instantâneo) |

## Performance

Todas sub-patterns compositor-only (`transform`, `opacity`, `stroke-dashoffset`). Universal browser baseline.

## Edge cases

- **Multiple campos com erro:** shake apenas o primeiro, focar nele; outros indicam com border + texto
- **Submit via Enter:** garantir `e.preventDefault()` ANTES do shake
- **Mobile keyboard pode dispensar focus:** reabrir explicitamente via `focus()`
- **Async validation (email já cadastrado):** só pode invalidar on blur OR após debounce 500ms; não a cada keystroke
- **Slow network:** spinner inline antes do checkmark, fade entre os dois
- **Re-validation:** reverter `dashoffset` para 1 antes de re-animar checkmark

## Boundary

- Reference 13 sec 2 (form validation patterns canonical)
- ux-audit (audita se feedback chega ao user em fluxo real)
- component-architect FormField anatomy (não absorver, só motion spec aqui)
- ui-design-system color tokens error (#ef4444) / success (#10b981) — não redefinir
