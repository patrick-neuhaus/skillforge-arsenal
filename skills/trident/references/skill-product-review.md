# Skill Product Review — Review de Skill como Produto

Consulte este arquivo no modo `--skill` para avaliar uma skill como produto publicavel.

---

## Checklist de Review

### 1. GEO Quality (Description)
- [ ] Score GEO >= 12/15 (usar scoring do geo-optimizer)
- [ ] Core capability na primeira frase
- [ ] 5+ verbos de acao
- [ ] 5+ substantivos de dominio
- [ ] Frases naturais PT-BR e EN
- [ ] Diferenciacao clara ("NAO use pra X")
- [ ] Under 1024 caracteres

### 2. Structure Quality
- [ ] SKILL.md < 250 linhas
- [ ] Frontmatter valido (name, description)
- [ ] Iron Law presente no topo
- [ ] Workflow checklist com markers
- [ ] Confirmation gates antes de acoes criticas
- [ ] Anti-patterns listados
- [ ] Pre-delivery checklist
- [ ] References carregados progressivamente

### 3. Architecture Decision
| Modelo | Adequado quando |
|--------|----------------|
| System-prompt-only | Raciocinio, criacao, analise |
| CLI-first | Retorna dados, output estruturado |
| Hibrida | IA decide + script executa |

- [ ] Modelo de arquitetura correto pro caso de uso
- [ ] Se CLI-first: output mais curto que API equivalente
- [ ] Se hibrida: scripts sao deterministicos e testados

### 4. Distribution Readiness
- [ ] Roteiro de perguntas incluido (coleta contexto do usuario)
- [ ] Exemplos concretos de uso
- [ ] Instalacao e um unico comando
- [ ] Funciona com conversa nova (nao depende de contexto previo)
- [ ] Documentacao de setup (se precisa de env vars, deps, etc.)

## Output Format

```markdown
## Skill Product Review: [nome]

### GEO Score: [X]/15
[detalhes]

### Structure Score: [X]/[total checks]
[findings]

### Architecture: [System-prompt / CLI-first / Hibrida]
[avaliacao]

### Distribution: [Ready / Needs Work / Not Ready]
[o que falta]

### Verdict: [PUBLISH / IMPROVE FIRST / MAJOR REWORK]
```
