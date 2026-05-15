---
name: ux-audit
description: "Audita, revisa, analisa, avalia e melhora UX em apps web/mobile. Antes de auditar, faz triagem (UX vs UI vs a11y vs DS vs component arch vs copy vs perf percebida) para confirmar que o problema cabe nesta skill. Identifica problemas de usabilidade com evidência observável, valida WCAG 2.2 AA como baseline, percorre fluxos reais ponta a ponta, classifica severidade Nielsen 0–4, gera recomendações com critério de aceite. Use SEMPRE em: UX, usabilidade, audit, auditoria, 'revisa a UX', 'olha a interface', 'feedback de UX', 'melhorar a experiência', 'usuário tá perdido', 'tá difícil de usar', heurísticas, Nielsen, 'fluxo tá ruim', evaluate usability, assess accessibility, redesign flow, validate WCAG, analyze user flow, cognitive walkthrough. NÃO use para: definir tokens/breakpoints/escala visual (ui-design-system), anatomia/slots/variants/estados de componente (component-architect), code review de frontend (trident --design), adesão a DS externo (design-system-audit), bugs funcionais (trident), cross-browser (react-patterns). Foco: EXPERIÊNCIA observável em fluxo real, não código nem visual isolado."
---

# UX Audit v4

**Iron Law:** Nunca entregue um audit sem percorrer o fluxo real do usuário passo a passo. Screenshots sozinhos escondem problemas de interação.

**Iron Law 2:** Todo finding fecha o ciclo: evidência observável → princípio violado → impacto no usuário → severidade → recomendação → **critério de aceite**. Finding sem critério de aceite não está pronto para entrega.

**Iron Law 3:** Antes de auditar, triar. Se o sintoma é UI puro, a11y puro, sistêmico de DS, anatomia de componente, copy ou perf técnica — encaminhe para a skill correta com nota. Auditar fora do escopo gera relatório que ninguém executa.

## Modos

| Modo | Quando usar | Escopo |
|------|-------------|--------|
| **Completo** | Revisão geral do produto | Triagem + heurísticas + fluxos + WCAG + estados + dark patterns + perf percebida + mobile + IA |
| **Focado** | Tela ou fluxo específico | Triagem + heurísticas relevantes + WCAG aplicável + estados |
| **Cognitive Walkthrough** | Learnability para novos usuários | Perfil + tarefas + 4 perguntas por passo |

## Workflow

```
UX Audit Progress:

- [ ] Fase 1: Contexto e triagem ⚠️ REQUIRED
  - [ ] 1.1 Identificar usuário-alvo (persona, nível técnico, frequência, dispositivo)
  - [ ] 1.2 Identificar objetivo principal do produto e tipo (operacional / landing / documentação / template)
  - [ ] 1.3 Identificar plataforma (web desktop, mobile, responsivo, nativo)
  - [ ] 1.4 Triagem do sintoma → Load references/triage-matrix.md
        → Se for UI puro / DS / component arch / cross-browser / code: encaminhar e parar
- [ ] Fase 2: Caminhar pelos fluxos ⚠️ REQUIRED (Iron Law 1)
  - [ ] 2.1 Listar 3–5 fluxos críticos
  - [ ] 2.2 Percorrer cada fluxo passo a passo: entrada, preenchimento, sucesso, erro, vazio, retorno
  - [ ] 2.3 Documentar fricções, bloqueios, acertos e edge cases
- [ ] Fase 3: Varredura heurística → Load references/ux-foundations.md
  - [ ] 3.1 Aplicar 10 Heurísticas de Nielsen
  - [ ] 3.2 Diagnosticar causa raiz com Princípios de Norman + Laws of UX
  - [ ] 3.3 Calibrar por contexto (operacional ≠ landing ≠ docs)
- [ ] Fase 4: Acessibilidade WCAG 2.2 AA → Load references/wcag-ux-checklist.md
  - [ ] 4.1 Contraste, foco visível, teclado, target size, labels
  - [ ] 4.2 Reflow 320 CSS px, zoom 200%/400%, status messages, error suggestion
  - [ ] 4.3 Reduced motion, focus order, content on hover, redundant entry, consistent help
- [ ] Fase 5: Verificações complementares
  - [ ] 5.1 Inventário de estados (default/hover/focus/pressed/disabled/loading/error/empty/success)
  - [ ] 5.2 Dark patterns (Purdue 7 categorias)
  - [ ] 5.3 Performance percebida (LCP/INP/CLS como percepção observável)
  - [ ] 5.4 UX de IA (se aplicável)
  - [ ] 5.5 Mobile ergonomics (se aplicável)
- [ ] Fase 6: Síntese ⛔ BLOCKING → Load references/ux-severity-rubric.md
  - [ ] 6.1 Classificar cada finding na escala Nielsen 0–4
  - [ ] 6.2 Cada finding tem: evidência + princípio + impacto + severidade + recomendação + critério de aceite
  - [ ] 6.3 Aplicar rubrica scored de 14 categorias (opcional, recomendado em audit completo)
  - [ ] 6.4 Listar o que está funcionando bem
  - [ ] ⛔ GATE: Todo finding tem critério de aceite testável?
  - [ ] ⛔ GATE: Cada fluxo crítico foi percorrido ponta a ponta?
  - [ ] ⛔ GATE: Findings que pertencem a outras skills foram encaminhados, não absorvidos?
- [ ] Fase 7: Apresentar ⛔ BLOCKING → Load references/audit-output-template.md
  - [ ] 7.1 Formatar output no template do modo escolhido
  - [ ] ⛔ GATE: Apresentar ao usuário — não implementar sem confirmação explícita
```

## Princípios

1. **Imparcialidade total.** Ignore quem construiu. Foque em quem usa.
2. **Evidência > opinião.** Toda crítica cita princípio violado. "Tá ruim" não serve.
3. **Severidade governa prioridade.** Escala Nielsen 0–4 em todo finding.
4. **Critério de aceite fecha o loop.** Sem ele, recomendação não é executável.
5. **Triagem antes de heurística.** Decida o tipo de problema antes de aplicar Nielsen.
6. **Calibragem por contexto.** Operacional, landing, docs e template têm regras diferentes.
7. **Se tá bom, diga que tá bom.** Não force crítica onde não existe.
8. **Acessibilidade não é opcional.** WCAG 2.2 AA é baseline, não capítulo.
9. **Acionável > teórico.** Cada finding vira tarefa. Cada tarefa tem critério de aceite.
10. **Boundary positiva.** Encaminhe para a skill certa quando o sintoma sair do escopo.

## Fase 1: Contexto e triagem

### Contexto (sempre)

1. **Quem é o usuário?** Persona, nível técnico, frequência, dispositivo dominante.
2. **Qual o objetivo principal do produto?** Tarefa central que o usuário vem fazer.
3. **Qual o tipo de produto?** Operacional (SaaS, dashboard, admin) / landing institucional / documentação técnica / template demonstrativo. Cada um tem rubrica diferente em `ux-foundations.md`.
4. **Qual a plataforma?** Web desktop, web mobile, responsivo, nativo.
5. **Existe onboarding?** First-time vs uso recorrente.
6. **Tem features de IA?** Chatbot, geração, agentes, recomendação.

Se faltar contexto, **pergunte**. Audit sem contexto é diagnóstico sem sintomas.

### Triagem (sempre)

Antes de aplicar heurística, classifique o sintoma usando `references/triage-matrix.md`. Se cair fora do escopo desta skill, **encaminhe e pare** (com nota explicando por quê).

| Sintoma cabe em | Skill |
|---|---|
| Fluxo, learnability, fricção, erro recuperável, feedback de tarefa, dark pattern | **`ux-audit`** (continue) |
| Token, escala visual, breakpoint, primitiva CSS, motion como sistema | `ui-design-system` |
| Anatomia, slots, variants, props, contrato de a11y do componente | `component-architect` |
| Adesão de app a DS externo específico | `design-system-audit` |
| Code review de frontend, qualidade de implementação React | `trident --design` |
| Bug cross-browser, build target, polyfill | `react-patterns` |
| Bug funcional, API quebrada | `trident` |

## Fase 2: Caminhar pelos fluxos (Iron Law 1)

Antes de listar findings, percorra os fluxos ponta a ponta:

1. **Liste 3–5 fluxos críticos** (ex: "criar conta → configurar → exportar").
2. **Percorra cada fluxo** como o usuário-alvo, passo a passo. Não pule estados.
3. **Para cada fluxo, audite:**
   - É completável sem ajuda externa?
   - Quantos passos tem? Pode ser reduzido sem perder controle?
   - Cada etapa tem feedback (visibilidade do status do sistema)?
   - Tem saída de emergência (voltar, cancelar, desfazer, salvar rascunho)?
   - O que acontece em estado vazio? E quando dá erro? E em loading lento?
   - Dados são preservados em volta?
4. **Veredicto por fluxo:** ✅ Fluido | ⚠️ Tem fricção | ❌ Quebrado.

## Fase 3: Varredura heurística

Load `references/ux-foundations.md` — heurísticas Nielsen, princípios Norman, Laws of UX, calibragem por contexto, dark patterns, mobile ergonomics, perf percebida.

Para cada heurística: **Passa?** → cite o acerto. **Viola?** → registre finding com evidência observável + severidade.

Use Norman + Laws of UX como ferramenta de **diagnóstico de causa raiz** dentro do finding. Não crie seção separada.

## Fase 4: Acessibilidade (WCAG 2.2 AA)

Load `references/wcag-ux-checklist.md`. WCAG 2.2 AA é **baseline**, não capítulo separado. Se a tela falha no básico, isso entra antes da discussão estética.

Foco mínimo: contraste (1.4.3), contraste não-texto (1.4.11), foco visível (2.4.7), teclado (2.1.1), target size (2.5.8), labels (1.3.1), reflow (1.4.10), status messages (4.1.3), error suggestion (3.3.3), focus order (2.4.3), reduced motion (2.3.3), dragging alternatives (2.5.7), accessible auth (3.3.8), redundant entry (3.3.7), consistent help (3.2.6), focus not obscured (2.4.11).

Notas:
- **axe e Lighthouse pegam ~30–40% dos problemas de a11y**; teste manual com teclado e screen reader é obrigatório para baseline AA.
- **Zoom 200% e 400%** e reflow em **320 CSS px** são teste de viewport — referência cruzada com `ui-design-system` (matriz de QA visual).

## Fase 5: Verificações complementares

### 5.1 Inventário de estados

Para cada componente interativo no fluxo crítico, verifique se default, hover, focus, pressed, selected, disabled, loading, error, success, empty fazem o que deveriam. Estados ausentes ou inconsistentes são finding (severidade conforme bloqueio de tarefa). Se o estado não existe **no componente**, encaminhe para `component-architect`.

### 5.2 Dark patterns

Aplicar 7 categorias Purdue (`ux-foundations.md`): nagging, obstruction, sneaking, interface interference, forced action, confirmshaming, roach motel. Em jurisdições com DSA/CPRA, é finding de severidade alta independente de impacto observável.

### 5.3 Performance percebida

LCP/INP/CLS como **percepção observável** ("a página parece travar ao salvar"), não medição. Se o problema é técnico (servidor lento, JS bundle grande), encaminhe para frontend/`react-patterns`.

### 5.4 UX de IA (se aplicável)

Transparência (sabe que é IA?), confiança (cita fontes? mostra incerteza?), loading (streaming? skeleton? progresso?), controle (override? feedback? human-in-the-loop?), error handling.

### 5.5 Mobile ergonomics (se aplicável)

CTAs na thumb zone, bottom nav vs top menu, targets ≥44×44px (WCAG pede 24, 44 é melhor para touch), gestos com alternativa em botão.

## Fase 6: Síntese (gate bloqueante)

Load `references/ux-severity-rubric.md`. Cada finding tem ciclo fechado:

```
Evidência: [fato verificável na interface]
Princípio: [heurística Nielsen / princípio Norman / Law of UX / WCAG]
Impacto: [consequência prática na tarefa do usuário]
Severidade: [Nielsen 0–4]
Recomendação: [mudança concreta — comportamento / estrutura / estado / copy / layout]
Critério de aceite: [como QA/design/dev valida que corrigiu]
```

Em audit completo, opcionalmente rode a **rubrica scored de 14 categorias** (`ux-severity-rubric.md`) para gerar score comparável.

⛔ Gate: nenhum finding sem critério de aceite. Nenhum fluxo crítico não percorrido. Nenhum sintoma fora do escopo absorvido como UX.

## Fase 7: Apresentar (gate bloqueante)

Load `references/audit-output-template.md`. Formate no template do modo escolhido (Completo / Focado / Cognitive Walkthrough). Inclua sempre seção "o que está funcionando bem".

⛔ Gate: nunca implemente sem escolha explícita do usuário.

## Anti-patterns

- **Auditar sem triagem** — gera findings que pertencem a outras skills.
- **Auditar sem contexto** — sem persona/tarefa, todo finding é questionável.
- **Pular fluxos e ir direto pra heurística** — viola Iron Law 1.
- **Finding sem critério de aceite** — viola Iron Law 2.
- **Forçar problema onde não existe** — infla report, mata credibilidade.
- **Linguagem vaga** — "mais moderno", "mais clean", "mais premium" não é audit.
- **Ignorar acessibilidade** — WCAG 2.2 AA é baseline, não opção.
- **Confundir UI com UX** — "botão feio" (UI) ≠ "botão não comunica clicabilidade" (UX).
- **Confundir achado pontual com sistêmico** — se aparece em várias telas, é DS, não tela.
- **Ignorar o que funciona bem** — relatório só negativo perde a confiança do time.
- **Audit que não calibra por contexto** — densidade de operacional ≠ landing.
- **Audit que ignora estados** — só revisa o "estado bonito".
- **Implementar sem confirmação** — viola gate de Fase 7.

## Pre-delivery checklist

- [ ] Triagem feita: o sintoma cabe nesta skill?
- [ ] Contexto do usuário foi explicitado (persona, tipo de produto, plataforma)?
- [ ] 3–5 fluxos críticos foram percorridos passo a passo (não só olhados)?
- [ ] Todo finding tem: evidência + princípio + impacto + severidade + recomendação + critério de aceite?
- [ ] Findings organizados por severidade (4 → 1)?
- [ ] WCAG 2.2 AA verificada (mínimo: contraste, foco, teclado, target, labels, reflow, status, error)?
- [ ] Estados auditados (default, hover, focus, disabled, loading, error, empty)?
- [ ] Seção "o que funciona bem" existe e não está vazia?
- [ ] Findings que pertencem a outras skills foram **encaminhados**, não absorvidos?
- [ ] Calibragem por contexto aplicada (operacional × landing × docs × template)?

## Quando NÃO usar esta skill

| Situação | Use em vez disso |
|----------|-----------------|
| Bug funcional, código quebrado, API falhando | **trident** |
| Code review de frontend por qualidade | **trident --design** |
| Definir tokens, escala visual, breakpoints, primitives | **ui-design-system** |
| Definir anatomia, slots, variants, estados de componente | **component-architect** |
| Verificar adesão de app a DS externo específico | **design-system-audit** |
| Cross-browser, build target, polyfills | **react-patterns** |
| Definir escopo de produto novo | **product-discovery-prd** |
| Revisar segurança | **security-audit** |
| Problema é só visual sem impacto em tarefa observável | **ui-design-system** |

## Integração

- **product-discovery-prd** — Após PRD, oferecer audit assim que primeiras telas existirem.
- **ui-design-system** — Findings sistêmicos (recorrentes em várias telas) viram input pra atualização do DS.
- **component-architect** — Findings de estado ausente ou contrato de a11y mal definido viram input pra anatomia.
- **trident --design** — Audit revisa experiência; trident revisa código. Audit primeiro, trident depois para implementar correção.
- **sdd** — Findings com critério de aceite viram specs prontas.
- **maestro** — Pode orquestrar discovery → build → ux-audit → fix.
- **security-audit** — Dark patterns que coletam dado desnecessário combinam com security audit.

## Referências

| Arquivo | Conteúdo |
|---------|----------|
| `references/triage-matrix.md` | Sintoma → tipo de problema → skill responsável (Fase 1) |
| `references/ux-foundations.md` | Heurísticas Nielsen, princípios Norman, Laws of UX, calibragem por contexto, dark patterns, mobile ergonomics, perf percebida |
| `references/wcag-ux-checklist.md` | WCAG 2.2 AA aplicado ao fluxo de audit (novos critérios + clássicos + reflow/zoom/status/error) |
| `references/ux-severity-rubric.md` | Severidade Nielsen 0–4 + rubrica scored de 14 categorias + formato canônico de finding com critério de aceite |
| `references/audit-output-template.md` | Templates de output: completo, focado, cognitive walkthrough |
| `references/states-inventory.md` | Inventário canônico de estados a auditar (próximo chat) |
