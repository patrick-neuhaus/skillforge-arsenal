# `references/ux-severity-rubric.md`

> Rubrica de severidade e fechamento de finding. Consultado a partir da Fase 6 do SKILL.md. Esta skill é dona canônica da **escala Nielsen 0–4** e da **rubrica scored** para auditoria de UX.

## 1. Escala de severidade Nielsen (canônica)

| Nível | Nome | Definição operacional | Quando aplicar | Ação esperada |
|-------|------|----------------------|----------------|---------------|
| **0** | Não é problema | Observação sem impacto demonstrável | Detalhe estético sem afetar tarefa; ressalva de design | Registrar, não priorizar |
| **1** | Cosmético | Pode ser corrigido se houver tempo extra | Microinconsistência local sem impacto em tarefa | Backlog geral |
| **2** | Menor | Baixa prioridade; afeta tarefa de forma leve ou rara | Fricção pontual em estado raro | Backlog priorizado |
| **3** | Maior | Alta prioridade; afeta muitos usuários ou tarefa frequente | Fricção recorrente; bloqueia eficiência | Próximo sprint |
| **4** | Catastrófico | Bloqueia tarefa, exclui acessibilidade, gera dano financeiro/legal | Impossível concluir; viola WCAG A; dark pattern legalmente questionável | Sprint atual / hotfix |

## 2. Critérios de calibragem

Cada severidade combina três fatores. Quando dois apontam alto, o finding sobe.

| Fator | 0 | 1 | 2 | 3 | 4 |
|-------|---|---|---|---|---|
| **Frequência** | Quase nunca | Raro | Ocasional | Frequente | Sempre |
| **Impacto** | Nenhum | Estético | Leve atrito | Bloqueio parcial | Bloqueio total / dano |
| **Persistência** | Aprende uma vez | Pequena curva | Recorrente | Persiste após uso prolongado | Não tem como aprender em volta |

### Calibragem por contexto (operacional × landing × docs × template)

A mesma observação pode ter severidade diferente conforme o contexto.

| Observação | SaaS operacional | Landing | Documentação | Template demonstrativo |
|---|---|---|---|---|
| Densidade alta | sev 0–1 (esperada) | sev 3 | sev 1–2 | sev 0–1 |
| Tabela sem sort/filter | sev 3 | n/a | sev 2 | sev 2 |
| CTA genérico ("Get started") | sev 1 | sev 3 | sev 1 | sev 2 |
| Estados (empty/error) ausentes | sev 3 | sev 2 | sev 2 | sev 4 (template não serve) |
| Sem FAQ/social proof | n/a | sev 2 | n/a | n/a |
| Falta busca/anchor | sev 2 | sev 1 | sev 3 | sev 1 |

## 3. Formato canônico de finding (com critério de aceite)

Todo finding fecha o ciclo em 6 campos. Sem critério de aceite, não está pronto para entrega.

```
1. Evidência       — fato observável e verificável na interface
2. Princípio       — heurística Nielsen / princípio Norman / Law of UX / WCAG
3. Impacto         — consequência prática para o usuário em tarefa real
4. Severidade      — Nielsen 0–4
5. Recomendação    — mudança concreta e implementável (comportamento / estrutura / estado / copy / layout)
6. Critério de aceite — como QA / design / dev valida que corrigiu
```

### Exemplo

```
1. Evidência: Ao clicar "Salvar" no formulário de configuração, nada visível acontece por ~3s; depois a página recarrega.
2. Princípio: Nielsen H1 (visibilidade do status do sistema); WCAG 4.1.3 (status messages).
3. Impacto: Usuário não sabe se a ação foi recebida, clica novamente, gera duplicação ou abandona.
4. Severidade: 3
5. Recomendação: Botão entra em estado loading com spinner inline e label "Salvando…"; ao concluir, exibir toast "Configuração salva" com role="status" para screen readers; permanecer na mesma URL.
6. Critério de aceite:
   (a) Após clique, botão muda para loading em < 100ms.
   (b) Toast de sucesso aparece em < 5s e é anunciado por VoiceOver/NVDA.
   (c) Página não recarrega; estado do form é preservado.
   (d) axe não reporta violação 4.1.3 na tela de resultado.
```

## 4. Critério de aceite — qualidade do critério

Critério bom é **observável, verificável e específico**. Não é o mesmo que recomendação.

| ❌ Ruim | ✅ Bom |
|---|---|
| "Melhorar feedback do botão" | "Botão exibe estado loading em < 100ms após clique; toast aparece em < 5s com role=status" |
| "Aumentar contraste" | "Texto cinza no card atinge 4.5:1 medido pelo axe; verificado em modo claro e escuro" |
| "Fazer responsivo" | "Em viewport 320 CSS px, fluxo de criar conta é completável sem scroll horizontal; testado em iPhone SE" |
| "Resolver acessibilidade" | "Tab pela página inteira atinge todos os controles; foco visível com 3:1 de contraste; VoiceOver anuncia label de cada campo" |

## 5. Mapeamento severidade → ação

| Severidade | Quando entra | Quem owns |
|-----------|-------------|-----------|
| 4 | Sprint atual / hotfix | Eng + Design + PM |
| 3 | Próximo sprint | Eng + Design |
| 2 | Backlog priorizado | Design |
| 1 | Backlog geral | Design |
| 0 | Registrado, não priorizado | — |

## 6. Rubrica scored de 14 categorias (audit completo, opcional)

Use em audit completo para gerar score comparável entre versões. Cada categoria recebe nota 1–5 e peso. Score final = soma ponderada / soma dos pesos × 20 (0–100).

| # | Categoria | Peso | Sinais para nota baixa | Sinais para nota alta |
|---|-----------|------|------------------------|------------------------|
| 1 | Clareza de objetivo e proposta | 3 | Hero genérico, não responde "o que é" em 5s | Proposta de valor imediata, ICP claro |
| 2 | Navegação e wayfinding | 3 | Usuário se perde, sem breadcrumb, IA confusa | Nav consistente, breadcrumb onde precisa |
| 3 | Hierarquia visual | 3 | Tudo com mesmo peso; KPI sem destaque | Hierarquia clara, pontos focais óbvios |
| 4 | Consistência e padrões | 3 | Mesma ação parece diferente em telas distintas | Padrões consistentes, aderência a convenções |
| 5 | Componentes e estados | 3 | Estados ausentes (empty, error, loading, disabled) | Inventário completo, estados comunicam |
| 6 | Formulários e validação | 3 | Erro genérico, sem inline, dados perdidos | Validação inline, mensagens específicas, dados preservados |
| 7 | Tabelas e dados densos | 2 | Sem sort/filter/empty/loading/sticky header | Sort/filter/bulk, estados, density toggle |
| 8 | Feedback e mensagens de erro | 3 | Toast vago, erro só no topo, sem sugestão | Específico, com sugestão, próximo da causa |
| 9 | Acessibilidade (WCAG 2.2 AA) | 4 | Falha contraste, foco, teclado, target size | Passa baseline AA, testado com SR |
| 10 | Responsividade e cross-device | 2 | Quebra em mobile, scroll horizontal indesejado | Reflow ok em 320 px, touch targets 44×44 |
| 11 | Performance percebida | 2 | LCP > 4s, INP > 500ms, CLS > 0.25 percebidos | Loading com skeleton/streaming; INP < 200ms percebido |
| 12 | Motion e feedback temporal | 1 | Animações distraem, ignoram reduced-motion | Motion comunica, respeita preferência |
| 13 | Copy / microcopy | 2 | Jargão técnico, CTA genérico, voz inconsistente | Linguagem do usuário, CTA específico, voz coerente |
| 14 | DS maturity (sistêmico) | 2 | Inconsistências sistêmicas em várias telas | Tokens, padrões e governança visíveis |

**Categorias 9 (a11y) e 1 (clareza) têm peso maior** porque excluem ou bloqueiam tarefa.

### Exemplo de cálculo

Soma de pesos = 36. Score = (Σ nota×peso) / 36 × 20 → 0–100.

Acima de 80 = maduro; 60–80 = aceitável com gaps; abaixo de 60 = redesign de fluxo crítico.

## 7. Métricas complementares (referência curta)

Para benchmark longitudinal e validação com usuário real.

- **SUS** — 10 perguntas, 0–100. Média global ≈ 68. Use para comparar versões.
- **UMUX-Lite** — 2 perguntas, monitoramento ágil.
- **NASA-TLX** — 6 dimensões de carga cognitiva. Complementa SUS medindo CUSTO.
- **HEART** — Happiness, Engagement, Adoption, Retention, Task Success. Conecta UX a metas via Goals → Signals → Metrics.

Estas métricas são **referência**, não substituem a rubrica de severidade nem o critério de aceite.

## 8. Quando o finding NÃO entra como UX

Antes de aplicar a rubrica, confirme que o problema cabe nesta skill (ver `triage-matrix.md`). Findings que pertencem a outras skills devem ser **encaminhados, não absorvidos**:

- Token, escala visual, breakpoint → `ui-design-system`
- Anatomia, slot, variant, contrato de a11y do componente → `component-architect`
- Code review, qualidade React → `trident --design`
- Cross-browser, build target → `react-patterns`
- Bug funcional → `trident`

Critério de aceite para encaminhamento: **citar a skill destino e o por quê**, em vez de gerar finding órfão.
