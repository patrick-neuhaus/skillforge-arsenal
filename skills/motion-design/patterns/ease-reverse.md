# Pattern: easeReverse (GSAP 2026 feature)

> **Source:** DR-0 GSAP 2026 release notes
> **Categoria:** asymmetric easing
> **Pilar:** 1 (funcional/estrutural) — modais, drawers, overlays
> **Quando usar:** animação onde reverse precisa easing diferente da entrada (entrada cinemática lenta, saída rápida funcional).
> **Quando NÃO usar:** animações simétricas (forward = reverse = mesmo timing).

---

## Snippet canonical

```js
import { gsap } from 'gsap';

gsap.to('.modal-panel', {
  y: 0,
  opacity: 1,
  duration: 0.32,
  ease: 'power2.out',     // entrada: pousa suave
  easeReverse: 'power3.in', // saída: decola rápido
});

// Quando reverte (close modal):
tl.reverse(); // automaticamente usa easeReverse
```

## Uso típico — modal pattern

```js
const modalTl = gsap.timeline({ paused: true });

modalTl.fromTo(
  '.modal-backdrop',
  { opacity: 0 },
  {
    opacity: 1,
    duration: 0.2,
    ease: 'power1.out',
    easeReverse: 'power1.in',
  }
);

modalTl.fromTo(
  '.modal-panel',
  { y: 20, opacity: 0 },
  {
    y: 0,
    opacity: 1,
    duration: 0.32,
    ease: 'power2.out',
    easeReverse: 'power3.in', // saída ainda mais rápida
  },
  '<' // mesmo tempo backdrop
);

// Open
openButton.addEventListener('click', () => modalTl.play());

// Close
closeButton.addEventListener('click', () => modalTl.reverse());
```

## Por quê funciona

- **Entrada serve "anúncio":** modal aparece com cuidado, anuncia presença, "pousa" no viewport.
- **Saída serve "liberar contexto":** user quer voltar pro fluxo atrás do modal — saída rápida = menos friction.
- **Carbon/Material guidelines:** convergem em "exit faster than enter".

## Embasamento teórico

> "easeReverse com exit power3.in porque saída de modal deve ser MAIS rápida que entrada — Carbon/Material guidelines convergem nisso. User quer voltar ao contexto, não esperar fade-out lento."

## Reduced motion

```js
ease: prefersReducedMotion ? 'none' : 'power2.out',
easeReverse: prefersReducedMotion ? 'none' : 'power3.in',
duration: prefersReducedMotion ? 0 : 0.32,
```

Snap-to-state em ambas direções.

## Anti-pattern

- **Mesmo easing entrada/saída:** modal de 320ms entrar + 320ms sair = saída parece "lentidão". User percebe como bug.
- **Saída MAIS lenta que entrada:** anti-padrão clássico — quebra expectativa user.
- **easeReverse em loops:** loops infinitos = forward = reverse, sem benefício.

## Casos de uso

- **Modal:** entrada 320ms `power2.out`, saída 200ms `power3.in`
- **Drawer:** entrada 360ms `power2.out`, saída 220ms `power3.in`
- **Toast:** entrada 220ms `power2.out`, saída 150ms `power3.in`
- **Dropdown:** entrada 180ms `power2.out`, saída 120ms `power3.in`
- **Tooltip:** entrada 150ms `power2.out`, saída 100ms `power3.in`

## Browser baseline

GSAP 3.13+ (release 2026). Universal browsers.

## A11y

- Reduced motion respeitado
- Foco preserved durante transição
- Screen reader announce state change

## React adapter

```tsx
import { useRef, useState, useEffect } from 'react';
import { gsap } from 'gsap';

function Modal({ isOpen }) {
  const modalRef = useRef(null);
  const tlRef = useRef(null);

  useEffect(() => {
    tlRef.current = gsap.timeline({ paused: true });

    tlRef.current.fromTo(
      modalRef.current,
      { y: 20, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.32,
        ease: 'power2.out',
        easeReverse: 'power3.in',
      }
    );

    return () => tlRef.current?.kill();
  }, []);

  useEffect(() => {
    if (isOpen) {
      tlRef.current.play();
    } else {
      tlRef.current.reverse();
    }
  }, [isOpen]);

  return <div ref={modalRef} className="modal" style={{ opacity: 0 }}>...</div>;
}
```

## Boundary

- Recipe completa em `references/05-gsap-recipes.md` Recipe 3
- Foundations easing semantics em `references/06-theoretical-foundations.md` sec 4.3
