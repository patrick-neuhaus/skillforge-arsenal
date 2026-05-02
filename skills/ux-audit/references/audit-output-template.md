# `references/audit-output-template.md`

> Templates de output. Consultado a partir da Fase 7 do SKILL.md. Três modos: **Completo**, **Focado**, **Cognitive Walkthrough**. Todos exigem critério de aceite por finding e seção "o que está funcionando bem".

## 1. Template — Audit Completo

Use em revisão geral de produto (3–5 fluxos críticos, todas as fases).

```markdown
# UX Audit — [Produto / versão]

**Data:** YYYY-MM-DD
**Auditor:** [nome]
**Modo:** Completo
**Tipo de produto:** [SaaS operacional / landing / documentação / template]

---

## 1. Contexto

- **Usuário-alvo:** [persona, nível técnico, frequência, dispositivo]
- **Objetivo principal:** [tarefa central que o usuário vem fazer]
- **Plataforma:** [web desktop / web mobile / responsivo / nativo]
- **Onboarding:** [first-time / recorrente]
- **Features de IA:** [sim / não — se sim, quais]
- **Calibragem aplicada:** [regras específicas do tipo de produto — ex: "densidade alta esperada por ser operacional"]

## 2. Triagem

Sintomas observados foram classificados antes do audit:

| Sintoma | Tipo | Skill responsável | Ação |
|---|---|---|---|
| [exemplo: contraste de tokens fraco em escala neutra] | DS | `ui-design-system` | Encaminhado |
| [exemplo: estado loading ausente no botão Salvar] | UX | `ux-audit` | Auditado abaixo |

## 3. Fluxos auditados

### Fluxo 1 — [nome]

**Veredicto:** ✅ Fluido | ⚠️ Tem fricção | ❌ Quebrado

**Passos percorridos:**
1. [passo] — [observação]
2. [passo] — [observação]

**Estados verificados:** default, hover, focus, loading, error, empty, success.

[repetir para cada fluxo crítico — mínimo 3]

## 4. Findings por severidade

### Severidade 4 — Catastrófico

#### F-01 [título curto]

- **Evidência:** [fato observável]
- **Princípio:** [Nielsen / Norman / Law / WCAG]
- **Impacto:** [consequência prática]
- **Recomendação:** [mudança concreta]
- **Critério de aceite:**
  - [ ] [verificação 1]
  - [ ] [verificação 2]

[demais findings sev 4]

### Severidade 3 — Maior
[…]

### Severidade 2 — Menor
[…]

### Severidade 1 — Cosmético
[…]

## 5. Acessibilidade (WCAG 2.2 AA)

| Critério | Status | Observação |
|---|---|---|
| 1.4.3 Contraste | ✅ / ⚠️ / ❌ | [nota] |
| 2.1.1 Teclado | ✅ / ⚠️ / ❌ | [nota] |
| 2.4.7 Foco visível | ✅ / ⚠️ / ❌ | [nota] |
| 2.5.8 Target size | ✅ / ⚠️ / ❌ | [nota] |
| 1.4.10 Reflow | ✅ / ⚠️ / ❌ | [nota] |
| 4.1.3 Status messages | ✅ / ⚠️ / ❌ | [nota] |
| 3.3.3 Error suggestion | ✅ / ⚠️ / ❌ | [nota] |
| [outros relevantes] | | |

## 6. Estados auditados

| Componente | Default | Hover | Focus | Pressed | Disabled | Loading | Error | Empty | Success |
|---|---|---|---|---|---|---|---|---|---|
| [nome] | ✅ | ✅ | ⚠️ | ✅ | ❌ | ✅ | ✅ | n/a | ✅ |

## 7. Dark patterns

[Verificação das 7 categorias Purdue. Se nenhum, declarar.]

## 8. Performance percebida

| Métrica | Percepção | Observação |
|---|---|---|
| LCP | "demora a aparecer" / ok | [nota] |
| INP | "clique trava" / ok | [nota] |
| CLS | "elementos pulam" / ok | [nota] |

## 9. Score (rubrica de 14 categorias)

| # | Categoria | Peso | Nota (1–5) | Pontos |
|---|---|---|---|---|
| 1 | Clareza de objetivo | 3 | | |
| 2 | Navegação | 3 | | |
| 3 | Hierarquia visual | 3 | | |
| 4 | Consistência | 3 | | |
| 5 | Estados | 3 | | |
| 6 | Formulários | 3 | | |
| 7 | Tabelas | 2 | | |
| 8 | Feedback | 3 | | |
| 9 | Acessibilidade | 4 | | |
| 10 | Responsividade | 2 | | |
| 11 | Perf percebida | 2 | | |
| 12 | Motion | 1 | | |
| 13 | Copy | 2 | | |
| 14 | DS maturity | 2 | | |
| **Total** | | **36** | | **/180** → **/100** |

## 10. O que está funcionando bem

- [ponto 1]
- [ponto 2]
- [ponto 3]

## 11. Encaminhamentos

| Item | Skill destino | Por quê |
|---|---|---|
| [problema sistêmico de tokens] | `ui-design-system` | Recorrente em várias telas |
| [estado ausente no componente Button] | `component-architect` | Anatomia precisa cobrir |

## 12. Próximos passos sugeridos

1. [próximo passo 1]
2. [próximo passo 2]
3. [próximo passo 3]
```

---

## 2. Template — Audit Focado

Use em revisão de uma tela ou fluxo específico.

```markdown
# UX Audit Focado — [Tela / fluxo]

**Data:** YYYY-MM-DD
**Modo:** Focado
**Escopo:** [tela ou fluxo]
**Tipo de produto:** [...]

## 1. Contexto

- **Usuário-alvo:** [...]
- **Objetivo da tela/fluxo:** [...]

## 2. Triagem

[Sintomas e classificação resumida.]

## 3. Caminho percorrido

[Passos do fluxo, observações por passo.]

## 4. Findings (top issues)

### F-01 [título]

- Evidência: [...]
- Princípio: [...]
- Impacto: [...]
- Severidade: [0–4]
- Recomendação: [...]
- Critério de aceite:
  - [ ] [...]

[3–7 findings, ordenados por severidade]

## 5. WCAG aplicável

[Critérios mais relevantes para esta tela com status.]

## 6. Estados verificados

[Inventário dos estados desta tela.]

## 7. O que está funcionando bem

[2–3 pontos.]

## 8. Encaminhamentos

[Se houver itens fora de escopo.]

## 9. Próximo passo sugerido

[1 ação.]
```

---

## 3. Template — Cognitive Walkthrough

Use para avaliar **learnability** com novo usuário em tarefa específica. Método Wharton/Rieman/Lewis/Polson.

```markdown
# Cognitive Walkthrough — [Tarefa]

**Data:** YYYY-MM-DD
**Modo:** Cognitive Walkthrough

## 1. Perfil do usuário hipotético

- Quem: [persona]
- Conhecimento prévio: [nível técnico, familiaridade com o domínio]
- Motivação: [por que está fazendo isso]
- Contexto: [onde, quando, com qual dispositivo]

## 2. Tarefa

[Descrição da tarefa que o usuário deve completar.]

## 3. Sequência de passos esperada

1. [passo 1]
2. [passo 2]
…

## 4. Análise por passo

Para cada passo, responder as 4 perguntas (Wharton et al.):

### Passo 1: [descrição]

| # | Pergunta | Resposta | Evidência |
|---|----------|----------|-----------|
| 1 | O usuário tentaria executar a ação correta? | ✅ / ⚠️ / ❌ | [nota] |
| 2 | A ação correta está visivelmente disponível? | ✅ / ⚠️ / ❌ | [nota] |
| 3 | O usuário associa o controle à ação que quer? | ✅ / ⚠️ / ❌ | [nota] |
| 4 | Após executar, o usuário percebe que progrediu? | ✅ / ⚠️ / ❌ | [nota] |

**Findings deste passo:**

#### F-01 [título]
- Evidência: [...]
- Princípio: [...]
- Impacto: [...]
- Severidade: [0–4]
- Recomendação: [...]
- Critério de aceite:
  - [ ] [...]

[repetir para todos os passos]

## 5. Síntese

- **Quantos passos têm falha?** [n / total]
- **Pontos com maior dificuldade:** [...]
- **Probabilidade de conclusão da tarefa por novo usuário:** Alta / Média / Baixa

## 6. O que está funcionando bem

[2–3 pontos.]

## 7. Recomendações priorizadas

| # | Mudança | Severidade | Critério de aceite |
|---|---------|-----------|---------------------|
| 1 | [...] | [0–4] | [...] |

## 8. Próximo passo sugerido

[1 ação — geralmente: usability testing com 5 usuários reais.]
```

---

## 4. Regras comuns aos 3 templates

- **Todo finding tem critério de aceite** (sem exceção).
- **Toda recomendação é implementável** (mudança concreta — não "tornar mais moderno").
- **Seção "o que está funcionando bem" é obrigatória** e não pode estar vazia.
- **Encaminhamentos para outras skills** são listados explicitamente.
- **Severidade Nielsen 0–4** padroniza prioridade.
- **Linguagem direta, sem jargão de venda.**

## 5. Checklist antes de entregar

- [ ] Modo escolhido foi compatível com o pedido?
- [ ] Contexto e usuário-alvo foram explicitados?
- [ ] Triagem aplicada (sintomas fora do escopo encaminhados)?
- [ ] Fluxos críticos foram percorridos passo a passo?
- [ ] Todo finding tem evidência + princípio + impacto + severidade + recomendação + critério de aceite?
- [ ] WCAG 2.2 AA verificada (mínimo: contraste, foco, teclado, target, labels, reflow, status, error)?
- [ ] Estados auditados?
- [ ] Seção "o que funciona bem" preenchida?
- [ ] Encaminhamentos listados quando aplicável?
- [ ] Calibragem por contexto refletida na severidade?
