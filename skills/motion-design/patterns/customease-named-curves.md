# Pattern: CustomEase nomeada (osmo-ease canonical + brand variants)

> **Source:** DR-C Osmo Supply (osmo-ease canonical) + DR-0 GSAP docs
> **Categoria:** easing semantics / brand identity
> **Pilar:** transversal (todos pilares)
> **Quando usar:** quando tom motion = "cinematic premium" / award-grade / brand-specific. CustomEase nomeada vira token reusável.
> **Quando NÃO usar:** SaaS operacional simples (ease-out CSS basta). Microinteractions repetitivas (overhead injustificado).

---

## Snippet canonical (define 1x boot)

```js
import { gsap } from 'gsap';
import { CustomEase } from 'gsap/CustomEase';

gsap.registerPlugin(CustomEase);

// Curves nomeadas globais (define 1x app boot)
CustomEase.create('osmo-ease', '0.625, 0.05, 0, 1');
CustomEase.create('cinematicSilk', 'M0,0 C0.215,0.61 0.355,1 1,1');
CustomEase.create('hop', 'M0,0 C0.05,0.7 0.1,1 0.5,1 0.6,1 0.65,0.95 0.7,0.85 0.8,0.6 1,0.5 1,1');

// Brand-specific exemplo
CustomEase.create('brand-luxe', '0.7, 0, 0.3, 1');
CustomEase.create('brand-snap', '0.85, 0, 0.15, 1');
```

## Uso

```js
gsap.to('.hero-title', {
  y: 0,
  opacity: 1,
  duration: 1.2,
  ease: 'osmo-ease', // referencia nome, não inline curve
});
```

## Curves canonical e suas sensações

### `osmo-ease (0.625, 0.05, 0, 1)`
- **Sensação:** orgânico não-mecânico, premium
- **Uso:** hero reveal, page transitions premium, brand-aligned motion
- **Vs default:** mais subtle que `power3.out` mas perceptível em side-by-side

### `cinematicSilk` (Bezier custom)
- **Sensação:** chegada cinematográfica, "telhado swung"
- **Uso:** landing premium B2C luxo, brand site institutional
- **Quando preferir:** quando osmo-ease parece "default Awwwards" e quer diferencial

### `hop` (Bezier multi-control)
- **Sensação:** bounce orgânico custom, ludicidade controlada
- **Uso:** creator brand, character-driven brand, lúdico criativo
- **Quando preferir:** brand precisa personality vs corporate clássico

### Brand variants (custom)
- **Padrão:** `brand-{descritor}` (ex: brand-luxe, brand-snap)
- **Calibração:** Patrick adapta CustomEase pra match brand identity cliente

## Por quê funciona

- **Token reusável:** define 1x, referencia por nome universal — consistência cross-app.
- **Brand identity:** CustomEase nomeada = "voice motion" do brand. Diferenciação vs SaaS genérico.
- **Cache performance:** curve calculada 1x, GSAP reusa internally.

## Embasamento teórico

> "CustomEase osmo-ease (0.625, 0.05, 0, 1) porque tom session narrative = cinematic premium. Curve orgânica não-mecânica match expectativa Awwwards-tier; power3.out seria genérico SaaS."

## Reduced motion

```js
ease: prefersReducedMotion ? 'none' : 'osmo-ease',
duration: prefersReducedMotion ? 0 : 1.2,
```

CustomEase + reduced motion = snap-to-end (duration 0 + ease none).

## Anti-pattern

- **CustomEase inline em cada call:** define 1x global, referencia por nome. Repetir inline = inconsistência + cache miss.
- **Default ease (sem especificar):** GSAP usa `power1.out` genérico — perde diferencial.
- **CustomEase complexo em microinteraction press:** overhead injustificado. `power2.out` simples basta pra 80ms feedback.
- **Múltiplas CustomEase aleatórias:** vira "salada de curves". Manter ≤ 5 nomeadas por app.

## Performance

- CustomEase plugin = ~5KB gzipped
- Curve compilada 1x no `create()`, depois reuso O(1)
- Animação rodando = idêntica perf a built-in eases

## Browser baseline

Universal (CustomEase é JS-only, não API browser).

## A11y

CustomEase não afeta a11y diretamente. Reduced motion gate sempre presente.

## Brand identity ritual

Ao iniciar projeto novo:

1. Define 1-3 CustomEase nomeadas matching brand
2. Documenta no design system (vira token)
3. Aplica universalmente: hero, transitions, microinteractions premium
4. Cliente vai "sentir" identidade motion mesmo sem saber GSAP

## React adapter

```tsx
// app/lib/customeases.ts
import { gsap } from 'gsap';
import { CustomEase } from 'gsap/CustomEase';

if (typeof window !== 'undefined') {
  gsap.registerPlugin(CustomEase);
  CustomEase.create('osmo-ease', '0.625, 0.05, 0, 1');
  // ... mais curves
}
```

Importar 1x em layout root.

## Boundary

- Recipe completa em `references/05-gsap-recipes.md` Recipe 2
- Foundations easing em `references/06-theoretical-foundations.md` sec 4
