# `references/12-react-adapters.md` — React Adapters (Wave 9)

> **GSAP em React específico.** useGSAP hook (@gsap/react), gsap.context() cleanup, React Three Fiber, Next.js SSR caveats, Lovable Vite specifics, Astro islands. Adapter layer entre recipes core (`05-gsap-recipes.md`) e implementação React.
> **Quando usar:** quando session narrative confirma stack React (Lovable, Next, Astro+React island, Vite). Phase 5 spec inclui adapter conforme stack.
> **Boundary:** React-specific adapters. Recipes vanilla em `05-gsap-recipes.md`. Vue/Svelte adapters = Wave 2 roadmap (cortado).

---

## 1. useGSAP hook (@gsap/react) — canonical React pattern

### 1.1 Setup

```bash
npm install gsap @gsap/react
```

### 1.2 Pattern básico

```jsx
import { useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';

function HeroSection() {
  const containerRef = useRef(null);

  useGSAP(() => {
    // Animations aqui — cleanup automático em unmount
    gsap.from('.hero-title', {
      y: 40,
      opacity: 0,
      duration: 1,
      ease: 'osmo-ease',
    });
  }, { scope: containerRef }); // scope = limita queries pro container

  return (
    <section ref={containerRef} className="hero">
      <h1 className="hero-title">Welcome</h1>
    </section>
  );
}
```

### 1.3 Por quê useGSAP > useEffect direto

`useGSAP` faz internamente:
1. Cria `gsap.context()` no mount
2. Registra todas animations no context
3. Cleanup automático no unmount via `context.revert()`
4. Restaura SplitText (`split.revert()` automático)
5. Mata ScrollTriggers (`ScrollTrigger.kill()`)
6. Reverte qualquer DOM modification

**Sem useGSAP (anti-pattern):**

```jsx
// ❌ NÃO FAZER — memory leak garantido
useEffect(() => {
  gsap.to('.hero-title', { x: 100 });
  return () => {
    // Você TEM que matar manualmente cada tween + ScrollTrigger + SplitText
    // Esquecer 1 = leak silencioso
  };
}, []);
```

---

## 2. gsap.context() pattern (alternativa sem hook)

Quando NÃO pode usar `@gsap/react` (ex: vanilla React + GSAP free tier), use `gsap.context()` manual:

```jsx
import { useRef, useEffect } from 'react';
import { gsap } from 'gsap';

function HeroSection() {
  const containerRef = useRef(null);

  useEffect(() => {
    const ctx = gsap.context(() => {
      gsap.from('.hero-title', { y: 40, opacity: 0, duration: 1 });
    }, containerRef);

    return () => ctx.revert(); // Cleanup manual mas robusto
  }, []);

  return (
    <section ref={containerRef}>
      <h1 className="hero-title">Welcome</h1>
    </section>
  );
}
```

**Diferença vs useGSAP:** mesmo resultado de cleanup, mas verbose. Use `useGSAP` quando puder.

---

## 3. ScrollTrigger em React específico

### 3.1 Pattern com useGSAP

```jsx
import { useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

function ScrollSection() {
  const containerRef = useRef(null);

  useGSAP(() => {
    gsap.to('.parallax-bg', {
      y: -100,
      scrollTrigger: {
        trigger: containerRef.current,
        start: 'top bottom',
        end: 'bottom top',
        scrub: 0.5,
      },
    });
  }, { scope: containerRef });

  return (
    <section ref={containerRef}>
      <div className="parallax-bg">...</div>
    </section>
  );
}
```

### 3.2 Refresh em route change (Next.js / SPA)

ScrollTrigger calcula posições NO MOUNT. Em SPA, route change pode invalidar.

**Solução Next.js App Router:**

```jsx
'use client';
import { usePathname } from 'next/navigation';
import { useEffect } from 'react';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

function useScrollTriggerRefresh() {
  const pathname = usePathname();

  useEffect(() => {
    ScrollTrigger.refresh();
  }, [pathname]);
}
```

---

## 4. React Three Fiber (R3F) + GSAP

### 4.1 Setup

```bash
npm install three @react-three/fiber @react-three/drei
npm install gsap @gsap/react
```

### 4.2 Pattern: animar camera com GSAP

```jsx
import { Canvas, useThree } from '@react-three/fiber';
import { useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

function SceneContent() {
  const { camera } = useThree();
  const meshRef = useRef();

  useGSAP(() => {
    gsap.to(camera.position, {
      z: 5,
      scrollTrigger: {
        trigger: '.scroll-container',
        start: 'top top',
        end: 'bottom bottom',
        scrub: 1,
      },
    });

    gsap.to(meshRef.current.rotation, {
      y: Math.PI * 2,
      duration: 4,
      repeat: -1,
      ease: 'none',
    });
  });

  return (
    <mesh ref={meshRef}>
      <boxGeometry />
      <meshStandardMaterial color="orange" />
    </mesh>
  );
}

function HeroScene() {
  return (
    <Canvas>
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
      <SceneContent />
    </Canvas>
  );
}
```

### 4.3 Caveat: GSAP anima objeto Three.js direto, NÃO React state

NUNCA usar setState em useFrame ou GSAP onUpdate Three.js — re-render React 60fps = perf disaster.

**Anti-pattern:**

```jsx
// ❌ NÃO FAZER
const [rotation, setRotation] = useState(0);
useFrame(() => setRotation(r => r + 0.01)); // re-render 60fps!
```

**Pattern:**

```jsx
// ✅ Anima ref direto
const meshRef = useRef();
useFrame(() => {
  meshRef.current.rotation.y += 0.01; // sem re-render React
});
```

---

## 5. Next.js SSR caveats

### 5.1 GSAP plugins precisam dynamic import

Plugins paid (SplitText, MorphSVG, Flip) não funcionam em SSR (window undefined).

**Pattern:**

```jsx
'use client';
import { useEffect, useState } from 'react';

function HeroSection() {
  const [gsapLoaded, setGsapLoaded] = useState(false);

  useEffect(() => {
    const loadGSAP = async () => {
      const { gsap } = await import('gsap');
      const { SplitText } = await import('gsap/SplitText');
      gsap.registerPlugin(SplitText);
      setGsapLoaded(true);
    };
    loadGSAP();
  }, []);

  if (!gsapLoaded) return <h1>Welcome</h1>; // SSR fallback estático

  return <h1 className="kinetic">Welcome</h1>;
}
```

### 5.2 ScrollTrigger + Next.js App Router

App Router agressive client/server split. ScrollTrigger SOMENTE em `'use client'` components.

```jsx
'use client'; // CRÍTICO

import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

if (typeof window !== 'undefined') {
  gsap.registerPlugin(ScrollTrigger);
}
```

### 5.3 Fonts loading caveat

Custom fonts (next/font) carregam após hydration. Animação que mede texto deve aguardar font load:

```jsx
useGSAP(() => {
  document.fonts.ready.then(() => {
    // Now safe to use SplitText / measure text
    const split = new SplitText('.hero-title', { type: 'words' });
    gsap.from(split.words, { y: 40, stagger: 0.04 });
  });
});
```

---

## 6. Lovable Vite specifics

### 6.1 Lovable é Vite + React

Stack: Vite 5+ + React 18 + TypeScript + Tailwind. GSAP funciona perfeito (Vite handles ES modules native).

### 6.2 Pattern recomendado Lovable

```tsx
// src/components/sections/Hero.tsx
import { useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { CustomEase } from 'gsap/CustomEase';

gsap.registerPlugin(ScrollTrigger, CustomEase);
CustomEase.create('osmo-ease', '0.625, 0.05, 0, 1');

export default function Hero() {
  const containerRef = useRef<HTMLElement>(null);

  useGSAP(
    () => {
      gsap.from('.hero-title', {
        y: 40,
        opacity: 0,
        duration: 1.2,
        ease: 'osmo-ease',
      });
    },
    { scope: containerRef }
  );

  return (
    <section ref={containerRef} className="hero min-h-screen">
      <h1 className="hero-title text-6xl">Welcome</h1>
    </section>
  );
}
```

### 6.3 Lovable Agent prompt template

```
Adiciona motion na <Hero /> usando GSAP + useGSAP hook:

1. Importa gsap, useGSAP, ScrollTrigger, CustomEase
2. Registra plugins + cria CustomEase 'osmo-ease' = '0.625, 0.05, 0, 1'
3. Em useGSAP com scope={containerRef}:
   - gsap.from('.hero-title', {y: 40, opacity: 0, duration: 1.2, ease: 'osmo-ease'})

4. Adiciona reduced motion check:
   const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
   if (prefersReduced) return; // skip animation

5. A11y: aria-label="Hero with reveal animation" no <section>

Critério aceite:
- [ ] Duração medida bate spec ±10ms
- [ ] reduced-motion testado em DevTools
- [ ] Cleanup roda em unmount (useGSAP cuida)
```

---

## 7. Astro islands + GSAP

### 7.1 Pattern: GSAP em React island

```astro
---
// src/pages/index.astro
import HeroIsland from '../components/HeroIsland.tsx';
---

<html>
  <body>
    <HeroIsland client:load />
  </body>
</html>
```

```tsx
// src/components/HeroIsland.tsx
import { useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';

export default function HeroIsland() {
  const ref = useRef(null);
  useGSAP(() => {
    gsap.from('.title', { y: 40, opacity: 0, duration: 1 });
  }, { scope: ref });

  return <section ref={ref}><h1 className="title">Welcome</h1></section>;
}
```

### 7.2 Pattern: GSAP vanilla em Astro (sem React)

```astro
---
// src/pages/index.astro
---

<html>
  <body>
    <h1 class="hero-title">Welcome</h1>

    <script>
      import { gsap } from 'gsap';

      gsap.from('.hero-title', {
        y: 40,
        opacity: 0,
        duration: 1,
      });
    </script>
  </body>
</html>
```

**Quando usar React island vs vanilla:** se motion é complexo + state-driven, React island. Se simples + standalone, vanilla.

---

## 8. Lenis em React

### 8.1 Pattern com useEffect

```tsx
import { useEffect } from 'react';
import Lenis from '@studio-freight/lenis';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

export function useLenis() {
  useEffect(() => {
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReduced) return; // skip Lenis

    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
      smoothTouch: false,
    });

    gsap.ticker.add((time) => {
      lenis.raf(time * 1000);
    });
    gsap.ticker.lagSmoothing(0);

    lenis.on('scroll', ScrollTrigger.update);

    return () => {
      lenis.destroy();
      gsap.ticker.remove(/* the function */); // cleanup ticker
    };
  }, []);
}
```

### 8.2 Uso em layout

```tsx
// app/layout.tsx (Next.js) OR src/App.tsx (Vite)
'use client';
import { useLenis } from '@/hooks/useLenis';

export default function RootLayout({ children }) {
  useLenis();
  return <>{children}</>;
}
```

---

## 9. Common patterns React-specific

### 9.1 SplitText cleanup em React

```tsx
import { useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { SplitText } from 'gsap/SplitText';

function KineticHeadline() {
  const ref = useRef(null);
  const splitRef = useRef(null);

  useGSAP(() => {
    splitRef.current = new SplitText('.headline', { type: 'words' });

    gsap.from(splitRef.current.words, {
      y: 40,
      opacity: 0,
      stagger: 0.04,
      duration: 0.8,
    });

    return () => {
      splitRef.current?.revert(); // CRÍTICO: revert preserva texto pra a11y/SEO
    };
  }, { scope: ref });

  return <h1 ref={ref} className="headline">Welcome to the future</h1>;
}
```

### 9.2 useState + GSAP synch (toggle pattern)

```tsx
import { useState, useRef, useEffect } from 'react';
import { gsap } from 'gsap';

function Modal() {
  const [isOpen, setIsOpen] = useState(false);
  const modalRef = useRef(null);

  useEffect(() => {
    if (!modalRef.current) return;

    if (isOpen) {
      gsap.to(modalRef.current, {
        y: 0,
        opacity: 1,
        duration: 0.32,
        ease: 'power2.out',
      });
    } else {
      gsap.to(modalRef.current, {
        y: 20,
        opacity: 0,
        duration: 0.2,
        ease: 'power3.in', // mais rápido na saída
      });
    }
  }, [isOpen]);

  return (
    <>
      <button onClick={() => setIsOpen(true)}>Open</button>
      <div ref={modalRef} className="modal" style={{ opacity: 0 }}>
        ...
        <button onClick={() => setIsOpen(false)}>Close</button>
      </div>
    </>
  );
}
```

---

## 10. Performance React-specific

### 10.1 Refs > queries quando possível

```tsx
// ❌ Slower — query DOM cada render
gsap.to('.hero-title', {...});

// ✅ Faster — ref direto
const titleRef = useRef(null);
gsap.to(titleRef.current, {...});
```

### 10.2 Memoize timelines pesadas

```tsx
import { useMemo, useRef } from 'react';

function ComplexAnimation() {
  const ref = useRef(null);

  const tl = useMemo(() => gsap.timeline({ paused: true }), []);

  useEffect(() => {
    tl.from('.item', { y: 40, stagger: 0.1 });
    tl.play();

    return () => tl.kill();
  }, []);
}
```

### 10.3 Suspend animations on tab blur

```tsx
useEffect(() => {
  const handleVisibilityChange = () => {
    if (document.hidden) {
      gsap.globalTimeline.pause();
    } else {
      gsap.globalTimeline.resume();
    }
  };
  document.addEventListener('visibilitychange', handleVisibilityChange);
  return () => document.removeEventListener('visibilitychange', handleVisibilityChange);
}, []);
```

---

## 11. Anti-patterns React + GSAP

1. **useEffect sem cleanup:** memory leak. SEMPRE usar useGSAP OR ctx.revert().
2. **setState em useFrame R3F:** re-render 60fps. Usa ref direto.
3. **Query DOM sem scope:** seletor `.hero-title` afeta múltiplos componentes. SEMPRE scope.
4. **GSAP plugins fora de useEffect SSR:** crash em SSR (window undefined). Dynamic import.
5. **SplitText sem revert:** quebra a11y/SEO em unmount.
6. **ScrollTrigger sem refresh em route change:** posições stale em SPA.
7. **Animar Three.js via React state:** perf disaster. Anima objeto direto.

---

## 12. Stack-specific cheat sheet

| Stack | Setup | Key pattern |
|---|---|---|
| **Lovable (Vite + React)** | useGSAP + CustomEase global | useRef + scope |
| **Next.js App Router** | 'use client' + dynamic import GSAP | Refresh ScrollTrigger em pathname change |
| **Astro + React island** | client:load + useGSAP | Island isolada do resto |
| **Astro vanilla** | `<script>` block + import gsap | Sem React |
| **R3F (any framework)** | useFrame + ref direto | NÃO setState em frame loop |

---

## 13. Boundary com outras skills

- **`react-patterns`** — patterns React gerais (useEffect, refs, etc). Esta ref é GSAP-specific React.
- **`react-patterns --audit-cross-browser`** — audit cross-browser. Esta ref dá pattern; cross-browser audita.
- **`05-gsap-recipes.md`** — recipes vanilla. Esta ref ADAPTA recipes pra React.

---

## 14. Manutenção desta ref

- Atualiza quando @gsap/react releases major change
- ADD framework novo (Vue, Svelte) só quando Patrick precisar real
- Refresh trimestral (Next.js / Vite mudam)
- Re-validar Lovable specifics conforme Lovable evolui
