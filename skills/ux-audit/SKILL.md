---
name: ux-audit
description: "Audita, revisa, analisa, avalia e melhora a experiencia do usuario em apps web e mobile. Identifica problemas de usabilidade, valida acessibilidade WCAG 2.2, verifica dark patterns, checa performance percebida e gera recomendacoes acionaveis com severidade. Use SEMPRE que o usuario mencionar: UX, UI, usabilidade, audit, auditoria, revisao de interface, 'o app ta confuso', 'revisa a UX', 'olha a interface', 'feedback de UX', 'melhorar a experiencia', 'o usuario ta perdido', 'ta dificil de usar', heuristicas, Nielsen, 'o fluxo ta ruim', fix UX issues, evaluate usability, assess accessibility, redesign flow, check user experience, review interface, improve UX, validate WCAG, analyze user flow. Nao confundir com ui-design-system (cria/padroniza componentes visuais) nem trident --design (review de codigo frontend). UX audit foca na EXPERIENCIA do usuario, nao no codigo nem no design system."
---

# UX Audit v3

IRON LAW: NUNCA entregue um audit de UX sem percorrer o fluxo real do usuario passo a passo. Screenshots sozinhos escondem problemas de interacao — sempre caminhe pelo fluxo como se fosse o usuario.

## Modos

| Modo | Quando usar | Escopo |
|------|-------------|--------|
| **Completo** | Revisao geral do produto | Todas as dimensoes (heuristicas, fluxos, WCAG, performance, dark patterns) |
| **Focado** | Tela ou fluxo especifico | Heuristicas + Laws of UX + WCAG relevantes ao escopo |
| **Cognitive Walkthrough** | Learnability pra novos usuarios | Perfil do usuario + tarefas + 4 perguntas por passo |

## Workflow

```
UX Audit Progress:

- [ ] Fase 1: Contexto ⚠️ REQUIRED
  - [ ] 1.1 Identificar usuario-alvo (persona, nivel tecnico, frequencia)
  - [ ] 1.2 Identificar objetivo principal do produto
  - [ ] 1.3 Identificar plataforma (web desktop, mobile, responsivo, nativo)
  - [ ] 1.4 Verificar se tem onboarding e features de IA
- [ ] Fase 2: Caminhar pelos fluxos ⚠️ REQUIRED
  - [ ] 2.1 Listar 3-5 fluxos criticos
  - [ ] 2.2 Percorrer cada fluxo passo a passo como usuario
  - [ ] 2.3 Documentar friccoes, bloqueios e acertos
- [ ] Fase 3: Varredura heuristica
  - [ ] 3.1 Aplicar 10 Heuristicas de Nielsen → Load references/ux-ui-foundations.md
  - [ ] 3.2 Diagnosticar causa raiz com Laws of UX
  - [ ] 3.3 Classificar severidade (0-4 Nielsen)
- [ ] Fase 4: Acessibilidade
  - [ ] 4.1 Verificar WCAG 2.2 AA → Load references/wcag-checklist.md
  - [ ] 4.2 Checar target size, contraste, labels, teclado
- [ ] Fase 5: Verificacoes complementares
  - [ ] 5.1 Dark patterns → Load references/dark-patterns-check.md
  - [ ] 5.2 Performance percebida (Core Web Vitals)
  - [ ] 5.3 UX de IA (se aplicavel)
  - [ ] 5.4 Mobile ergonomics (se aplicavel)
- [ ] Fase 6: Sintese ⛔ BLOCKING
  - [ ] 6.1 Compilar findings por severidade → Load references/scoring-rubrics.md
  - [ ] 6.2 Listar o que esta funcionando bem
  - [ ] ⛔ GATE: Revisar — todos os findings tem evidencia + principio + recomendacao?
  - [ ] ⛔ GATE: Cada fluxo critico foi percorrido? Nenhum foi pulado?
- [ ] Fase 7: Apresentar ⛔ BLOCKING
  - [ ] 7.1 Formatar output → Load references/audit-templates.md
  - [ ] ⛔ GATE: Apresentar ao usuario — NAO implementar sem confirmacao
```

## Principios

1. **Imparcialidade total.** Ignore quem construiu. Foque na experiencia de quem usa.
2. **Evidencia > opiniao.** Toda critica cita principio/heuristica violado. "Ta ruim" nao serve.
3. **Severidade governa prioridade.** Escala de Nielsen (0-4) em todo finding.
4. **Se ta bom, diga que ta bom.** Nao force critica onde nao existe.
5. **Pense no usuario real.** Dashboard pra analista e app de delivery tem regras diferentes.
6. **Acionavel > teorico.** Cada finding vira tarefa no ClickUp.
7. **Acessibilidade nao e opcional.** WCAG 2.2 AA e baseline legal.

## Fase 1: Contexto

Antes de analisar qualquer coisa, levante:

1. **Quem e o usuario?** (persona, nivel tecnico, frequencia de uso)
2. **Qual o objetivo principal do produto?**
3. **Qual a plataforma?** (web desktop, web mobile, app nativo, responsivo)
4. **Existe onboarding?** (primeiro uso vs uso recorrente)
5. **Tem features de IA?** (chatbot, geracao de conteudo, agentes)

Se o usuario nao fornecer, pergunte. Auditar sem saber quem usa e como diagnosticar sem sintomas.

## Fase 2: Caminhar pelos fluxos

ANTES de listar findings, percorra os fluxos de ponta a ponta:

1. **Liste 3-5 fluxos criticos** (ex: "criar conta → configurar → exportar")
2. **Percorra cada fluxo** como se fosse o usuario, passo a passo
3. **Pra cada fluxo, responda:**
   - E completavel sem confusao?
   - Quantos passos tem? Pode ser reduzido?
   - Tem feedback em cada etapa?
   - Tem saida de emergencia (voltar, cancelar, desfazer)?
   - O que acontece quando da erro?
4. **Veredicto por fluxo:** ✅ Fluido | ⚠️ Tem friccao | ❌ Quebrado

## Fase 3: Varredura heuristica

Load `references/ux-ui-foundations.md` — contem as 10 Heuristicas de Nielsen, 7 Principios de Norman, e 21 Laws of UX.

Para cada heuristica: **Passa?** → cite o acerto. **Viola?** → descreva com evidencia + severidade (0-4).

Use as Laws of UX como ferramenta de diagnostico da causa raiz. Nao crie secao separada — cite a Law diretamente no finding quando explicar melhor que a heuristica.

## Fase 4: Acessibilidade (WCAG 2.2)

Load `references/wcag-checklist.md` — contem criterios WCAG 2.2 novos e classicos que mais falham.

Foco minimo: target size (2.5.8), contraste (1.4.3), labels (1.3.1), teclado (2.1.1), dragging alternatives (2.5.7).

## Fase 5: Verificacoes complementares

Load `references/dark-patterns-check.md` — contem categorias de dark patterns, checklist de UX de IA, e ergonomia mobile.

### Performance percebida
Nao precisa medir com ferramentas — percepcao subjetiva e valida:
- Pagina principal demora pra carregar → possivel LCP alto
- Clique sem feedback imediato → possivel INP alto
- Elementos pulam durante carregamento → CLS

### UX de IA (se aplicavel)
Loading states, indicadores de confianca, explainability, error handling, human-in-the-loop, feedback loop.

### Mobile ergonomics (se aplicavel)
CTAs na thumb zone, bottom nav vs top menu, targets de toque 44x44px.

## Fase 6-7: Sintese e apresentacao

Load `references/audit-templates.md` — contem templates de output pra audit completo, focado e cognitive walkthrough.

Load `references/scoring-rubrics.md` — contem escala de severidade, SUS, NASA-TLX, HEART framework.

### Output final

```markdown
## Resumo Executivo
**Heuristicas com falha:** [H1, H3, H5...]
**WCAG 2.2 violacoes:** [criterios]
**Findings totais:** [N] — Sev4: [N] | Sev3: [N] | Sev2: [N] | Sev1: [N]

## Analise de Fluxos
[Fluxo → Passos → Veredicto → Observacao]

## Findings Priorizados
### Severidade 4 — Corrigir imediatamente
### Severidade 3 — Corrigir antes do proximo release
### Severidade 2 — Prioridade baixa
### Severidade 1 — Cosmetico

## Acessibilidade (WCAG 2.2)
## O que esta funcionando bem
## Oportunidade criativa
```

⛔ **Confirmation Gate:** NUNCA implemente correcoes sem escolha explicita do usuario.

## Anti-Patterns

- **Auditar sem contexto** — nao saber quem e o usuario torna todo finding questionavel
- **Pular fluxos e ir direto pras heuristicas** — viola a Iron Law. Fluxos revelam problemas que analise estatica nao ve
- **Forcar problemas onde nao existem** — infla o report e mata credibilidade
- **Findings sem fundamentacao** — "ta ruim" sem citar principio/heuristica e opiniao, nao audit
- **Ignorar acessibilidade** — WCAG 2.2 AA e requisito legal, nao sugestao
- **Misturar UI com UX** — "o botao e feio" (UI) ≠ "o botao nao comunica que e clicavel" (UX)
- **Ignorar o positivo** — report so com criticas perde a confianca do time
- **Generalizar** — "a navegacao poderia ser melhor" e inutil. Cite o elemento especifico
- **Implementar sem confirmacao** — viola o gate de confirmacao

## Pre-delivery Checklist

Antes de apresentar o audit ao usuario, confirme:

- [ ] Todo finding tem: evidencia especifica + principio violado + severidade + recomendacao acionavel?
- [ ] Todos os fluxos criticos foram percorridos passo a passo (nao so olhados)?
- [ ] A secao "o que esta funcionando bem" existe e nao esta vazia?
- [ ] Findings estao organizados por severidade (4 → 1)?
- [ ] Acessibilidade WCAG 2.2 AA foi verificada explicitamente?
- [ ] Recomendacoes sao acionaveis (podem virar tarefa no ClickUp)?
- [ ] Contexto do usuario foi considerado (nao aplicou regras de SaaS publico num app interno)?

## Quando NAO usar esta skill

| Situacao | Use em vez disso |
|----------|-----------------|
| Bug funcional (codigo quebrado, API falhando) | **trident** (code review) |
| Revisar codigo frontend por qualidade | **trident --design** |
| Criar/padronizar design system ou componentes | **ui-design-system** |
| Criar componentes React reutilizaveis | **component-architect** |
| Definir escopo de produto novo | **product-discovery-prd** |
| Revisar seguranca da aplicacao | **security-audit** |
| Problema e so visual/estetico sem impacto em usabilidade | **ui-design-system** |

## Integracao

- **product-discovery-prd** — Apos gerar PRD, oferecer: "Quer um audit de UX quando as primeiras telas ficarem prontas?"
- **ui-design-system** — Se o audit encontrar inconsistencias visuais recorrentes, sugerir criacao/atualizacao do design system.
- **component-architect** — Se findings apontam componentes com usabilidade ruim, sugerir refatoracao do componente.
- **trident --design** — Trident revisa o CODIGO frontend; UX audit revisa a EXPERIENCIA. Complementares. Rodar UX audit primeiro, depois trident pra implementar correcoes.
- **sdd** — Se o audit gerar tasks de correcao, usar SDD pra implementar com spec → code → review.
- **maestro** — Maestro pode orquestrar: discovery → build → UX audit → fix cycle. Parte de composition chains.
- **security-audit** — Se encontrar dark patterns ou fluxos que induzem compartilhamento de dados desnecessarios, combinar com security audit.
- **lovable-knowledge** — Se o audit encontrar padroes recorrentes (ex: botoes pequenos), sugerir regra no Project Knowledge.

## Referencias

| Arquivo | Conteudo |
|---------|----------|
| `references/ux-ui-foundations.md` | Heuristicas de Nielsen, Principios de Norman, Laws of UX |
| `references/wcag-checklist.md` | Criterios WCAG 2.2 novos + classicos que mais falham |
| `references/dark-patterns-check.md` | Dark patterns, UX de IA, mobile ergonomics, thumb zone |
| `references/audit-templates.md` | Templates de output: audit completo, focado, cognitive walkthrough |
| `references/scoring-rubrics.md` | Escala de severidade, SUS, NASA-TLX, HEART framework |
