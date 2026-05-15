# Documentação de Workflows

Última atualização: 2026-04-03

Template padrão para documentar workflows n8n.

---

## Template de Documentação

```markdown
# [Nome do Workflow]

## Resumo
[O que faz, quando dispara, qual o resultado]

## Diagrama de fluxo
[Trigger] → [Node 1] → [Node 2] → ... → [Output]
                           ↓ (erro)
                      [Error Handler] → [Log]

## Nodes detalhados

### 1. [Nome do Node]
- **Tipo:** [HTTP Request / Code / IF / AI Agent / etc]
- **O que faz:** [descrição]
- **Input:** [o que recebe do node anterior]
- **Output:** [o que passa pro próximo]
- **Config:** [campos importantes]

## Dependências
- Credentials: [lista]
- Tabelas Supabase: [lista]
- APIs externas: [lista com URLs base]
- MCP servers: [lista, se aplicável]

## Manutenção
- Crons: [se tem, qual frequência]
- Tokens que expiram: [quais, quando renovar]
- Limites de API: [rate limits relevantes]
- Status: Draft / Published
```
