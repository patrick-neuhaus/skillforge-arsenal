# Cross-browser checklist

> Carregado por `react-patterns` na **Phase 5** do workflow. Checklist por categoria. Cada item tem: feature, leitura prática 2026, sintoma típico, fix preferencial. Fonte: DR-04. Não duplica WCAG (mora em `ux-audit`) nem regras visuais (moram em `ui-design-system`).

---

## 1. Browser APIs

| API | Leitura 2026 | Sintoma típico | Fix |
|---|---|---|---|
| **Clipboard read/write avançado** | Exige secure context, transient activation, permissions divergem entre Chrome/Firefox/Safari | "Copiar" falha só em Firefox; paste exige gesto | Feature-detect; fallback para `document.execCommand` ou copy via input selecionado |
| **Storage Access API** | Necessário em embed/SSO/iframe quando third-party cookies são bloqueados | Login some no Safari/Firefox/Edge tracking prevention | Adotar Storage Access; CHIPS/partitioned cookies quando aplicável |
| **Autoplay** | Heurística por browser/OS; muted+gesture é o caminho mais seguro | Vídeo não toca em Safari/Edge | Iniciar muted; tratar falha como caso esperado |
| **Codecs (H.264, AV1, HEVC)** | Depende de browser, SO e hardware | Mídia funciona em um browser, falha em outro | Servir múltiplos formatos via `<source>` |
| **`showPicker()`** | Bem disponível em evergreen recente | OK como enhancement | Feature-detect antes de chamar |
| **`input[type=color]` `alpha`/`colorspace`** | Suporte muito restrito | Alpha não funciona fora de Chrome | Tratar como enhancement; nunca obrigatório |
| **Pointer Events** | Caminho preferido; MDN recomenda sobre Touch Events | Gestos inconsistentes entre mouse/touch/pen | Modelar em Pointer Events |
| **Permissions API** | Comportamento divergente entre engines | "Permissão negada" inesperada | Defensivo: tratar `denied`, `prompt`, `granted` separadamente |

## 2. CSS support

| Feature | Leitura 2026 | Recomendação |
|---|---|---|
| **CSS nesting** | Newly Available 2023+; risco em WebView corporativa antiga | Usar; desconfiar de embed antigo |
| **`:has()`** | Viável em evergreen; cuidado: seletor inteiro falha sem `:is()/:where()` | Usar para enhancement; layout crítico precisa de fallback |
| **Container queries** | Amplamente utilizáveis | Usar; testar componentes em página real |
| **`dvh` / `svh` / `lvh`** | Suporte amplo | Em mobile, preferir `dvh/svh` em vez de `100vh` |
| **`<dialog>`** | Disponível desde 2022 | Preferir para modal real |
| **Popover API** | Baseline 2025; Safari iOS ainda tem histórico de suporte parcial | OK com fallback simples |
| **Anchor positioning** | Sensível; suporte tardio em Firefox/Safari | Tratar como enhancement; tooltip/menu crítico precisa de fallback JS/CSS |
| **Anchor position container queries** | Sem suporte em Firefox/Safari (mar/2026) | Não basear comportamento essencial |
| **`scroll-behavior`, scroll-snap básico** | Suportado | Confiar; UA pode ignorar `scroll-behavior` |
| **Eventos novos de scroll snap** | Limitado | Apenas opcional |
| **`:focus-visible`** | Seguro em evergreen | Padrão no DS |
| **`backdrop-filter`** | Disponível, mas sensível a composição | Testar em múltiplos engines; aceitar diferença visual |
| **`color()` / OKLCH** | Bem mais disponível, mas estética varia | Testar visualmente; fallback hex/rgb |
| **`@supports`** | Suporte universal | Usar como gate de qualquer feature recente |

## 3. Rendering / layout bugs (3 clássicos)

### 3.1 Auto minimum size em flex/grid
**Sintoma:** card/coluna vaza horizontalmente; texto não quebra; painel interno não scrolla.
**Causa:** itens flex/grid não encolhem abaixo do min-content por padrão.
**Fix:** `min-width: 0` (e/ou `min-height: 0`) no item. Reservar gutter se necessário.
**Boundary:** regra preventiva mora em `ui-design-system`. Aqui é diagnóstico.

### 3.2 `position: sticky` em ancestor com overflow
**Sintoma:** sticky não gruda, ou gruda no container errado.
**Causa:** sticky cola no ancestral com mecanismo de rolagem; `overflow: hidden|auto|scroll` em ancestor pode inibir.
**Fix:** remover/realocar overflow no ancestor; `scrollbar-gutter: stable` para evitar jumps.

### 3.3 Stacking context com `transform`/`filter`/`perspective`/`opacity<1`
**Sintoma:** modal atrás do header; tooltip cortado; dropdown preso; `fixed` se comportando como `absolute`.
**Causa:** `transform≠none` cria stacking context **e** containing block para descendentes `absolute`/`fixed`. `z-index` só faz sentido dentro do mesmo stacking context.
**Fix:** remover/realocar o ancestor; usar portal/camada superior; simplificar hierarquia.

## 4. Inputs nativos

| Input | Variação típica | Recomendação |
|---|---|---|
| `date` / `time` / `datetime-local` | UI muda por SO/browser; partial em Safari/Firefox em parte do ecossistema | Manter valor/semântica nativos; wrapper visual quando necessário |
| `color` | Picker varia muito; `alpha`/`colorspace` parciais | Wrapper próprio se brand exige consistência |
| `file` | Picker nativo; mobile vs desktop diferem | Aceitar variação |
| `number` | Spin buttons divergem; locale issues | Considerar `inputmode="decimal"` + parsing manual |

**Princípio:** preservar o valor/semântica nativos; normalizar UX por cima quando necessário.

## 5. Storage / cookies / SSO

- **Third-party cookies** sendo restringidos em Safari (ITP), Firefox (ETP), Edge (tracking prevention).
- **CHIPS / partitioned cookies** quando contexto third-party é necessário.
- **Storage Access API** para SSO embutido em iframe.
- **Reproduzir em janela privada + tracking protection alta** sempre que houver embed/SSO/preferências persistentes.

## 6. Sintomas → suspeita rápida

| Sintoma | Suspeita primeira |
|---|---|
| Tela branca antes de renderizar | build.target / ESM / dynamic import / import.meta / transpilation |
| Modal/tooltip/dropdown atrás de outras camadas | stacking context / transform em ancestor |
| Sticky falha "aleatório" | overflow em ancestor |
| Painel flex/card explode | auto minimum size sem `min-width: 0` |
| Copy/paste falha em browser X | secure context / gesture / permission policy |
| Date/time/color picker some | suporte parcial; dependência de UI nativa |
| SSO/embed perde sessão | third-party cookies / Storage Access |
| Layout mobile corta no rodapé/cabeçalho | `100vh` em vez de `dvh/svh` |
| Menu/tooltip novo só funciona em Blink | popover / anchor positioning / multiple import maps |

## 7. Ferramentas de evidência

- **MDN Browser Compatibility Data (BCD)** — base para suporte por feature.
- **Can I Use** — decisão rápida.
- **wpt.fyi (web-platform-tests)** — confirmar bug de engine / spec.
- **axe-core** — a11y técnica (complemento; canônico em `ux-audit`).
- **Lighthouse** — perf/best practices (complemento).

## 8. Como reproduzir direito

1. Isolar o componente em página mínima.
2. Registrar browser, versão, SO, viewport, DPR, modo de navegação.
3. Capturar console, network, computed styles, screenshot/vídeo.
4. Reduzir até caso mínimo equivalente.
5. Confirmar feature em MDN/Can I Use; suspeita de bug → wpt.fyi.

## 9. Como corrigir sem quebrar o Chrome

Sequência canônica:
1. Manter caminho feliz no engine principal.
2. Aplicar enhancement com `@supports` / feature detection.
3. Alinhar build target.
4. Polyfill **só** se necessário.
5. Evitar UA sniffing (último caso).

**Nunca** patch que regrida o Chrome para "funcionar igual no Safari". Use progressive enhancement.
