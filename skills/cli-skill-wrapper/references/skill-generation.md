# Skill Generation — Template de SKILL.md para CLI Tools

Consulte este arquivo no **Step 4** para gerar o SKILL.md que acompanha o CLI.

---

## Principio

O SKILL.md de um CLI tool NAO e um --help melhorado. E um "manual de instrucoes" que ensina o agente:
1. QUANDO usar o CLI (triggers, cenarios)
2. COMO compor comandos em workflows
3. O QUE o output significa (parsing)

## Template

```markdown
---
name: [tool-name]
description: "[GEO-otimizado — usar geo-optimizer]"
---

# [Tool Name] — [subtitulo curto]

IRON LAW: [regra inquebravel especifica do dominio]

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `scripts/tool.py search <query>` | [o que faz] | `scripts/tool.py search "react table"` |
| `scripts/tool.py get <id>` | [o que faz] | `scripts/tool.py get abc123` |
| `scripts/tool.py list` | [o que faz] | `scripts/tool.py list --limit 5` |

## Common Workflows

### Buscar e usar
1. `scripts/tool.py search "query"` → encontrar item
2. `scripts/tool.py get <id>` → ver detalhes
3. [acao baseada nos detalhes]

### [Outro workflow comum]
1. [passo 1]
2. [passo 2]

## Output Format

### search
```
ID        NAME                           STATUS
abc123    Widget Alpha                   active
def456    Gadget Beta                    draft
```
Cada linha: ID (8 chars) + Nome (30 chars) + Status

### get
```
id: abc123
name: Widget Alpha
status: active
created_at: 2025-01-01
```
Key-value pairs, um por linha.

## Setup

```bash
# Configurar API key
export TOOL_API_KEY="your-key-here"

# Testar
scripts/tool.py --help
```

## When NOT to use

- [cenario onde outra skill e melhor]
- [cenario onde API direta e suficiente]
```

## Checklist de Geracao

- [ ] Description e GEO-otimizada (5+ verbos, triggers PT-BR + EN)
- [ ] Commands table cobre todas as operacoes
- [ ] Pelo menos 1 workflow documentado
- [ ] Output format explicado (agente sabe parsear)
- [ ] Setup instructions (auth, install)
- [ ] When NOT to use (diferenciacao)
- [ ] SKILL.md < 250 linhas

## Dicas

### Autodiscovery
O SKILL.md deve mencionar que o agente pode usar `--help`:
```
Para descobrir todos os comandos disponíveis: `scripts/tool.py --help`
```
Isso habilita composicao emergente — o agente pode explorar comandos que nao estao no workflow documentado.

### Versionamento
Incluir versao do CLI no SKILL.md para detectar drift:
```
## Version
CLI v1.0 — Last verified: 2026-04-03
```

### Exemplos > Descricoes
Um exemplo de output vale mais que 3 paragrafos explicando o formato.
Sempre incluir output real de cada comando principal.
