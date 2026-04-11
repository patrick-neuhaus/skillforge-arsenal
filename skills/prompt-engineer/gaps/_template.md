# Gap Template

Copie este arquivo pra `gap_YYYY-MM-DD_<topico>.md` quando descobrir gap novo.

---

**Data:** YYYY-MM-DD
**Descobridor:** Patrick / Claude / qual sub-skill
**Tipo de prompt afetado:** claude-md / technical-plan / iron-laws / system-prompt

## O prompt testado

```
<cole o trecho relevante>
```

## O que a rubric atual NÃO pegou

<descreva o problema concreto que o rubric deveria ter detectado mas não detectou>

## Consequência real

<o que aconteceu por causa do gap — perda de tempo, retrabalho, decisão errada>

## Critério proposto

```yaml
# Adicionar em rubric/<tipo>.yaml
- type: llm-rubric
  value: |
    <descrição do critério em natural language>

    Critérios de score:
    - Caso A → 100
    - Caso B → 60
    - Caso C → 30
```

## ID sugerido

R<NNN> (próximo livre na rubric correspondente)

## Status

- [ ] Aprovado pra inclusão
- [ ] Adicionado na rubric
- [ ] Test case de regressão criado
