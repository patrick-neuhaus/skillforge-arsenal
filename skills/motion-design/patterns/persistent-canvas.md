# Pattern: Persistent Three.js canvas (Barba page transitions)

> **Source:** DR-B Codrops + DR-A Hatom Protocol
> **Categoria:** spatial / continuidade rotas
> **Pilar:** 4 (espacial/imersivo)
> **Quando usar:** SPA com Barba.js precisando Three.js scene PERSISTIR entre rotas (configurador, brand site imersivo, portfolio Awwwards-tier).
> **Quando NÃO usar:** Lovable/Next/Astro (router próprio, não Barba). SaaS sem 3D. Site one-page.

---

## Snippet canonical

```js
import barba from '@barba/core';
import * as THREE from 'three';
import { gsap } from 'gsap';

// Canvas FORA do barba container — mounted no body, persiste rota
const canvas = document.createElement('canvas');
canvas.id = 'persistent-canvas';
canvas.style.cssText = 'position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;';
document.body.appendChild(canvas);

const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

// Render loop independente — sobrevive route changes
let frameId;
function animate() {
  frameId = requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
animate();

// Pause em tab blur (perf + bateria)
document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    cancelAnimationFrame(frameId);
  } else {
    animate();
  }
});

// Barba transitions atualizam scene state — não destroem
barba.init({
  transitions: [{
    name: 'fade-3d',
    leave({ current }) {
      gsap.to(camera.position, { z: 8, duration: 0.6, ease: 'osmo-ease' });
      return gsap.to(current.container, { opacity: 0, duration: 0.6 });
    },
    enter({ next }) {
      updateSceneForRoute(next.namespace);
      return gsap.from(next.container, { opacity: 0, duration: 0.6 });
    },
  }],
});

function updateSceneForRoute(namespace) {
  scene.children.forEach(child => scene.remove(child));
  if (namespace === 'home') addHomeMeshes(scene);
  if (namespace === 'about') addAboutMeshes(scene);
}

// Resize handler
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```

## Por quê funciona

- **Continuity espacial entre rotas:** scene 3D = "world" persistente, rotas = "camera shots" diferentes. Sem persistent canvas, cada rota recria scene = boot cost + flash visual.
- **Single source of truth:** scene unificada vs múltiplas instances Three.js per route.
- **Performance:** boot cost 1x (asset load + scene init), depois só transições leves.

## Embasamento teórico

> "Persistent canvas Three.js porque continuity gestalt entre rotas — user percebe world coeso, não páginas isoladas. Brand site imersivo Awwwards-tier exige essa continuidade visual."

## Reduced motion

```js
if (prefersReducedMotion) {
  // Pode manter scene mas:
  // 1. Snap camera positions sem GSAP transitions
  // 2. Desliga auto-rotate / idle animations
  // 3. Render apenas no resize (não 60fps continuous)
}
```

## Anti-pattern

- **Render loop sem visibility pause:** GPU desperdiçada quando tab inativa.
- **Pixel ratio sem cap:** retina displays renderizam 4x pixels = mobile high-DPI < 30fps.
- **Scene rebuild em cada route change:** anula benefício persistent (volta a boot cost).
- **Persistent canvas em saas operational:** GPU overhead sem ROI.

## Performance targets

- Desktop: 60fps em scenes médias (< 100k polygons)
- Mobile médio: 30fps OR fallback estático
- Boot: < 2s pra interactive
- Bundle: Three.js ~150KB gzipped, GLTF compressed Draco/meshopt

## Browser baseline

Chrome 88+, Safari 14+, Firefox 80+. WebGL2 idealmente.

## A11y

- Alternative content: imagem estática + descrição textual sempre disponível
- Reduced motion: desliga auto-rotate, pausa idle animations
- Save-Data: respeita header — fallback estático
- Keyboard equivalent: hotspots clicáveis precisam DOM equivalente

## React adapter

Three.js + Barba não é stack típico React. Pra React + 3D persistente, usar `references/12-react-adapters.md` sec 4 (R3F + Drei).

## Boundary

- Recipe completa em `references/05-gsap-recipes.md` Recipe 5
- Pilar 4 detalhamento em `references/04-espacial-imersivo.md`
