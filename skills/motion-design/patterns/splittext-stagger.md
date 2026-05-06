# Pattern: SplitText word/char stagger timeline

> **Source:** DR-B + DR-0
> **Categoria:** kinetic typography
> **Pilar:** 2 (vetorial/branding) + 3 (narrativo/editorial)
> **Quando usar:** kinetic headline em hero/manifesto/launch page. Reveal por palavra/caractere.
> **Quando NÃO usar:** corpo de texto, parágrafos, body copy (atrapalha leitura WCAG 2.2.2).

---

## Snippet canonical — split por palavra (preferido)

```js
import { gsap } from 'gsap';
import { SplitText } from 'gsap/SplitText';

gsap.registerPlugin(SplitText);

const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const headline = document.querySelector('.hero-title');

if (prefersReduced) {
  // Snap final state — sem motion
} else {
  // Aguarda fonts loaded (mede texto correto)
  document.fonts.ready.then(() => {
    const split = new SplitText(headline, {
      type: 'words',
      wordsClass: 'split-word',
    });

    gsap.from(split.words, {
      y: 40,
      opacity: 0,
      duration: 0.8,
      stagger: 0.04, // 40ms entre palavras
      ease: 'osmo-ease',
      delay: 0.3,
      onComplete: () => {
        // Cleanup importante: revert preserva texto pra a11y/SEO
        // Em React useGSAP faz automático, vanilla precisa manual em unmount
      },
    });
  });
}
```

## Snippet — split por caractere

```js
const split = new SplitText(headline, {
  type: 'chars,words',
  charsClass: 'split-char',
  wordsClass: 'split-word',
});

gsap.from(split.chars, {
  y: 20,
  opacity: 0,
  duration: 0.6,
  stagger: 0.02, // 20ms entre chars (rápido pra não virar lentidão)
  ease: 'power3.out',
});
```

## Snippet — split por linha

```js
const split = new SplitText(headline, {
  type: 'lines',
  linesClass: 'split-line',
});

gsap.from(split.lines, {
  y: 60,
  opacity: 0,
  duration: 1,
  stagger: 0.1, // 100ms entre linhas (mais espaçado)
  ease: 'osmo-ease',
});
```

## Cleanup obrigatório (React)

```tsx
import { useGSAP } from '@gsap/react';
import { useRef } from 'react';
import { gsap } from 'gsap';
import { SplitText } from 'gsap/SplitText';

function KineticHeadline() {
  const ref = useRef(null);
  const splitRef = useRef(null);

  useGSAP(() => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    document.fonts.ready.then(() => {
      splitRef.current = new SplitText('.headline', { type: 'words' });
      gsap.from(splitRef.current.words, {
        y: 40,
        opacity: 0,
        stagger: 0.04,
        duration: 0.8,
      });
    });

    return () => {
      splitRef.current?.revert(); // CRÍTICO: revert preserva texto pra a11y/SEO
    };
  }, { scope: ref });

  return <h1 ref={ref} className="headline">Welcome to the future</h1>;
}
```

## Stagger calibration

| Stagger | Sensação | Quando usar |
|---|---|---|
| 0.02 (20ms) | Quase sincronizado | Char-level reveal rápido |
| 0.04 (40ms) | Ritmo natural leitura | Word-level reveal default |
| 0.06 (60ms) | Lento controlado | Hero premium cinematic |
| 0.08 (80ms) | LIMITE — começa parecer "fila" | Manifesto deliberadamente lento |
| > 0.1 (100ms+) | "Uma palavra de cada vez" | Apenas line-level (3-5 linhas) |

## Por quê funciona

- **Continuity gestalt:** stagger 40ms cria trajetória horizontal de leitura — olho segue palavra-em-palavra.
- **Anti-pattern stagger > 80ms:** vira "fila lenta", quebra fluxo.
- **Anti-pattern stagger < 20ms:** sincronizado, perde efeito staggered.

## Embasamento teórico

> "SplitText word stagger 40ms porque continuity gestalt mantém olho do user em trajetória horizontal de leitura — stagger > 80ms vira fila lenta; < 20ms perde efeito."

## Reduced motion

Skip animation. Texto aparece direto no estado final. SplitText `revert()` preserva HTML original pra screen readers.

## Anti-pattern

- **SplitText sem cleanup `revert()`:** quebra a11y/SEO em unmount — texto fica fragmentado em spans sem revert.
- **Body copy em SplitText:** atrapalha leitura linear. Use APENAS headlines/manifesto.
- **Char-level em texto longo:** vira "máquina de escrever" mecânico em paragraph.
- **Sem `document.fonts.ready`:** SplitText mede texto antes font carregar = posições erradas.
- **Stagger > 80ms em headline:** quebra ritmo natural de leitura.

## A11y

- `split.revert()` em unmount = texto original preservado
- Screen readers veem texto completo (não palavras isoladas)
- Texto continua selecionável durante motion
- Reduced motion respeitado
- WCAG 2.2.2 — texto > 5s em motion contínuo precisa pause (kinetic loops)

## Browser baseline

SplitText paid plugin (GSAP Bonus / GSAP Premium).

**Free alternative:** `SplitType` lib npm (similar API, menos refinado):

```bash
npm install split-type
```

```js
import SplitType from 'split-type';

const split = new SplitType('.headline', { types: 'words' });
gsap.from(split.words, { y: 40, opacity: 0, stagger: 0.04, duration: 0.8 });
```

## Casos de uso

### Hero kinetic headline
- Stagger 0.04 (40ms)
- Duração 0.8-1.2s
- Ease `osmo-ease`
- Delay 0.3s after page load

### Manifesto cinematic
- Stagger 0.08 (80ms LIMITE)
- Duração 1.5s
- Ease `power3.out`
- Linha-por-linha pode ser apropriado

### Launch headline punchy
- Stagger 0.02 (20ms char-level)
- Duração 0.6s
- Ease `back.out(1.5)`

## Boundary

- Recipe completa em `references/05-gsap-recipes.md` Recipe 7
- Foundations gestalt continuity em `references/06-theoretical-foundations.md` sec 1.1
- React cleanup em `references/12-react-adapters.md` sec 9.1
