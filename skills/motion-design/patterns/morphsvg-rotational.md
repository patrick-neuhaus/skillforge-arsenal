# Pattern: MorphSVG rotational mapping

> **Source:** DR-C Osmo + DR-0
> **Categoria:** vetorial / icon state change
> **Pilar:** 2 (vetorial/branding)
> **Quando usar:** ícone state change com formas que NÃO são parentes geometricamente (arrow → check, hamburger → close com curva orgânica, play → pause stylized).
> **Quando NÃO usar:** formas geometricamente parentes (CSS rotate basta), formas sem relação semântica (confunde user), microinteraction repetitiva (overhead injustificado).

---

## Snippet canonical

```js
import { gsap } from 'gsap';
import { MorphSVGPlugin } from 'gsap/MorphSVGPlugin';

gsap.registerPlugin(MorphSVGPlugin);

gsap.to('#icon-arrow', {
  morphSVG: {
    shape: '#icon-check',
    type: 'rotational', // CRÍTICO: rotational para morphs naturais
    map: 'complexity', // mapeia pontos por complexidade (não distância)
  },
  duration: 0.6,
  ease: 'osmo-ease',
});
```

## HTML structure

```html
<svg viewBox="0 0 24 24">
  <!-- Path visível (será morphado) -->
  <path id="icon-arrow" d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" />

  <!-- Path target (escondido, só pra MorphSVG referenciar) -->
  <path id="icon-check" d="M5 12l5 5L20 7" stroke="currentColor" stroke-width="2" style="visibility: hidden;" />
</svg>
```

## Snippet — toggle state (menu hamburger ↔ close)

```js
let isOpen = false;
const button = document.querySelector('.btn-menu');

button.addEventListener('click', () => {
  isOpen = !isOpen;

  gsap.to('#icon-current', {
    morphSVG: {
      shape: isOpen ? '#icon-close' : '#icon-hamburger',
      type: 'rotational',
      map: 'complexity',
    },
    duration: 0.4,
    ease: 'power2.inOut',
  });
});
```

```html
<svg viewBox="0 0 24 24">
  <path id="icon-current" d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2" />
  <path id="icon-hamburger" d="M3 6h18M3 12h18M3 18h18" style="display: none;" />
  <path id="icon-close" d="M6 6l12 12M6 18L18 6" style="display: none;" />
</svg>
```

## Reduced motion

```js
if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
  // Snap direto pra forma final, sem morph
  document.querySelector('#icon-current').setAttribute('d', isOpen ? closeShape : hamburgerShape);
  return;
}

// ...morphSVG normal
```

## Por quê funciona

- **`type: "rotational"`:** mapeia pontos por rotação ao redor do centro = morph natural
- **`map: "complexity"`:** prioritiza pontos complexos (curvas, ângulos), não distância linear
- **Diferença vs default `linear`:** linear causa "spaghetti" visual em formas complexas — paths cruzam de forma estranha
- **Continuity gestalt:** transição suave entre estados semânticos relacionados

## Embasamento teórico

> "MorphSVG rotational + complexity porque morph natural sem cruzamento de paths estranho. Default `linear` map causa 'spaghetti' visual em formas complexas. Type rotational mantém rotação pontos ao redor do centro = transição orgânica."

## Anti-pattern

- **`type: "linear"` default em formas complexas:** spaghetti paths
- **Morph entre formas sem relação semântica:** confunde user (ex: morph entre coffee mug ↔ rocket = nonsensical)
- **Morph em microinteraction 100+/dia:** overhead injustificado, CSS rotate basta
- **Sem fallback reduced motion:** snap final state obrigatório
- **Path target visible:** target precisa `display: none` OR `visibility: hidden`

## Performance

- MorphSVG = ~30KB gzipped (paid plugin)
- Cada morph = recálculo points (uma vez por animação)
- Rodando = idêntica perf a tween normal
- Cap em ~5 morphs simultâneos (perf-safe)

## Browser baseline

MorphSVG paid plugin (GSAP Bonus). Funciona em todos browsers que suportam SVG (universal).

## A11y

- `aria-label` no button descrevendo state actual
- `aria-expanded` em menu toggles
- Keyboard activation funciona
- Reduced motion respeitado (snap-to-state)
- Screen reader announce state change

## Casos de uso

### Menu hamburger ↔ close
Hambúrguer 3 lines → X close. Rotational morph mantém continuity visual.

### Play ↔ pause
Triangle play → 2 bars pause. Morph stylized vs CSS swap.

### Search ↔ close
Magnifying glass → X. Brand-specific touch.

### Like / heart fill
Empty heart → filled heart. Continuity emotion.

### Arrow direction change
Arrow → arrow rotated. Rotational morph natural.

## DIY vs Lottie/Rive

| Técnica | Custo | Quando usar |
|---|---|---|
| MorphSVG | Plugin paid + dev time | Brand-specific, controle total |
| Lottie animado em After Effects | Designer time + asset size | Animação complexa, designer-led |
| Rive interactive | Tooling Rive + asset | State machine complexo |
| CSS rotate / clip-path | Free, simple | Formas geometricamente parentes |
| SVG nativo `<animate>` | Free, declarativo | Animações simples sem GSAP |

## React adapter

```tsx
import { useState, useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';
import { MorphSVGPlugin } from 'gsap/MorphSVGPlugin';

gsap.registerPlugin(MorphSVGPlugin);

function MenuButton() {
  const [isOpen, setIsOpen] = useState(false);
  const pathRef = useRef(null);

  useGSAP(() => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
      pathRef.current.setAttribute(
        'd',
        isOpen ? 'M6 6l12 12M6 18L18 6' : 'M3 6h18M3 12h18M3 18h18'
      );
      return;
    }

    gsap.to(pathRef.current, {
      morphSVG: {
        shape: isOpen ? 'M6 6l12 12M6 18L18 6' : 'M3 6h18M3 12h18M3 18h18',
        type: 'rotational',
        map: 'complexity',
      },
      duration: 0.4,
      ease: 'power2.inOut',
    });
  }, [isOpen]);

  return (
    <button
      onClick={() => setIsOpen(!isOpen)}
      aria-label={isOpen ? 'Close menu' : 'Open menu'}
      aria-expanded={isOpen}
    >
      <svg viewBox="0 0 24 24" width="24" height="24">
        <path
          ref={pathRef}
          d="M3 6h18M3 12h18M3 18h18"
          stroke="currentColor"
          strokeWidth="2"
          fill="none"
        />
      </svg>
    </button>
  );
}
```

## Boundary

- Recipe completa em `references/05-gsap-recipes.md` Recipe 10
- Pilar 2 morphing em `references/02-vetorial-branding.md`
- Foundations gestalt continuity em `references/06-theoretical-foundations.md` sec 1.1
