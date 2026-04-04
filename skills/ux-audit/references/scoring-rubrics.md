# Scoring Rubrics — Metricas e Escalas

Escalas de classificacao e metricas quantitativas pra fundamentar recomendacoes.

---

## Escala de Severidade de Nielsen

Usada pra classificar TODO finding do audit.

| Nivel | Nome | Criterio | Acao | Cor no report |
|-------|------|----------|------|---------------|
| 0 | Nao e problema | Sem impacto na usabilidade | Nenhuma | — |
| 1 | Cosmetico | Usuario nota, tarefa nao afetada | Quando sobrar tempo | Azul |
| 2 | Menor | Leve confusao ou delay | Prioridade baixa | Amarelo |
| 3 | Maior | Dificulta significativamente a tarefa | Antes do proximo release | Laranja |
| 4 | Catastrofico | Bloqueia tarefa essencial | Imediatamente | Vermelho |

### Criterios pra classificar

- **Frequencia:** Acontece raramente ou toda vez?
- **Impacto:** O usuario consegue contornar ou fica preso?
- **Persistencia:** Acontece uma vez ou toda vez que o usuario tenta?

### Regras

- Se bloqueia tarefa essencial → sempre 4
- Se o usuario contorna mas perde tempo significativo → 3
- Se causa confusao momentanea mas nao impede → 2
- Se e notavel mas irrelevante pra tarefa → 1
- Na duvida entre dois niveis, use o mais alto (melhor prevenir)

---

## SUS (System Usability Scale)

Score de 0-100 (NAO e porcentagem). Media global: 68.

### 10 perguntas padrao

1. Eu acho que gostaria de usar este sistema com frequencia
2. Eu achei o sistema desnecessariamente complexo
3. Eu achei o sistema facil de usar
4. Eu acho que precisaria de suporte tecnico pra usar este sistema
5. Eu achei que as funcoes do sistema estao bem integradas
6. Eu achei que tem muita inconsistencia no sistema
7. Eu imagino que a maioria das pessoas aprenderia a usar rapido
8. Eu achei o sistema muito complicado de usar
9. Eu me senti confiante usando o sistema
10. Eu precisei aprender muitas coisas antes de usar o sistema

### Calculo

- Itens impares (1,3,5,7,9): score = resposta - 1
- Itens pares (2,4,6,8,10): score = 5 - resposta
- SUS = 2.5 x (soma de todos os scores)

### Interpretacao

| Score | Classificacao | Percentil | Grade (Sauro) |
|-------|--------------|-----------|---------------|
| 90+ | Excelente | Top 5% | A+ |
| 80-89 | Muito bom | Top 10% | A/B |
| 70-79 | Bom | Top 30% | C |
| 68 | Media global | 50% | C- |
| 50-67 | Abaixo da media | < 50% | D |
| < 50 | Inaceitavel | — | F |

### Quando usar
- O usuario tem dados de pesquisa com usuarios reais → use SUS como fundamentacao
- O usuario nao tem dados → sugira aplicar (10 perguntas, 5 minutos por usuario)
- Minimo de 5 usuarios pra ter significancia estatistica razoavel

---

## NASA-TLX (Task Load Index)

Mede carga cognitiva em 6 dimensoes, escala 0-100 cada.

| Dimensao | Pergunta | Quando e critica |
|----------|----------|-----------------|
| **Mental Demand** | Quanto esforco mental? | Formularios complexos, configuracoes |
| **Physical Demand** | Quanto esforco fisico? | Mobile com muitos toques, gestos complexos |
| **Temporal Demand** | Quanta pressao de tempo? | Timers, sessoes que expiram |
| **Performance** | Quao bem-sucedido se sentiu? | Tarefas com resultado ambiguo |
| **Effort** | Quanto esforco total? | Fluxos longos, multi-step |
| **Frustration** | Quanta frustracao? | Error recovery, retry loops |

### Quando usar
- Tarefas complexas onde SUS sozinho nao captura o custo cognitivo
- "O usuario consegue, mas fica exausto?" → NASA-TLX responde
- Complementa SUS: SUS mede PERCEPCAO DE USABILIDADE, NASA-TLX mede CUSTO COGNITIVO

---

## HEART Framework (Google)

Framework de metricas de UX em escala. Cada dimensao se desdobra em Goals → Signals → Metrics (GSM).

| Dimensao | O que mede | Metrica exemplo | Quando monitorar |
|----------|-----------|-----------------|-----------------|
| **Happiness** | Satisfacao | SUS score, NPS, CSAT | Pos-lancamento, pesquisas periodicas |
| **Engagement** | Envolvimento | Sessions/week, features used | Retencao, product-market fit |
| **Adoption** | Novos usuarios | Signups, first-time users | Lancamento, growth |
| **Retention** | Retorno | Churn rate, return visits | Saude do produto |
| **Task Success** | Completude | Completion rate, error rate, time on task | Otimizacao de fluxos |

### Quando usar no audit
- Se o usuario tem dados de analytics → mapear metricas HEART pros findings
- Se nao tem dados → sugerir instrumentacao das metricas mais relevantes
- Task Success e a dimensao mais diretamente conectada ao UX audit

---

## Mapeamento Severidade → Acao no ClickUp

| Severidade | Prioridade ClickUp | Sprint | Tag |
|------------|-------------------|--------|-----|
| 4 (catastrofico) | Urgente | Sprint atual — interrompe o que estiver fazendo | `ux-sev4` |
| 3 (maior) | Alta | Proximo sprint (ou atual se tiver espaco) | `ux-sev3` |
| 2 (menor) | Normal | Backlog priorizado | `ux-sev2` |
| 1 (cosmetico) | Baixa | Backlog geral | `ux-sev1` |
