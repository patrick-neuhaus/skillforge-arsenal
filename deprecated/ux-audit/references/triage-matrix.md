# `references/triage-matrix.md`

> Matriz de triagem do sintoma → tipo de problema → skill responsável. Consultado a partir da Fase 1 (1.4) do SKILL.md. Iron Law 3: triagem antes de heurística. Sem isso, o audit absorve sintomas que pertencem a outras skills e gera relatório que ninguém executa.

## 1. Como usar

Antes de aplicar Nielsen ou WCAG, classifique o sintoma. Se cabe nesta skill → continue. Se não → encaminhe explicitamente (com nota explicando por quê) e pare.

**Encaminhamento NÃO é falha.** É boundary positiva. Finding órfão (em skill errada) é falha.

## 2. Tabela canônica de triagem

| Sintoma observado | Tipo | Skill responsável | Por quê |
|---|---|---|---|
| Usuário não sabe o que aconteceu após uma ação | UX (feedback / H1) | **`ux-audit`** | Visibilidade do status — heurística pura |
| Fluxo tem N passos quando bastam M | UX (eficiência / H7) | **`ux-audit`** | Análise de tarefa |
| Erro vago, sem orientação acionável | UX (recuperação / H9) + a11y (3.3.3) | **`ux-audit`** | Ambos moram aqui |
| Modal trap, sem voltar/cancelar | UX (controle / H3) | **`ux-audit`** | Liberdade do usuário |
| Cancelar uma assinatura exige 15 passos | Dark pattern (Obstruction) | **`ux-audit`** | Categoria Purdue + DSA/FTC |
| CTA genérico ("Get started") em landing | UX (clareza) | **`ux-audit`** | Calibragem por contexto |
| Densidade alta em SaaS operacional | Não é finding | **`ux-audit`** (calibragem) | Operacional permite densidade |
| Densidade alta em landing | UX (hierarquia / H8) | **`ux-audit`** | Calibragem por contexto |
| Tabela sem sort/filter em SaaS | UX (eficiência) | **`ux-audit`** | Operacional precisa |
| Botão de fechar 16×16 px | a11y (WCAG 2.5.8) | **`ux-audit`** | Target size |
| Foco invisível ao tab | a11y (WCAG 2.4.7) | **`ux-audit`** | Foco visível |
| Contraste 3.5:1 em texto normal | a11y (WCAG 1.4.3) | **`ux-audit`** (audita) + `ui-design-system` (corrige token) | UX detecta, DS corrige |
| Contraste fraco recorrente em vários componentes | DS sistêmico | **`ui-design-system`** | Token errado, não tela errada |
| Spacing inconsistente entre telas | DS sistêmico | **`ui-design-system`** | Falta de tokens de spacing |
| Cor primária mudando entre páginas | DS sistêmico | **`ui-design-system`** | Token de cor não governado |
| Não sei qual cor primária derivar do logo | DS (tokens) | **`ui-design-system --generate`** | Algoritmo de derivação |
| Quero auditar maturidade visual do produto | DS (maturity) | **`ui-design-system --audit`** | Rubrica 3×7 |
| Breakpoints em px puro | DS (responsividade) | **`ui-design-system`** | rem é regra |
| Motion sem reduced-motion | DS (motion-as-system) | **`ui-design-system`** (regra) + `ux-audit` (audita resultado) | Política em DS, observação em UX |
| Animação que distrai da tarefa | UX (motion auditável) | **`ux-audit`** | Atrapalha tarefa observável |
| Componente sem estado loading | Anatomia | **`component-architect`** | Estado faz parte do contrato |
| Modal sem focus trap | Anatomia (a11y interno) | **`component-architect`** | Contrato de a11y do componente |
| Botão precisa de 12 props para configurar | Anatomia (regra dos 7) | **`component-architect`** | Discriminated unions |
| Componente de 800 linhas | Anatomia | **`component-architect`** | Decomposição |
| Variante boolean soup (`isPrimary && !isSecondary`) | Anatomia | **`component-architect`** | Discriminated unions |
| App "funciona em Chrome, quebra em Safari" | Cross-browser | **`react-patterns --audit-cross-browser`** | Build target / feature support |
| Modal atrás do header | Cross-browser (stacking) — diagnóstico | **`react-patterns`** | + regra preventiva em `ui-design-system` |
| Sticky não gruda no Firefox | Cross-browser (rendering) | **`react-patterns`** | Diagnóstico técnico |
| Date picker some no iOS | Cross-browser (input nativo) | **`react-patterns`** | + wrapper visual em `ui-design-system` |
| `useEffect` para fetch de dados | React anti-pattern | **`react-patterns`** | Pattern audit |
| Re-render excessivo | React perf | **`react-patterns`** | Pattern audit |
| `'use client'` na página inteira | React anti-pattern | **`react-patterns`** | Server Components |
| Hydration error | React (hydration) | **`react-patterns`** | Pattern audit |
| Tela branca antes de renderizar em browser X | Cross-browser (build) | **`react-patterns --audit-cross-browser`** | ESM / transpilation / target |
| `useEffect` para state derivado | React anti-pattern | **`react-patterns`** | Pattern audit |
| Bug funcional, API quebrada | Bug | **`trident`** | Code review |
| Code review por qualidade React | Code review | **`trident --design`** | Frontend code review |
| Bug de segurança / injection / XSS | Security | **`security-audit`** | OWASP |
| App não segue shadcn corretamente | Adesão a DS externo | **`design-system-audit`** | Conformidade contra DS declarado |
| App "tem cara de IA" | Adesão a DS interno | **`design-system-audit`** | Default `anti-ai-design-system` |
| Drift de tokens entre app e DS canônico | Adesão a DS externo | **`design-system-audit`** | Delta report |
| Microcopy de erro confusa | UX (copy / H9) | **`ux-audit`** | Afeta entendimento |
| Headline da landing genérico | Marketing copy | **`copy`** + **`ux-audit`** (se afeta tarefa) | Domínio marketing |
| Quero criar pitch deck | Sales | **`sales-enablement`** | Marketing |
| Quero gerar PRD pra produto novo | Discovery | **`product-discovery-prd`** | Pré-build |
| App está lento em produção (não percebido em dev) | Perf técnico | **`react-patterns`** | Bundle / hydration / etc |
| App parece lento (LCP/INP/CLS percebidos) | Perf percebida | **`ux-audit`** (audita) + `react-patterns` (corrige) | Observação em UX, fix em React |

## 3. Critérios de decisão por sintoma ambíguo

Quando dois ou mais tipos parecem aplicáveis:

- **a11y vs DS:** se o problema é o **token** errado (cor, tamanho, contraste sistêmico), é DS. Se é a **tela** específica violando, é UX/a11y.
- **UX vs Anatomia:** se o problema é o **fluxo** (passo perdido, decisão errada, feedback ausente), é UX. Se é o **componente** (estado faltando, contrato a11y mal feito), é arquitetura.
- **UX vs Cross-browser:** se o sintoma só aparece em **um browser** ou tem cheiro de feature/build target, é cross-browser. Se aparece em todos, é UX.
- **DS vs Cross-browser (CSS de composição):** regra preventiva (não usar `transform` em ancestor de modal) mora em `ui-design-system`. Diagnóstico do sintoma ("modal atrás do header") mora em `react-patterns`. Os dois lados convergem.
- **UX vs Code review:** se afeta **experiência observável**, é UX. Se afeta **qualidade do código** sem mudar experiência, é trident.

## 4. Output da triagem

Antes de prosseguir com o audit, registre:

```markdown
## Triagem aplicada

| Sintoma observado | Tipo classificado | Skill responsável | Decisão |
|---|---|---|---|
| [...] | UX | ux-audit | Auditado nas Fases 2–6 |
| [...] | DS sistêmico | ui-design-system | Encaminhado, não auditado aqui |
| [...] | Cross-browser | react-patterns --audit-cross-browser | Encaminhado |
```

A triagem é **gate**: não passe à Fase 2 (fluxos) sem ela registrada.

## 5. Anti-padrões da triagem

- **Auditar tudo como UX** — vira relatório inflado e impreciso.
- **Achar que "encaminhar" é desistir** — encaminhamento é boundary positiva, gera ação na skill correta.
- **Triagem genérica** — "tem coisas de DS aqui" não é triagem. Lista o sintoma específico e a skill destino.
- **Ignorar overlaps legítimos** — alguns sintomas têm 2 donos (ex.: contraste fraco = ux-audit detecta + ui-design-system corrige). Registre os dois.
- **Triagem depois da Fase 6** — não adianta. A triagem orienta o que percorrer e o que ignorar.

## 6. Quando a triagem é mínima

Em audit **focado** numa tela já confirmada como UX (cliente já filtrou o tipo do problema), a triagem pode ser declarativa:

> "Triagem: cliente trouxe fluxo de checkout com fricção observada em usabilidade. Sintomas técnicos (perf, cross-browser) e DS (tokens) não fazem parte deste escopo. Auditando UX puro nas Fases 2–6."

Mesmo nesse caso, **não pula** — declarar a triagem mantém o gate.
