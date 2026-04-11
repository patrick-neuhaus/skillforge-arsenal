**Data:** 2026-04-10
**Descobridor:** Claude (durante Sub-fase 1.5 de execução do plano v3)
**Tipo de prompt afetado:** technical-plan

## O prompt testado

Plano v3 fluffy-giggling-phoenix.md, Wave 1.5 ("Re-validar plano com setup novo"). Wave assume que `promptfoo eval` vai rodar end-to-end mas não declara que precisa de `ANTHROPIC_API_KEY` ou similar configurada.

## O que a rubric atual NÃO pegou

A rubric `technical-plan.yaml` v1 tem 9 critérios, nenhum verifica "as ferramentas que esse plano usa estão CONFIGURADAS no ambiente onde vai rodar?".

Critérios atuais checam: DAG, reversibilidade, sucesso por fase, chicken-and-egg, failure modes, decisões pra humano, esforço, escopo negativo, checkpoints. Nenhum sobre setup ambiental das ferramentas usadas.

## Consequência real

Wave 1.5 falhou em executar o plano como escrito. Tive que pivotar pra "rodar a rubric mentalmente" porque promptfoo não rodava sem API key. **Plano de score 87.6 mas que precisava de setup adicional não declarado.** Patrick teria que configurar API key entre Wave 1.4 e 1.5 sem aviso prévio.

Em projetos reais isso vira: developer junior segue plano linear, chega na Fase X, ferramenta não roda, perde 30 min descobrindo o que faltou configurar.

## Critério proposto

Adicionar em `rubric/technical-plan.yaml`:

```yaml
# R008 — Environment prerequisites declared (peso 80)
- type: llm-rubric
  value: |
    Pra cada ferramenta externa usada no plano, há declaração explícita
    de pré-requisito de configuração?

    Procure por:
    - "Pré-requisito de ambiente: <tool> instalado E <env var> configurada"
    - Lista de "Setup checklist" no início do plano
    - Por wave: "Antes de executar, garantir que <X> está configurado"

    Ferramentas que tipicamente precisam de setup:
    - npm packages globais (precisa npm + node)
    - APIs externas (precisa API key em env)
    - Comandos CLI customizados (precisa estar no PATH)
    - Hooks (precisa Claude Code suportar protocolo)
    - Containers/Docker (precisa Docker rodando)

    Se TODOS os requisitos de setup estão declarados → score 100
    Se >60% → score 70
    Se <30% → score 30
    Se nada → score 0

    Liste pré-requisitos de ambiente IMPLÍCITOS (assumidos mas não declarados).
```

## ID sugerido

**R008** (próximo livre na rubric `technical-plan.yaml`, depois de R007)

## Status

- [x] Aprovado pra inclusão (decisão de Claude — gap real, descoberto durante execução)
- [ ] Adicionado na rubric (precisa Patrick aprovar via `prompt-engineer --update-rubric --gap <este_arquivo>`)
- [ ] Test case de regressão criado
