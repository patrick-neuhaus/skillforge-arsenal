# Orchestrator Recipe (Phase 6)

> Receita testada 2026-05-04 (DECISIONS.md ADR "Hands-on validation EXTENDED mode"). Carrega na Phase 6.

## Steps

### 1. Init consumer project

```bash
cd <output-parent-dir>
npx -y @open-slide/cli init <repo-name>-deck
cd <repo-name>-deck
```

Init usa npm (não pnpm) e instala 475 packages em ~47s.

### 2. Aplicar patch Windows path (skip se Linux/Mac)

Bug detectado em `node_modules/@open-slide/core/dist/config-Bxtztw-H.js` linha 1965:

```js
// Original (bug Windows):
const importPath = isDev ? `/@fs${abs}` : abs;

// Fix:
const importPath = isDev ? `/@fs/${abs.replace(/^\//, "")}` : abs;
```

Persistir via patch-package:

```bash
npm install --save-dev patch-package
# Editar arquivo acima
npx patch-package @open-slide/core
# Adiciona "scripts.postinstall": "patch-package" em package.json
```

Resultado: gera `patches/@open-slide+core+<version>.patch`. Sobrevive `npm install`.

### 3. Sobrescrever consumer CLAUDE.md

Template `init` gera `CLAUDE.md` com regra "Do not add dependencies. Use only react and standard web APIs". Substituir por:

```markdown
# open-slide consumer — Agent Guide

Você está autorando slides neste repo.

## Hard rules

- Slides em `slides/<kebab-case-id>/`
- Entry: `slides/<id>/index.tsx`
- Assets em `slides/<id>/assets/`
- NÃO modificar `package.json`, `open-slide.config.ts`, ou outros slides

## Deps pré-instaladas (project-slide-maker bridge)

- `framer-motion` — para slides com medium=framer
- `@lottiefiles/dotlottie-react` — para slides com medium=lottie
- `@rive-app/react` — para slides com medium=rive

Use os imports correspondentes ao medium declarado no header de cada slide.
NÃO adicionar outras deps sem consulta.
```

### 4. Install motion deps (baseado em mediums escolhidos)

Inferir do `slide-plan.json`:

```bash
# Se algum slide.medium == 'framer-motion':
npm install framer-motion

# Se algum slide.medium == 'lottie':
npm install @lottiefiles/dotlottie-react

# Se algum slide.medium == 'rive':
npm install @rive-app/react
```

### 5. Copy tokens anti-ai-ds (Phase 4 output)

Criar `slides/global.css` com vars HSL extraídos do anti-ai-ds:

```css
:root {
  --background: 240 10% 4%;
  --foreground: 0 0% 98%;
  --accent: 240 100% 70%;
  /* ... etc */
}
```

Cada slide importa via `<link>` no Page root ou inline `style={{ background: 'hsl(var(--background))' }}`.

### 6. Escrever slides

Para cada slide do `slide-plan.json`:

1. Criar `slides/<id>/index.tsx`
2. Header obrigatório (IL2 gate):
   ```tsx
   // MEDIUM: <css | framer-motion | lottie | rive | video>
   // FUNÇÃO: <causalidade | foco | state change | continuidade espacial | reducao de espera>
   // REDUCED-MOTION: <fallback descrito>
   ```
3. Importar componentes anti-ai-ds (Phase 4 list)
4. Aplicar pattern do catálogo (`references/04-motion-patterns-catalog.md`)
5. Export default array `[Page1, Page2, ...] satisfies Page[]`

### 7. Validation handoff (→ Phase 7)

```bash
npm run dev
# Server up em :5173 (ou alt)
```

Phase 7 valida via curl:
- `/@id/virtual:open-slide/slides` retorna todos slideIds
- Para cada slide: `/@fs/<abs>/slides/<id>/index.tsx` HTTP 200
- Dev log sem `error|Error|ENOENT|Failed to resolve`
