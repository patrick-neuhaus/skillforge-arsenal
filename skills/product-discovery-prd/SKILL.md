---
name: product-discovery-prd
description: "Skill para conduzir discovery de produto e gerar PRDs otimizados para Lovable e outras ferramentas de desenvolvimento. Use esta skill SEMPRE que o usuário mencionar: novo projeto, nova feature, PRD, discovery, briefing, especificação, 'quero construir', 'preciso de um app', 'vou fazer um sistema', 'me ajuda a pensar no que construir', MVP, escopo, requisitos, ou qualquer variação que indique que algo novo vai ser planejado ou especificado — mesmo que o usuário não use a palavra 'PRD' explicitamente. Também use quando o usuário disser que vai 'jogar no Lovable' ou 'mandar pro Lovable' algo que ainda não tem especificação clara. Se houver dúvida se o usuário precisa de discovery ou já sabe o que quer, USE esta skill — é melhor perguntar do que deixar passar. NÃO use se o usuário já tem PRD pronto e só quer revisar — nesse caso, dê feedback direto sem acionar a skill. Se o pedido é implementação (código, SQL, workflow), use a skill técnica apropriada."
---

# Product Discovery & PRD Generator v5

## Visão geral

Esta skill conduz o usuário por um processo de discovery e gera um PRD em formato .md otimizado para ser consumido por AI coding tools (Lovable, Cursor, Bolt) ou usado como briefing técnico (n8n/Supabase).

O usuário geralmente chega com um rascunho mental — sabe o que quer mas não estruturou. O papel desta skill é transformar ideia vaga em especificação precisa o suficiente pra uma IA executar sem ambiguidade.

## Princípios

1. **Extrair, não inventar.** O objetivo é tirar da cabeça do usuário o que ele já sabe. Não assume nada. Pergunta.
2. **Problema antes de solução.** Nunca aceite a primeira ideia como definitiva. Cave até o problema raiz.
3. **Questionar antes de documentar.** "Você precisa mesmo disso no MVP?" é uma pergunta válida.
4. **MVP primeiro, sempre.** Cortar escopo é mais valioso do que adicionar.
5. **Output AI-first.** O PRD não é pra humano ler bonito — é pra uma IA entender com precisão e executar sem ambiguidade.
6. **Sem tasks.** O PRD não inclui breakdown de tasks. Isso é papel da skill de Tech Lead & PM.

## Fluxo de trabalho

### Fase 1: Entendimento inicial

NÃO faça todas as perguntas de uma vez — agrupe em blocos de 2-3 e aprofunde conforme as respostas.

**Bloco 1 — O problema (não a solução):**

O usuário vai chegar falando da SOLUÇÃO ("quero um app que faz X"). Seu trabalho é voltar pro PROBLEMA.

- O que você quer construir? (deixe falar livremente)
- Qual o problema que isso resolve? O que acontece HOJE sem essa solução?
- Quem sofre com esse problema? Com que frequência?
- Por que agora? O que muda se não fizer?

**Mom Test (Rob Fitzpatrick) — regras pra extrair verdade:**
- NUNCA "você acha que usariam isso?" → "como vocês resolvem isso hoje?"
- NUNCA "você pagaria por isso?" → "quanto tempo/dinheiro gastam com isso hoje?"
- NUNCA sobre o futuro ("você usaria se...") → sobre o passado ("quando foi a última vez que...")

Se o usuário disser "meu cliente quer X", questione: "Ele DISSE que quer X ou ele tá SOFRENDO com um problema que você acha que X resolve?"

**Declaração do Problema:**
"Nós observamos que [estado atual] faz com que [pessoas] sofram com [problema], o que causa [consequência]."

**Bloco 2 — Contexto técnico:**
- App web, automação, integração, ou mix?
- Qual a stack? (Lovable + Supabase? n8n? Outro?)
- Tem algo já construído? (banco, API, fluxo existente)
- Integrações com sistemas externos? Quais?

**Bloco 3 — Usuários e escopo:**
- Quem vai usar? (perfil, quantidade esperada)
- Fluxo principal? (caminho feliz do início ao fim)
- Autenticação? Roles diferentes?
- Regras de negócio não óbvias?

Se mais de um tipo de usuário, crie **personas simplificadas** (máx 3):
- Nome + papel (ex: "Ana, gerente de operações")
- O que FAZ no sistema
- Problema principal DELA
- NÃO inclua idade, hobby, foto

**Bloco 4 — MVP e prioridade:**

Use **How Might We** (HMW):
- "Como podemos [resolver problema X] para [persona Y] de forma que [resultado Z]?"
- Gere 2-3 HMWs e valide com o usuário

Depois:
- Se pudesse lançar com UMA funcionalidade, qual seria?
- O que é MVP vs "legal ter depois"?
- Tem prazo? Restrição de orçamento/tempo?

**Bloco 5 — UX e visual (se app web):**
- Referência visual? (outro app, screenshot, wireframe)
- Layout? (sidebar, tabs, dashboard, lista)
- Mobile-first ou desktop-first?
- Branding? (cores, logo, tom)

### Fase 2: Validação de Risco

Antes de estruturar a solução, valide os riscos com duas técnicas:

**Assumption Mapping (David Bland — Testing Business Ideas):**

Mapeie as suposições do projeto numa matriz 2×2:
- Eixo Y: Importância pra o sucesso (alta ↔ baixa)
- Eixo X: Evidência que temos (forte ↔ fraca)

O quadrante **alta importância + pouca evidência** = "Leap of Faith" — teste ANTES de construir.

Categorize cada suposição:
- **Desirability**: "Eles querem isso?" (demanda real)
- **Feasibility**: "Conseguimos fazer?" (técnico)
- **Viability**: "O negócio se sustenta?" (financeiro)

Apresente as top 3 suposições de risco pro usuário: "Essas são as apostas mais arriscadas desse projeto. Tem evidência pra alguma delas ou estamos no escuro?"

**Pre-mortem:**

"Imagina que passaram 3 meses e esse projeto fracassou completamente. Por que fracassou?"

Categorize os riscos:
- **Project killers** — bloqueios que impedem o lançamento
- **Known-but-unsaid** — coisas que a equipe suspeita mas ninguém fala
- **Execution risks** — desafios de viabilidade técnica

Se o projeto tiver riscos graves no pre-mortem, discuta mitigações ANTES de seguir pra estruturação.

### Fase 3: Oportunidades e Soluções (Opportunity Solution Tree)

Organize o que foi levantado usando a árvore de Teresa Torres:

```
Outcome desejado (resultado de negócio)
├── Oportunidade 1 (problema/necessidade)
│   ├── Solução A
│   └── Solução B
├── Oportunidade 2
│   ├── Solução C
│   └── Solução D (escolhida pro MVP)
└── Oportunidade 3 (deixar pra depois)
    └── Solução E
```

**Complemento — Impact Mapping (Gojko Adzic):**

Se o projeto envolver múltiplos stakeholders ou for estratégico, use Impact Mapping pra conectar a árvore ao negócio:

```
Goal (objetivo de negócio)
└── Actor (quem influencia)
    └── Impact (que mudança de comportamento)
        └── Deliverable (o que entregar)
```

Impact Mapping responde "que mudança de comportamento gera valor"; OST responde "que dor do cliente cria essa oportunidade de mudança".

Se o projeto for simples (1 problema, 1 solução óbvia), pule e vá pra Fase 4.

### Fase 4: Estruturação (User Story Mapping)

Organize a implementação:

1. **Eixo horizontal (backbone):** Atividades principais em ordem cronológica
2. **Eixo vertical (profundidade):** Tarefas do mais essencial ao menos essencial
3. **Linha do MVP:** Separa o que entra do que fica pra depois
4. **Dividir em Waves** (se MVP for grande):
   - **Wave 1:** Mínimo absoluto pra validar a hipótese. 1-2 fluxos principais.
   - **Wave 2:** Complementos que tornam usável no dia a dia.
   - **Wave 3:** O que completa o MVP.

Cada wave testável sozinha. Se Wave 1 não funciona sem Wave 2, tá errado.

No PRD, marque cada fluxo/tela: `[Wave 1]`, `[Wave 2]`, `[Wave 3]`.

### Fase 5: Validação e confronto

ANTES de gerar o PRD:

1. **Resuma** em 3-5 frases e peça confirmação
2. **Declare a hipótese:** "Nós acreditamos que [fazendo X] para [pessoa Y] vamos [resultado Z]. Saberemos que é verdade quando [métrica/evidência]."
3. **North Star Metric:** Qual a métrica única que define sucesso? (ex: "documentos processados por semana", "leads qualificados por dia"). Pode ser de atenção (DAU, sessões), transação (conversões, valor), ou produtividade (tarefas completas, itens processados).
4. **Appetite (Shape Up — Ryan Singer):** "Quanto tempo/esforço QUER gastar nisso?" O escopo se adapta ao appetite, não o contrário.
5. **Aponte inconsistências** — se algo contradiz, fala
6. **Questione escopo** — demais pro appetite = sugere cortes
7. **Identifique buracos** — informação crítica faltando

### Fase 6: Geração do PRD (AI-First)

O PRD agora é otimizado pra AI coding tools. Isso muda a estrutura:

```markdown
# [Nome do Projeto]

## Resumo
[1 frase: o que é, pra quem, qual problema resolve]

## Declaração do problema
Nós observamos que [estado atual] faz com que [pessoas] sofram com [problema], o que causa [consequência].

## Hipótese
Nós acreditamos que [fazendo X] para [pessoa Y] vamos [resultado Z]. Saberemos que é verdade quando [métrica/evidência].

## North Star Metric
[Métrica única que define sucesso. Ex: "Documentos SST processados sem erro por semana"]

## Stack técnica
- Frontend: [ex: Lovable (React + Tailwind + shadcn/ui)]
- Backend: [ex: Supabase (PostgreSQL + Auth + Edge Functions)]
- Integrações: [ex: Evolution API, n8n, Kommo]

## Usuários
[Quem usa, roles, volume esperado]
[Personas se houver: nome + papel + problema + o que faz]

## Fluxos principais

### Fluxo 1: [Nome] [Wave N]

**Trigger:** [O que inicia este fluxo]
**Resultado:** [O que acontece no final]

1. [Passo 1] → Estado: [loading/success/error]
2. [Passo 2] → Estado: [...]
3. [Passo 3] → Estado: [...]

**Comportamentos explícitos:**
- Quando [condição X]: faça [ação Y]
- Quando [erro Z]: mostre [mensagem W]
- Quando [lista vazia]: mostre [empty state com texto e CTA]

**Input/Output de exemplo:**
```json
{
  "input": { "campo1": "valor", "campo2": 123 },
  "output": { "status": "success", "resultado": "..." }
}
```

### Fluxo 2: [Nome] [Wave N]
...

## User Stories / Job Stories
[Apenas pros fluxos principais do MVP]

User Story: "Como [persona], eu quero [ação] para que [benefício]"
Job Story: "Quando [situação], eu quero [motivação] para que [resultado]"

Critérios INVEST por story.

## Regras de negócio
- [Regra 1]: [descrição clara e sem ambiguidade]
- [Regra 2]: ...

## Modelo de dados (se aplicável)
[Tabelas, campos essenciais, relacionamentos. Incluir tipos.]

## Telas / Páginas (se app web) [Wave N]

### [Nome da tela]
- **Objetivo:** [o que o usuário faz aqui]
- **Estados:** empty | loading | filled | error | success
- **Elementos:** [componentes, campos, botões]
- **Ações:** [o que o usuário pode fazer + resultado de cada ação]
- **Regras:** [comportamentos condicionais]

## Integrações externas
- [Sistema]: [o que entra, o que sai, quando dispara, formato]

## NÃO construa (fora do escopo MVP)
[Lista explícita e específica do que NÃO entra]
- NÃO: [feature X] — motivo
- NÃO: [feature Y] — motivo
- NÃO: [otimização Z] — motivo

## Notas para implementação
[Decisões técnicas, padrões, preferências, ordem sugerida de build]
- Sequência recomendada: schema → auth → fluxo principal → UI → error handling
- [Decisão de webhook: direto vs Edge Function + Fila]
- [Libs específicas, padrões de naming, etc]
```

### Regras do output AI-first

1. **Descrição em 1 frase.** O resumo do projeto deve caber em 1 frase. Se precisa de mais, o escopo tá grande demais.
2. **User flows numerados.** Cada passo do fluxo com número, estado, e resultado esperado.
3. **Comportamentos explícitos.** "Quando X, faça Y" pra CADA interação não-trivial. AI coding tools executam literalmente — se não especificou, vai chutar.
4. **Estados obrigatórios.** Toda tela/componente deve definir: empty, loading, filled, error, success. AI que não sabe o empty state inventa algo feio.
5. **Input/Output de exemplo.** Pra fluxos com dados complexos (OCR, integrações, formulários), inclua JSON de exemplo. Modelos performam dramaticamente melhor com exemplos concretos.
6. **Lista de exclusões.** "NÃO construa" é TÃO importante quanto "construa". Sem isso, AI tools adicionam features não solicitadas.
7. **Modelo de dados com tipos.** Se incluir, use tipos explícitos (`UUID`, `TIMESTAMPTZ`, `TEXT`, `JSONB`), não descrições vagas.
8. **Português brasileiro** exceto termos técnicos universais.
9. **Dois arquivos sempre.** PRD MVP e Roadmap pós-MVP são SEPARADOS.
10. **Sequência de build.** Na seção "Notas para implementação", sugira a ordem: schema → auth → fluxo principal → UI → error handling. AI tools constroem melhor com phasing explícito.

### Fase 7: Roadmap pós-MVP

Gere segundo arquivo `roadmap-pos-mvp.md`:

```markdown
# [Nome do Projeto] — Roadmap pós-MVP

## Features cortadas do MVP
- [Feature]: [por que cortada] → [quando implementar]

## Suposições não validadas
[Top 3 do Assumption Mapping que ainda não têm evidência]

## Riscos identificados (pre-mortem)
[Riscos do pre-mortem + mitigações planejadas]

## Segurança e permissões
[MVP básico vs produção]

## Performance e escalabilidade
[O que no MVP não importa mas em produção sim]

## Integrações adiadas
- [Sistema]: [o que faria, complexidade estimada]

## UX e melhorias visuais
[Funcional mas não ideal no MVP]

## Monitoramento
- Logs, alertas, métricas, health checks

## Estimativa de esforço
1. [Item] — esforço: [baixo/médio/alto] — impacto: [baixo/médio/alto]
```

### Regras do roadmap
1. Só inclua o que veio do discovery.
2. Seja específico ao projeto.
3. Estimativa honesta.

## Variações por tipo de projeto

### Para apps web (Lovable)
- Foco em telas, fluxos visuais, componentes com estados
- "Telas / Páginas" detalhada com empty/loading/error states
- Responsividade explícita
- Referência visual quando houver

### Para automações (n8n)
- Foco em triggers, condições, outputs
- "Workflows" no lugar de "Telas"
- Job Stories > User Stories
- Decisão de webhook obrigatória: direto vs Edge Function + Fila

### Para projetos mistos
- Separe frontend, backend, automação
- Especifique QUEM chama QUEM
- Onde cada parte vive (Lovable, Supabase, n8n)

## Frameworks complementares (use quando relevante)

### Lean UX Canvas (Jeff Gothelf)
Use quando o projeto precisar de alinhamento OKR + JTBD:
- Box 1: Business Problem (Objective)
- Box 2: Success Metrics (Key Results)
- Box 3: Assumptions
- Box 4: JTBD + Métricas de comportamento

### Dual Track Agile
Use quando houver discovery contínuo em paralelo com delivery:
- Track 1 (Discovery): validando suposições, entrevistas, protótipos
- Track 2 (Delivery): construindo o que já foi validado

Sugira esses frameworks quando o contexto pedir — não force em todo projeto.

## Quando NÃO usar esta skill

- PRD pronto e só quer revisar → feedback direto
- Ajuda com implementação → skill técnica apropriada
- Task pequena e isolada → faz direto

## Integração com outras skills

- **Lovable Knowledge:** Após gerar PRD, sugira gerar Project Knowledge. PRD = O QUE, Knowledge = COMO.
- **Tech Lead & PM:** PRD pronto → skill de Tech Lead gera tasks e briefings.
- **Supabase Architect:** Se PRD inclui modelo de dados, a skill de Supabase valida e refina.
- **n8n Architect:** Se PRD inclui automações, a skill de n8n define implementação.

## Exemplo de interação

**Usuário:** "Quero fazer um app pra gerenciar documentos de SST, com OCR"

**Skill (Bloco 1):**
"Antes de pensar no app, me ajuda a entender o problema:
1. O que acontece HOJE com esses documentos? Como são gerenciados?
2. Quem sofre com isso? Você, o cliente, a equipe?
3. O OCR é pra resolver qual problema específico?"

**Usuário responde...**

**Skill (Declaração do problema):**
"Deixa eu checar: 'Nós observamos que os documentos de SST chegam em PDF e são conferidos manualmente, o que faz com que a equipe gaste X horas/semana e cometa erros de validação, causando risco de multa.' É isso?"

**Skill (Assumption Mapping):**
"Antes de seguir, as 3 suposições mais arriscadas desse projeto:
1. Que o OCR do Gemini consegue extrair campos de documentos SST com precisão suficiente (feasibility, pouca evidência)
2. Que a equipe vai adotar o sistema no dia a dia (desirability, sem evidência)
3. Que o volume justifica o investimento (viability, alguma evidência)

A suposição 1 é um project killer — se o OCR não funciona, nada funciona. Quer testar isso antes de construir o app?"

**Skill avança pelos blocos, estrutura (User Story Map), valida, e gera os 2 .md.**
