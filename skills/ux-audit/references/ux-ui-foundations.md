# UX/UI Foundations — Referência Rápida

Consulte este arquivo antes de iniciar qualquer auditoria. Contém os frameworks, heurísticas e critérios que fundamentam a análise.

---

## 10 Heurísticas de Nielsen

| # | Heurística | Pergunta-chave |
|---|-----------|----------------|
| H1 | Visibilidade do status do sistema | O usuário sabe o que está acontecendo? |
| H2 | Correspondência entre sistema e mundo real | A linguagem faz sentido pro usuário? |
| H3 | Controle e liberdade do usuário | Tem desfazer, voltar, cancelar? |
| H4 | Consistência e padrões | Mesma ação = mesmo resultado em todo lugar? |
| H5 | Prevenção de erros | O design evita erros antes que aconteçam? |
| H6 | Reconhecimento em vez de lembrança | As opções estão visíveis ou o usuário precisa lembrar? |
| H7 | Flexibilidade e eficiência de uso | Tem atalhos pra usuários experientes? |
| H8 | Design estético e minimalista | Sem informação irrelevante competindo por atenção? |
| H9 | Recuperação de erros | Mensagens de erro são claras e oferecem solução? |
| H10 | Ajuda e documentação | Se precisa de ajuda, ela existe e é encontrável? |

---

## 7 Princípios de Design de Norman

1. **Discoverability** — O usuário descobre o que pode fazer olhando a interface?
2. **Feedback** — Toda ação tem resposta imediata e clara?
3. **Conceptual Model** — O modelo mental do usuário casa com o do sistema?
4. **Affordances** — Os elementos comunicam como devem ser usados?
5. **Signifiers** — Há indicadores visuais de onde clicar/tocar/arrastar?
6. **Mappings** — A relação entre controle e efeito é natural?
7. **Constraints** — O design limita ações inválidas?

---

## Laws of UX (Yablonski) — As mais úteis pra auditorias

### Tomada de decisão
- **Hick's Law** — Tempo de decisão aumenta logaritmicamente com número de opções. Regra: se uma tela tem 10+ opções sem agrupamento, tem problema.
- **Miller's Law** — Memória de trabalho segura ~7 (±2) itens. Agrupe informação em chunks.

### Interação física
- **Fitts's Law** — Tempo de alcançar um alvo depende de distância e tamanho. CTAs devem ser grandes e perto de onde o cursor/dedo já está.
- **Doherty Threshold** — Se o sistema responde em <400ms, produtividade sobe. Acima, frustração cresce.

### Percepção visual
- **Gestalt: Proximity** — Itens próximos parecem relacionados.
- **Gestalt: Common Region** — Itens dentro de uma mesma área/borda parecem grupo.
- **Gestalt: Similarity** — Itens visualmente similares parecem ter mesma função.

### Comportamento
- **Jakob's Law** — Usuários esperam que seu app funcione como os outros que já usam. Não reinvente a roda.
- **Peak-End Rule** — Pessoas julgam experiências pelo pico (melhor/pior momento) e pelo final. Otimize esses pontos.
- **Aesthetic-Usability Effect** — Interfaces bonitas são percebidas como mais fáceis de usar (mesmo que não sejam).
- **Tesler's Law** — Toda tarefa tem complexidade irredutível. Se não está no design, está no usuário.

### Viés e hábito
- **Endowment Effect** — Usuários valorizam mais o que já possuem. Cuidado ao remover features.
- **Serial Position Effect** — Primeiro e último item de uma lista são mais lembrados. Coloque o mais importante no início ou fim.

---

## WCAG 2.2 — Critérios mais impactantes

### Novos no WCAG 2.2 (outubro 2023)

**Nível A:**
- **3.2.6 Consistent Help** — Mecanismo de ajuda na mesma posição em todas as páginas
- **3.3.7 Redundant Entry** — Não pedir ao usuário pra redigitar informação já fornecida no processo

**Nível AA:**
- **2.4.11 Focus Not Obscured (Minimum)** — Elemento com foco não pode ser totalmente coberto
- **2.5.7 Dragging Movements** — Alternativa sem arrastar pra toda funcionalidade de drag
- **2.5.8 Target Size (Minimum)** — Alvos interativos ≥ 24×24 CSS pixels
- **3.3.8 Accessible Authentication (Minimum)** — Login sem teste cognitivo obrigatório

**Nível AAA:**
- **2.4.12 Focus Not Obscured (Enhanced)** — Foco nunca coberto por nenhum conteúdo
- **2.4.13 Focus Appearance** — Indicador de foco com contraste e tamanho suficiente
- **3.3.9 Accessible Authentication (Enhanced)** — Versão mais restritiva de 3.3.8

### Critérios clássicos que mais falham

| Critério | Nível | O que verificar |
|----------|-------|-----------------|
| 1.1.1 Non-text Content | A | Alt text em imagens informativas |
| 1.3.1 Info and Relationships | A | Labels em todos os campos de formulário |
| 1.4.3 Contrast (Minimum) | AA | Texto: 4.5:1 normal, 3:1 large |
| 2.1.1 Keyboard | A | Tudo funciona sem mouse |
| 2.4.7 Focus Visible | AA | Indicador de foco visível no teclado |
| 4.1.2 Name, Role, Value | A | Componentes custom com roles ARIA corretos |

---

## Core Web Vitals (desde março 2024)

| Métrica | O que mede | Bom | Precisa melhorar | Ruim |
|---------|-----------|-----|-------------------|------|
| **LCP** | Loading — tempo até o maior elemento visível | ≤ 2.5s | 2.5s–4s | > 4s |
| **INP** | Responsividade — tempo entre interação e próximo paint | ≤ 200ms | 200ms–500ms | > 500ms |
| **CLS** | Estabilidade visual — quanto o layout muda | ≤ 0.1 | 0.1–0.25 | > 0.25 |

**INP substituiu FID em março 2024.** INP mede TODAS as interações na página (não só a primeira como FID). É mais representativo da experiência real.

---

## Dark Patterns — Categorias (Purdue University Framework)

| Categoria | O que é | Exemplo | Legal? |
|-----------|---------|---------|--------|
| **Nagging** | Interrupções persistentes | Pop-up de newsletter que aparece toda página | Pode violar DSA |
| **Obstruction** | Dificultar tarefas que não beneficiam o negócio | Cancelamento em 15 passos vs assinatura em 2 | Ilegal (FTC, DSA) |
| **Sneaking** | Esconder informação relevante | Custo extra revelado só no checkout | Ilegal (CPRA, DSA) |
| **Interface Interference** | Manipular interface pra favorecer uma ação | "Aceitar" em verde grande, "Recusar" em cinza pequeno | Pode violar CPRA |
| **Forced Action** | Obrigar ação não relacionada | Criar conta pra ver preço | Depende do contexto |

**Legislação:** EU Digital Services Act (2024+), California CPRA, FTC enforcement. Consent obtido via dark patterns é INVÁLIDO.

---

## SUS (System Usability Scale)

10 perguntas com escala Likert 1-5. Resultado de 0-100.

**Cálculo:** SUS = 2.5 × (soma itens ímpares − soma itens pares)
- Itens ímpares (1,3,5,7,9): score = resposta − 1
- Itens pares (2,4,6,8,10): score = 5 − resposta

**Interpretação:**
| Score | Classificação | Percentil |
|-------|--------------|-----------|
| 90+ | Excelente | Top 5% |
| 80-89 | Muito bom | Top 10% |
| 68 | Média global | 50% |
| 50-67 | Abaixo da média | < 50% |
| < 50 | Inaceitável | — |

---

## NASA-TLX (Task Load Index)

6 dimensões de carga de trabalho, escala 0-100 cada:
1. **Mental Demand** — Quanto esforço mental?
2. **Physical Demand** — Quanto esforço físico?
3. **Temporal Demand** — Quanta pressão de tempo?
4. **Performance** — Quão bem-sucedido se sentiu?
5. **Effort** — Quanto esforço total?
6. **Frustration** — Quanta frustração?

**Quando usar:** Tarefas complexas onde SUS sozinho não captura o custo cognitivo. NASA-TLX mede ESFORÇO, SUS mede PERCEPÇÃO DE USABILIDADE. Juntos, dão quadro completo.

---

## Escala de Severidade de Nielsen

| Nível | Nome | Critério | Ação |
|-------|------|----------|------|
| 0 | Não é problema | Sem impacto | Nenhuma |
| 1 | Cosmético | Usuário nota, tarefa não afetada | Quando sobrar tempo |
| 2 | Menor | Leve confusão ou delay | Prioridade baixa |
| 3 | Maior | Dificulta significativamente a tarefa | Antes do próximo release |
| 4 | Catastrófico | Bloqueia tarefa essencial | Imediatamente |

---

## HEART Framework (Google)

| Dimensão | O que mede | Métrica exemplo |
|----------|-----------|-----------------|
| **Happiness** | Satisfação do usuário | SUS score, NPS, satisfaction survey |
| **Engagement** | Envolvimento | Sessions/week, features used, time on task |
| **Adoption** | Novos usuários | Signups, first-time users, feature adoption |
| **Retention** | Retorno | Churn rate, return visits, subscription renewal |
| **Task Success** | Completude | Task completion rate, error rate, time on task |

Cada dimensão se desdobra em: Goals → Signals → Metrics (GSM framework).

---

## Thumb Zone — Referência Rápida

**Dados (Steven Hoober, 2013 + atualizações):**
- 49% usam celular com uma mão
- 75% das interações são com polegar
- Em telas 6.5"+, zona confortável é menor

**Zonas:**
- **Confortável:** Centro e centro-baixo da tela
- **Esticar:** Bordas e parte superior
- **Difícil:** Cantos superiores (especialmente top-left em telas grandes)

**Implicações pra design:**
- CTAs primários: centro-baixo
- Bottom nav: acessível (mas verificar em phones 6.7"+)
- FABs: bottom-center ou bottom-right (não top)
- Ações destrutivas: fora da zona fácil (evita toque acidental)
- Close/Back no top-left: difícil em telas grandes — considere gesto de swipe
