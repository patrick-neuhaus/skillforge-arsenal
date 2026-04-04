# Tasks — Templates e Guias

Referência detalhada para criação de tasks executáveis a partir de PRDs ou briefings.

## Template de task para ClickUp

```
Titulo: [Verbo no infinitivo] + [o que] + [onde]
Ex: "Criar tela de login com autenticacao Supabase"

Descricao:
## Contexto
[Por que essa task existe. 1-2 frases. O junior precisa entender o porque.]

## O que fazer
[Lista objetiva do que precisa ser implementado]
1. ...
2. ...
3. ...

## Criterios de aceitacao
[Quando essa task esta PRONTA. Seja especifico.]
- [ ] [Criterio 1]
- [ ] [Criterio 2]
- [ ] [Criterio 3]

## Recursos
[Links, referencias, exemplos que ajudam]
- PRD: [link]
- Figma/referencia: [link]
- API docs: [link]

## Duvidas?
Pergunte ANTES de comecar, nao depois de fazer errado.
```

## Regras de ouro

- Task sem criterio de aceitacao = task mal escrita. SEMPRE inclua.
- Task >4h estimadas provavelmente pode ser quebrada.
- Task deve ter UM responsavel. "Patrick e Hygor" nao e responsavel.
- Inclua o "Contexto" sempre. Junior sem contexto chuta, e chuta errado.
- No ClickUp, use tags ou custom fields pra marcar a wave.

## Formato: User Stories vs Job Stories

- **User Story:** "Como [persona], eu quero [acao] para que [beneficio]"
  - Melhor pra: features voltadas pro usuario final
- **Job Story:** "Quando [situacao], eu quero [motivacao] para que [resultado]"
  - Melhor pra: automacoes, triggers, fluxos tecnicos

## Criterio INVEST

Toda story boa segue INVEST:
- **I**ndependent — pode ser feita sem depender de outra
- **N**egotiable — escopo pode ser ajustado
- **V**aluable — entrega valor mensuravel
- **E**stimable — da pra estimar esforco
- **S**mall — cabe num ciclo/sprint
- **T**estable — tem criterio de aceitacao verificavel

## Working Backwards (tasks complexas)

Quando a task e grande demais pra quebrar direto:
1. Escreva o resultado final PRIMEIRO
2. Liste o que precisa existir pra esse resultado acontecer
3. Quebre cada item em sub-tasks
4. Ordene por dependencia

## Agrupamento por Waves

Se o PRD ja veio com waves (da skill product-discovery-prd), respeite. Se nao, agrupe:

- **Wave 1:** Tasks do fluxo principal. O que precisa existir pra testar a hipotese.
- **Wave 2:** Tasks complementares. Integracoes, fluxos secundarios, ajustes.
- **Wave 3:** Tasks de polimento. UX, performance, edge cases.

**Regra:** A equipe so comeca a Wave 2 quando a Wave 1 ta concluida e validada. Nao misture waves.

## Estimativa P/M/G

| Tamanho | Tempo estimado | Quando usar |
|---------|---------------|-------------|
| P (Pequeno) | ate 2h | Bug fix, ajuste de copy, config simples |
| M (Medio) | 2-4h | Feature simples, integracao basica, tela nova |
| G (Grande) | 4-8h | Feature complexa, refactor, integracao com API nova |

Se passou de G, quebre em tasks menores. Nao existe GG — existe task mal quebrada.
