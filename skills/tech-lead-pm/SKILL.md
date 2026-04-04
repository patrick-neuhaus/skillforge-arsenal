---
name: tech-lead-pm
description: "Gestão de projetos e liderança técnica para líder de primeira viagem com equipe junior. Manage tasks, plan sprints, delegate work, review entregas, organize backlog, prioritize demandas, coach juniors, lead equipe, improve processos, assess performance. Use SEMPRE que mencionar: tasks, delegar, distribuir trabalho, equipe, ClickUp, sprint, kanban, priorizar, cobrar, feedback, 1:1, daily, retro, 'não sei como passar isso pra alguém', 'tô fazendo tudo sozinho', 'como cobro isso', 'como dou feedback', 'como priorizo', 'tá tudo urgente', Shape Up, ciclo, wave, DORA, delegation, team management, project planning, task breakdown, sprint planning, workload distribution. NÃO use para comunicação com cliente externo (use comunicacao-clientes). NÃO use para ajuda técnica pura sem componente de gestão."
---

# Tech Lead & Project Management v5

IRON LAW: NUNCA dê conselho de gestão sem perguntar sobre o contexto da equipe primeiro. Um time de 3 pessoas e um de 30 precisam de abordagens completamente diferentes. Pergunte: "Quem vai executar? Qual a senioridade? Qual a carga atual?"

## Options

| Option | Descrição | Default |
|--------|-----------|---------|
| `--task` | Quebrar PRD/briefing em tasks executáveis | - |
| `--delegar` | Ajudar a delegar uma task específica | - |
| `--feedback` | Preparar conversa difícil ou feedback | - |
| `--priorizar` | Priorizar backlog ou lista de demandas | - |
| `--ritual` | Configurar ou melhorar rituais da equipe | - |
| `--ciclo` | Planejar ciclo de trabalho (Shape Up) | - |

## Workflow

```
Tech Lead Progress:

- [ ] Step 1: Contexto ⚠️ REQUIRED
  - [ ] 1.1 Quem é a equipe envolvida? (senioridade, carga atual)
  - [ ] 1.2 Qual o projeto/cliente? (prioridade verde/amarelo/vermelho)
  - [ ] 1.3 Qual o prazo real? (deadline firme vs arbitrário)
- [ ] Step 2: Diagnóstico
  - [ ] 2.1 É problema de processo, pessoas, ou prioridade?
  - [ ] 2.2 Aplicar filtro de alavancagem: fazer, delegar, ou automatizar?
  - [ ] ⛔ GATE: Se resposta é "delegar" → questionar ANTES de executar
- [ ] Step 3: Ação (varia por módulo)
  - [ ] 3.1 Escolher módulo relevante (tasks/delegação/feedback/etc.)
  - [ ] 3.2 Executar workflow do módulo
  - [ ] ⛔ GATE: Feedback para equipe → confirmar com usuário antes
  - [ ] ⛔ GATE: Decisão de delegação → confirmar com usuário antes
- [ ] Step 4: Output
  - [ ] 4.1 Gerar artefato (task, roteiro, plano)
  - [ ] 4.2 Validar contra pre-delivery checklist
```

## Contexto

O usuário está em transição de 100% operacional para liderança. Primeira vez gerenciando pessoas. Equipe junior e crescendo.

- **Willy:** chefe/mentor — espera crescimento como líder
- **Hygor:** freela junior, precisa de contexto claro mas executa
- **Jonas:** quase estagiário, precisa acompanhamento próximo
- **Novas contratações:** vão entrar, processo precisa escalar
- **Ferramentas:** ClickUp (kanban), WhatsApp/Telegram (comunicação)

## Princípios

1. **Processo mínimo viável.** Equipe de 3-5 não precisa de Scrum completo. Se ritual não gera valor, mata.
2. **Task boa > líder presente.** Task bem escrita = junior executa sozinho. Mal escrita = você vira gargalo.
3. **80% por outro > 100% por você.** Delegar libera tempo pra coisa mais importante. Perfeição não escala.
4. **Consistência > perfeição.** Daily de 10min todo dia vale mais que reunião perfeita 1x/mês.
5. **Fixed time, variable scope.** Nunca prometa escopo fixo em prazo fixo. Defina appetite, ajuste escopo.
6. **Transparência.** Diga que está aprendendo. Peça feedback sobre sua gestão. Isso gera confiança.

## Módulo 1: Quebrar PRD em Tasks

Load `references/tasks-templates.md` para templates completos e exemplos.

**Processo:**
1. Leia o PRD (da skill product-discovery-prd ou outro doc)
2. Identifique fluxos principais
3. Quebre em tasks atômicas — cada uma com entrega verificável
4. Ordene por dependência
5. Estime esforço (P/M/G) — task >4h provavelmente pode ser quebrada
6. Agrupe em waves (Wave 1 = fluxo principal, Wave 2 = complementar, Wave 3 = polimento)

**Regras críticas:**
- Task sem critério de aceitação = task mal escrita. SEMPRE inclua
- Task deve ter UM responsável. "Patrick e Hygor" não é responsável
- Equipe só começa Wave 2 quando Wave 1 tá concluída e validada

## Módulo 2: Delegação

Load `references/delegacao-frameworks.md` para frameworks completos.

⛔ **GATE: Antes de sugerir delegação, confirme com o usuário: "Vou sugerir delegar isso pra [pessoa]. Faz sentido dado a carga atual dela?"**

**Framework rápido — 5 componentes:** O QUÊ, POR QUÊ, COMO (proporcional à senioridade), QUANDO (prazo claro), VERIFICAÇÃO (critérios).

**Calibração rápida:**
- **Jonas:** passo a passo, check-in diário, confirma antes de agir
- **Hygor:** resultado + restrições, check a cada 2-3 dias, decide coisas pequenas
- **Sênior futuro:** só objetivo, check semanal, autonomia alta

**Decision Zones (Green/Yellow/Red):** defina QUAIS decisões cada pessoa toma sem consultar. Comunique pro-ativamente. Reduz ~70% das interrupções.

## Módulo 3: Rituais

Load `references/rituais-equipe.md` para templates e roteiros completos.

**Rituais mínimos pra equipe <5:**
- **Weekly sync** (30min, 1x/semana) — alinha a semana, resolve bloqueios
- **Daily async** (0min seu tempo) — cada pessoa manda 3 perguntas no ClickUp até 10h
- **1:1 semanal** (30min, com cada pessoa) — sobre a PESSOA, não sobre tasks
- **Retro quinzenal** (30min) — 1 ação concreta por retro, não 10

## Módulo 4: Conversas Difíceis

Load `references/conversas-dificeis.md` para roteiros detalhados por tipo.

⛔ **GATE: Antes de gerar roteiro de feedback, pergunte: "Com quem? Qual situação? O que quer que mude? Qual seu medo?"**

**Framework central: SCI (Situação-Comportamento-Impacto)**
1. Descreva a SITUAÇÃO (fato)
2. Descreva o COMPORTAMENTO específico
3. Descreva o IMPACTO

**Regra de ouro:** Foque no comportamento, nunca na pessoa.
- "Essa task ficou incompleta" -- correto
- "Você é desorganizado" -- errado

## Módulo 5: Priorização

Load `references/priorizacao-frameworks.md` para todos os frameworks.

**Decisão rápida — qual framework usar:**
- Dia a dia → Impacto x Esforço (matriz 2x2)
- Backlog de produto → RICE
- Experimentos rápidos → ICE
- Múltiplos projetos competindo → WSJF
- Entender expectativa do usuário → Kano
- Dependências entre tasks → Caminho Crítico

**Processo prático:**
1. Liste tudo que tá "urgente"
2. Pra cada: "Se NÃO fizer essa semana, o que acontece de CONCRETO?"
3. Se resposta vaga → não é urgente
4. Se mais de 3 no topo → algo tá errado
5. O que ficou no fundo — MATA

## Módulo 6: Acompanhamento

**Regra de ouro:** Pergunte sobre RESULTADO, não sobre PROCESSO.

**Intent-based leadership (por senioridade):**
- Jonas: "me avisa o que pretende fazer ANTES" — espera ok
- Hygor: "me avisa, se não responder em 2h, segue" — silêncio = ok
- Sênior futuro: "faz e me conta depois" — autonomia total

**Sinais de alerta:**
- Task no "Fazendo" há +3 dias sem update
- "Tá quase pronto" por +2 dias
- Junior que não pergunta (provavelmente tá perdido, não confiante)

## Módulo 7: Stakeholders e Ciclos

Load `references/stakeholders-gestao.md` para DACI e gestão de stakeholders.
Load `references/ciclos-trabalho.md` para Shape Up, DORA metrics, ClickUp setup.

**Demanda não planejada:** "Se a gente fizer isso, o que sai do sprint atual?"

**Shape Up resumo:** Fixed time, variable scope. Appetite (quanto vale investir) > estimativa. Shaping antes de passar pra equipe. Cooldown entre ciclos.

## Anti-Patterns

- **"Mais rápido eu fazer"** → Compra velocidade hoje, vende escala amanhã. Toda vez que faz em vez de ensinar, acumula dívida de delegação.
- **Task vaga** → "Fazer a tela de login" não é task. Sem critério de aceitação, sem contexto, sem chance de o junior acertar de primeira.
- **Microgerenciar vs abandonar** → Acompanhar = perguntar COMO ESTÁ. Microgerenciar = dizer COMO FAZER. São coisas diferentes.
- **Urgência = ansiedade** → Antes de priorizar: "Isso é urgente de verdade ou tô confundindo urgência com ansiedade?"
- **Ritual sem valor** → Se a retro é só reclamação sem ação, mata. Processo existe pra servir, não pra existir.
- **Feedback genérico** → "Precisa melhorar" não é feedback. SCI: situação + comportamento + impacto, sempre.
- **Gestão sem contexto** → Dar conselho pra time de 3 como se fosse time de 30 (IRON LAW).

## Pre-Delivery Checklist

Antes de entregar qualquer artefato de gestão ao usuário:

- [ ] Contexto da equipe foi perguntado (quem, senioridade, carga)?
- [ ] Filtro de alavancagem aplicado (fazer, delegar, ou automatizar)?
- [ ] Tasks têm: título com verbo, contexto, critérios de aceitação, UM responsável?
- [ ] Prazos são reais (não "quando puder")?
- [ ] Feedback/delegação passaram por gate de confirmação com usuário?
- [ ] Output é acionável (não conselho genérico)?
- [ ] Complexidade proporcional ao tamanho da equipe?

## Quando NÃO usar

- **Ajuda técnica pura** (código, SQL, n8n) sem componente de gestão → use skill técnica diretamente
- **Criar PRD** → use **product-discovery-prd**
- **Comunicação com cliente externo** → use **comunicacao-clientes**
- **Implementar feature** → use **sdd**
- **Dúvida sobre qual skill usar** → use **maestro**
- **Agendar algo** → use **schedule**

## Integration

| Contexto | Skill | Quando |
|----------|-------|--------|
| PRD pronto, precisa virar tasks | **product-discovery-prd** → esta skill | Módulo 1 |
| Task delegada envolve comunicação com cliente | esta skill → **comunicacao-clientes** | Módulo 2/7 |
| Feature precisa ser implementada | esta skill → **sdd** | Após tasks criadas |
| Precisa decidir qual skill usar | **maestro** | Quando ambíguo |
| Agendar ritual ou lembrete | **schedule** | Módulo 3 |
| Reporte diário/semanal | esta skill | Use formato do CLAUDE.md |
