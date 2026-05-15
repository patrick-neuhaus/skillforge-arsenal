---
name: product-discovery-prd
description: "Conduz discovery de produto e gera PRDs otimizados para Lovable, Cursor, Bolt e outras AI coding tools. Use esta skill para: criar PRD, planejar projeto, definir escopo, fazer discovery, pesquisar requisitos, validar hipótese, analisar personas, desenhar fluxos, revisar briefing, construir especificação. Triggers: novo projeto, nova feature, PRD, discovery, briefing, especificação, 'quero construir', 'preciso de um app', 'vou fazer um sistema', 'me ajuda a pensar', MVP, escopo, requisitos, 'jogar no Lovable', 'mandar pro Lovable'. Product discovery and PRD generation — create, plan, design, validate, review, analyze, build, define, research, discover product specs for AI-first development."
---

# Product Discovery & PRD Generator v6

IRON LAW: NUNCA escreva um PRD sem conversar com o usuário sobre QUEM é o usuário final. PRD sem personas é lista de features, não especificação de produto. Sem problema claro, sem PRD.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--quick` | Pula discovery, gera PRD direto de briefing existente | false |
| `--full` | Discovery completo com todas as fases | true |
| `--review` | Revisa PRD existente contra checklist de qualidade | false |

## Workflow

```
Product Discovery Progress:

- [ ] Step 1: Entender o Problema ⚠️ REQUIRED
  - [ ] 1.1 Extrair problema real (não a solução)
  - [ ] 1.2 Identificar quem sofre (personas)
  - [ ] 1.3 Mapear contexto técnico e escopo
  - [ ] 1.4 Definir MVP e appetite
  - [ ] ⛔ GATE: Declaração do problema validada pelo usuário
- [ ] Step 2: Validar Riscos
  - [ ] 2.1 Assumption Mapping (top 3 riscos)
  - [ ] 2.2 Pre-mortem
  - [ ] 2.3 Oportunidades e soluções (OST)
  - [ ] ⛔ GATE: Riscos apresentados e discutidos
- [ ] Step 3: Gerar PRD ⚠️ REQUIRED
  - [ ] 3.1 Estruturar fluxos e waves
  - [ ] 3.2 Gerar PRD (arquivo .md)
  - [ ] 3.3 Gerar roadmap pos-MVP (arquivo .md separado)
  - [ ] ⛔ GATE: Usuário revisa PRD antes de considerar pronto
- [ ] Step 4: Validação Final ⛔ BLOCKING
  - [ ] Run pre-delivery checklist
  - [ ] ⛔ GATE: Aprovação explícita do usuário
```

Se `--quick`: Pula Step 1-2, vai direto pro Step 3 usando briefing existente.
Se `--review`: Pula Step 1-2, avalia PRD existente contra o Pre-Delivery Checklist.

## Princípios

1. **Extrair, não inventar.** O objetivo é tirar da cabeça do usuário o que ele já sabe. Pergunta.
2. **Problema antes de solução.** Cave até o problema raiz antes de documentar qualquer coisa.
3. **MVP primeiro, sempre.** Cortar escopo é mais valioso do que adicionar.
4. **Output AI-first.** O PRD é pra IA entender e executar, não pra humano ler bonito.
5. **Sem tasks.** PRD não inclui breakdown de tasks — isso é papel da skill Tech Lead & PM.
6. **Dois arquivos sempre.** PRD MVP e Roadmap pos-MVP são SEPARADOS.

## Step 1: Entender o Problema ⚠️ REQUIRED

Load `references/discovery-workflow.md` para o roteiro completo de perguntas (5 blocos).

Resumo dos blocos:
1. **O Problema** — voltar da solução pro problema real. Usar Mom Test (Fitzpatrick).
2. **Contexto técnico** — stack, integrações, o que já existe.
3. **Usuários e escopo** — quem usa, fluxo principal, roles, regras de negócio.
4. **MVP e prioridade** — How Might We, appetite (Shape Up), cortes de escopo.
5. **UX e visual** — referências, layout, responsividade (se app web).

Perguntas por bloco, NÃO todas de uma vez. Aprofunde conforme respostas.

Se mais de 1 tipo de usuário, crie personas simplificadas (máx 3): nome + papel + o que faz + problema principal. Sem idade, hobby, foto.

⛔ **GATE:** Declaração do problema: "Nós observamos que [estado atual] faz com que [pessoas] sofram com [problema], o que causa [consequência]." Valide com o usuário antes de prosseguir.

## Step 2: Validar Riscos

Load `references/discovery-frameworks.md` para Assumption Mapping, Pre-mortem, Impact Mapping, e outros frameworks.

1. **Assumption Mapping** — mapeie top 3 suposições (desirability, feasibility, viability). Apresente: "Essas são as apostas mais arriscadas. Tem evidência pra alguma?"
2. **Pre-mortem** — "3 meses, projeto fracassou. Por quê?" Se tiver project killer sem mitigação, resolva ANTES de prosseguir.
3. **OST (Teresa Torres)** — organize oportunidades → soluções. Se projeto simples (1 problema, 1 solução), pule.
4. **Hipótese** — "Nós acreditamos que [fazendo X] para [Y] vamos [Z]. Saberemos quando [métrica]."
5. **North Star Metric** — métrica única de sucesso.

⛔ **GATE:** Riscos e hipótese validados com o usuário.

## Step 3: Gerar PRD ⚠️ REQUIRED

Load `references/prd-template.md` para template completo e regras AI-first.
Load `references/roadmap-template.md` para template do roadmap pos-MVP.

### Estruturação (User Story Mapping)

Antes de escrever, organize em waves:
- **Wave 1:** Mínimo absoluto pra validar hipótese. 1-2 fluxos.
- **Wave 2:** Complementos pra uso no dia a dia.
- **Wave 3:** O que completa o MVP.

Cada wave testável sozinha. Se Wave 1 depende de Wave 2, tá errado.

### Gerar dois arquivos

1. **PRD** — seguindo template AI-first (fluxos numerados, estados, comportamentos explícitos, I/O de exemplo, lista de exclusões)
2. **Roadmap pos-MVP** — features cortadas, suposições pendentes, riscos, próximos passos

⛔ **GATE:** Apresente o PRD completo ao usuário. Peça revisão explícita antes de considerar pronto.

## Step 4: Validação Final ⛔ BLOCKING

### Pre-Delivery Checklist

**Conteúdo:**
- [ ] Tem declaração do problema (não só descrição da solução)
- [ ] Tem personas ou descrição clara de quem usa
- [ ] Tem hipótese com métrica de validação
- [ ] Tem North Star Metric
- [ ] Fluxos numerados com trigger → resultado → estados
- [ ] Comportamentos explícitos ("Quando X, faça Y") pra interações não-triviais
- [ ] Estados obrigatórios por tela: empty, loading, filled, error, success
- [ ] Lista de exclusões ("NÃO construa") com motivo
- [ ] Modelo de dados com tipos explícitos (se aplicável)
- [ ] Sequência de build sugerida

**Estrutura:**
- [ ] Resumo cabe em 1 frase
- [ ] PRD e Roadmap são arquivos separados
- [ ] Waves marcadas em cada fluxo/tela
- [ ] Português brasileiro (exceto termos técnicos)

**Validação:**
- [ ] Usuário revisou e aprovou declaração do problema
- [ ] Usuário revisou e aprovou PRD final
- [ ] Nenhum project killer sem mitigação

## Anti-Patterns

- **Pular direto pra solução** — usuário diz "quero um app" e você começa a documentar features sem entender o problema. VOLTE pro problema.
- **PRD sem personas** — Iron Law. Quem usa? Se não sabe, não escreva PRD.
- **Aceitar tudo sem questionar** — "Você precisa mesmo disso no MVP?" é pergunta obrigatória. Cortar escopo salva projetos.
- **Inventar features** — Discovery é EXTRAIR do usuário, não ADICIONAR do seu repertório.
- **PRD genérico** — "O sistema deve ser responsivo" não é especificação. Cada comportamento precisa ser explícito pra AI tool executar.
- **Telas sem estados** — AI coding tool que não sabe o empty state inventa algo feio. SEMPRE definir empty/loading/error/success.
- **Roadmap solto** — roadmap precisa vir do discovery, não ser lista genérica de "nice to have".
- **Assumption Mapping como formalidade** — se fez o mapping e ignorou o project killer, não fez nada.

## When NOT to use

- **PRD pronto, quer revisar** → use `--review` ou dê feedback direto sem acionar a skill
- **Implementação** (código, SQL, workflow) → use skill técnica apropriada (SDD, n8n, Supabase)
- **Task pequena e isolada** → faz direto, não precisa de discovery
- **Já tem spec técnica** → pule direto pra SDD
- **Quer só o template** → Load `references/prd-template.md` direto

## Integration

| Etapa | Skill | Quando |
|-------|-------|--------|
| Pos-PRD | **SDD** | PRD alimenta a fase de Research do SDD. PRD = O QUE, Spec = COMO |
| Pos-PRD | **Lovable Knowledge** | Gerar Project Knowledge a partir do PRD. PRD = spec, Knowledge = padrões |
| Pos-PRD | **Tech Lead & PM** | PRD pronto → gera tasks e briefings pra equipe |
| Se app web | **UI Design System** | PRD define o que, Design System define a aparência |
| Se app web | **UX Audit** | Após implementar, auditar UX contra o que o PRD especificou |
| Se modelo de dados | **Supabase DB Architect** | PRD inclui schema → Supabase valida e refina |
| Se automação | **N8n Architect** | PRD inclui workflows → n8n define implementação |
| Orquestração | **Maestro** | Se não sabe por onde começar, Maestro direciona pra cá |

## Exemplo de Interação

**Usuário:** "Quero fazer um app pra gerenciar documentos de SST, com OCR"

**Skill (Bloco 1):** "Antes de pensar no app, me ajuda a entender o problema:
1. O que acontece HOJE com esses documentos? Como são gerenciados?
2. Quem sofre com isso? Você, o cliente, a equipe?
3. O OCR é pra resolver qual problema específico?"

**Skill (Assumption Mapping):** "As 3 suposições mais arriscadas:
1. OCR do Gemini extrai campos SST com precisão suficiente (feasibility, pouca evidência)
2. Equipe vai adotar o sistema (desirability, sem evidência)
3. Volume justifica investimento (viability, alguma evidência)

A suposição 1 é project killer. Quer testar antes de construir o app?"

**Skill avança pelos blocos, valida, e gera 2 arquivos .md.**
