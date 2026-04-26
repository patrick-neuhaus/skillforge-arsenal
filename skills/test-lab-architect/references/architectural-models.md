# Architectural Models — Step 5 reference

Carrega no Step 5 do `test-lab-architect`. Decide entre 3 modelos arquiteturais.

## Os 3 modelos

### Inline (gascat-style)

Validação acontece **dentro do fluxo de produção**. Cada output da IA tem campo de validação humana logo depois. Acurácia é calculada agregando essas validações.

- **Onde vive**: numa tela do app principal, geralmente perto do detalhe do objeto validado
- **Quem opera**: usuário final que já tá usando o app pra outros fins
- **Edita config?**: não — só anota divergências
- **Gabarito**: construído conforme valida (cada caso validado vira gabarito futuro)
- **Saída**: acurácia agregada por período

**Bom pra**: apps onde validação faz parte do trabalho real (ex: cada doc é revisado de qualquer jeito). Operador não precisa parar pra "testar".

**Ruim pra**: iterar prompts/critérios. Quem usa não pode editar lógica em produção. Mudança de prompt requer ciclo completo de dev + deploy.

### Standalone (athié-style)

Lab é um **ambiente paralelo isolado** da produção. Gestor entra no lab, edita prompts/critérios, roda contra base de gabarito, vê assertividade, compara com experimentos anteriores.

- **Onde vive**: tela ou subproduto separado (`/lab` no mesmo app, ou rota separada)
- **Quem opera**: gestor / domain expert / dev — quem tem permissão de editar lógica
- **Edita config?**: sim — prompts, critérios, validações
- **Gabarito**: pré-existe, é entrada do lab (não é gerado pelo lab)
- **Saída**: assertividade do experimento + diff vs experimentos anteriores

**Bom pra**: iterar lógica antes de mexer em prod. Múltiplos experimentos comparáveis. Gestor não-técnico mexe em prompt sem quebrar app real.

**Ruim pra**: capturar casos novos da realidade. Lab roda em mundo fechado (gabarito). Se tipo de caso novo aparecer em prod, lab não vê.

### Híbrido

Combina os dois: lab standalone pra iterar + canal de feedback inline em prod que alimenta o gabarito do lab.

- **Onde vive**: lab em rota separada, mas validações inline em prod alimentam a base de gabarito do lab
- **Edita config?**: sim no lab, não em prod
- **Gabarito**: cresce continuamente via inline; lab consome essa base
- **Saída**: lab dá assertividade dos experimentos; inline dá assertividade contínua de prod

**Bom pra**: apps maduros onde lab vai rodar por muito tempo e gabarito precisa evoluir com a realidade.

**Ruim pra**: MVP. Complexidade dobra. Não vale antes de validar que lab simples resolve.

## Como decidir — tabela de critérios

| Critério | Inline | Standalone | Híbrido |
|----------|:------:|:----------:|:-------:|
| Operador edita config (prompt/critério)? | Não | **Sim** | Sim |
| Operador é técnico? | Não importa | **Sim** | Sim |
| Volume de teste é alto (>50/semana)? | Não importa | **Sim** | Sim |
| Gabarito existe pronto? | Não precisa | **Sim, blocking** | Sim |
| Validação é parte do trabalho real do operador? | **Sim** | Não | Sim |
| Quer comparar versões de prompt/critério? | Não | **Sim** | Sim |
| Cliente paga pelo lab como produto? | Improvável | Sim | Sim |
| MVP ou maduro? | MVP | MVP | Maduro |

Default: se Patrick não tiver claro qual escolher, pergunte essas 3 primeiro:
1. Operador vai editar config no lab?
2. Validação é trabalho real ou parada pra testar?
3. Tem gabarito pronto?

Sim/Não/Sim → standalone. Não/Sim/Não → inline. Tudo sim → híbrido.

## Anti-pattern: escolher híbrido por achar "mais completo"

Híbrido só vale quando inline e standalone já provaram valor sozinhos. MVP de híbrido = construir 2 sistemas que conversam = 3x esforço. Sempre comece simples.

## Exemplos reais

- **Gascat**: validação de código de regulador. Operador valida o doc real contra IA no detalhe do regulador. **Inline** — caso clássico.
- **Athié**: gestor edita prompts/critérios de validação documental, testa contra base validada de SST. **Standalone** — caso clássico.
- **Cliente futuro com volume alto + iteração contínua**: híbrido pode justificar depois de 6+ meses do standalone rodando.