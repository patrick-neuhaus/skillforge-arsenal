# `references/01-funcional-estrutural.md` — Pilar 1: Motion Funcional e Estrutural

> Motion que **paga função em UI**: feedback, causalidade, continuidade. Inclui microinteractions e transições de navegação. É o pilar que melhor cabe em SaaS operacional, dashboards, admin, wizards. Quase tudo aqui mora também em `ui-design-system` (tokens) — esta skill cobre o **catálogo de padrões + decisão técnica**.

## 1. Quando este pilar entra

| Contexto | Aplicabilidade | Severidade se ausente |
|---|---|---|
| SaaS operacional / dashboard / admin | Alta — feedback é obrigatório | Sev 3 (ausência de feedback = H1 violado) |
| Landing institucional | Média — feedback básico em CTAs | Sev 2 |
| Documentação técnica | Baixa — só feedback funcional pontual | Sev 1 |
| Template demonstrativo | Alta — precisa demonstrar estados | Sev 3 |
| Produto visual / brand-heavy | Média — coexiste com pilares 2-4 | Sev 2 |

## 1.5 Craft gate para UI polish

Antes de escolher qualquer padrao funcional, classifique frequencia e origem da acao:

| Caso | Regra |
|---|---|
| 100+ vezes/dia | sem motion ou <=100ms, sem bloquear proxima acao |
| teclado | instantaneo ou quase instantaneo; foco e estado mudam primeiro |
| dezenas/dia | feedback minimo, <=150ms, sem bounce |
| ocasional | motion funcional padrao, 150-250ms |
| raro/brand | delight permitido se nao competir com tarefa |

Perguntas de corte:

- A animacao explica estado, causalidade ou continuidade?
- Se o usuario repetir isso 100 vezes, ainda ajuda?
- O mesmo feedback existe sem motion em `prefers-reduced-motion`?
- O movimento pode ser interrompido sem travar a UI?

## 2. Catálogo de padrões

### 2.1 Microinteractions

Respostas curtíssimas a ação do usuário; precisão, tato, confiança.

| Padrão | Quando | Duração | Easing | Técnica preferida |
|---|---|---|---|---|
| Botão pressed | Clique/toque | 80–120ms | ease-out | CSS `:active` + `transform: scale(0.98)` |
| Toggle on/off | Mudança de estado | 150–200ms | ease-in-out | CSS transition + `:checked` |
| Radio/checkbox tick | Seleção | 120–180ms | ease-out | SVG path stroke-dasharray |
| Chip remove | Tag/filtro removido | 150ms | ease-in | CSS scale+opacity |
| Tooltip aparece | Hover/focus | 120–200ms (delay 300ms) | ease-out | CSS opacity + reduced-motion fallback |
| Input label float | Foco em input | 150ms | ease-out | CSS `:focus-within` + transform |
| Dropdown open | Click trigger | 150–200ms | ease-out | CSS height/opacity OU Motion stagger |
| Card hover lift | Mouse over card | 200ms | ease-out | CSS `transform: translateY(-2px)` + shadow |

**Regra:** microinteraction nunca atrasa tarefa. Se o usuário tem que esperar a animação acabar pra agir, está errado.

Checklist de polish:

- Nao usar `transition: all`; declarar propriedades exatas.
- Nao iniciar entrada de elemento em `scale(0)`; preferir `opacity` + `scale(0.95)` quando scale pagar funcao.
- Evitar `ease-in` em feedback comum; entrada/feedback precisa responder rapido.
- Dropdown/popover abre a partir do trigger; modal abre centrado.
- Hover com movimento usa `@media (hover: hover) and (pointer: fine)`.
- UI interrompivel prefere `transition`/WAAPI cancelavel a `@keyframes` rigido.
- Animar preferencialmente `transform` e `opacity`; medir qualquer animacao de layout.
- Stagger curto e nao bloqueante; se atrasa leitura/acao, cortar.
- Em motion critico, fazer QA em slow motion/frame-by-frame.

### 2.2 Feedback de estado

| Padrão | Quando | Duração | Técnica |
|---|---|---|---|
| Toast de sucesso | Confirmação de ação | Entrada 200ms / saída 150ms / dwell 4–5s | CSS slide+fade ou Motion `<AnimatePresence>` |
| Banner de erro | Erro recuperável | Entrada 200ms / persistente até dismiss | CSS slide-down |
| Skeleton loading | Cargas com estrutura conhecida | Loop infinito 1.5s, shimmer linear | CSS `@keyframes` shimmer + `linear-gradient` |
| Spinner | Operações curtas/indeterminadas | 800–1200ms loop | CSS rotate ou SVG circular indeterminate |
| Progress bar | Operações com progresso conhecido | Linear sync com fetch | CSS width transition ou `<progress>` |
| Pulse on update | Valor mudou | 600ms ease-out (1 ciclo) | CSS scale 1 → 1.05 → 1 |

**Regra:** spinner em delay < 200ms é ruído (Doherty). Use skeleton ou nada.

### 2.3 Page transitions / shared elements

| Padrão | Quando | Duração | Técnica preferida |
|---|---|---|---|
| Cross-fade route | SPA navigation simples | 150–200ms | View Transitions API (`view-transition-name`) |
| Slide route | Mobile-style nav | 250–320ms | View Transitions ou Motion |
| Shared element (card→detail) | Continuidade espacial | 320–480ms | View Transitions com `view-transition-name` no elemento + `@view-transition` |
| Back navigation reverse | Voltar | Mesma duração ida (espelhada) | View Transitions automático |
| Modal in/out | Overlay aparece | Entrada 200ms / saída 150ms | CSS + focus trap + `inert` no fundo |

**Regra:** transição de rota frequente (≤ 3 cliques pra completar tarefa) tem que ser ≤ 200ms. Caso contrário soma fricção.

### 2.4 Listas e tabelas

| Padrão | Quando | Técnica |
|---|---|---|
| FLIP reorder | Sort/filter mudou ordem | FLIP (First-Last-Invert-Play) via Motion ou WAAPI |
| Insert/remove row | CRUD | CSS height transition + opacity (cuidado com layout thrash) |
| Highlight changed cell | Real-time update | CSS background pulse 600ms |
| Loading row | Cell async | Skeleton dentro da célula |

**Regra:** não animar 100% das linhas em sort de tabela com 500+ rows. Custo de paint > benefício de continuidade.

## 3. Decisão técnica

```
Default → CSS transitions/keyframes (90% dos casos)
   ├─ Precisa interpolação programática complexa? → WAAPI
   ├─ Precisa orchestration (stagger, sequence)?  → Motion (Framer Motion)
   ├─ Precisa gestos/drag/spring physics?         → Motion (React) ou GSAP
   ├─ Precisa transição de rota com shared element? → View Transitions API
   └─ Precisa animar SVG path complexo?           → SVG `stroke-dasharray` + WAAPI/Motion
```

**Anti-pattern:** importar GSAP só pra fade de 150ms. Tamanho de bundle > benefício.

## 4. Bom uso vs mau uso (DR-05)

| ✅ Bom | ❌ Mau |
|---|---|
| Confirmar clique com pressed state | Cada clique virar mini show |
| Loading skeleton com estrutura conhecida | Shimmer infinito sem conteúdo chegando |
| Shared element em galeria → detalhe | Shared element entre coisas sem relação visual |
| Toast com role="status" e auto-dismiss | Toast persistente competindo com modal |
| Dropdown 150ms ease-out | Dropdown 600ms com bounce em SaaS |
| Pulse 1 ciclo em valor mudado | Pulse infinito em todo KPI |

## 5. Reduced motion

Pilar inteiro tem que respeitar `prefers-reduced-motion: reduce`:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Mas **fallback inteligente**: feedback de estado (skeleton, error, success) deve **continuar funcionando** sem motion — apenas instantâneo, não removido. Estado de loading sem feedback nenhum = usuário sem orientação.

## 6. Spec template (output do `--spec`)

```
Padrão: <nome>
Pilar: 1 (funcional/estrutural)
Contexto: <onde aparece>
Frequencia de uso: <100+/dia / dezenas/dia / ocasional / raro>
Origem da acao: <teclado / ponteiro / sistema / route-change>
Trigger: <click/hover/route-change/state-change>
Duração: <ms>
Easing: <curve>
Propriedades animadas: <transform/opacity/...>
Reduced motion fallback: <comportamento sem motion>
Técnica: <CSS/WAAPI/Motion/View Transitions>
Browser support: <baseline + fallback>
Critério de aceite:
  - [ ] Duração medida bate spec ±10ms
  - [ ] prefers-reduced-motion testado
  - [ ] Não bloqueia main thread (sem layout thrash)
  - [ ] Foco preservado pós-transição
```

## 7. Boundary com outras skills

- **`ui-design-system`** — define **tokens** de duração/easing (`--motion-fast: 150ms` etc). Esta ref usa esses tokens; não redefine.
- **`ux-audit`** — audita se feedback observável funciona em fluxo real. Findings de "feedback ausente" volta pra cá pra prescrever padrão.
- **`react-patterns`** — implementação React (`useEffect` em animações, refs, focus management). Esta ref dá o spec; React skill aplica.
- **`component-architect`** — anatomia do componente declara quais estados existem (default/hover/loading/etc). Esta ref dá o motion de cada estado.
