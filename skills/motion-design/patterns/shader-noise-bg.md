# Pattern: Shader noise background (GLSL)

> **Source:** DR-A + DR-B Codrops shader tutorials
> **Categoria:** ambient / experimental
> **Pilar:** 4 (espacial/imersivo)
> **Quando usar:** brand site premium querendo background ambient orgânico não-mecânico. Diferenciação visual high-end vs gradients CSS comuns.
> **Quando NÃO usar:** SaaS operacional, mobile baixo (GPU custo alto), conteúdo contraste-crítico (shader pode quebrar legibility).

---

## Setup R3F

```bash
npm install three @react-three/fiber
```

## Shader code (GLSL)

```glsl
// Vertex shader
varying vec2 vUv;
void main() {
  vUv = uv;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
```

```glsl
// Fragment shader — Perlin-style noise
uniform float uTime;
uniform vec2 uResolution;
varying vec2 vUv;

// Simplex noise function (compact)
vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec2 mod289(vec2 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec3 permute(vec3 x) { return mod289(((x * 34.0) + 1.0) * x); }

float snoise(vec2 v) {
  const vec4 C = vec4(0.211324865405187, 0.366025403784439, -0.577350269189626, 0.024390243902439);
  vec2 i = floor(v + dot(v, C.yy));
  vec2 x0 = v - i + dot(i, C.xx);
  vec2 i1 = (x0.x > x0.y) ? vec2(1.0, 0.0) : vec2(0.0, 1.0);
  vec4 x12 = x0.xyxy + C.xxzz;
  x12.xy -= i1;
  i = mod289(i);
  vec3 p = permute(permute(i.y + vec3(0.0, i1.y, 1.0)) + i.x + vec3(0.0, i1.x, 1.0));
  vec3 m = max(0.5 - vec3(dot(x0, x0), dot(x12.xy, x12.xy), dot(x12.zw, x12.zw)), 0.0);
  m = m * m;
  m = m * m;
  vec3 x = 2.0 * fract(p * C.www) - 1.0;
  vec3 h = abs(x) - 0.5;
  vec3 ox = floor(x + 0.5);
  vec3 a0 = x - ox;
  m *= 1.79284291400159 - 0.85373472095314 * (a0 * a0 + h * h);
  vec3 g;
  g.x = a0.x * x0.x + h.x * x0.y;
  g.yz = a0.yz * x12.xz + h.yz * x12.yw;
  return 130.0 * dot(m, g);
}

void main() {
  vec2 uv = vUv;
  float n = snoise(uv * 3.0 + uTime * 0.1);
  vec3 color1 = vec3(0.1, 0.2, 0.4); // brand color A
  vec3 color2 = vec3(0.4, 0.1, 0.5); // brand color B
  vec3 finalColor = mix(color1, color2, n * 0.5 + 0.5);
  gl_FragColor = vec4(finalColor, 1.0);
}
```

## React component

```tsx
import { Canvas, useFrame } from '@react-three/fiber';
import { useRef } from 'react';
import * as THREE from 'three';

const vertexShader = `/* ... */`;
const fragmentShader = `/* ... */`;

function NoiseShaderMesh() {
  const meshRef = useRef(null);

  const uniforms = useRef({
    uTime: { value: 0 },
    uResolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
  }).current;

  useFrame((state) => {
    uniforms.uTime.value = state.clock.getElapsedTime();
  });

  return (
    <mesh ref={meshRef}>
      <planeGeometry args={[2, 2]} />
      <shaderMaterial
        vertexShader={vertexShader}
        fragmentShader={fragmentShader}
        uniforms={uniforms}
      />
    </mesh>
  );
}

export default function NoiseBackground() {
  return (
    <Canvas
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        zIndex: -1,
        pointerEvents: 'none',
      }}
      dpr={[1, 2]} // pixel ratio cap
      camera={{ position: [0, 0, 1] }}
    >
      <NoiseShaderMesh />
    </Canvas>
  );
}
```

## Reduced motion + low-end fallback

```tsx
import { useEffect, useState } from 'react';

function NoiseBackgroundWithFallback() {
  const [shouldRender, setShouldRender] = useState(false);

  useEffect(() => {
    const prefersReduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const isLowEnd = navigator.hardwareConcurrency <= 2 || navigator.deviceMemory <= 2;
    const saveData = navigator.connection?.saveData;

    setShouldRender(!prefersReduced && !isLowEnd && !saveData);
  }, []);

  if (!shouldRender) {
    // Fallback: CSS gradient estático
    return (
      <div
        style={{
          position: 'fixed',
          inset: 0,
          background: 'linear-gradient(135deg, #1a3380 0%, #663380 100%)',
          zIndex: -1,
        }}
      />
    );
  }

  return <NoiseBackground />;
}
```

## Por quê funciona

- **Visual diferencial:** shader noise = orgânico, único, não-mecânico vs gradient CSS comum
- **GPU-accelerated:** roda em GPU, não main thread = não atrapalha React/animations
- **Custom brand:** cores GLSL customizáveis = identidade brand única
- **Lightweight:** plane geometry simples (2 triangles) — perf headroom

## Embasamento teórico

> "Shader noise background porque brand premium experimental — gradient CSS comum vira genérico, shader custom entrega assinatura visual única + materialidade orgânica que diferencia do AI-generated common landing."

## Reduced motion

Triple gate: prefers-reduced-motion OR low-end OR save-data → fallback CSS gradient.

## Anti-pattern

- **Shader pesado em mobile sem fallback:** GPU drain + bateria
- **Sem pixel ratio cap:** retina renders 4x = mobile high-DPI lag
- **Shader contraste-quebrante atrás de texto:** quebra WCAG legibility
- **Shader como LCP element:** shader não pode atrasar conteúdo principal
- **Sem `pointer-events: none`:** shader bloqueia clicks no DOM atrás

## Performance targets

- Desktop: 60fps em scenes shader simples
- Mobile médio: 30fps OR fallback estático
- Bundle: Three.js ~150KB gzipped + shader inline ~2KB

## Otimizações

- **Pixel ratio cap:** `dpr={[1, 2]}`
- **Plane geometry simple:** não complexity em geometry
- **Suspend on tab blur:** `useEffect` listening visibility
- **Lazy load:** load Three.js apenas quando viewport relevante

## Browser baseline

WebGL2: Chrome 88+, Safari 14+, Firefox 80+. Universal modernos.

## A11y

- Background com `pointer-events: none` + `aria-hidden="true"`
- Contraste de texto sobre shader testado em frames extremos
- Reduced motion fallback estático
- Save-Data fallback respeitado

## Casos de uso award-grade

### Hero brand premium
Shader background sutil + hero text overlay. Brand recall sem atrapalhar mensagem.

### Section transition
Shader muda cor / pattern entre sections via uniforms scroll-driven.

### Landing fintech / AI
Shader tech-aesthetic (lines, particles) + minimal text foreground.

### Portfolio agency creative
Shader experimental + content sections rolling on top.

## Boundary

- Pilar 4 detalhamento em `references/04-espacial-imersivo.md`
- React adapter em `references/12-react-adapters.md` sec 4
- Persistent canvas em `patterns/persistent-canvas.md`
