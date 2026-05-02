# Build targets and polyfills (proposed reference)

> Carregado por `react-patterns` na **Phase 5.5**. Quando a app "nem monta" em browser X, suspeite do target antes do componente. Fonte: DR-04.

---

## 1. Princípio

**Se a página nem monta, suspeite do target antes do componente.** Antes de procurar bug em React/CSS, verifique:

- `build.target` (Vite) ou equivalente.
- Browserslist (lido por Autoprefixer, Babel preset-env, SWC, plugin-legacy).
- Plugin de fallback legacy ativo se a matriz inclui browsers fora do alvo moderno.
- Polyfills de runtime apenas se necessários.

## 2. Vite

### 2.1 `build.target`

- Default moderno: `'modules'` (ESM nativo, top-level await opcional, suporte a browsers ~2020+).
- Para alvo mais amplo: especificar lista (`['es2020', 'edge88', 'firefox78', 'chrome87', 'safari14']` ou similar).
- **Atenção:** `build.target` controla apenas a saída. Não traduz "última geração de CSS" automaticamente — Autoprefixer cuida disso via Browserslist.

### 2.2 `@vitejs/plugin-legacy`

- Gera bundle adicional para browsers fora do alvo moderno (ES5).
- Carregado via `<script nomodule>` automaticamente.
- **Necessário se:** matriz declarada inclui browsers que não suportam ESM nativo, dynamic import, ou `import.meta`.
- **Não usar como "rede de proteção" defensiva:** custo de bundle dobrado. Decisão deve ser explícita.

### 2.3 Sintomas que indicam target desalinhado

- "Tela branca em produção antes do app montar" → ESM/dynamic import/optional chaining/nullish.
- "Chunk não carrega" → import map / dynamic import sem fallback.
- "Syntax error em browser X antes do bundle rodar" → target moderno demais para a matriz real.

## 3. Next.js

- Next gerencia transpilation via SWC por padrão.
- Targets vêm de `browserslist` (`package.json` ou `.browserslistrc`) — Next lê.
- **Verificar:** se há `browserslist` declarado e se reflete a matriz real.
- Polyfills automáticos para browsers não-modernos: `core-js`, `fetch` em ambientes antigos.

## 4. Browserslist

- Arquivo `.browserslistrc` ou campo `browserslist` em `package.json`.
- **Lido por:** Autoprefixer, PostCSS preset-env, Babel preset-env, SWC, `@vitejs/plugin-legacy`, Next.js.
- **NÃO é lido por:** `vite.build.target` diretamente.

### 4.1 Configurações comuns

```
# Conservador (alvo amplo)
> 0.5%
last 2 versions
not dead
not IE 11

# Moderno (alvo mais estreito)
last 2 chrome versions
last 2 firefox versions
last 2 safari versions
last 2 edge versions
```

### 4.2 Anti-patterns

- **Browserslist default sem revisão** — herdado do create-react-app/template, não reflete matriz real.
- **Browserslist diverge de `build.target`** — Vite gera moderno, Autoprefixer gera para IE11. Patch errado.
- **Atualizar Browserslist sem rodar `npx update-browserslist-db@latest`** — versões desatualizadas.

## 5. Autoprefixer

- Lê Browserslist; adiciona prefixos vendor.
- Não adiciona polyfills JS — só prefixos CSS.
- **Verificar:** prefixos vendor inúteis em alvo moderno (custo no bundle CSS).

## 6. Babel / SWC

- Babel `preset-env` ou SWC `targets` lê Browserslist (ou aceita override).
- Transpilação JS para a matriz declarada.
- **Verificar:** `corejs` version se `useBuiltIns: 'usage'` (Babel) — versão velha = polyfills incorretos.

## 7. Polyfills

### 7.1 Princípio

Polyfill **só** quando:
1. Feature é usada no código (confirmado).
2. Matriz declarada inclui browser que não suporta (confirmado em MDN BCD).
3. `@supports` ou feature detection não resolve o caso de uso.

### 7.2 Polyfills comuns que valem revisão

| Polyfill | Quando | Risco |
|---|---|---|
| `core-js` | Babel preset-env com `useBuiltIns: 'usage'` | Bundle inflado se mal configurado |
| `regenerator-runtime` | async/await transpilado para ES5 | Necessário se target inclui ES5 |
| `intersection-observer` | IE/Safari antigo | Hoje raramente necessário |
| `resize-observer-polyfill` | Safari antigo | Hoje raramente necessário |
| `whatwg-fetch` | IE | Não necessário em evergreen |
| `smooth-scroll-polyfill` | Safari/iOS antigo | Hoje raramente necessário |

### 7.3 Anti-patterns

- **Polyfill defensivo** — instalar "por garantia" sem confirmar matriz.
- **Polyfill no client em vez de no build** — custo runtime desnecessário.
- **`@vitejs/plugin-legacy` + polyfills explícitos** — duplicação.

## 8. Checklist de Phase 5.5

- [ ] `vite.config.*` `build.target` ou Next.js config — declarado e revisado?
- [ ] Browserslist declarado, atualizado (`update-browserslist-db`) e coerente com matriz real?
- [ ] `@vitejs/plugin-legacy` ativado **se e somente se** matriz inclui browsers fora do alvo moderno?
- [ ] Babel/SWC targets lendo Browserslist ou explícitos?
- [ ] Autoprefixer lendo Browserslist? Prefixos vendor não inflando além do necessário?
- [ ] Polyfills explícitos justificados (feature usada + browser na matriz não suporta)?
- [ ] `core-js` na versão correta se `useBuiltIns: 'usage'`?
- [ ] Build moderno + legacy testados em pelo menos 1 browser de cada categoria?

## 9. Quando suspeitar de target

| Sintoma | Causa provável |
|---|---|
| Tela branca antes do app montar | ESM/dynamic import/`import.meta` em browser sem suporte |
| Syntax error de `??` ou `?.` no console | Optional chaining/nullish sem transpile |
| `Cannot read property 'X' of undefined` em runtime | Polyfill ausente para feature usada |
| CSS sem prefixo em browser antigo | Autoprefixer/Browserslist desalinhado |
| Bundle moderno servido para IE11 | Plugin-legacy ausente |
| Bundle inflado em alvo moderno | Polyfills/prefixos para alvo amplo desnecessários |

## 10. Boundary

- **Não definimos** Browserslist do projeto — cabe ao time/usuário.
- **Recomendamos** matriz coerente com a política de produto.
- **Não substituímos** `ui-design-system` em decisões de feature CSS — aqui é só suporte/baseline; uso mora lá.
