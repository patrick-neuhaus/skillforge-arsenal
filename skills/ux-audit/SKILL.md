---
name: ux-audit
description: "Audita, revisa, analisa, avalia e melhora a experiência do usuário em apps web e mobile. Identifica problemas de usabilidade, valida acessibilidade WCAG 2.2, verifica dark patterns, checa performance percebida e gera recomendações acionáveis com severidade. Use SEMPRE que o usuário mencionar: UX, UI, usabilidade, audit, auditoria, revisão de interface, 'o app tá confuso', 'revisa a UX', 'olha a interface', 'feedback de UX', 'melhorar a experiência', 'o usuário tá perdido', 'tá difícil de usar', heurísticas, Nielsen, 'o fluxo tá ruim', fix UX issues, evaluate usability, assess accessibility, redesign flow, check user experience, review interface, improve UX, validate WCAG, analyze user flow. Não confundir com ui-design-system (cria/padroniza componentes visuais) nem trident --design (review de código frontend). UX audit foca na EXPERIÊNCIA do usuário, não no código nem no design system."
---

# UX Audit v3

**Iron Law:** Nunca entregue um audit de UX sem percorrer o fluxo real do usuário passo a passo. Screenshots sozinhos escondem problemas de interação — sempre caminhe pelo fluxo como se fosse o usuário.

## Modos

| Modo | Quando usar | Escopo |
|------|-------------|--------|
| **Completo** | Revisão geral do produto | Todas as dimensões (heurísticas, fluxos, WCAG, performance, dark patterns) |
| **Focado** | Tela ou fluxo específico | Heurísticas + Laws of UX + WCAG relevantes ao escopo |
| **Cognitive Walkthrough** | Learnability pra novos usuários | Perfil do usuário + tarefas + 4 perguntas por passo |

## Workflow

```
UX Audit Progress:

- [ ] Fase 1: Contexto ⚠️ REQUIRED
  - [ ] 1.1 Identificar usuário-alvo (persona, nível técnico, frequência)
  - [ ] 1.2 Identificar objetivo principal do produto
  - [ ] 1.3 Identificar plataforma (web desktop, mobile, responsivo, nativo)
  - [ ] 1.4 Verificar se tem onboarding e features de IA
- [ ] Fase 2: Caminhar pelos fluxos ⚠️ REQUIRED
  - [ ] 2.1 Listar 3-5 fluxos críticos
  - [ ] 2.2 Percorrer cada fluxo passo a passo como usuário
  - [ ] 2.3 Documentar fricções, bloqueios e acertos
- [ ] Fase 3: Varredura heurística
  - [ ] 3.1 Aplicar 10 Heurísticas de Nielsen → Load references/ux-ui-foundations.md
  - [ ] 3.2 Diagnosticar causa raiz com Laws of UX
  - [ ] 3.3 Classificar severidade (0-4 Nielsen)
- [ ] Fase 4: Acessibilidade
  - [ ] 4.1 Verificar WCAG 2.2 AA → Load references/wcag-checklist.md
  - [ ] 4.2 Checar target size, contraste, labels, teclado
- [ ] Fase 5: Verificações complementares
  - [ ] 5.1 Dark patterns → Load references/dark-patterns-check.md
  - [ ] 5.2 Performance percebida (Core Web Vitals)
  - [ ] 5.3 UX de IA (se aplicável)
  - [ ] 5.4 Mobile ergonomics (se aplicável)
- [ ] Fase 6: Síntese ⛔ BLOCKING
  - [ ] 6.1 Compilar findings por severidade → Load references/scoring-rubrics.md
  - [ ] 6.2 Listar o que está funcionando bem
  - [ ] ⛔ GATE: Revisar — todos os findings têm evidência + princípio + recomendação?
  - [ ] ⛔ GATE: Cada fluxo crítico foi percorrido? Nenhum foi pulado?
- [ ] Fase 7: Apresentar ⛔ BLOCKING
  - [ ] 7.1 Formatar output → Load references/audit-templates.md
  - [ ] ⛔ GATE: Apresentar ao usuário — não implementar sem confirmação
```

## Princípios

1. **Imparcialidade total.** Ignore quem construiu. Foque na experiência de quem usa.
2. **Evidência > opinião.** Toda crítica cita princípio/heurística violado. "Tá ruim" não serve.
3. **Severidade governa prioridade.** Escala de Nielsen (0-4) em todo finding.
4. **Se tá bom, diga que tá bom.** Não force crítica onde não existe.
5. **Pense no usuário real.** Dashboard pra analista e app de delivery têm regras diferentes.
6. **Acionável > teórico.** Cada finding vira tarefa no ClickUp.
7. **Acessibilidade não é opcional.** WCAG 2.2 AA é baseline legal.

## Fase 1: Contexto

Antes de analisar qualquer coisa, levante:

1. **Quem é o usuário?** (persona, nível técnico, frequência de uso)
2. **Qual o objetivo principal do produto?**
3. **Qual a plataforma?** (web desktop, web mobile, app nativo, responsivo)
4. **Existe onboarding?** (primeiro uso vs uso recorrente)
5. **Tem features de IA?** (chatbot, geração de conteúdo, agentes)

Se o usuário não fornecer, pergunte. Auditar sem saber quem usa é como diagnosticar sem sintomas.

## Fase 2: Caminhar pelos fluxos

Antes de listar findings, percorra os fluxos de ponta a ponta:

1. **Liste 3-5 fluxos críticos** (ex: "criar conta → configurar → exportar")
2. **Percorra cada fluxo** como se fosse o usuário, passo a passo
3. **Pra cada fluxo, responda:**
   - É completável sem confusão?
   - Quantos passos tem? Pode ser reduzido?
   - Tem feedback em cada etapa?
   - Tem saída de emergência (voltar, cancelar, desfazer)?
   - O que acontece quando dá erro?
4. **Veredicto por fluxo:** ✅ Fluido | ⚠️ Tem fricção | ❌ Quebrado

## Fase 3: Varredura heurística

Load `references/ux-ui-foundations.md` — contém as 10 Heurísticas de Nielsen, 7 Princípios de Norman, e 21 Laws of UX.

Para cada heurística: **Passa?** → cite o acerto. **Viola?** → descreva com evidência + severidade (0-4).

Use as Laws of UX como ferramenta de diagnóstico da causa raiz. Não crie seção separada — cite a Law diretamente no finding quando explicar melhor que a heurística.

## Fase 4: Acessibilidade (WCAG 2.2)

Load `references/wcag-checklist.md` — contém critérios WCAG 2.2 novos e clássicos que mais falham.

Foco mínimo: target size (2.5.8), contraste (1.4.3), labels (1.3.1), teclado (2.1.1), dragging alternatives (2.5.7).

## Fase 5: Verificações complementares

Load `references/dark-patterns-check.md` — contém categorias de dark patterns, checklist de UX de IA, e ergonomia mobile.

### Performance percebida
Não precisa medir com ferramentas — percepção subjetiva é válida:
- Página principal demora pra carregar → possível LCP alto
- Clique sem feedback imediato → possível INP alto
- Elementos pulam durante carregamento → CLS

### UX de IA (se aplicável)
Loading states, indicadores de confiança, explainability, error handling, human-in-the-loop, feedback loop.

### Mobile ergonomics (se aplicável)
CTAs na thumb zone, bottom nav vs top menu, targets de toque 44x44px.

## Fase 6-7: Síntese e apresentação

Load `references/audit-templates.md` — contém templates de output pra audit completo, focado e cognitive walkthrough.

Load `references/scoring-rubrics.md` — contém escala de severidade, SUS, NASA-TLX, HEART framework.

### Output final

```markdown
## Resumo Executivo
**Heurísticas com falha:** [H1, H3, H5...]
**WCAG 2.2 violações:** [critérios]
**Findings totais:** [N] — Sev4: [N] | Sev3: [N] | Sev2: [N] | Sev1: [N]

## Análise de Fluxos
[Fluxo → Passos → Veredicto → Observação]

## Findings Priorizados
### Severidade 4 — Corrigir imediatamente
### Severidade 3 — Corrigir antes do próximo release
### Severidade 2 — Prioridade baixa
### Severidade 1 — Cosmético

## Acessibilidade (WCAG 2.2)
## O que está funcionando bem
## Oportunidade criativa
```

⛔ **Confirmation Gate:** Nunca implemente correções sem escolha explícita do usuário.

## Anti-Patterns

- **Auditar sem contexto** — não saber quem é o usuário torna todo finding questionável
- **Pular fluxos e ir direto pras heurísticas** — viola a Iron Law. Fluxos revelam problemas que análise estática não vê
- **Forçar problemas onde não existem** — infla o report e mata credibilidade
- **Findings sem fundamentação** — "tá ruim" sem citar princípio/heurística é opinião, não audit
- **Ignorar acessibilidade** — WCAG 2.2 AA é requisito legal, não sugestão
- **Misturar UI com UX** — "o botão é feio" (UI) ≠ "o botão não comunica que é clicável" (UX)
- **Ignorar o positivo** — report só com críticas perde a confiança do time
- **Generalizar** — "a navegação poderia ser melhor" é inútil. Cite o elemento específico
- **Implementar sem confirmação** — viola o gate de confirmação

## Pre-delivery Checklist

Antes de apresentar o audit ao usuário, confirme:

- [ ] Todo finding tem: evidência específica + princípio violado + severidade + recomendação acionável?
- [ ] Todos os fluxos críticos foram percorridos passo a passo (não só olhados)?
- [ ] A seção "o que está funcionando bem" existe e não está vazia?
- [ ] Findings estão organizados por severidade (4 → 1)?
- [ ] Acessibilidade WCAG 2.2 AA foi verificada explicitamente?
- [ ] Recomendações são acionáveis (podem virar tarefa no ClickUp)?
- [ ] Contexto do usuário foi considerado (não aplicou regras de SaaS público num app interno)?

## Quando NÃO usar esta skill

| Situação | Use em vez disso |
|----------|-----------------|
| Bug funcional (código quebrado, API falhando) | **trident** (code review) |
| Revisar código frontend por qualidade | **trident --design** |
| Criar/padronizar design system ou componentes | **ui-design-system** |
| Criar componentes React reutilizáveis | **component-architect** |
| Definir escopo de produto novo | **product-discovery-prd** |
| Revisar segurança da aplicação | **security-audit** |
| Problema é só visual/estético sem impacto em usabilidade | **ui-design-system** |

## Integração

- **product-discovery-prd** — Após gerar PRD, oferecer: "Quer um audit de UX quando as primeiras telas ficarem prontas?"
- **ui-design-system** — Se o audit encontrar inconsistências visuais recorrentes, sugerir criação/atualização do design system.
- **component-architect** — Se findings apontam componentes com usabilidade ruim, sugerir refatoração do componente.
- **trident --design** — Trident revisa o código frontend; UX audit revisa a experiência. Complementares. Rodar UX audit primeiro, depois trident pra implementar correções.
- **sdd** — Se o audit gerar tasks de correção, usar SDD pra implementar com spec → code → review.
- **maestro** — Maestro pode orquestrar: discovery → build → UX audit → fix cycle. Parte de composition chains.
- **security-audit** — Se encontrar dark patterns ou fluxos que induzem compartilhamento de dados desnecessários, combinar com security audit.
- **lovable-knowledge** — Se o audit encontrar padrões recorrentes (ex: botões pequenos), sugerir regra no Project Knowledge.

## Referências

| Arquivo | Conteúdo |
|---------|----------|
| `references/ux-ui-foundations.md` | Heurísticas de Nielsen, Princípios de Norman, Laws of UX |
| `references/wcag-checklist.md` | Critérios WCAG 2.2 novos + clássicos que mais falham |
| `references/dark-patterns-check.md` | Dark patterns, UX de IA, mobile ergonomics, thumb zone |
| `references/audit-templates.md` | Templates de output: audit completo, focado, cognitive walkthrough |
| `references/scoring-rubrics.md` | Escala de severidade, SUS, NASA-TLX, HEART framework |
