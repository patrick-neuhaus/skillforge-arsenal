---
name: motion-design
description: "Cataloga, especifica e audita motion (animacoes) na web seguindo 4 pilares: funcional/estrutural (microinteractions, page transitions, feedback), vetorial/branding (logos animados, kinetic typography, character, doodle, line/morph SVG), narrativo/editorial (scrollytelling, hero entry, parallax, ambient backgrounds, sticky narrative), espacial/imersivo (WebGL/3D, AR/VR via WebXR, faux 3D, isometric, liquid/glassmorphic). Decide entre tecnicas: CSS transitions, WAAPI, Motion (Framer Motion), GSAP, Rive, dotLottie, SVG, Canvas, WebGL/Three.js, View Transitions API, Scroll-driven Animations. Calibra severidade por contexto: SaaS operacional pede motion funcional contido; landing/showcase/brand-heavy pode expressivo; documentacao tecnica e minimo. Use SEMPRE em: qual animacao usar pra X, que motion cabe nesse hero, avaliar se a animacao paga aluguel, escolher entre Lottie ou Rive, spec de motion pra implementar, animacao ta atrapalhando, queremos algo mais animado, parallax/scrollytelling/3D no site, logo animado, kinetic type, page transition entre rotas, configurador 3D de produto, AR try-on, motion design, animation design, motion specification, motion audit. NAO use para: tokens de duracao/easing como sistema (ui-design-system e dono), auditoria observavel de motion atrapalhando tarefa (ux-audit), implementacao tecnica React/cross-browser/polyfill (react-patterns), anatomia de componente animado (component-architect). Foco: catalogo + decisao criativa + escolha tecnica + spec executavel."
---

# Motion Design

**Iron Law 1:** Motion paga aluguel ou sai. Cada animacao justifica funcao observavel (causalidade, foco, mudanca de estado, continuidade espacial, reducao de espera) ou e cortada. Animacao por animacao nao entra.

**Iron Law 2:** Calibragem por contexto. SaaS operacional pede motion funcional contido. Landing/showcase pode expressivo. O mesmo efeito que encanta em hero atrapalha em tabela. Sem calibragem, a recomendacao e generica e gera regressao.

**Iron Law 3:** Reduced motion + a11y sao gates, nao revisao final. Toda animacao declara fallback prefers-reduced-motion. Auto-play, parallax, loops tem pause. Texto kinetic > 5s viola WCAG 2.2.2 sem controle. Sem isso, spec nao esta pronto.

## Modes

| Mode | Quando | Output |
|---|---|---|
| --catalog (default) | Quais animacoes cabem nesse projeto? | Mapa de pilares aplicaveis ao contexto + padroes recomendados |
| --spec | Como implementar essa animacao especifica? | Spec executavel (duracao, easing, tecnica, fallback, browser, criterio de aceite) |
| --audit | Esse motion existente paga aluguel? | Findings por animacao (cabe / atrapalha / encaminhar) com severidade |

## Workflow

- Phase 1: Contexto REQUIRED
  - 1.1 Tipo de produto (operational SaaS / landing / docs / template / brand-heavy / spatial product)
  - 1.2 Audiencia e dispositivo dominante (desktop / mobile / mix)
  - 1.3 Fluxo ou tela especifica em foco
  - 1.4 Restricoes (perf budget, browser matrix, time team, prazo)
- Phase 2: Triagem por pilar REQUIRED (Iron Law 2)
  - 2.1 Pilar 1 (funcional/estrutural) cabe? quase sempre sim
  - 2.2 Pilar 2 (vetorial/branding) cabe? landing/brand sim, SaaS op nao
  - 2.3 Pilar 3 (narrativo/editorial) cabe? landing/editorial sim, SaaS op nao
  - 2.4 Pilar 4 (espacial/imersivo) cabe? so se produto e visual/spatial por natureza
  - 2.5 Decisao: lista de pilares legitimos + pilares descartados com motivo
- Phase 3: Catalogo aplicavel - Load reference do(s) pilar(es) selecionado(s)
  - 3.1 Pilar 1 - references/01-funcional-estrutural.md
  - 3.2 Pilar 2 - references/02-vetorial-branding.md
  - 3.3 Pilar 3 - references/03-narrativo-editorial.md
  - 3.4 Pilar 4 - references/04-espacial-imersivo.md
- Phase 4: Decisao tecnica
  - 4.1 Para cada padrao escolhido, decidir tecnica (CSS / WAAPI / Motion / GSAP / Rive / dotLottie / SVG / Canvas / WebGL / View Transitions / Scroll-driven)
  - 4.2 Validar suporte browser contra alvo declarado (encaminhar a react-patterns se baseline incerto)
  - 4.3 Estimar custo de bundle + perf
- Phase 5: Spec BLOCKING (Iron Law 1 + 3)
  - 5.1 Cada animacao fecha spec: padrao + pilar + trigger + duracao + easing + tecnica + fallback reduced-motion + browser + criterio de aceite
  - 5.2 Justificativa de funcao observavel (Iron Law 1)
  - 5.3 Reduced-motion fallback declarado (Iron Law 3)
  - GATE: Animacao sem funcao observavel = cortar. Sem fallback = nao esta pronto.
- Phase 6: Apresentar BLOCKING
  - 6.1 Output no formato do modo (catalog / spec / audit)
  - 6.2 GATE: Nao invocar implementacao sem confirmacao. Encaminhar pra react-patterns/component-architect quando aplicavel.

## Phase 1: Contexto

Sem contexto, a recomendacao e generica e engana. Pergunte ANTES de propor:

1. Tipo de produto. Operational SaaS, dashboard, admin? Landing institucional? Documentacao? Template demo? Brand-heavy / showcase? Produto visual/spatial (configurador, e-comm de moda, fintech premium)?
2. Audiencia. Profissional B2B em Chrome desktop? Consumer mobile-first? Designer/dev avaliando? Investidor em pitch?
3. Fluxo / tela. Hero da landing? Form de checkout? Dashboard de KPI? Onboarding? Configurador?
4. Restricoes. Perf budget (LCP, INP)? Browser matrix? Mobile pesa quanto? Time tem capacidade pra Three.js? Prazo permite Rive integration?

Se faltar, pergunte. Audit/spec sem contexto do produto = motion fora de calibragem.

## Phase 2: Triagem por pilar (Iron Law 2)

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

## Phase 3: Catalogo aplicavel

Carrega reference do(s) pilar(es) selecionado(s). Nao carrega tudo. Cada reference tem: quando entra, padroes com duracao/easing/tecnica, bom uso vs mau uso, decisao tecnica, reduced-motion, spec template, boundary com outras skills.

## Phase 4: Decisao tecnica

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

## Phase 5: Spec (gate bloqueante)

Spec template canonico:

```
Padrao: <nome>
Pilar: <1/2/3/4>
Contexto justificado: <onde aparece + por que cabe>
Funcao observavel (Iron Law 1): <causalidade / foco / state change / continuidade espacial / reducao de espera>
Trigger: <click/hover/focus/route-change/viewport-enter/scroll-progress/time>
Duracao: <ms ou loop>
Easing: <curve>
Propriedades animadas: <transform/opacity/path/...>
Reduced motion fallback (Iron Law 3): <comportamento sem motion - nao remover, snap ou simplificar>
Tecnica: <CSS / WAAPI / Motion / GSAP / SVG / Lottie / Rive / Canvas / WebGL / View Transitions / Scroll-driven>
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
```

Gate: animacao sem funcao observavel = cortar. Sem fallback reduced-motion = nao pronto.

## Phase 6: Apresentar (gate bloqueante)

Formate output no modo escolhido:

- --catalog: lista de pilares aplicaveis + padroes recomendados, sem implementacao ainda
- --spec: 1 ou mais specs canonicos, prontos pra react-patterns --scaffold ou component-architect --plan
- --audit: findings por animacao existente - paga aluguel / atrapalha / encaminhar

Gate: nao implementa. Encaminha.

## Principios

1. Funcao antes de estetica. Animacao primeiro responde "que problema do usuario resolve?" (causalidade, foco, continuidade, espera). Beleza e consequencia, nao meta.
2. Calibragem por contexto. Mesmo padrao muda de status entre operacional, landing e brand-heavy. Sem calibragem, recomendacao e desonesta.
3. Tecnica segue funcao. CSS resolve 90% dos casos. Three.js resolve 5%. Nao use ferramenta cara pra problema barato - bundle mata perf.
4. Reduced-motion e regra. Toda animacao tem fallback. Funcao preserva, motion some.
5. Mobile sempre testado. Desktop animado pode ser mobile travado. Spec inclui dispositivo medio como referencia.
6. A11y e gate. Texto kinetic > 5s sem pause = WCAG 2.2.2. 3+ flashes/s = 2.3.1. WebGL sem keyboard alt = excludente.
7. Bundle importa. Importar GSAP pra fade simples = anti-pattern. Justifique cada lib pesada.
8. Loop infinito = ruido. Se o usuario olha 2 segundos e nao muda nada, e decoracao competindo com tarefa.

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

## Pre-delivery Checklist

- [ ] Tipo de produto + contexto explicitados (Phase 1)
- [ ] Pilares aplicaveis declarados (Phase 2 - nao usar todos por default)
- [ ] Cada animacao tem funcao observavel justificada (Iron Law 1)
- [ ] Calibragem por contexto aplicada (Iron Law 2)
- [ ] Reduced-motion fallback declarado em todo spec (Iron Law 3)
- [ ] Decisao tecnica respeita bundle + suporte browser
- [ ] Mobile testado ou versao simplificada declarada
- [ ] Criterio de aceite por animacao (testavel)
- [ ] Boundaries respeitadas (nao absorveu trabalho de ui-DS / ux-audit / react-patterns / component-architect)

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

## Integracao

- ui-design-system - tokens de duracao (--motion-fast/normal/slow/decorative) e easing (--ease-state/layout/decorative) moram la. Esta skill consome os tokens, nao redefine. Iron Law 3 do DS (reduced-motion como regra) e gate compartilhado.
- ux-audit - audita motion observavel atrapalhando tarefa em fluxo real. Findings de essa animacao distrai volta pra ca pra prescrever ajuste ou cortar.
- react-patterns - implementacao React: lazy load Three.js/GSAP, useEffect em animacoes, refs, focus management pos-transicao, suporte browser de View Transitions / Scroll-driven, polyfills.
- component-architect - se animacao vira parte de componente reutilizavel, anatomia/props/estados moram la; spec de motion vem desta skill.
- design-system-audit - coverage de motion na auditoria de DS externo (raro overlap).
- maestro - chain Novo produto brand-heavy pode encadear ui-design-system --generate -> motion-design --catalog -> react-patterns --scaffold (apos handoff de design.json).

## Referencias

| Arquivo | Conteudo |
|---|---|
| references/01-funcional-estrutural.md | Pilar 1: microinteractions, feedback, page transitions, shared elements, listas/tabelas. Padroes + duracao + easing + decisao tecnica + spec. |
| references/02-vetorial-branding.md | Pilar 2: line/self-drawing SVG, morphing, animated logos, kinetic typography, character animations, doodle. SVG + dotLottie + Rive como base. |
| references/03-narrativo-editorial.md | Pilar 3: hero entry, scrollytelling, scroll effects, ambient backgrounds, sticky narrative, reading progress. CSS scroll-driven + GSAP + sticky CSS. |
| references/04-espacial-imersivo.md | Pilar 4: WebGL/3D real-time, AR/VR via WebXR, faux 3D, isometric, liquid/glassmorphic. Three.js + R3F + Drei + Spline + CSS 3D transforms. |