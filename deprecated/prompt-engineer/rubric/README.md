# Rubrics — prompt-engineer

Rubrics YAML por tipo de prompt validado. Cada rubric carrega critérios específicos pro tipo de artefato, evitando aplicação errada de critérios genéricos (gap principal documentado em `prompt-engineer-gaps-2026-04-10.md`).

## Tipos disponíveis

| Tipo | Arquivo | Quando usar |
|------|---------|-------------|
| `claude-md` | `claude-md.yaml` | CLAUDE.md, system prompts híbridos com behavioral + operational + memory + routing sections |
| `technical-plan` | `technical-plan.yaml` | Planos de implementação, PRDs, specs, planos de refactor |
| `iron-laws` | `iron-laws.yaml` | Blocos de IRON LAWS, routing tables, regras comportamentais |
| `system-prompt` | `system-prompt.yaml` | System prompts de chatbots/agents, SKILL.md, prompts de produção |

## Como usar

### Via prompt-engineer skill (recomendado)
```
prompt-engineer --validate --type <tipo> <arquivo>
```

### Via promptfoo direto
```bash
promptfoo eval -c rubric/<tipo>.yaml --vars file=<path>
```

## Estrutura de uma rubric

Cada rubric tem:
- **Critérios CORE** (peso 80-100) — deal-breakers
- **Critérios USEFUL** (peso 50-79) — warnings
- **Critérios MARGINAL** (peso 0-49) — nice-to-have
- **Critérios UNIVERSAIS** — relevantes pra >1 tipo (calibração 4.x, attention budget, etc)

Cada critério tem ID (R001, U001, etc) pra rastreabilidade dos gaps documentados.

## Threshold

Score >= 75/100 = APROVADO pra produção.
Score 60-74 = APROVADO COM RESSALVAS (corrigir P1 antes).
Score < 60 = REPROVADO.

## Retroalimentação

Quando descobrir um gap que a rubric atual não pega:

1. Crie arquivo em `gaps/gap_YYYY-MM-DD_<topico>.md` (template em `gaps/_template.md`)
2. Documente: prompt testado, o que rubric perdeu, consequência real, critério proposto
3. Aprove inclusão na rubric (manual — auto-edição é proibida pela regra anti-drift)
4. Adicione critério novo no YAML com novo ID (Rxxx)
5. Incremente version no header do YAML

**Regra anti-drift:** rubric só cresce via gap documentado. Proibido adicionar critério especulativo.

## Histórico

- **v1 — 2026-04-10:** versão inicial. Rubrics derivadas de:
  - `prompt-engineer-gaps-2026-04-10.md` (3 alvos auditados manualmente)
  - 5 gaps estruturais do `prompt-engineer` atual
  - 4 erros de aplicação em planos técnicos
  - 6 gaps em routing tables
