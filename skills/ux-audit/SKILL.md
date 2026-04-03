---
name: ux-audit
description: "Skill para auditorias de UX/UI em aplicações web e mobile. Use esta skill SEMPRE que o usuário mencionar: UX, UI, usabilidade, audit, auditoria, revisão de interface, 'o app tá confuso', 'revisa a UX', 'olha a interface', 'feedback de UX', 'melhorar a experiência', 'o usuário tá perdido', 'tá difícil de usar', heurísticas, Nielsen, 'o fluxo tá ruim', ou qualquer variação que indique que um produto digital precisa de análise de experiência do usuário. Também use quando o usuário compartilhar screenshots de um app ou mencionar que vai 'jogar no Lovable' um PRD e quiser garantir qualidade de UX antes ou depois. Se houver dúvida entre UX e feature request, USE esta skill — problemas de UX disfarçados de feature request são comuns. NÃO use pra bugs funcionais (código quebrado, API falhando) — isso é debug, não UX. Se é revisão de código pra encontrar bugs, use repo-review."
---

# UX Audit v2 — Auditoria de Experiência do Usuário

## Visão geral

Esta skill conduz auditorias de UX/UI em aplicações web e mobile. Combina frameworks consagrados (Heurísticas de Nielsen, Laws of UX de Yablonski, Princípios de Norman) com padrões modernos (WCAG 2.2, Core Web Vitals, dark patterns, UX de IA) pra produzir análises estruturadas, priorizadas por severidade, com recomendações acionáveis.

A skill funciona em três modos:
1. **Audit completo** — Análise sistemática por todas as dimensões (revisão geral)
2. **Audit focado** — Análise de fluxo específico, tela específica, ou problema específico
3. **Cognitive Walkthrough** — Avaliação de learnability pra novos usuários (NOVO v2)

### Novidades na v2

- **WCAG 2.2** — 9 novos critérios de acessibilidade (target size, dragging alternatives, accessible auth)
- **Core Web Vitals** — INP substituiu FID em março 2024 como métrica de responsividade
- **Dark patterns** — Legislação EU DSA, CA CPRA, FTC enforcement — patterns agora ilegais
- **Cognitive Walkthrough** — Método complementar às heurísticas focado em learnability
- **UX de IA** — Padrões emergentes pra features com LLM (streaming, confiança, human-in-the-loop)
- **Design System Evaluation** — Consistência de componentes e tokens
- **Métricas quantitativas** — SUS + NASA-TLX pra fundamentar recomendações
- **Thumb zone** — Ergonomia mobile pra telas grandes (6.5"+)

## Princípios

1. **Imparcialidade total.** Ignore quem construiu. Foque exclusivamente na experiência de quem vai usar.
2. **Evidência > opinião.** Toda crítica deve citar o princípio/heurística violado. "Tá ruim" não serve — "viola a Heurística 1 de Nielsen (visibilidade do status) porque o botão não dá feedback visual ao ser clicado" serve.
3. **Severidade governa prioridade.** Use a Escala de Severidade de Nielsen (0-4) pra classificar cada finding. Sem isso, tudo parece igualmente urgente.
4. **Se tá bom, diga que tá bom.** Não force crítica onde não existe. Reconhecer acertos constrói credibilidade e ajuda a equipe a preservar o que funciona.
5. **Pense no usuário real.** Sempre contextualize: quem é o usuário, em que situação usa, qual o objetivo dele. Um dashboard pra analista e um app de delivery têm regras diferentes.
6. **Acionável > teórico.** Cada finding deve ter uma recomendação concreta que pode virar tarefa no ClickUp.
7. **Acessibilidade não é opcional.** WCAG 2.2 AA é o baseline. Não é "nice to have" — é requisito legal em muitas jurisdições.

## Referências (leia antes de auditar)

Antes de iniciar qualquer auditoria, leia o reference file:
- `references/ux-ui-foundations.md` — Contém: 10 Heurísticas de Nielsen, 7 Princípios de Norman, 21 Laws of UX (Yablonski), HEART Framework (Google), Princípios de Krug, Escala de Severidade, WCAG 2.2 critérios, Core Web Vitals, dark patterns, SUS/NASA-TLX

## Fluxo de trabalho — Audit Completo

### Passo 0: Contexto

Antes de analisar qualquer coisa, entenda:
1. **Quem é o usuário?** (persona, nível técnico, frequência de uso)
2. **Qual o objetivo principal do produto?** (o que o usuário vem fazer aqui?)
3. **Qual a plataforma?** (web desktop, web mobile, app nativo, responsivo)
4. **Existe onboarding?** (primeiro uso vs uso recorrente)
5. **Tem features de IA?** (chatbot, geração de conteúdo, agentes — ativa avaliação de UX de IA)

Se o usuário não fornecer esse contexto, pergunte. Auditar sem saber quem usa é como diagnosticar sem saber os sintomas.

### Passo 1: Varredura heurística (10 Heurísticas de Nielsen)

Examine a aplicação contra cada uma das 10 heurísticas. Pra cada heurística:
- **Passa?** → Cite o que está funcionando bem (breve)
- **Viola?** → Descreva a violação com evidência específica (cite o elemento real do app) + severidade (0-4)

Formato por heurística:
```
### H1: Visibilidade do Status do Sistema
**Veredicto:** ✅ Passa | ⚠️ Parcial | ❌ Viola

**Evidências:**
- [Elemento X] faz/não faz [comportamento] — Severidade: [0-4]
- [Elemento Y] faz/não faz [comportamento] — Severidade: [0-4]

**Recomendação:** [Ação concreta]
```

### Passo 2: Análise de fluxos críticos

ANTES de listar findings, percorra os fluxos de ponta a ponta:

1. **Liste os 3-5 fluxos mais importantes** do produto (ex: "criar conta → configurar → exportar")
2. **Percorra cada fluxo** como se fosse o usuário, passo a passo
3. **Pra cada fluxo, responda:**
   - É completável sem confusão?
   - Quantos passos tem? Pode ser reduzido?
   - Tem feedback em cada etapa?
   - Tem saída de emergência (voltar, cancelar, desfazer)?
   - O que acontece quando dá erro?
4. **Dê um veredicto por fluxo:** ✅ Fluido | ⚠️ Tem fricção | ❌ Quebrado

Formato:
```
### Fluxo: [nome]
**Passos:** [passo 1] → [passo 2] → [passo 3] → ...
**Veredicto:** ✅ | ⚠️ | ❌
**Observação:** [2-3 linhas]
```

### Passo 3: Diagnóstico com Laws of UX

As Laws of UX são FERRAMENTAS de diagnóstico — use-as pra explicar a causa raiz dos problemas encontrados. Não crie seção separada. Cite a Law diretamente no finding quando ela explicar o problema melhor que a heurística.

**Laws mais úteis em auditorias:**
- **Jakob's Law** — O app segue padrões que o usuário já conhece? Se não, qual o custo cognitivo?
- **Hick's Law** — Alguma tela apresenta opções demais? Contar os itens ajuda
- **Fitts's Law** — Alvos de clique são grandes e próximos de onde o cursor já está?
- **Miller's Law** — Listas/formulários com mais de 7 itens sem agrupamento?
- **Gestalt** (Proximity, Common Region, Similarity) — Espaçamento visual reflete relação lógica?
- **Aesthetic-Usability Effect** — Visual profissional transmite confiança?
- **Tesler's Law** — Complexidade empurrada pro usuário que poderia estar no backend?
- **Peak-End Rule** — Em fluxos longos: como o usuário se sente no pico e no final?

### Passo 4: Acessibilidade (WCAG 2.2)

Verifique contra os critérios de acessibilidade mais impactantes:

**Critérios novos do WCAG 2.2 (verificar explicitamente):**
- **2.5.7 Dragging Movements (AA)** — Toda funcionalidade de drag tem alternativa sem arrastar? (ex: botões de mover, dropdowns)
- **2.5.8 Target Size Minimum (AA)** — Alvos interativos têm pelo menos 24×24 CSS pixels?
- **3.2.6 Consistent Help (A)** — Mecanismos de ajuda aparecem na mesma posição em todas as páginas?
- **3.3.7 Redundant Entry (A)** — Informação já inserida é auto-preenchida? Usuário não redigita dados no mesmo processo?
- **3.3.8 Accessible Authentication (AA)** — Login não requer teste cognitivo (CAPTCHA sem alternativa acessível)?

**Critérios clássicos que mais falham:**
- Contraste de cor (1.4.3 — mínimo 4.5:1 pra texto normal)
- Labels em inputs (1.3.1 — todo campo tem label associado?)
- Navegação por teclado (2.1.1 — tudo funciona sem mouse?)
- Alt text em imagens (1.1.1 — imagens informativas têm alt?)

**Formato:** Use severidade de Nielsen pra classificar, mas adicione o critério WCAG violado:
```
**Problema:** Botão de fechar modal tem 16x16px
**WCAG:** 2.5.8 Target Size (Minimum) — AA
**Severidade:** 3
**Recomendação:** Aumentar pra mínimo 24x24px (ideal 44x44px pra touch)
```

### Passo 5: Performance percebida (Core Web Vitals)

Se tiver acesso ao app rodando, avalie a percepção de performance:

**Core Web Vitals atuais (desde março 2024):**
- **LCP (Largest Contentful Paint)** — Bom: ≤ 2.5s. A tela principal carrega rápido?
- **INP (Interaction to Next Paint)** — Bom: ≤ 200ms. Cliques/toques respondem rápido? (substituiu FID)
- **CLS (Cumulative Layout Shift)** — Bom: ≤ 0.1. Elementos pulam na tela durante carregamento?

Não precisa medir com ferramentas — percepção subjetiva é válida em UX audit:
- "A página principal demora visivelmente pra carregar o conteúdo principal" = possível LCP alto
- "Ao clicar num botão, o feedback demora" = possível INP alto
- "Ao carregar, o botão pula de posição" = CLS

### Passo 6: Dark patterns check

Verifique se o app usa padrões que agora são ilegais ou anti-éticos:

**Categorias a verificar:**
- **Nagging** — Pop-ups persistentes que interrompem a tarefa principal (ex: "assine agora" que aparece toda vez)
- **Obstruction** — Cancelamento mais difícil que assinatura? Esconder opção de deletar conta?
- **Sneaking** — Custos ocultos revelados só no checkout? Itens adicionados ao carrinho automaticamente?
- **Interface interference** — Botão de aceitar em destaque, recusar escondido? Pré-seleções que beneficiam o negócio?
- **Forced action** — Obrigar criação de conta pra ver conteúdo que poderia ser público?

**Contexto legal:** EU Digital Services Act, California CPRA, e FTC enforcement tornam dark patterns explicitamente ilegais. Mesmo que o app não esteja nessas jurisdições, é bad practice.

### Passo 7: UX de IA (se aplicável)

Se o app tem features de IA/LLM, avalie:

- **Loading states:** Respostas de LLM mostram streaming progressivo ou tela em branco? Spinner sem estimativa de tempo?
- **Confiança:** O usuário sabe quando a IA tem certeza vs quando está "chutando"? Tem indicadores de confiança?
- **Explainability:** O usuário entende POR QUE a IA sugeriu algo? Tem fontes/referências?
- **Error handling:** O que acontece quando a IA falha? Mensagem genérica ou orientação clara?
- **Human-in-the-loop:** Ações destrutivas passam por confirmação humana? Tem override fácil?
- **Feedback loop:** Tem botão de like/dislike ou feedback pra melhorar respostas?
- **Conversation UX:** Se é chat, mantém contexto entre turnos? Tem histórico acessível?

### Passo 8: Mobile ergonomics (se aplicável)

Se o app é responsivo ou mobile-first, avalie thumb zone:

- **CTAs primários** estão na zona confortável do polegar (centro-baixo da tela)?
- **Navegação** é por bottom nav (acessível) ou top menu (requer esticar)?
- **Modais e ações destrutivas** não estão em zonas fáceis de tocar acidentalmente?
- **Targets de toque** têm pelo menos 44x44px? (WCAG 2.5.8 pede 24px mínimo, mas 44px é melhor pra touch)
- Em telas grandes (6.5"+), ações no topo-esquerdo são difíceis de alcançar com uma mão

**Referência:** 75% das interações mobile são com o polegar. 49% dos usuários usam o celular com uma mão só (Steven Hoober). Em telas modernas de 6.7"+, a zona segura é menor do que se imagina.

### Passo 9: Síntese e priorização

Compile todos os findings e organize por severidade:

```
## Resumo Executivo

**Heurísticas com falha:** [liste quais falharam, ex: H1, H3, H5]
**WCAG 2.2 violações:** [critérios violados]
**Findings totais:** [N]
- Severidade 4 (catastrófico): [N]
- Severidade 3 (maior): [N]
- Severidade 2 (menor): [N]
- Severidade 1 (cosmético): [N]

## Análise de Fluxos

### Fluxo 1: [nome]
**Passos:** [passo 1] → [passo 2] → [passo 3] → ...
**Veredicto:** ✅ Fluido | ⚠️ Tem fricção | ❌ Quebrado
**Observação:** [2-3 linhas]

[repetir pra cada fluxo]

## Findings Priorizados

### 🔴 Severidade 4 — Corrigir imediatamente
[Lista de findings com evidência + princípio + recomendação]

### 🟠 Severidade 3 — Corrigir antes do próximo release
[Lista de findings com evidência + princípio + recomendação]

### 🟡 Severidade 2 — Prioridade baixa
[Lista de findings com evidência + princípio + recomendação]

### 🔵 Severidade 1 — Cosmético
[Lista de findings com evidência + princípio + recomendação]

## Acessibilidade (WCAG 2.2)
[Resumo de conformidade + violações específicas]

## O que está funcionando bem
[Lista do que não deve ser mexido]

## Oportunidade criativa
[Uma ideia fora do óbvio que transformaria a experiência]
```

### Passo 10: Gerar tarefas (se solicitado)

Se o usuário pedir, transforme os findings em tarefas pro ClickUp:
- 1 tarefa por finding
- Título: [Severidade] [Área] - Descrição curta
- Descrição: Problema → Heurística/WCAG violado → Recomendação
- Tag de severidade pra priorização

## Fluxo de trabalho — Audit Focado

Quando o usuário traz uma tela ou fluxo específico:

1. **Identifique o objetivo da tela/fluxo**
2. **Aplique as heurísticas relevantes** (não precisa passar pelas 10 se é um problema localizado)
3. **Aplique as Laws of UX relevantes**
4. **Verifique WCAG 2.2** nos elementos da tela (target size, contraste, labels)
5. **Dê feedback estruturado:** Problema → Princípio violado → Severidade → Recomendação

Formato compacto:
```
| # | Problema | Princípio | Severidade | Recomendação |
|---|---|---|---|---|
| 1 | [descrição] | [heurística/law/WCAG] | [0-4] | [ação] |
```

## Fluxo de trabalho — Cognitive Walkthrough (NOVO v2)

Método focado em learnability pra novos usuários. Complementa a heuristic evaluation com foco em "o novo usuário consegue completar a tarefa sem ajuda?".

### Quando usar
- Apps walk-up-and-use (kiosks, onboarding, ferramentas públicas)
- Avaliação de learnability pra usuários de primeiro uso
- Quando o público-alvo é não-técnico

### Método (baseado em Wharton, Rieman, Lewis, Polson — 1994)

1. **Defina o perfil do usuário** (experiência, motivação, contexto)
2. **Defina as tarefas** (3-5 tarefas mais importantes)
3. **Pra cada passo de cada tarefa, pergunte:**
   - O usuário vai TENTAR fazer a ação correta? (sabe o que quer fazer?)
   - O usuário vai NOTAR que a ação correta está disponível? (é visível?)
   - O usuário vai ASSOCIAR a ação com o efeito desejado? (o label faz sentido?)
   - Após executar, o usuário vai PERCEBER que progrediu? (tem feedback?)
4. **Documente falhas** como findings com severidade

### Formato
```
### Tarefa: [nome]
**Usuário:** [perfil]

| Passo | Ação esperada | Tentativa? | Visível? | Associação? | Feedback? | Problema |
|-------|---------------|------------|----------|-------------|-----------|----------|
| 1 | [ação] | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | [se houver] |
| 2 | [ação] | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | [se houver] |
```

## Métricas quantitativas (pra fundamentar recomendações)

### SUS (System Usability Scale)
Score de 0-100 (não é porcentagem). Média global: 68.
- 90-100: Excelente
- 80-89: Muito bom
- 70-79: Bom
- 60-69: Aceitável
- < 50: Inaceitável

Use como referência quando o usuário tiver dados de SUS. Se não tiver, sugira aplicar (10 perguntas, 5 minutos por usuário).

### NASA-TLX (Task Load Index)
Mede carga cognitiva em 6 dimensões: mental, física, temporal, performance, esforço, frustração.
Use quando a tarefa é complexa e a pergunta é "o usuário consegue mas fica exausto?". Complementa SUS: SUS mede usabilidade percebida, NASA-TLX mede custo cognitivo.

## Escala de Severidade — Referência Rápida

| Nível | Nome | Significado | Ação |
|---|---|---|---|
| 0 | Não é problema | Sem impacto na usabilidade | Nenhuma |
| 1 | Cosmético | Usuário nota mas não afeta tarefa | Corrigir quando sobrar tempo |
| 2 | Menor | Causa leve confusão ou delay | Prioridade baixa |
| 3 | Maior | Impede ou dificulta significativamente uma tarefa | Corrigir antes do próximo release |
| 4 | Catastrófico | Bloqueia o usuário de completar uma tarefa essencial | Corrigir imediatamente |

## O que NÃO fazer

1. **Não generalize.** "A navegação poderia ser melhor" é inútil. "O menu principal tem 12 itens no nível 1, violando Hick's Law — reduzir pra 5-7 agrupando por categoria" é útil.
2. **Não force problemas.** Se a interface é boa, diga que é boa. Credibilidade > volume de feedback.
3. **Não ignore o positivo.** Sempre inclua uma seção de "o que tá funcionando bem".
4. **Não dê feedback sem fundamentação.** Toda crítica precisa citar pelo menos 1 princípio/heurística/law/WCAG.
5. **Não ignore o contexto.** Um app interno pra 5 pessoas tem requisitos diferentes de um SaaS público.
6. **Não misture UI com UX.** "O botão é feio" (UI) ≠ "O botão não comunica que é clicável" (UX). Ambos importam, mas são análises diferentes.
7. **Não ignore acessibilidade.** WCAG 2.2 AA não é sugestão — é requisito. Target size de 12px em mobile é severidade 3, não "detalhe".

## Integração com outras skills

- **Product Discovery & PRD:** Após gerar PRD, ofereça: "Quer que eu faça um audit de UX quando as primeiras telas ficarem prontas?"
- **Lovable Knowledge:** Se o audit encontrar padrões recorrentes, sugira adicionar regras ao Project Knowledge: "O Lovable tá gerando botões pequenos demais consistentemente — vamos adicionar uma regra no Knowledge pra target mínimo de 44px"
- **Tech Lead & PM:** Findings do audit podem virar sprint items. Sugira: "Quer que eu transforme esses findings em tarefas pro ClickUp?"
- **Security Audit:** Se encontrar dark patterns ou fluxos que induzem o usuário a compartilhar dados desnecessários, combine com security audit pra avaliar implicações de privacidade.
