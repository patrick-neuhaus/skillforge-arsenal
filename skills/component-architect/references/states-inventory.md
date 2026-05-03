# `references/states-inventory.md`

> Inventário canônico dos estados que componentes interativos devem cobrir. **Esta skill é dona da anatomia + comportamento + a11y de cada estado.** Tokens visuais (cores/contraste/motion) moram em `ui-design-system/references/component-state-rubric.md`. `ux-audit` referencia este arquivo na Fase 5.1 (estados auditados).

## 1. Como usar

Para cada componente interativo planejado/auditado, percorra os 17 estados. Para cada um, declare:

| Aspecto | Onde | Dono |
|---|---|---|
| **Anatomia** (DOM, slots, sub-elementos no estado) | aqui | `component-architect` |
| **Comportamento** (eventos, transições, foco, anúncio SR) | aqui | `component-architect` |
| **Contrato de a11y** (ARIA, role, aria-*) | aqui | `component-architect` |
| **Token visual** (cor de fundo/borda/texto, contraste, motion) | `ui-design-system/references/component-state-rubric.md` | `ui-design-system` |
| **Auditoria observável** (estado funciona em fluxo real?) | `ux-audit/Fase 5.1` | `ux-audit` |

Estado ausente OU contrato de a11y mal definido = finding `component-architect`.
Token errado/inconsistente = finding `ui-design-system`.
Estado existe mas não funciona em fluxo = finding `ux-audit`.

## 2. Os 17 estados canônicos

### Estados de presença (todo componente interativo precisa)

| # | Estado | Quando | Anatomia / comportamento | a11y |
|---|--------|--------|--------------------------|------|
| 1 | **default** | Repouso, sem interação | Componente visível, interativo, sem ênfase | Foco programático possível; role correto |
| 2 | **hover** | Mouse sobre o alvo | Sinal visual de affordance; cursor: pointer em controles | Não exclusivo — toda info em hover precisa equivalente em focus (1.4.13) |
| 3 | **focus-visible** | Foco por teclado / SR | Indicador visível distinto de hover; nunca `outline:none` sem substituto | 2.4.7 obrigatório AA; 3:1 contraste (ui-DS owns) |
| 4 | **active / pressed** | No instante do clique/toque | Feedback tátil; deformação leve permitida | aria-pressed em toggles; estado anunciado |
| 5 | **disabled** | Indisponível por contexto | Não focável OU focável-com-aria-disabled (preferir o segundo); cursor: not-allowed | Explicar **por que** está disabled (tooltip ou texto adjacente); `aria-disabled="true"` |
| 6 | **read-only** | Leitura sem edição | Visual ≠ disabled; foco e cópia funcionam | `aria-readonly="true"`; nunca confundir com disabled |

### Estados de atividade (componentes com fluxo)

| # | Estado | Quando | Anatomia / comportamento | a11y |
|---|--------|--------|--------------------------|------|
| 7 | **loading** | Operação assíncrona em curso | Spinner inline + texto "Salvando…"; controle some/desabilita; preserva layout | `aria-busy="true"` no container; live region para texto de progresso |
| 8 | **async** | Background fetch sem bloquear UI | Indicador discreto (skeleton, opacidade, bar) | aria-live polite; não roubar foco |
| 9 | **error** | Falha após tentativa | Mensagem inline próxima da causa; sugestão acionável; dado preservado | `role="alert"` ou live region assertive; foco programado pra primeiro erro do form |
| 10 | **success** | Conclusão observável | Confirmação visual + textual; toast OU inline | `role="status"` (4.1.3); auto-dismiss respeita reduced-motion |
| 11 | **empty** | Sem dado pra mostrar | Ilustração opcional + headline + ação primária ("Criar primeiro X") | Não é erro — não usar role=alert; texto descritivo |
| 12 | **no-results** | Filtro/busca não retorna | Diferente de empty: usuário **fez algo** que não retornou | Sugerir limpar filtro / refinar query |

### Estados de seleção / expansão

| # | Estado | Quando | Anatomia / comportamento | a11y |
|---|--------|--------|--------------------------|------|
| 13 | **selected** | Item ativo em lista/tab/radio | Indicador visual claro; permanece após scroll | `aria-selected="true"` ou `aria-current="page/step/true"` |
| 14 | **expanded** | Disclosure aberto (accordion, dropdown, tree) | Conteúdo aparece próximo do trigger; chevron rotaciona | `aria-expanded="true"` no trigger; `aria-controls` aponta painel |
| 15 | **drag** | Item sendo arrastado | Cursor: grabbing; ghost/preview; alvos válidos destacados | Alternativa sem arrastar (2.5.7 AA); foco no item após drop |

### Estados de overflow / restrição

| # | Estado | Quando | Anatomia / comportamento | a11y |
|---|--------|--------|--------------------------|------|
| 16 | **overflow** | Conteúdo excede container | Truncate + tooltip OU scroll + indicador; nunca corte silencioso | Tooltip não pode forçar mouse fora; dispensável (1.4.13) |
| 17 | **invalid** (sub de error) | Validação síncrona | Borda/ícone + mensagem inline; revalida em blur ou input | `aria-invalid="true"`; `aria-describedby` aponta mensagem |

## 3. Matriz por componente (exemplos)

| Componente | default | hover | focus | active | disabled | loading | error | success | empty | selected | expanded |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Button | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (action button) | n/a | n/a | n/a | n/a | n/a |
| Input | ✅ | n/a | ✅ | n/a | ✅ | n/a | ✅ | n/a | n/a | n/a | n/a |
| Select / Combobox | ✅ | ✅ | ✅ | n/a | ✅ | ✅ (async load) | ✅ | n/a | ✅ (no options) | ✅ | ✅ |
| Tabs | ✅ | ✅ | ✅ | n/a | n/a | n/a | n/a | n/a | n/a | ✅ | n/a |
| Modal / Dialog | ✅ | n/a | ✅ (focus trap) | n/a | n/a | n/a | n/a | n/a | n/a | n/a | ✅ |
| Table row | ✅ | ✅ | ✅ | n/a | n/a | ✅ (loading row) | n/a | n/a | ✅ (no data) | ✅ | ✅ (expand) |
| Form | ✅ | n/a | n/a | n/a | n/a | ✅ (submitting) | ✅ | ✅ | n/a | n/a | n/a |
| List item (drag) | ✅ | ✅ | ✅ | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a + drag |

✅ = obrigatório / n/a = não se aplica.

## 4. Critério de auditoria por estado

Para cada estado declarado:

```
- Existe no DOM/render do componente?
- O token visual está conforme `ui-design-system/component-state-rubric.md` (cor, contraste, motion)?
- O contrato de a11y está implementado (aria-*, role, foco)?
- Em fluxo real, o estado é alcançável e perceptível pelo usuário (validar via `ux-audit`)?
```

Falha em qualquer uma das 4 = finding. A skill responsável pelo finding muda conforme a falha:
- Falta no DOM / a11y errado → `component-architect`
- Token visual errado / inconsistente → `ui-design-system`
- Estado existe mas não funciona em fluxo → `ux-audit`

## 4.5 Contrato de microinteracao por estado

Para cada componente interativo, declare o comportamento minimo dos estados, sem definir token visual aqui:

| Estado / caso | Contrato comportamental | Dono do detalhe visual |
|---|---|---|
| press / active | feedback imediato; se for botao, estado nao espera animacao para confirmar clique | `ui-design-system` tokens; `motion-design` se precisar spec |
| focus-visible | separado de hover; teclado recebe feedback instantaneo ou quase instantaneo | `ui-design-system` contraste/focus token |
| loading | preserva dimensao do componente; nao causa layout shift; texto ou live region quando bloqueia acao | `ui-design-system` motion token |
| disabled | explica motivo quando a causa nao e obvia; nao vira read-only | `ui-design-system` cor/contraste |
| tooltip / popover | ancora no trigger; dismiss por Esc/click outside; foco preservado | `motion-design` se origem/motion for problema |
| expanded | `aria-expanded` muda junto com DOM; conteudo aparece proximo do trigger | `motion-design` se precisar spec de reveal |

Boundary:

- Anatomia, eventos, foco, ARIA e layout sem shift ficam aqui.
- Cor, contraste, duration, easing e press token ficam em `ui-design-system`.
- Motion criativo, origem espacial, timing refinado e auditoria `Antes | Depois | Por que` ficam em `motion-design`.
- Bug React, focus refs e browser runtime ficam em `react-patterns`.

## 5. Anti-patterns

- **Disabled sem motivo visível** — usuário não sabe por quê. Pelo menos tooltip/texto adjacente.
- **Loading que esconde o controle** — usuário pensa que clicou errado. Manter visível, com estado.
- **Error genérico** — "Erro ao processar" não é estado, é desistência. Sugestão acionável obrigatória.
- **Empty = error** — `role="alert"` em estado vazio. Não é alerta; é convite à primeira ação.
- **Hover sem focus equivalente** — exclui teclado e SR (1.4.13).
- **Drag sem alternativa** — viola 2.5.7. Botão "mover para X" obrigatório.
- **Outline:none sem substituto** — viola 2.4.7. Use `:focus-visible` com 3:1 contraste.
- **Estados visuais sem token** — drift sistêmico. Cada estado consome token nominado (`--color-state-X`).
- **Selected = active visual** — diferentes semânticas, não confundir. Active é instante; selected é persistente.

## 6. Output do estado-inventário (no plano de componente)

Componente novo / refatorado declara explicitamente os estados cobertos:

```markdown
## States — <ComponentName>

| Estado | Coberto | Token (DS) | a11y | Critério aceite |
|---|---|---|---|---|
| default | ✅ | --color-surface-1 | role="button" | render limpo |
| hover | ✅ | --color-surface-1-hover | — | mouse over altera fundo |
| focus-visible | ✅ | --color-focus-ring | outline visível | tab com 3:1 contraste |
| active/pressed | sim | --motion-press | aria-pressed quando toggle | clique tem feedback imediato |
| disabled | ✅ | --color-surface-disabled | aria-disabled | não recebe submit |
| loading | ✅ | --motion-spinner | aria-busy + live region | spinner < 100ms; texto "Salvando…" |
| ... | | | | |
```

Sem essa tabela = componente incompleto. Não passa Phase 4 review.

## 7. Boundary com outras skills

- **`ui-design-system`** — define **token visual** de cada estado (cor, contraste, easing). Não define anatomia/comportamento.
- **`ux-audit`** — referencia este arquivo na Fase 5.1 para auditar inventário em fluxo real. Findings de "estado ausente em uso" → encaminhar pra esta skill.
- **`react-patterns`** — implementação técnica (useState, effects, refs, focus management). Não duplica o contrato; aplica.
- **`design-system-audit`** — verifica adesão de app a DS externo, não anatomia interna.
