---
name: cli-skill-wrapper
description: "Transform any API into a CLI tool optimized for AI agents, then generate the companion SKILL.md. Bridges the gap between heavy JSON APIs and lightweight CLI outputs that preserve context window. Use when user asks: 'quero wrapar essa API', wrap API, create CLI tool, 'transformar API em CLI', build agent tool, API to CLI, 'criar ferramenta pro Claude', 'o MCP tá pesado', reduce context bloat, 'fazer um CLI pra isso', generate CLI wrapper, 'empacotar essa API', create skill from API, 'quero que o agente use essa API', tool for agents, CLI-first skill, agent tooling, optimize API for agents. Also: 'MCP tá lento', 'JSON pesado demais', 'quero output mais curto'."
---

# CLI Skill Wrapper — API → CLI → Skill

IRON LAW: NEVER wrap an API without verifying the CLI output is shorter than the raw API JSON response. The entire point is context window savings — if the CLI returns MORE tokens than the API, the wrapper is counterproductive.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--analyze` | Analyze API and recommend CLI design | default |
| `--wrap` | Full pipeline: analyze → design → generate CLI + skill | - |
| `--compare` | Compare CLI output size vs raw API JSON | - |

## Workflow

```
CLI Skill Wrapper Progress:

- [ ] Step 1: Analyze API ⚠️ REQUIRED
  - [ ] 1.1 Identify API type (REST, GraphQL, SDK, local binary)
  - [ ] 1.2 Map endpoints/commands the agent would use
  - [ ] 1.3 Analyze response format and size
  - [ ] 1.4 Identify auth requirements
- [ ] Step 2: Design CLI Interface
  - [ ] 2.1 Map API operations → CLI commands
  - [ ] 2.2 Design flags and arguments
  - [ ] 2.3 Design output format (compact, parseable)
  - [ ] ⛔ GATE: Present CLI design for approval
- [ ] Step 3: Generate Wrapper Script
  - [ ] 3.1 Write CLI script (Python/Node/Shell)
  - [ ] 3.2 Implement auth handling
  - [ ] 3.3 Implement output compression
  - [ ] 3.4 Add --help autodiscovery
  - [ ] 3.5 Test script
- [ ] Step 4: Generate SKILL.md ⛔ BLOCKING
  - [ ] 4.1 Write skill as "instruction manual" for the CLI
  - [ ] 4.2 Apply GEO to description
  - [ ] 4.3 Verify output is shorter than raw API (IRON LAW)
  - [ ] ⛔ GATE: Present complete package for approval
```

If `--analyze`: Steps 1 only → report with recommendation.
If `--compare`: Quick comparison of CLI vs raw API response sizes.

## Step 1: Analyze API

Ask (if not clear from context):
- "Qual a API?" — URL, docs, SDK, ou binary local
- "Quais operações o agente precisa?" — listar, buscar, criar, atualizar, deletar
- "Qual a resposta típica?" — tamanho do JSON, campos relevantes vs noise

### API Type Classification

| Type | Wrapper approach | Example |
|------|-----------------|---------|
| REST API | Python/Node script com requests | Tavily, Exa, GitHub API |
| GraphQL | Script com query pré-definidas | Shopify, GitHub GraphQL |
| SDK/Package | Thin wrapper sobre SDK instalado | Supabase JS, Stripe |
| Local binary | Shell wrapper com output parsing | FFmpeg, ImageMagick |
| MCP Server | CLI replacement for heavy MCP | Any MCP returning large JSON |

Load `references/api-to-cli-patterns.md` for patterns per API type.

## Step 2: Design CLI Interface

### Command Structure

```
tool <command> [arguments] [--flags]

# Examples:
tool search "query" --limit 5 --format table
tool get <id> --fields name,email,status
tool list --filter active --sort created_at
tool create --input data.json
```

### Design Rules

1. **Commands map 1:1 to agent needs** — not to API endpoints. If the agent needs "search and get top result", make that ONE command
2. **Output is compact** — tables, key:value pairs, or minimal JSON. Never raw API response
3. **Flags have sensible defaults** — `--limit 10`, `--format table`
4. **`--help` lists all commands** — agent autodiscovery
5. **`--json` flag for structured output** — when agent needs to parse
6. **Exit codes are meaningful** — 0=success, 1=error, 2=warning

Load `references/skill-generation.md` for the SKILL.md template.

⛔ **GATE:** Present the command tree to user before generating code.

## Step 3: Generate Wrapper Script

### Output Compression Strategies

| Strategy | When to use | Example |
|----------|------------|---------|
| **Field filtering** | API returns 50 fields, agent needs 5 | `--fields name,email` |
| **Table format** | List of items | Tabulated output vs JSON array |
| **Summary mode** | Large response | `Found 42 items. Top 5: ...` |
| **Count only** | Agent just needs number | `--count` returns single number |
| **Pagination** | Large datasets | `--page 1 --limit 10` |

### Script Requirements

- **Language:** Python preferred (available everywhere), Node as alternative
- **Dependencies:** Minimal. Prefer stdlib over external packages
- **Auth:** env vars (`TOOL_API_KEY`) or config file (`~/.tool/config`)
- **Error handling:** stderr for errors, stdout clean for agent parsing
- **Timeout:** Default 30s, configurable with `--timeout`

### Testing

```bash
# Test basic commands
python scripts/tool.py --help
python scripts/tool.py search "test query"
python scripts/tool.py get <id>

# Verify output size (IRON LAW)
python scripts/tool.py search "test" | wc -c    # CLI output
curl -s "api.example.com/search?q=test" | wc -c  # Raw API
# CLI must be smaller
```

## Step 4: Generate SKILL.md

The SKILL.md is NOT a copy of --help. It's the "instruction manual" that teaches the agent WHEN and HOW to use the CLI.

Load `references/skill-generation.md` for the template.

Key sections:
1. **Description** — GEO-optimized (use geo-optimizer)
2. **Commands table** — command, description, example
3. **Workflow** — typical sequence of commands for common tasks
4. **Output format** — how to interpret CLI output
5. **When NOT to use** — differentiation

⛔ **GATE:** Present complete package (script + SKILL.md). Verify IRON LAW: CLI output < raw API.

## Anti-Patterns

- **Wrapping everything:** Not every API needs a CLI. If the agent uses it once, just call the API directly
- **Fat CLI:** CLI that returns MORE data than the API — defeats the purpose
- **No autodiscovery:** Without `--help`, agent can't explore capabilities
- **Hardcoded auth:** API keys in script code instead of env vars
- **No error messages:** Silent failures make debugging impossible for the agent
- **Duplicating MCP:** If a well-maintained MCP exists and context isn't an issue, don't reinvent

## Pre-Delivery Checklist

- [ ] CLI output is shorter than raw API response (IRON LAW — measure in bytes)
- [ ] `--help` works and lists all commands
- [ ] Auth uses env vars (not hardcoded)
- [ ] Error messages go to stderr
- [ ] Exit codes are meaningful (0/1/2)
- [ ] SKILL.md has GEO-optimized description
- [ ] SKILL.md has commands table with examples
- [ ] At least 2 common workflows documented

## When NOT to use

- API is already a local binary with good CLI → just write the skill, no wrapper needed
- Agent uses API once → call directly, don't wrap
- Well-maintained MCP exists and context isn't a problem → use the MCP
- Creating a skill (no API involved) → use **skill-builder**

## Integration

- **skill-builder** — cli-skill-wrapper generates the CLI + basic SKILL.md; skill-builder can then evolve it
- **geo-optimizer** — optimize the generated SKILL.md description
- **context-guardian** — context-guardian detects MCP bloat; cli-skill-wrapper provides the fix
