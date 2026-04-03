# Padrões Agentic pra Skills — Referência

Última atualização: 2026-03-27

Consulte este arquivo quando estiver na **Fase 1 (Discovery)** ou **Fase 3 (Escrita)** e precisar decidir qual padrão arquitetural usar pra skill.

---

## Por que isso importa

Skills complexas não são apenas texto — são programas que orquestram comportamento. O padrão arquitetural determina como a skill gerencia complexidade, paralelismo, e qualidade do output. Escolher o padrão errado cria fragilidade; escolher o certo gera robustez sem complexidade desnecessária.

## Os 5 padrões

### 1. Linear (Sequential)

```
Input → Fase 1 → Fase 2 → Fase 3 → Output
```

**O que é:** Processo sequencial com fases claras. Cada fase recebe o output da anterior.

**Quando usar:**
- A maioria das skills (80%+)
- O processo tem ordem natural que não pode ser paralelizada
- Cada fase depende da anterior
- Complexidade moderada (3-6 fases)

**Exemplos reais:**
- Product Discovery & PRD: Discovery → Pesquisa → Estruturação → Template
- Comunicação com Clientes: Identificar tipo → Aplicar ACPR → Validar tom → Entregar

**Vantagens:** Simples, previsível, fácil de debugar. Se uma fase falha, sabe exatamente onde.

**Riscos:** Se uma fase depende de contexto muito grande das anteriores, pode ter context loss em skills longas.

**Dica:** Se o linear tá falhando por context loss, considere structured note-taking entre fases — a skill salva resumo do que decidiu em cada fase antes de seguir.

---

### 2. Pipeline Multi-Agente

```
Input → Agente 1 (Especialista) → Agente 2 (Verificador) → Agente 3 (Árbitro) → Output
```

**O que é:** Agentes especializados em sequência, cada um com papel distinto. O output de um é input do próximo. Crítico: cada agente tem viés e limitações diferentes, e o pipeline explora isso pra aumentar qualidade.

**Quando usar:**
- Quando o processo requer expertise isolada (cada agente "pensa diferente")
- Quando você precisa de contra-argumentos forçados (verificação adversarial)
- Quando a confiança no output precisa ser alta (auditoria, segurança)

**Exemplos reais:**
- Repo Review: Bug Finder → Bug Verifier → Final Arbiter
- Security Audit: Scanner → Verifier → Arbiter
- Skill Builder (loop de melhoria): Generator → Grader → Comparator → Analyzer

**Vantagens:** Cada agente tem contexto limpo e focado. Verificação adversarial reduz falsos positivos.

**Riscos:** Latência (sequencial). Cada agente consome tokens. Se o Agente 1 tem recall baixo, os seguintes não podem compensar.

**Regras de implementação:**
- Cada agente recebe instrução INDEPENDENTE (não copia a skill inteira)
- O handoff entre agentes deve ser estruturado (JSON com achados, evidências, confiança)
- O último agente tem poder de veto (pode rejeitar achados dos anteriores)

---

### 3. Fan-Out/Gather (Parallel)

```
                  ┌→ Agente A (Segurança) ──┐
Input → Splitter ─┼→ Agente B (UX)         ─┼→ Synthesizer → Output
                  └→ Agente C (Performance) ─┘
```

**O que é:** Tarefas independentes rodam em paralelo, cada uma com escopo isolado. Um sintetizador consolida os resultados.

**Quando usar:**
- Quando análises são independentes entre si
- Quando latência importa (paralelo > sequencial)
- Quando cada dimensão tem framework próprio

**Exemplos reais:**
- Audit combo: UX Audit + Security Audit + Infra Audit simultâneos
- Code Review com dimensões: Security + Style + Performance + Architecture em paralelo

**Vantagens:** Reduz latência drasticamente. Cada agente tem contexto limpo e focado na sua dimensão.

**Riscos:** O Synthesizer é crítico — se consolidar mal, perde o valor do parallelismo. Pode ter achados contraditórios entre agentes.

**Regras de implementação:**
- Cada agente paralelo retorna output estruturado (mesma schema) pra facilitar consolidação
- O Synthesizer recebe APENAS os outputs, não o contexto completo de cada agente
- Priorizar achados por severidade/impacto, não por agente de origem
- Deduplica achados que múltiplos agentes encontraram

---

### 4. Reflection (Generator → Critic)

```
Input → Generator → Output Draft → Critic → Feedback → Generator (v2) → Output Final
```

**O que é:** O modelo gera um output, depois avalia criticamente, e refina. Pode iterar N vezes.

**Quando usar:**
- Quando qualidade do output é mais importante que velocidade
- Quando o modelo tende a errar de formas previsíveis que ele mesmo pode detectar
- Quando o domínio tem critérios claros de qualidade (checklist, rubric)

**Exemplos reais:**
- Skill Builder: Escreve skill → Valida com checklist → Itera
- PRD: Gera template → Revisa contra critérios → Refina
- Prompt Engineer: Gera prompt → Testa mentalmente → Ajusta

**Vantagens:** Melhora qualidade sem input externo. Auto-correção baseada em critérios.

**Riscos:** O critic pode ser "bonzinho demais" (concordar com tudo). Solução: dar critérios ESPECÍFICOS e forçar o critic a encontrar pelo menos N problemas.

**Regras de implementação:**
- O critic deve ter critérios EXPLÍCITOS (não "avalie se tá bom")
- Limite de iterações (2-3 é o sweet spot, depois disso retornos decrescentes)
- O critic deve justificar cada crítica com evidência
- Se o critic não encontra problemas em 2 rodadas, pare — mais iterações = overthinking

---

### 5. Plan-and-Execute

```
Input → Planner (gera plano) → Executor (segue plano) → Verificador → Output
```

**O que é:** Separa o planejamento da execução. O planner cria um plano detalhado, o executor segue sem desviar. Pesquisas mostram 92% task completion rate e 3.6x speedup vs abordagem sequencial sem plano.

**Quando usar:**
- Tarefas longas com escopo variável
- Quando o modelo tende a se perder no meio da execução
- Quando o plano precisa de aprovação antes da execução

**Exemplos reais:**
- Projeto novo: Planner define scope → Executor implementa feature a feature
- Migração de banco: Planner mapeia mudanças → Executor aplica migrations
- Automação complexa: Planner define workflows → Executor configura n8n

**Vantagens:** O planner pode explorar alternativas sem custo de execução. O executor tem direção clara. Checkpoint natural entre plano e execução.

**Riscos:** Plano pode ficar desatualizado se a execução revela informações novas. O executor precisa ter autonomia pra ajustar.

**Regras de implementação:**
- O plano deve ser estruturado (não narrativo) — lista de steps com inputs/outputs esperados
- O executor marca cada step como done/failed/adjusted
- Se o executor precisa desviar do plano, ele DOCUMENTA por que antes de desviar
- Checkpoint: verificador roda após cada step crítico, não só no final

---

## Árvore de decisão

```
A skill precisa de verificação adversarial? (contra-argumentos, auditoria)
├── Sim → Pipeline Multi-Agente
└── Não
    ├── Tem análises independentes que podem rodar em paralelo?
    │   ├── Sim → Fan-Out/Gather
    │   └── Não
    │       ├── O output precisa de auto-avaliação antes de entregar?
    │       │   ├── Sim → Reflection
    │       │   └── Não
    │       │       ├── É uma tarefa longa com escopo variável?
    │       │       │   ├── Sim → Plan-and-Execute
    │       │       │   └── Não → Linear
    │       │       └──
    │       └──
    └──
```

**Regra de ouro:** Comece com Linear. Só suba de complexidade quando o Linear demonstrar falhas que o padrão mais complexo resolve. Complexidade prematura é pior que simplidade insuficiente.

---

## Combinações válidas

Padrões podem ser compostos:

- **Plan-and-Execute + Fan-Out:** Planner divide em tasks → tasks rodam em paralelo → Synthesizer consolida
- **Pipeline + Reflection:** Agente 1 gera → Agente 2 reflete e critica → Agente 3 decide
- **Fan-Out + Pipeline:** Análises paralelas → cada uma passa por verificação → Synthesizer final

Evite: composições de 3+ padrões. Se precisa disso, provavelmente a skill tá tentando fazer demais — quebre em skills menores.

---

## Fontes

- Anthropic: "Building effective agents" — patterns de orquestração
- Anthropic: "Effective context engineering for AI agents" — sub-agent architectures, compaction
- Paper "Plan-and-Execute" — 92% task completion rate benchmark
- CodeRabbit architecture — fan-out com agentes especializados paralelos
- Claude Code multi-agent review — pipeline adversarial
