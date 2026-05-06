---
name: motion-design
description: "Cataloga, especifica e audita motion/animation design para web e UI polish. Modo --full faz workflow consultivo research-first (Phase 0 discovery → pattern lookup → decision → proposal embasamento teorico → validation gate → spec) com GSAP recipes, foundations gestalt/attention/scroll psych/easing semantics, case studies Awwwards/Codrops/Osmo. Modo --quick (--catalog/--spec/--audit) catalogo direto Wave 7+8 preservado. Decide qual animacao usar, se paga aluguel, gera spec executavel. Cobre microinteractions, button press, page transitions, animated logo, kinetic typography, SVG, Lottie/dotLottie, Rive, parallax, scrollytelling, WebGL/Three.js, Canvas, View Transitions, Scroll-driven Animations, GSAP, Lenis, CustomEase nomeada, easeReverse, Flip.fit consecutive, persistent canvas, registerEffect Custom Elements. Use em: motion design, animation audit, motion spec, GSAP, Awwwards, Codrops, Osmo Supply, scrollytelling, embasamento teorico animacao, que motion faz sentido aqui. NAO use para tokens/easing de sistema (ui-design-system), UX observavel/WCAG (ux-audit), implementacao React/cross-browser/polyfill (react-patterns), anatomia de componente (component-architect)."
---

# Motion Design

**Iron Law 1:** Motion paga aluguel ou sai. Cada animacao justifica funcao observavel (causalidade, foco, mudanca de estado, continuidade espacial, reducao de espera) ou e cortada. Animacao por animacao nao entra.

**Iron Law 2:** Calibragem por contexto. SaaS operacional pede motion funcional contido. Landing/showcase pode expressivo. O mesmo efeito que encanta em hero atrapalha em tabela. Sem calibragem, a recomendacao e generica e gera regressao.

**Iron Law 3:** Reduced motion + a11y sao gates, nao revisao final. Toda animacao declara fallback prefers-reduced-motion. Auto-play, parallax, loops tem pause. Texto kinetic > 5s viola WCAG 2.2.2 sem controle. Sem isso, spec nao esta pronto.

## Modes

| Mode | Quando | Output |
|---|---|---|
| `--full` (NEW Wave 9) | Input rico (URL/Figma/repo/PDF/Notion/briefing). Nao sabe qual padrao escolher. Quer embasamento teorico pra justificar venda. Cliente premium award-grade. | 2 artefatos: spec tecnico embasamento teorico + prompt copy-paste Lovable Agent (opcional) |
| `--quick` (default) / `--catalog` | Sabe pilar/contexto, quer catalogo direto. | Mapa de pilares aplicaveis ao contexto + padroes recomendados |
| `--quick --spec <padrao>` / `--spec` | Sabe padrao especifico, quer spec executavel direto. | Spec canonico (duracao, easing, tecnica, fallback, browser, criterio aceite) |
| `--quick --audit` / `--audit` | Esse motion existente paga aluguel? | Findings tabela `Antes \| Depois \| Por que` por animacao |

**Default sem flag:**
- Input = URL/Figma/repo/PDF/Notion/briefing texto livre → `--full`
- Input = nome de pilar/padrao direto ("microinteraction press", "hero reveal") → `--quick`
- Ambiguo → pergunta usuario qual modo

## Workflow `--full` (NEW Wave 9 — research-first consultivo)

5 fases sequenciais com gates BLOCKING:

```
Phase 0: Discovery (research-first)         REQUIRED
  - 0.1 Detectar input type (URL/Figma/repo/PDF/Notion/briefing)
  - 0.2 Tool primaria (WebFetch/MCP Figma/Glob+Read/Read PDF/Q&A)
  - 0.3 Q&A calibrado por input type (1-5 rodadas)
  - 0.4 Output: session narrative card consolidado
  - GATE: session narrative confirmado pelo usuario antes Phase 1

Phase 1: Pattern lookup                     REQUIRED
  - 1.1 Cruza session narrative contra references/07-session-narratives.md
  - 1.2 Busca candidatos em references/05-gsap-recipes + references/08-case-studies + patterns/
  - 1.3 Aplica scorecard DR-05 (13 criterios escala 0-2)
  - 1.4 Output: top 3 candidatos com match score

Phase 2: Decision                           REQUIRED
  - 2.1 Score >= 22/26 → ENCAIXAR PRONTO
  - 2.2 Score 14-21/26 → MODIFICAR (variantes ajustaveis)
  - 2.3 Score < 14 → CRIAR DO ZERO
  - 2.4 Output: padrao escolhido + justificativa por que nao os outros 2

Phase 3: Proposal embasamento teorico       REQUIRED
  - 3.1 Consulta references/06-theoretical-foundations.md (gestalt + attention + scroll psych + easing semantics)
  - 3.2 Usa template references/11-validation-prompts.md "X porque Y"
  - 3.3 Output: proposta com motivacao + alternativas rejeitadas justificadas

Phase 4: Validation gate                    BLOCKING
  - 4.1 Apresenta proposta Phase 3 ao usuario
  - 4.2 Espera aprovacao explicita ("vai" / "pau na maquina" / "aprovado")
  - 4.3 Estados: Pending / Approved / Rejected (loop Phase 2) / Modified (loop Phase 3) / Clarification
  - GATE: NAO prosseguir Phase 5 sem aprovacao explicita

Phase 5: Spec/Implement                     REQUIRED
  - 5.1 Artefato 1: Spec tecnico embasamento teorico (template em references/11)
  - 5.2 Artefato 2 (opcional): Prompt copy-paste Lovable Agent (formato ~/.claude/rules/prompt-copy-format.md)
  - 5.3 Reduced motion fallback obrigatorio
  - GATE: spec sem fallback = nao pronto (Iron Law 3)
```

**Profundidade Phase 0 calibrada por input type:**

| Input | Tool primaria | Profundidade Q&A | Tempo alvo |
|---|---|---|---|
| URL site publico | WebFetch | 1-2 rodadas | <= 3 min |
| Figma URL/file | MCP Figma `get_design_context` + `get_screenshot` | 2-3 rodadas | <= 8 min |
| GitHub repo / path local | Glob + Grep + Read estrutura | 3-5 rodadas | <= 15 min |
| PDF deck | Read tool nativo (ate 100 paginas) | 2-3 rodadas | <= 8 min |
| Notion/Tome URL | WebFetch publico OR Patrick cola texto | 2-3 rodadas | <= 5 min |
| Briefing texto livre | Q&A iterativo | 3-5 rodadas | <= 10 min |

**Output Phase 5 — Artefato 1 template:**

```
# Motion Spec — <projeto / section>

## Session narrative descoberto (Phase 0)
<resumo 2-3 frases consolidado>

## Decisao (Phase 2)
Padrao: <nome> | Pilar: <1/2/3/4> | Modo: <ENCAIXAR/MODIFICAR/CRIAR>
Source: <reference/pattern path>

## Embasamento teorico (Phase 3)
- <Principio A>: <X porque Y>
- <Principio B>: <X porque Y>
- Easing semantics: <CustomEase> -> <sensacao>
- Anti-pattern evitado: <Z porque atrapalha W>

## Spec tecnico canonical
<template Phase 5 secao "Spec template canonico" abaixo>
```

## Workflow `--quick` (Wave 7+8 preservado)

Modo aliasa `--catalog/--spec/--audit` originais. Pula Phase 0-4 do `--full`. Vai direto Phase 1-6 originais usando references 01-04. Comportamento Wave 7+8 INTACTO.

```
Phase 1: Contexto                           REQUIRED
  1.1 Tipo de produto (operational SaaS / landing / docs / template / brand-heavy / spatial product)
  1.2 Audiencia e dispositivo dominante (desktop / mobile / mix)
  1.3 Fluxo ou tela especifica em foco
  1.4 Restricoes (perf budget, browser matrix, time team, prazo)

Phase 2: Triagem por pilar                  REQUIRED (Iron Law 2)
  2.1 Pilar 1 (funcional/estrutural) cabe? quase sempre sim
  2.2 Pilar 2 (vetorial/branding) cabe? landing/brand sim, SaaS op nao
  2.3 Pilar 3 (narrativo/editorial) cabe? landing/editorial sim, SaaS op nao
  2.4 Pilar 4 (espacial/imersivo) cabe? so se produto e visual/spatial por natureza
  2.5 Decisao: lista de pilares legitimos + pilares descartados com motivo

Phase 2.5: Craft gate                       REQUIRED
  2.5.1 Classificar frequencia de uso: 100+/dia, dezenas/dia, ocasional, raro/brand
  2.5.2 Declarar origem da acao: teclado, ponteiro, scroll, viewport, route-change ou sistema
  2.5.3 Decidir se motion deve ser instantaneo, reduzido, funcional padrao ou delight
  2.5.4 Para --audit, usar tabela `Antes | Depois | Por que`

Phase 3: Catalogo aplicavel
  3.1 Pilar 1 - references/01-funcional-estrutural.md
  3.2 Pilar 2 - references/02-vetorial-branding.md
  3.3 Pilar 3 - references/03-narrativo-editorial.md
  3.4 Pilar 4 - references/04-espacial-imersivo.md

Phase 4: Decisao tecnica
  4.1 Para cada padrao escolhido, decidir tecnica (CSS / WAAPI / Motion / GSAP / Rive / dotLottie / SVG / Canvas / WebGL / View Transitions / Scroll-driven)
  4.2 Validar suporte browser contra alvo declarado (encaminhar a react-patterns se baseline incerto)
  4.3 Estimar custo de bundle + perf

Phase 5: Spec                               BLOCKING (Iron Law 1 + 3)
  5.1 Cada animacao fecha spec canonico
  5.2 Justificativa de funcao observavel (Iron Law 1)
  5.3 Reduced-motion fallback declarado (Iron Law 3)
  GATE: Animacao sem funcao observavel = cortar. Sem fallback = nao esta pronto.

Phase 6: Apresentar                         BLOCKING
  6.1 Output no formato do modo (catalog / spec / audit)
  6.2 GATE: Nao invocar implementacao sem confirmacao. Encaminhar pra react-patterns/component-architect quando aplicavel.
```

## Lookup map (Phase 1 do `--full`)

Skill cruza session narrative card contra esta tabela pra ranking inicial candidatos:

| Tipo de site (Phase 0) | References primarias | Patterns primarios |
|---|---|---|
| sales / landing premium | 03-narrativo-editorial + 02-vetorial-branding + 07-session-narratives + 08-case-studies | hero layered reveal, kinetic headline, scroll narrative, count-up |
| portfolio (designer/agency) | 03-narrativo-editorial + 04-espacial-imersivo + 08-case-studies + 09-osmo-comparable | persistent canvas, R3F hero, scrollytelling, Barba+GSAP |
| saas operacional | 01-funcional-estrutural (DOMINANTE) + 06-theoretical-foundations + 13-microinteractions-canonical (Wave 9.1) | microinteractions, FLIP reorder, skeleton, modal easeReverse, drawer, form-field-label-float, form-validation-feedback, button-press-compress, button-loading-async, toast-sonner, tooltip-floating-ui (Wave 9.1) |
| slide deck (sales/pitch) | 02-vetorial-branding + 03-narrativo-editorial + 07-session-narratives | kinetic headline, section enter stagger, logo reveal |
| brand site (creative) | 02-vetorial-branding (DOMINANTE) + 04-espacial-imersivo + 08-case-studies + 09-osmo-comparable | morphing, character, doodle, blob, R3F hero, kinetic typography |
| editorial / blog / docs | 03-narrativo-editorial (DOMINANTE) + 01-funcional-estrutural | reading progress, parallax leve, hover preview, scroll-driven CSS vars |
| e-comm | 01-funcional-estrutural + 04-espacial-imersivo (3D produto) | configurador 3D, AR try-on, FLIP filter grid, microinteractions cart |

**Stack adapter (todas categorias):**
- React (Lovable/Next/Astro) → references/12-react-adapters.md (useGSAP hook, R3F, SSR caveats)
- Vanilla GSAP → references/05-gsap-recipes.md direto

**DIY vs Comprar Osmo:** consulta references/09-osmo-comparable.md decision tree antes Phase 2.

## Phase 1: Contexto (modo --quick)

Sem contexto, a recomendacao e generica e engana. Pergunte ANTES de propor:

1. Tipo de produto. Operational SaaS, dashboard, admin? Landing institucional? Documentacao? Template demo? Brand-heavy / showcase? Produto visual/spatial (configurador, e-comm de moda, fintech premium)?
2. Audiencia. Profissional B2B em Chrome desktop? Consumer mobile-first? Designer/dev avaliando? Investidor em pitch?
3. Fluxo / tela. Hero da landing? Form de checkout? Dashboard de KPI? Onboarding? Configurador?
4. Restricoes. Perf budget (LCP, INP)? Browser matrix? Mobile pesa quanto? Time tem capacidade pra Three.js? Prazo permite Rive integration?

Se faltar, pergunte. Audit/spec sem contexto do produto = motion fora de calibragem.

## Phase 2: Triagem por pilar (Iron Law 2 — modo --quick)

Tabela de cabimento por contexto:

| Contexto | P1 funcional | P2 branding | P3 narrativo | P4 espacial |
|---|---|---|---|---|
| SaaS operacional / dashboard / admin | obrigatorio | logo splash apenas | nao cabe | nao cabe |
| Landing institucional B2B/B2C | obrigatorio | alta aplicabilidade | hero+scrollytelling cabem | so se produto pede |
| Documentacao tecnica | feedback basico | line/diagram apenas | progress bar apenas | nao cabe |
| Template demonstrativo | obrigatorio (mostrar estados) | se template e brand-heavy | so se template aplica | nao cabe |
| Brand-heavy / creative agency / portfolio | obrigatorio | centro da experiencia | alta aplicabilidade | caso a caso |
| Produto visual / spatial (e-comm fashion, configurador) | obrigatorio | alta aplicabilidade | alta aplicabilidade | pilar core do produto |

Aplique e declare explicitamente:

```
Pilares legitimos pro contexto: P1, P2
Pilares descartados: P3 (nao cabe SaaS operacional), P4 (nao justifica ROI mobile-heavy)
```

Sem essa declaracao, a Phase 3 sai generica.

## Phase 2.5: Craft gate (modo --quick)

Antes de catalogar efeito, decida se a animacao merece existir naquela frequencia de uso:

| Frequencia / origem | Decisao padrao | Motivo |
|---|---|---|
| 100+ vezes/dia | Sem animacao ou instantaneo | Operacao repetitiva amplifica friccao |
| Acao por teclado | Instantaneo ou quase instantaneo | Teclado exige resposta direta; motion nao pode atrasar percepcao |
| Dezenas/dia | Motion minimo, <=150ms | Feedback sim, teatro nao |
| Ocasional | Motion funcional padrao | Pode explicar estado/continuidade |
| Raro, first-time, brand | Delight permitido | Valor de memorabilidade pode pagar o custo |

Pergunte: "Se isso rodar 100 vezes no dia, ainda ajuda?" Se a resposta for nao, reduza ou corte.

Para `--audit`, use:

| Antes | Depois | Por que |
|---|---|---|
| <motion atual> | <ajuste ou corte> | <funcao observavel, frequencia, risco> |

## Phase 3: Catalogo aplicavel (modo --quick)

Carrega reference do(s) pilar(es) selecionado(s). Nao carrega tudo. Cada reference tem: quando entra, padroes com duracao/easing/tecnica, bom uso vs mau uso, decisao tecnica, reduced-motion, spec template, boundary com outras skills.

## Phase 4: Decisao tecnica (modo --quick)

Arvore de decisao simplificada (detalhe nos references):

```
CSS transitions/keyframes  -> 90% dos casos funcionais (default)
WAAPI                       -> interpolacao programatica que CSS nao cobre
Motion (Framer Motion)      -> React + orchestration (stagger, AnimatePresence, useScroll)
GSAP                        -> timeline complexa, ScrollTrigger pesado, gestos
View Transitions API        -> page/route transitions com shared elements
Scroll-driven Animations    -> motion ligado ao scroll, com fallback (baseline incerto)
SVG nativo                  -> line, self-drawing, morph leve, icones - bundle minimo
dotLottie                   -> animacao criada em After Effects/ferramenta visual
Rive                        -> character interativo com state machine
Canvas 2D                   -> particles, shaders 2D leves, image sequences
WebGL / Three.js / R3F      -> 3D real-time, configurador, hero premium
WebXR                       -> AR/VR especifico
```

Validar suporte browser contra a matriz declarada do produto. Se baseline incerto (popover, anchor, scroll-driven em Safari) - encaminhar react-patterns --audit-cross-browser pra confirmar fallback.

**Pra GSAP-specific recipes:** consulta references/05-gsap-recipes.md (Lenis canonical, CustomEase, easeReverse, Flip.fit consecutive, persistent canvas, registerEffect Custom Elements, SplitText, scroll CSS vars, Flip layout, MorphSVG rotational, gsap.quickTo).

**Pra React adapter:** consulta references/12-react-adapters.md (useGSAP hook, gsap.context() cleanup, R3F, Next.js SSR caveats, Lovable Vite specifics, Astro islands).

**Pra micro-interactions canonical UI** (form fields, buttons, toast, drawer, tooltip — Wave 9.1): consulta references/13-microinteractions-canonical.md ANTES de propor easing/duracao genericos. Cobre 18 patterns canonical (Material 3, Radix, Sonner, Vaul, Floating UI) + ANTI-USE Section pra SaaS B2B operacional.

## Phase 5: Spec canonical (gate bloqueante — Iron Law 1 + 3)

Spec template canonico (usado em ambos `--full` Phase 5 e `--quick` Phase 5):

```
Padrao: <nome>
Pilar: <1/2/3/4>
Contexto justificado: <onde aparece + por que cabe>
Funcao observavel (Iron Law 1): <causalidade / foco / state change / continuidade espacial / reducao de espera>
Frequencia de uso: <100+/dia / dezenas/dia / ocasional / raro/brand>
Origem da acao: <teclado / ponteiro / scroll / viewport / route-change / sistema>
Trigger: <click/hover/focus/route-change/viewport-enter/scroll-progress/time>
Duracao: <ms ou loop>
Easing: <curve OR CustomEase nomeada (ex: osmo-ease)>
Propriedades animadas: <transform/opacity/path/...>
Reduced motion fallback (Iron Law 3): <comportamento sem motion - nao remover, snap ou simplificar>
Tecnica: <CSS / WAAPI / Motion / GSAP / SVG / Lottie / Rive / Canvas / WebGL / View Transitions / Scroll-driven>
Stack adapter: <vanilla / useGSAP hook React / R3F / Next.js dynamic import>
Browser baseline + fallback: <X>
Asset (se aplicavel): <tamanho KB>
Criterio de aceite:
  - [ ] Funcao observavel demonstrada
  - [ ] Duracao medida bate spec +-10ms
  - [ ] prefers-reduced-motion testado em 2 browsers
  - [ ] LCP NAO afetado (lazy load se necessario)
  - [ ] 60fps em desktop / 30fps em mobile medio
  - [ ] Foco preservado pos-transicao
  - [ ] axe nao reporta violacao a11y
  - [ ] Cleanup gsap.context() OR useGSAP hook (se React + GSAP)
```

Gate: animacao sem funcao observavel = cortar. Sem fallback reduced-motion = nao pronto.

## Phase 6: Apresentar (gate bloqueante — modo --quick)

Formate output no modo escolhido:

- `--catalog`: lista de pilares aplicaveis + padroes recomendados, sem implementacao ainda
- `--spec`: 1 ou mais specs canonicos, prontos pra react-patterns --scaffold ou component-architect --plan
- `--audit`: tabela `Antes | Depois | Por que` por animacao existente - paga aluguel / atrapalha / encaminhar. Gate: nao implementa. Encaminha.

## Principios

1. Funcao antes de estetica. Animacao primeiro responde "que problema do usuario resolve?" (causalidade, foco, continuidade, espera). Beleza e consequencia, nao meta.
2. Calibragem por contexto. Mesmo padrao muda de status entre operacional, landing e brand-heavy. Sem calibragem, recomendacao e desonesta.
3. Tecnica segue funcao. CSS resolve 90% dos casos. Three.js resolve 5%. Nao use ferramenta cara pra problema barato - bundle mata perf.
4. Reduced-motion e regra. Toda animacao tem fallback. Funcao preserva, motion some.
5. Mobile sempre testado. Desktop animado pode ser mobile travado. Spec inclui dispositivo medio como referencia.
6. A11y e gate. Texto kinetic > 5s sem pause = WCAG 2.2.2. 3+ flashes/s = 2.3.1. WebGL sem keyboard alt = excludente.
7. Bundle importa. Importar GSAP pra fade simples = anti-pattern. Justifique cada lib pesada.
8. Loop infinito = ruido. Se o usuario olha 2 segundos e nao muda nada, e decoracao competindo com tarefa.
9. Teclado e soberano. Acao iniciada por teclado nao depende de animacao para parecer responsiva.
10. Embasamento teorico (modo --full): cada decisao motion declara principio gestalt/attention/scroll/easing aplicavel. Sem isso, vira receita sem alma.
11. Discovery antes proposta (modo --full): Phase 0 lê repo/slide/contexto antes de propor. Sem isso, motion fora de calibragem.
12. Validation gate (modo --full): Phase 4 espera aprovacao explicita antes Phase 5. Sem isso, dilui workflow consultivo.

## Anti-patterns

- Animacao por animacao - sem funcao observavel, vira ruido. Iron Law 1.
- Sair de calibragem - usar regra de landing em SaaS operacional (e vice-versa). Iron Law 2.
- Reduced motion como afterthought - implementar e ver depois. Ja viola na entrega.
- Loop infinito chamativo atras de texto - competicao com leitura. Sempre.
- Spinner em delay < 200ms - Doherty threshold. Skeleton ou nada.
- Toast persistente competindo com modal - atencao quebrada.
- GSAP pra fade simples - ~50KB de bundle pra 3 linhas de CSS.
- Three.js em SaaS B2B - exclusivo ROI raramente justifica.
- Parallax pesado mobile - vestibular trigger (WCAG 2.3.3).
- Kinetic type em corpo de texto - leitura comprometida.
- Animar 100% das linhas em sort de tabela 500+ rows - paint cost > continuidade.
- Implementar antes de spec - sem criterio de aceite, retrabalho garantido.
- `transition: all` - anima propriedades acidentais e cria bugs invisiveis.
- Entrada com `scale(0)` - parece spawn barato; use `scale(0.95)` + opacity quando scale for justificavel.
- `ease-in` em feedback comum - comeca lento justamente quando o usuario espera resposta.
- Popover/dropdown sem origem do trigger - quebra causalidade espacial.
- Hover motion sem media query - vira comportamento fantasma em touch.
- Keyframes em UI interrompivel - preferir transition/WAAPI cancelavel.
- Animar layout quando transform/opacity resolvem - cria jank.
- (--full) Phase 0 longa em input simples - URL + 1 frase basta. Cortar.
- (--full) Aceitar resposta vaga em Phase 0 - "tipo motion premium" nao e session narrative. Pivot pra concreto.
- (--full) Pular Phase 4 validation gate - dilui workflow consultivo, perde anti-IA framing.
- (--full) CustomEase inline em cada call - define 1x global nomeada, referencia por nome.
- (--full) useGSAP esquecido em React - memory leak. SEMPRE usar useGSAP OR ctx.revert().

## Pre-delivery Checklist

**Geral (ambos modos):**
- [ ] Tipo de produto + contexto explicitados
- [ ] Pilares aplicaveis declarados (nao usar todos por default)
- [ ] Cada animacao tem funcao observavel justificada (Iron Law 1)
- [ ] Frequencia de uso + origem da acao declaradas (Craft gate)
- [ ] Calibragem por contexto aplicada (Iron Law 2)
- [ ] Reduced-motion fallback declarado em todo spec (Iron Law 3)
- [ ] Decisao tecnica respeita bundle + suporte browser
- [ ] Mobile testado ou versao simplificada declarada
- [ ] Criterio de aceite por animacao (testavel)
- [ ] Boundaries respeitadas (nao absorveu trabalho de ui-DS / ux-audit / react-patterns / component-architect)
- [ ] Se motion e micro-interaction UI operacional, consultou references/13 ANTES de propor easing/duracao generico (Wave 9.1)

**Modo `--full` adicional:**
- [ ] Phase 0 discovery completou com session narrative confirmado
- [ ] Phase 1 lookup entregou top 3 candidatos com match score
- [ ] Phase 2 decisao declarou modo (encaixar/modificar/criar) + justificativa
- [ ] Phase 3 proposal incluiu embasamento teorico (gestalt + attention + scroll + easing)
- [ ] Phase 3 incluiu alternativas rejeitadas com razao
- [ ] Phase 4 validation gate aprovado explicitamente pelo usuario
- [ ] Phase 5 Artefato 1 (spec) entregue
- [ ] Phase 5 Artefato 2 (prompt Lovable) entregue se solicitado

**Modo `--audit` adicional:**
- [ ] Audit usa `Antes | Depois | Por que`
- [ ] Cada motion existente classificado (paga aluguel / atrapalha / encaminhar)

## When NOT to use

| Situacao | Use em vez disso |
|---|---|
| Definir tokens de duracao/easing como sistema | ui-design-system (motion-as-system mora la) |
| Auditar se motion atrapalha tarefa observavel | ux-audit (Iron Law 1 dele) |
| Implementar React + cross-browser do motion tecnico | react-patterns (useReducedMotion, View Transitions polyfill) |
| Criar componente reutilizavel com motion proprio | component-architect (anatomia) - depois usar esta skill pra spec do motion |
| Criar/auditar adesao a DS externo com motion especifico | design-system-audit |
| Otimizar perf real (Core Web Vitals tecnicos) | react-patterns ou trident --design |
| Bug funcional em animacao (nao toca) | trident |
| Decidir qual ferramenta de design usar (Figma, Spline) | fora de escopo - esta skill cobre web runtime |
| Discovery completo de produto (waves, personas) | product-discovery-prd (esta skill faz discovery LIGHT focado em motion) |

## Integracao

- ui-design-system - tokens de duracao (--motion-fast/normal/slow/decorative) e easing (--ease-state/layout/decorative) moram la. Esta skill consome os tokens, nao redefine. Iron Law 3 do DS (reduced-motion como regra) e gate compartilhado.
- ux-audit - audita motion observavel atrapalhando tarefa em fluxo real. Findings de essa animacao distrai volta pra ca pra prescrever ajuste ou cortar.
- react-patterns - implementacao React: lazy load Three.js/GSAP, useEffect em animacoes, refs, focus management pos-transicao, suporte browser de View Transitions / Scroll-driven, polyfills.
- component-architect - se animacao vira parte de componente reutilizavel, anatomia/props/estados moram la; spec de motion vem desta skill.
- design-system-audit - coverage de motion na auditoria de DS externo (raro overlap).
- maestro - chain Novo produto brand-heavy pode encadear ui-design-system --generate -> motion-design --full -> react-patterns --scaffold (apos handoff de design.json).
- product-discovery-prd - discovery completo de produto. Esta skill faz discovery LIGHT focado em motion (Phase 0 do --full).
- copy - copy decide MENSAGEM, motion decide REVEAL. Phase 0 confirma mensagem-chave, nao redefine.

## Referencias

| Arquivo | Conteudo |
|---|---|
| references/01-funcional-estrutural.md | Pilar 1: microinteractions, feedback, page transitions, shared elements, listas/tabelas. Padroes + duracao + easing + decisao tecnica + spec. |
| references/02-vetorial-branding.md | Pilar 2: line/self-drawing SVG, morphing, animated logos, kinetic typography, character animations, doodle. SVG + dotLottie + Rive como base. |
| references/03-narrativo-editorial.md | Pilar 3: hero entry, scrollytelling, scroll effects, ambient backgrounds, sticky narrative, reading progress. CSS scroll-driven + GSAP + sticky CSS. |
| references/04-espacial-imersivo.md | Pilar 4: WebGL/3D real-time, AR/VR via WebXR, faux 3D, isometric, liquid/glassmorphic. Three.js + R3F + Drei + Spline + CSS 3D transforms. |
| references/05-gsap-recipes.md (Wave 9) | 11 receitas GSAP byte-perfect: Lenis canonical sync, CustomEase nomeada (osmo-ease), easeReverse 2026, Flip.fit consecutive, persistent canvas Barba, registerEffect Custom Elements, SplitText stagger, scroll-driven CSS vars, Flip layout, MorphSVG rotational, gsap.quickTo. |
| references/06-theoretical-foundations.md (Wave 9) | 4 foundations teoricas: Gestalt (continuity/common fate/closure/proximity) + Attention economy (first fold + operational vs decorative + distraction tax) + Scroll psychology (modos skim/read/search/hunt + vestibular WCAG 2.3.3) + Easing semantics (curves transmitem sensacoes + asymmetric easing). |
| references/07-session-narratives.md (Wave 9) | Mapeamento 7 tipos de site (sales/portfolio/saas/slide/brand/editorial/e-comm) x audiencia x acao -> motion language calibrada. Lookup map Phase 1. |
| references/08-case-studies.md (Wave 9) | 40+ case studies: 10 showcases criativos (DR-A) + 30 Awwwards (DR-B) + 24 Codrops tutorials. 5 stack patterns categorizados. 10 lessons learned cross-cutting. |
| references/09-osmo-comparable.md (Wave 9) | Osmo Supply 30+ patterns + DIY vs comprar matrix + custos replicacao + 12 competitors mapeados. Decision tree make vs buy. |
| references/10-discovery-prompts.md (Wave 9) | 12 perguntas Phase 0 calibradas + profundidade por input type + frases pivot quando Q&A travou + validacao Phase 0 -> Phase 1. |
| references/11-validation-prompts.md (Wave 9) | Frases template "X porque Y" prontas pra Phase 3 copy-paste. 30+ frases por foundation (gestalt/attention/scroll/easing/reduced-motion/perf) + frases "nao usaria Z porque W". |
| references/12-react-adapters.md (Wave 9) | useGSAP hook (@gsap/react) + gsap.context() cleanup + R3F + Next.js SSR caveats + Lovable Vite specifics + Astro islands. Adapter layer recipes vanilla -> React. |
| references/13-microinteractions-canonical.md (Wave 9.1) | 18 patterns canonical micro-interactions UI (form fields, buttons, feedback, overlays, interactive). Princípios transversais 8 + decision tree por contexto + ANTI-USE Section SaaS B2B + cross-refs Wave 1 + tabelas easings tecnicas/semanticas + lessons cross-cutting + auto-critica. |
| patterns/lenis-gsap-canonical.md | Pattern: Lenis + GSAP ticker sync canonical |
| patterns/persistent-canvas.md | Pattern: Three.js scene persiste entre rotas Barba |
| patterns/customease-named-curves.md | Pattern: osmo-ease + cinematicSilk + hop + brand variants |
| patterns/flip-fit-consecutive.md | Pattern: Flip.fit() consecutive scrub waypoints |
| patterns/ease-reverse.md | Pattern: GSAP 2026 easeReverse pra modal/drawer |
| patterns/registerEffect-custom-elements.md | Pattern: Telha Clarke registerEffect + Custom Elements |
| patterns/barba-gsap-page-transition.md | Pattern: Barba+GSAP page transitions cinematograficas |
| patterns/scroll-driven-css-vars.md | Pattern: CSS variables driven by GSAP onUpdate scroll |
| patterns/splittext-stagger.md | Pattern: SplitText word/char stagger timeline |
| patterns/three-r3f-hero.md | Pattern: React Three Fiber hero scene |
| patterns/osmo-button-pack.md | Pattern: 8 variants Osmo-style button effects |
| patterns/osmo-text-effects.md | Pattern: 10 variants Osmo-style text effects |
| patterns/shader-noise-bg.md | Pattern: GLSL shader noise background |
| patterns/flip-layout-shift.md | Pattern: Flip layout animation (state shift) |
| patterns/morphsvg-rotational.md | Pattern: MorphSVG rotational mapping |
| patterns/form-field-label-float.md (Wave 9.1) | Pattern: Material floating label canonical (CSS-only via :placeholder-shown), 150ms cubic-bezier(0.2,0,0,1), anti-placeholder-only WCAG 1.3.1. |
| patterns/form-validation-feedback.md (Wave 9.1) | Pattern: 4 sub-patterns consolidated (Shake error / Checkmark draw / Helper text / Error-clear). Shake 400ms 4 oscilacoes, checkmark 400-600ms pathLength, helper 150-200ms ease-out, error-clear 200ms ease-out. |
| patterns/button-press-compress.md (Wave 9.1) | Pattern: scale(0.97) press + cubic-bezier(0.34,1.56,0.64,1) easeOutBack release. CRITICAL gap site-consultoria/JRG Corp. Substitui translateY(-2px)-only anti-pattern. |
| patterns/button-loading-async.md (Wave 9.1) | Pattern: anti-double-submit + width preserve, data-loading toggle + aria-busy + disabled, spinner 600ms linear infinite, reduced motion spin lento (nao eliminar). |
| patterns/toast-sonner-canonical.md (Wave 9.1) | Pattern: Sonner direto canonical (~5KB MIT), mount 400ms ease-out + dismiss 300ms ease-in + stack interruptivel + auto-close 4000ms + swipe velocity. CSS transitions > keyframes (Sonner lesson). |
| patterns/tooltip-floating-ui.md (Wave 9.1) | Pattern: Radix/Floating UI canonical, open delay 700ms warmup + cooldown 0ms, close 100-300ms, fade+translate 4px 120-180ms, edge detection flip+shift. |
