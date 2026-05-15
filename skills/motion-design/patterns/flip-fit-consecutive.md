# Pattern: Flip.fit() consecutive scrub waypoints

> **Source:** DR-A Awwwards showcase + DR-B
> **Categoria:** narrative / scroll-driven layout
> **Pilar:** 3 (narrativo/editorial)
> **Quando usar:** elemento "viaja" entre 3+ posições conforme scroll progress (each waypoint = layout state diferente).
> **Quando NÃO usar:** transição simples 2 estados (FLIP normal basta), lista 500+ items, mobile baixo (custo paint elevado).

---

## Snippet canonical

```js
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { Flip } from 'gsap/Flip';

gsap.registerPlugin(ScrollTrigger, Flip);

const card = document.querySelector('.product-card');
const waypoint1 = document.querySelector('#waypoint-1');
const waypoint2 = document.querySelector('#waypoint-2');
const waypoint3 = document.querySelector('#waypoint-3');

// Reduced motion gate
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReduced) {
  // Posiciona card no waypoint final, sem scroll-driven
  waypoint3.appendChild(card);
} else {
  // Cria timeline scrubbed pelo scroll
  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: '.product-section',
      start: 'top top',
      end: 'bottom bottom',
      scrub: 1, // 1s smoothing
    },
  });

  // Waypoint 1
  tl.add(() => {
    const state1 = Flip.getState(card);
    waypoint1.appendChild(card);
    Flip.fit(card, state1, { duration: 0, scale: true, rotation: true });
  });

  // Waypoint 2 (consecutive)
  tl.add(() => {
    const state2 = Flip.getState(card);
    waypoint2.appendChild(card);
    Flip.fit(card, state2, { duration: 0, scale: true });
  });

  // Waypoint 3
  tl.add(() => {
    const state3 = Flip.getState(card);
    waypoint3.appendChild(card);
    Flip.fit(card, state3, { duration: 0, scale: true });
  });
}
```

## Por quê funciona

- **Continuity gestalt:** olho do user segue trajetória contínua mesmo entre containers diferentes (waypoints).
- **Scrub 1:** smoothing 1s previne jitter em scroll fast.
- **`Flip.fit` consecutive:** mantém continuidade espacial sem cortes visuais.
- **`scale: true, rotation: true`:** captura transformações além de position.

## Embasamento teórico

> "Flip.fit consecutive scrub waypoints porque continuity gestalt — olho do user segue trajetória contínua mesmo trocando containers. Sem Flip.fit, card 'salta' entre waypoints = quebra rastreabilidade visual."

## Reduced motion

Skip ScrollTrigger inteiro. Posiciona card direto no waypoint final.

## Anti-pattern

- **Sem scrub smoothing:** scroll fast causa jitter visual.
- **Waypoints muito próximos:** user não percebe trajetória — vira "card desaparece e reaparece".
- **Mais que 5 waypoints:** fadiga + perf cost.
- **Mobile baixo sem fallback:** Flip recalcula DOM em cada waypoint = lentidão.
- **Sem `Flip.getState` antes da mudança:** Flip.fit não tem origin reference = bug.

## Performance

- Cada Flip.fit = recalc DOM measurements + layout shift
- Cap em 5 waypoints máximo
- Considera `absolute: true` em Flip pra remover do fluxo durante anim

## Browser baseline

Chrome 76+, Safari 14+, Firefox 70+. Flip plugin paid (GSAP Bonus / GSAP Premium).

## A11y

- Card permanece DOM-accessible em todos waypoints
- Keyboard navigation deve continuar funcionando
- Reduced motion = card final state direto (sem scroll dependency)

## Casos de uso award-grade

- **Product reveal:** card de produto "viaja" através de specs (waypoint 1 = specs lado A, waypoint 2 = lado B, waypoint 3 = preço)
- **Storytelling brand:** logo "aparece" em 3 contextos diferentes ao longo página
- **Process explainer:** ícone do processo move por 5 etapas sticky

## React adapter

```tsx
import { useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { Flip } from 'gsap/Flip';

gsap.registerPlugin(ScrollTrigger, Flip);

function FlipFitSection() {
  const sectionRef = useRef(null);

  useGSAP(() => {
    const card = sectionRef.current.querySelector('.card');
    const waypoints = sectionRef.current.querySelectorAll('.waypoint');

    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: sectionRef.current,
        start: 'top top',
        end: 'bottom bottom',
        scrub: 1,
      },
    });

    waypoints.forEach((wp) => {
      tl.add(() => {
        const state = Flip.getState(card);
        wp.appendChild(card);
        Flip.fit(card, state, { duration: 0, scale: true });
      });
    });
  }, { scope: sectionRef });

  return (
    <section ref={sectionRef}>
      <div className="card">Travel me</div>
      <div className="waypoint" id="wp-1">Position 1</div>
      <div className="waypoint" id="wp-2">Position 2</div>
      <div className="waypoint" id="wp-3">Position 3</div>
    </section>
  );
}
```

## Boundary

- Recipe completa em `references/05-gsap-recipes.md` Recipe 4
- Foundations gestalt continuity em `references/06-theoretical-foundations.md` sec 1.1
