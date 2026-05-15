# `references/ux-foundations.md`

> Fundamentos de UX para auditoria. Consultado a partir da Fase 3 do SKILL.md. **Foco em UX:** heurísticas, princípios, métodos, calibragem por contexto. Não trata de tokens, breakpoints, anatomia de componente nem build target — esses moram em outras skills.

## 1. 10 Heurísticas de Nielsen (canônicas para auditoria)

| # | Heurística | Pergunta-chave | Sinal de violação | Correção típica |
|---|-----------|----------------|-------------------|-----------------|
| H1 | Visibilidade do status do sistema | Após uma ação, o usuário sabe o que aconteceu? | Dead click, loading ambíguo, toast vago, ausência de confirmação | Indicador de progresso, feedback inline, confirmação contextual |
| H2 | Correspondência sistema ↔ mundo real | A linguagem é do usuário, não do sistema? | Jargão interno, IA refletindo estrutura da empresa | Renomear conforme domínio do usuário e top tasks |
| H3 | Controle e liberdade do usuário | Tem voltar, cancelar, desfazer, escapar? | Modal trap, autosubmit, sequência forçada | Undo, cancelamento claro, rascunho/autosave |
| H4 | Consistência e padrões | Mesma ação parece e age igual em todo lugar? | "Salvar" vira "Confirmar", botão primário muda de cor | Tokens, content standards, aderência a convenções |
| H5 | Prevenção de erros | O design impede erro antes dele acontecer? | Combinações inválidas permitidas, ações destrutivas sem proteção | Validação inline, máscaras, opções indisponíveis explicadas |
| H6 | Reconhecimento em vez de lembrança | As opções estão visíveis? | Atalhos ocultos no hover, dependência de memória entre telas | Progressive disclosure, defaults, ajuda contextual |
| H7 | Flexibilidade e eficiência | Usuário recorrente tem atalho? | Mesmo número de cliques para iniciante e expert | Atalhos, persistência de preferências, bulk actions |
| H8 | Design estético e minimalista | Ruído visual compete com a tarefa? | Tudo com mesmo peso, KPI sem prioridade | Hierarquia visual, eliminar info irrelevante |
| H9 | Recuperação de erros | Mensagem de erro é específica e acionável? | "Erro ao processar"; erro só no topo; campo errado não destacado | Mensagem específica, sugestão acionável, dados preservados |
| H10 | Ajuda e documentação | Se precisar, ajuda existe e é encontrável? | Doc inexistente ou desconectada do contexto | Help inline, links contextuais, FAQ orientada a tarefa |

## 2. 7 Princípios de Norman (vocabulário de causa raiz)

1. **Discoverability** — o usuário descobre o que pode fazer só olhando?
2. **Feedback** — toda ação tem resposta imediata?
3. **Conceptual model** — o modelo mental do usuário casa com o do sistema?
4. **Affordances** — o elemento sugere como ser usado?
5. **Signifiers** — pistas visíveis de onde e como agir?
6. **Mappings** — relação entre controle e efeito é natural?
7. **Constraints** — o design impede ações inválidas?

Use Norman para **explicar a causa raiz** dentro do finding, não como seção separada.

## 3. Laws of UX úteis para auditoria

- **Hick's Law** — tempo de decisão cresce com nº de opções. Tela com 10+ opções sem agrupamento → finding.
- **Miller's Law** — memória de trabalho ~7 ±2. Agrupe em chunks.
- **Fitts's Law** — tempo até alvo depende de distância e tamanho. CTAs devem ser grandes e perto do cursor.
- **Doherty Threshold** — resposta < 400ms mantém produtividade.
- **Jakob's Law** — usuários esperam que seu app funcione como os outros. Não reinvente convenção.
- **Peak-End Rule** — pessoas julgam pelo pico e pelo fim. Otimize esses pontos.
- **Aesthetic-Usability Effect** — interfaces bonitas parecem mais usáveis. **Cuidado:** estética pode mascarar fricção real.
- **Tesler's Law** — toda tarefa tem complexidade irredutível. Se não está no design, está no usuário.
- **Gestalt: Proximity / Common Region / Similarity** — relações percebidas sem leitura.
- **Serial Position Effect** — primeiro e último itens são mais lembrados.

## 4. Métodos de auditoria (qual pergunta cada um responde)

| Método | Responde a quê | Quando usar | Entregável | Armadilha |
|---|---|---|---|---|
| **Heuristic evaluation** | Que princípios essa UI viola? | Cedo, sem orçamento de pesquisa | Lista por heurística com severidade | Virar checklist mecânico sem contexto de tarefa |
| **Cognitive walkthrough** | Usuário novo entenderia o próximo passo? | Onboarding, first-use, fluxo crítico | 4 perguntas por passo (tentativa / visibilidade / associação / feedback) | Avaliar "beleza" no método feito para learnability |
| **Task analysis** | Que subtarefas e decisões compõem o trabalho? | Antes de redesenhar fluxo complexo | Mapa de tarefa com passos, decisões, frequência | Modelar fluxo idealizado em vez do real |
| **Journey mapping** | Onde estão dores e handoffs ao longo da jornada? | Estratégia, multicanal, retenção | Linha do tempo com fases, ações, emoções | Substituir fluxo detalhado por jornada macro demais |
| **Usability testing** | O problema acontece com usuário real em tarefa real? | Sempre que houver risco/dúvida/conflito | Evidência observável de falha/sucesso | Testar opinião em vez de tarefa |

**Heurística não substitui usuário real.** Se o achado é crítico, recomende usability testing.

## 5. Calibragem por contexto (rubrica varia por tipo de produto)

| Contexto | Prioridade | Densidade | O que observar | Onde calibrar finding |
|---|---|---|---|---|
| **SaaS operacional / dashboard / admin** | Throughput, comparação, decisão recorrente | Pode ser alta | Filters, tables, bulk actions, estados (empty/error/loading), hierarquia | Density alta NÃO é finding; tabela sem sort/filter É finding sev 3 |
| **Landing institucional** | Proposta de valor, prova, diferenciação, CTA | Baixa | Hero claro, CTA específico, social proof, FAQ | "Get started" genérico É finding; densidade alta É finding |
| **Documentação técnica** | Encontrabilidade, escaneabilidade, profundidade progressiva | Média a alta | TOC, in-page links, headings, exemplos, busca | Falta de busca/anchor links É finding sev 3 |
| **Template demonstrativo** | Mostrar padrão, não simular valor | Variável, controlada | Edge cases, estados, responsividade, comportamento real | Só "happy path" É finding (template não serve como referência) |

Esta tabela impede o erro clássico de aplicar régua de SaaS público num app interno (ou vice-versa).

## 6. UX × UI × a11y × DS × component arch × copy × perf percebida

Glossário curto. Para tabela completa de triagem, ver `triage-matrix.md`.

- **UX** — problema de tarefa, entendimento, decisão, fluxo. Audita esta skill.
- **UI** — problema de sinal visual, organização perceptiva, hierarquia. Calibragem aqui se afeta tarefa; senão `ui-design-system`.
- **Acessibilidade** — exclusão ou fricção por capacidade/modalidade. Baseline desta skill (WCAG 2.2 AA).
- **Design system** — problema sistêmico, padrão, token, governança. Encaminha para `ui-design-system` se recorrente.
- **Component architecture** — anatomia, slots, variants, estados, contratos. Encaminha para `component-architect`.
- **Copy / microcopy** — linguagem, rótulo, instrução, feedback verbal. Audita aqui se afeta entendimento da tarefa.
- **Performance percebida** — experiência do tempo (não tempo técnico). Audita aqui como percepção; encaminha implementação para frontend.

## 7. Dark patterns (Purdue, 7 categorias)

Verificações complementares — não são heurísticas, mas impactam confiança e legalidade (DSA 2024+, CPRA, FTC).

| Categoria | O que é | Sinal | Status legal |
|-----------|---------|-------|--------------|
| Nagging | Interrupções persistentes | Pop-up de newsletter em toda página | Pode violar DSA |
| Obstruction | Dificultar tarefa que não beneficia o negócio | Cancelamento em 15 passos vs assinatura em 2 | Ilegal (FTC, DSA) |
| Sneaking | Esconder info relevante | Custo extra revelado só no checkout | Ilegal (CPRA, DSA) |
| Interface interference | Manipular UI para favorecer ação | "Aceitar" verde grande, "Recusar" cinza pequeno | Pode violar CPRA |
| Forced action | Obrigar ação não relacionada | Criar conta para ver preço | Depende do contexto |
| Confirmshaming | Texto manipulativo na recusa | "Não, eu não quero economizar" | Anti-ético |
| Roach motel | Fácil entrar, difícil sair | Free trial que exige ligação para cancelar | Ilegal (FTC) |

**Consent obtido via dark pattern é INVÁLIDO sob DSA.** Severidade default = 3 ou 4.

## 8. Mobile ergonomics (thumb zone, Hoober 2013+)

- 49% usam celular com uma mão; 75% das interações são com polegar.
- **Confortável:** centro e centro-baixo → CTAs primários, navegação principal.
- **Esticar:** bordas, parte superior → ações secundárias.
- **Difícil:** cantos superiores → ações destrutivas (evita toque acidental).

Targets ≥ 44×44px (WCAG pede 24, 44 é melhor para touch). Bottom nav é mais acessível que top menu em telas 6.5"+. Gestos de swipe devem ter alternativa em botão.

## 9. Performance percebida (heurística observável, não medição)

| Métrica | O que mede | Bom | Ruim | Sintoma observável |
|---------|-----------|-----|------|---------------------|
| LCP | Tempo até maior elemento visível | ≤ 2.5s | > 4s | "A página demora a aparecer" |
| INP | Tempo entre interação e próximo paint | ≤ 200ms | > 500ms | "O clique demora a responder" |
| CLS | Estabilidade visual | ≤ 0.1 | > 0.25 | "Os elementos pulam ao carregar" |

INP substituiu FID em março/2024. **Audit faz percepção observável**; medição técnica e otimização ficam com frontend/`react-patterns`.

## 10. Vocabulário de métricas (referência curta)

- **SUS** — System Usability Scale, 10 perguntas, score 0–100, média global 68. Use para benchmark de versão.
- **UMUX-Lite** — 2 perguntas, contexto ágil, monitoramento.
- **NASA-TLX** — 6 dimensões de carga cognitiva (mental, físico, temporal, performance, esforço, frustração). Mede CUSTO COGNITIVO, complementa SUS.
- **HEART** — Happiness, Engagement, Adoption, Retention, Task Success. Conecta UX a metas de produto via Goals → Signals → Metrics.

## 11. UX de IA (se aplicável)

- **Transparência:** usuário sabe que é IA? Cita fontes? Mostra incerteza?
- **Feedback:** streaming progressivo? Conteúdo parcial? Estimativa de tempo?
- **Controle:** override fácil? Like/dislike? Confirmação humana em ação destrutiva sugerida?
- **Error handling:** timeout tem fallback? Rate limit comunicado de forma amigável?

## 12. Red flags de skill ruim (autoavaliação)

- Feedback genérico ("mais moderno", "mais clean", "mais premium").
- Não cita princípio, heurística, WCAG ou método.
- Não percorre interações, estados, loading, erro, vazio.
- Confunde acessibilidade com estética.
- Não diferencia local × sistêmico.
- Não prioriza por severidade.
- Não aponta nada que funciona bem.
- Não produz recomendação implementável nem critério de aceite.
