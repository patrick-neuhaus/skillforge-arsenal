# Pattern: React Three Fiber (R3F) hero scene

> **Source:** DR-A + DR-B (Awwwards stack pattern A)
> **Categoria:** spatial / 3D hero
> **Pilar:** 4 (espacial/imersivo)
> **Quando usar:** hero 3D em React app (Lovable / Next.js) com produto, brand experience, configurador, environment imersivo.
> **Quando NÃO usar:** SaaS operacional, mobile baixo prioridade, projeto sem GPU justificável.

---

## Setup

```bash
npm install three @react-three/fiber @react-three/drei
npm install gsap @gsap/react
```

## Snippet canonical — hero 3D scrubed scroll

```tsx
import { Canvas, useThree, useFrame } from '@react-three/fiber';
import { OrbitControls, useGLTF, Environment } from '@react-three/drei';
import { useRef } from 'react';
import { useGSAP } from '@gsap/react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

function ProductMesh() {
  const meshRef = useRef(null);
  const { scene } = useGLTF('/models/product.glb');

  useGSAP(() => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    gsap.to(meshRef.current.rotation, {
      y: Math.PI * 2,
      scrollTrigger: {
        trigger: '.hero-section',
        start: 'top top',
        end: 'bottom top',
        scrub: 1,
      },
    });
  });

  return <primitive ref={meshRef} object={scene} />;
}

function CameraRig() {
  const { camera } = useThree();

  useGSAP(() => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    gsap.to(camera.position, {
      z: 3,
      scrollTrigger: {
        trigger: '.hero-section',
        start: 'top top',
        end: 'bottom top',
        scrub: 1,
      },
    });
  });

  return null;
}

function HeroScene() {
  return (
    <Canvas
      dpr={[1, 2]} // pixel ratio cap pra perf
      camera={{ position: [0, 0, 5], fov: 50 }}
      style={{ position: 'fixed', top: 0, width: '100%', height: '100vh' }}
    >
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} intensity={1} />
      <Environment preset="studio" />
      <ProductMesh />
      <CameraRig />
    </Canvas>
  );
}

export default function HeroSection() {
  return (
    <>
      <HeroScene />
      <section className="hero-section min-h-[200vh] relative z-10">
        <h1 className="text-6xl">Premium product reveal</h1>
      </section>
    </>
  );
}
```

## Snippet — fallback estático (mobile baixo / Save-Data)

```tsx
import { useEffect, useState } from 'react';

function HeroWithFallback() {
  const [shouldRender3D, setShouldRender3D] = useState(false);

  useEffect(() => {
    // Detect device capability
    const isLowEnd = navigator.hardwareConcurrency <= 2 || navigator.deviceMemory <= 2;
    const saveData = navigator.connection?.saveData;
    const prefersReduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

    setShouldRender3D(!isLowEnd && !saveData && !prefersReduced);
  }, []);

  if (!shouldRender3D) {
    return <img src="/hero-fallback.jpg" alt="Product" className="hero-fallback" />;
  }

  return <HeroScene />;
}
```

## Por quê funciona

- **R3F = Three.js declarativo:** components React + JSX em vez de imperative scene.create.
- **useFrame ref-direct:** anima `meshRef.current.rotation.y` sem React state = sem re-render 60fps.
- **Drei utilities:** `useGLTF`, `Environment`, `OrbitControls` reduzem boilerplate.
- **Pixel ratio cap:** `dpr={[1, 2]}` previne mobile 4x render.

## Embasamento teórico

> "R3F hero porque audience [premium / configurador product / brand imersivo] espera materialidade — 3D entrega trust signal 'produto físico real' que image estática não consegue. Mas só justifica se ROI conversion > custo bundle/perf."

## Reduced motion + Save-Data + low-end

Triple gate fallback estático:

```tsx
const isLowEnd = navigator.hardwareConcurrency <= 2 || navigator.deviceMemory <= 2;
const saveData = navigator.connection?.saveData;
const prefersReduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

if (isLowEnd || saveData || prefersReduced) {
  return <ProductImageStatic />;
}
```

## Anti-pattern

- **`useState` em useFrame:** re-render 60fps = perf disaster. Use ref direto.
- **Pixel ratio sem cap:** retina renders 4x pixels = mobile high-DPI < 30fps.
- **Modelo GLTF sem compressão:** sem Draco/meshopt = MB+ bundle.
- **Sem suspend on tab blur:** GPU desperdiçada quando user trocou tab.
- **Hero LCP-blocking 3D:** atrasa LCP do conteúdo principal = SEO ruim.
- **Sem fallback estático:** mobile baixo / accessibility = exclusão.

## Performance targets

| Cenário | FPS alvo | Boot alvo | Asset alvo |
|---|---|---|---|
| Hero 3D desktop | 60 | < 2s | < 2 MB |
| Hero 3D mobile médio | 30 | < 3s | < 1 MB |
| Configurador desktop | 60 | < 4s | < 5 MB |
| Configurador mobile | 30 OU fallback | < 6s OU desligar | < 2 MB |

## Otimizações obrigatórias

- **Compress GLTF:** Draco / meshopt
- **Compress textures:** KTX2 / Basis
- **LOD:** mesh menor pra mobile
- **Lazy load:** dynamic import quando scene out-of-viewport
- **Suspend on blur:** `useEffect` listening visibility change
- **Frustum culling:** Three.js faz default

## Browser baseline

WebGL2: Chrome 88+, Safari 14+, Firefox 80+. Universal modernos.

## A11y

- **Alternative content:** image estática + descrição textual sempre disponível
- **Keyboard navigation:** OrbitControls com keys (drei tem `enableKeys`)
- **Screen reader:** `aria-label` descrevendo cena
- **Focus indication:** hotspots clicáveis precisam DOM equivalente focável
- **Reduced motion:** desliga auto-rotate / idle animations
- **Pause control:** idle animations sempre têm pause

## Drei utilities úteis

```tsx
import {
  OrbitControls,    // controls câmera
  useGLTF,          // load GLTF model
  Environment,      // HDR environment lighting
  Float,            // simulate floating
  PresentationControls, // wrapped orbit pra UX guiada
  Html,             // HTML inside canvas (labels)
  Stage,            // pre-configured scene wrapper
} from '@react-three/drei';
```

## Casos de uso award-grade

### Product hero — e-comm luxury
Modelo produto + Environment HDR + scroll rotation + camera dolly.

### Brand site experimental
Custom geometry + shader noise material + scroll-driven camera path.

### Configurador interativo
GLTF product + OrbitControls + UI overlay React + state-driven materials.

### Spatial portfolio
Multiple scenes em rotas + persistent canvas pattern (ver `patterns/persistent-canvas.md` adapter R3F).

## Boundary

- Pilar 4 detalhamento em `references/04-espacial-imersivo.md`
- React adapter completo em `references/12-react-adapters.md` sec 4
- Persistent canvas em `patterns/persistent-canvas.md`
