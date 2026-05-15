# Orchestrator Recipe (Phase 6)

> Receita v2 (2026-05-04): pos artemis-slides fork. Phase 6 simplificada.
> Carrega na Phase 6.

## Pre-requisito (path config)

```
OPEN_SLIDE_FORK = "C:/Users/Patrick Neuhaus/Documents/Github/open-slide"
ANTI_AI_DS_LOCAL = "C:/Users/Patrick Neuhaus/Documents/Github/anti-ai-design-system"
```

Skill assume:
- Fork artemis-slides clonado em `OPEN_SLIDE_FORK` com mods aplicados (Mod 1+2+3+4+5+6+7)
- Fork buildado: `cd $OPEN_SLIDE_FORK && pnpm install && pnpm build` (uma vez)
- `slides/global.css` populated via `scripts/sync-anti-ai-ds-tokens.sh`

## Steps v2 (4 ao inves de 7)

### 1. Copy template do fork local

```bash
cp -r "$OPEN_SLIDE_FORK/packages/cli/template" "$OUTPUT_DIR/<repo-name>-deck"
cd "$OUTPUT_DIR/<repo-name>-deck"
```

Template ja vem com:
- ✅ AGENTS.md/CLAUDE.md (libera deps motion, header obrigatorio MEDIUM/FUNCAO/REDUCED-MOTION)
- ✅ package.json com framer-motion + dotlottie default
- ✅ slides/exemplo-plus/index.tsx (pattern reusable, deletar opcional)
- ✅ slides/global.css (tokens anti-ai-ds CRM dark baked)
- ✅ Open-slide config + tsconfig

### 2. Wire @open-slide/core local (file: link)

Mods 1+2 (Windows path + optimizeDeps) estao no fork local, NAO em npm registry.
Substituir dep version por file: protocol:

```bash
# Edit package.json:
# "@open-slide/core": "^0.0.6"  ->  "@open-slide/core": "file:$OPEN_SLIDE_FORK/packages/core"
node -e "
  const pkg = require('./package.json');
  pkg.dependencies['@open-slide/core'] = 'file:$OPEN_SLIDE_FORK/packages/core'.replace(/\\\\/g, '/');
  require('fs').writeFileSync('./package.json', JSON.stringify(pkg, null, 2));
"
```

### 3. Install + Rive on-demand

```bash
npm install
```

Se algum slide.medium == 'rive':
```bash
npm install @rive-app/react
```

Rive opt-in (Patrick decision D8). Lottie + framer-motion ja default.

### 4. Escrever slides

Para cada slide do `slide-plan.json`:

1. Criar `slides/<id>/index.tsx`
2. Header obrigatorio (IL2 gate):
   ```tsx
   // MEDIUM: <css | framer-motion | lottie | rive | video>
   // FUNCAO: <causalidade | foco | state change | reveal | reduce-load>
   // REDUCED-MOTION: <fallback descrito>
   ```
3. `import './global.css'` no topo (tokens anti-ai-ds disponiveis)
4. Aplicar pattern do catalogo (`references/04-motion-patterns-catalog.md`)
5. Export `[Page1, Page2, ...] satisfies Page[]`

### 5. Validation handoff (-> Phase 7)

```bash
npm run dev
# Server up em :5173
```

Phase 7 valida via curl + runtime grep (ver SKILL.md Phase 7).

## Cherry-pick upstream (manutencao)

Se quiser pegar feature nova do open-slide upstream:

```bash
cd $OPEN_SLIDE_FORK
git fetch upstream
git log upstream/master --oneline -20
git cherry-pick <commit-hash>
git push origin main  # backup privado
```

Conflitos em arquivos modificados (open-slide-plugin.ts, config.ts, template/) precisam
resolve manual. Skip mudancas que conflitam com Mod 1-7.
