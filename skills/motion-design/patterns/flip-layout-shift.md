# Pattern: Flip layout animation (state shift)

> **Source:** DR-0 + DR-A
> **Categoria:** layout transitions / continuity
> **Pilar:** 1 (funcional/estrutural)
> **Quando usar:** layout changes (sort/filter/reorder/grid→list switch) onde elementos precisam continuidade visual.
> **Quando NÃO usar:** lista 500+ items (custo paint > benefício), animação simples 2 estados (CSS transition basta), mobile baixo.

---

## Snippet canonical — filter grid

```js
import { gsap } from 'gsap';
import { Flip } from 'gsap/Flip';

gsap.registerPlugin(Flip);

const grid = document.querySelector('.products-grid');
const items = grid.querySelectorAll('.product-card');
const filterButton = document.querySelector('.btn-filter');

filterButton.addEventListener('click', () => {
  // 1. Captura state ANTES da mudança
  const state = Flip.getState(items);

  // 2. Aplica mudança (toggle classes/estilos OR remove items DOM)
  applyFilter('category-A');

  // 3. Anima do state antigo pro novo
  Flip.from(state, {
    duration: 0.6,
    ease: 'osmo-ease',
    stagger: 0.04,
    absolute: true, // remove de fluxo durante animação
    onLeave: (elements) =>
      gsap.to(elements, { opacity: 0, scale: 0.8, duration: 0.3 }),
    onEnter: (elements) =>
      gsap.from(elements, { opacity: 0, scale: 0.8, duration: 0.3 }),
  });
});

function applyFilter(category) {
  document.querySelectorAll('.product-card').forEach((card) => {
    const matches = card.dataset.category === category || category === 'all';
    card.style.display = matches ? '' : 'none';
  });
}
```

## Snippet — sort animation

```js
function sortByPrice(direction) {
  const state = Flip.getState(items);

  // Reorder DOM
  const sorted = [...items].sort((a, b) => {
    const priceA = parseFloat(a.dataset.price);
    const priceB = parseFloat(b.dataset.price);
    return direction === 'asc' ? priceA - priceB : priceB - priceA;
  });

  sorted.forEach((item) => grid.appendChild(item));

  // Animate
  Flip.from(state, {
    duration: 0.6,
    ease: 'osmo-ease',
    stagger: 0.02,
  });
}
```

## Snippet — grid → list view toggle

```js
const viewToggle = document.querySelector('.btn-toggle-view');

viewToggle.addEventListener('click', () => {
  const state = Flip.getState(items);

  grid.classList.toggle('view-grid');
  grid.classList.toggle('view-list');

  Flip.from(state, {
    duration: 0.5,
    ease: 'osmo-ease',
    absolute: true,
  });
});
```

```css
.view-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.view-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
```

## Reduced motion

```js
if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
  // Apply filter/sort/view sem animação
  applyFilter('category-A');
  return;
}
```

## Por quê funciona

- **FLIP technique (First-Last-Invert-Play):** mede before/after, calcula transform inverse, anima pra zero
- **Continuity visual:** items "viajam" entre posições em vez de "saltarem"
- **Performance:** transforms compostos (GPU-friendly), não animação de top/left
- **Stagger 0.04 (40ms):** ritmo natural sem virar "fila lenta"

## Embasamento teórico

> "FLIP layout animation porque continuity gestalt em layout shifts — sem FLIP, items 'saltam' entre posições = perda rastreabilidade visual, user perde contexto de qual item foi pra onde."

## Anti-pattern

- **Flip em lista 500+ items:** custo paint > benefício
- **Sem `absolute: true`:** items podem afetar layout durante animação
- **Stagger > 80ms:** vira "fila", quebra ritmo
- **Sem `onLeave/onEnter` em items entrando/saindo:** items aparecem/desaparecem sem fade
- **Animar properties não-GPU-friendly:** Flip já cuida de transform, mas custom OnLeave deve evitar layout properties

## Performance

- Cap em ~50 items animando simultâneo
- `absolute: true` previne layout thrash
- GPU compositor handles transforms
- Stagger curto (≤ 60ms) previne fadiga visual

## Browser baseline

Flip plugin paid (GSAP Bonus / GSAP Premium).

## A11y

- Foco preserved no item se ele continua existindo pós-filter
- Screen reader announce result count change (`aria-live`)
- Keyboard navigation funciona durante/após animação
- Reduced motion respeitado

## Casos de uso comuns

### E-comm filter
Grid produtos + filtro categoria/preço/marca. FLIP suaviza reorder.

### Portfolio gallery
Filter por categoria de projeto. Items moves entre posições.

### Dashboard reorder
Sort tabela por column. Rows shift smooth.

### Image gallery layout switch
Grid ↔ list toggle. Items adaptam dimensions.

### Filtro busca
Removing items que não match. Remaining items collapse sem "buracos".

## React adapter

```tsx
import { useState, useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';
import { Flip } from 'gsap/Flip';

gsap.registerPlugin(Flip);

function FilterableGrid() {
  const gridRef = useRef(null);
  const [category, setCategory] = useState('all');

  const handleFilter = (newCategory) => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
      setCategory(newCategory);
      return;
    }

    const items = gridRef.current.querySelectorAll('.card');
    const state = Flip.getState(items);

    setCategory(newCategory);

    requestAnimationFrame(() => {
      Flip.from(state, {
        duration: 0.6,
        ease: 'osmo-ease',
        stagger: 0.04,
        absolute: true,
        onLeave: (els) => gsap.to(els, { opacity: 0, scale: 0.8, duration: 0.3 }),
        onEnter: (els) => gsap.from(els, { opacity: 0, scale: 0.8, duration: 0.3 }),
      });
    });
  };

  return (
    <>
      <button onClick={() => handleFilter('a')}>Category A</button>
      <button onClick={() => handleFilter('b')}>Category B</button>
      <div ref={gridRef} className="grid">
        {items
          .filter((item) => category === 'all' || item.category === category)
          .map((item) => (
            <div key={item.id} className="card">{item.name}</div>
          ))}
      </div>
    </>
  );
}
```

## Boundary

- Recipe completa em `references/05-gsap-recipes.md` Recipe 9
- Pilar 1 listas em `references/01-funcional-estrutural.md`
- Foundations continuity em `references/06-theoretical-foundations.md` sec 1.1
