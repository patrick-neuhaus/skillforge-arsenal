# Comparison Strategies — Step 6 reference

Carrega no Step 6 do `test-lab-architect`. Define **granularidade** + **tipo de comparação** por output. Decide caso a caso, não one-size-fits-all.

## Granularidade

### Macro
Compara só o **resultado final** da IA com o gabarito.

- Ex: IA decidiu `aprovado`, humano decidiu `aprovado` → match. Acurácia = % de matches sobre total.
- Bom pra: decisão binária ou de poucas classes (ex: aprovado/recusado/pendente).
- Limitação: não diz **por que** errou. IA reprovou um doc, humano aprovou — qual critério específico falhou?

### Micro
Compara cada **componente da decisão** com gabarito por componente.

- Ex: doc tem 5 critérios. IA atendeu 4, humano atendeu 5. Diff: critério X. Acurácia = % de critérios que batem por doc, agregada.
- Bom pra: outputs com sub-componentes (decisão final + lista de critérios atendidos, ou output multi-campo).
- Limitação: precisa gabarito mais detalhado (não só "aprovado", mas "aprovado porque atendeu A, B, C, D, E").

### Macro + Micro juntos (recomendado pra apps tipo athié)
Lab mostra os dois lados:
- Acurácia macro: "IA decidiu igual ao humano em 87% dos docs"
- Acurácia micro: "IA atende em média 94% dos critérios; critério X é o mais divergente (60% match)"

Macro responde "é confiável?", micro responde "onde tá errando?". Sem micro, gestor não sabe o que ajustar.

## Tipo de comparação — escolha por output

### Binária
Output é uma classe definida (aprovado/recusado, válido/inválido, A/B/C). Compara via igualdade direta.

- Implementação trivial: `output_ia === output_humano`
- Acurácia: contagem direta
- Custo: zero por comparação
- Bom pra: status, classificação, decisão final

### LLM-as-judge
Output é texto qualitativo (resumo, análise, justificativa). Outro LLM avalia se o output da IA bate com o gabarito.

- Implementação: prompt do judge recebe (output_ia, output_humano) → retorna score 0-1 ou aprovado/reprovado com razão
- Acurácia: média dos scores ou % de aprovações do judge
- Custo: 1 chamada de LLM por comparação (não trivial em volume — 1000 testes ≠ baratos)
- Bom pra: outputs sem resposta única correta. Resumo de doc, análise de risco, recomendação.
- Pegadinha: judge pode ter os próprios vieses. **Calibrar contra labels humanas** antes de confiar (ver hamelsmu/evals-skills/validate-evaluator).

### Híbrida
Output tem partes binárias + partes qualitativas. Cada parte usa estratégia própria.

- Ex (athié): decisão final = binária (aprovado/recusado), justificativa textual da decisão = LLM-as-judge.
- Implementação: comparison runner roda parte binária local + chama judge só pra parte qualitativa.
- Acurácia: reporta as duas separadas. Não soma — significados diferentes.
- Bom pra: maioria dos casos reais. Pouco output é puramente binário ou puramente qualitativo.

## Tabela de decisão

| Output da IA | Granularidade | Tipo de comparação |
|--------------|---------------|--------------------|
| Status binário (aprovado/recusado) | Macro | Binária |
| Classificação multi-classe (A/B/C/D) | Macro | Binária |
| Decisão + lista de critérios atendidos | Macro + Micro | Binária (tudo) |
| Score numérico (0-100) | Macro | Threshold ou diff numérico |
| Resumo / análise textual | Macro | LLM-as-judge |
| Decisão + justificativa textual | Macro + Micro | Híbrida (binária + judge) |
| Multi-campo extraído (CPF, nome, data) | Micro | Binária por campo |

## Considerações de custo

LLM-as-judge não é gratuito. Pra batch de 1000 casos, com Claude 4.7 1M, custo é não-trivial. Considerações:

- **Modelo do judge ≠ modelo do agente**. Judge pode ser modelo mais barato (haiku) se o critério é claro.
- **Cache**: se o gabarito é estável, judge pode salvar score por (input_hash, output_hash) e reusar.
- **Sample**: pra rodar o lab full-batch ocasionalmente + amostra de 50 a cada teste pra iteração rápida.

## Calibração de LLM-as-judge

Importante mas fora do escopo desta skill. Se Patrick precisar de calibração rigorosa (TPR/TNR contra labels humanas, bias correction), encaminha pra `hamelsmu/evals-skills/validate-evaluator`.

Mínimo aqui: documenta que judge não foi calibrado, e que primeiros runs do lab vão ter erro do judge embutido na medição. Patrick decide se isso é aceitável pro caso ou se precisa investir em calibração.

## Anti-padrões

- **One-size-fits-all**: usar binária pra tudo (incluindo texto qualitativo) → não detecta nuances. Ou usar LLM-judge pra tudo (incluindo binário) → custo absurdo sem ganho.
- **Acurácia agregada misturando tipos**: nunca soma acurácia binária com score do judge. Reporta separado.
- **Confiar no judge sem calibrar**: judge pode ter viés sistemático. Sempre rodar amostra contra labels humanas antes de confiar nos números.