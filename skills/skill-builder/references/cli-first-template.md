# CLI-First Skill Template

Consulte este arquivo no **Step 3** quando a skill wrapa um CLI tool ou API externa.

---

## Quando Usar CLI-First

Escolha CLI-first quando:
- A skill **retorna dados** (nao apenas raciocina)
- O output e **estruturado e previsivel** (JSON, tabelas, listas)
- A operacao e **deterministrica** (mesma entrada = mesma saida)
- O output precisa ser **curto** pra preservar context window

CLI-first e superior a MCP porque:
- CLIs retornam outputs curtos e diretos
- MCPs retornam JSONs pesados que degradam performance progressivamente
- O agente pode descobrir novos comandos dinamicamente (`tool --help`)

## Tres Modelos de Skill

| Modelo | Quando usar | Exemplo |
|--------|-------------|---------|
| **System-prompt-only** | Raciocinio, criacao, analise | Prompt Engineer, Reference Finder |
| **CLI-first** | Dados, ferramentas, APIs | Agent Tools (inference.sh), scan tools |
| **Hibrida** | IA decide + script executa | Branding (IA cria brief → script aplica) |

## Anatomia de uma Skill CLI-First

```
minha-skill/
├── SKILL.md           # Manual de instrucoes pro CLI
│                      # Documenta: comandos, flags, output format
│                      # NAO duplica o --help, complementa com workflow
├── references/        # Exemplos de uso, patterns avancados
├── scripts/           # O CLI real (Python, shell, Node)
│   └── tool.py        # Ponto de entrada: `python scripts/tool.py <args>`
└── assets/            # Arquivos que o CLI usa (templates, configs)
```

## Template SKILL.md para CLI-First

```markdown
---
name: minha-tool
description: "[keywords GEO otimizadas]"
---

# Nome da Tool

IRON LAW: [regra inquebravel]

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `scripts/tool.py scan <path>` | Scans X for Y | `scripts/tool.py scan ./src` |
| `scripts/tool.py fix <id>` | Fixes issue #id | `scripts/tool.py fix BUG-001` |

## Workflow

1. Run `scripts/tool.py scan` to identify issues
2. Review output with user
3. ⛔ GATE: Confirm before applying fixes
4. Run `scripts/tool.py fix` for approved items

## Output Format

[Documenta o formato de output do CLI pra que o agente saiba interpretar]

## When NOT to use

[Diferenciacao clara]
```

## Regras de Design do CLI

1. **Output curto:** Maximo 20-30 linhas por operacao. Se precisa de mais, pagine
2. **Formato parseavel:** JSON ou tabela. Nunca texto livre longo
3. **Exit codes:** 0 = sucesso, 1 = erro, 2 = warning
4. **Stderr pra erros:** Stdout e limpo, stderr tem diagnostico
5. **Flags padrao:** `--help`, `--verbose`, `--json`, `--dry-run`
6. **Autodiscovery:** `tool --help` lista todos os comandos disponiveis

## Composicao Emergente

Quando o agente tem acesso a um CLI com multiplos comandos, ele comeca a compor workflows sozinho:
- "Scan → filter by severity → fix critical only"
- Nao precisa pre-configurar o pipeline — o agente descobre

Isso e **composicao emergente** — o padrao mais poderoso do CLI-first.
