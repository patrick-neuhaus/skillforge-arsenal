# Window Management — Estrategias de Gestao de Context

Consulte este arquivo no **Step 1** para entender o que consome context e como mitigar.

---

## O que Consome Context Window

### Ranking por impacto (maior → menor)

| Fonte | Impacto | Mitigacao |
|-------|:-------:|-----------|
| **MCP tool responses** | Muito alto | JSON pesado. Preferir CLI tools que retornam outputs curtos |
| **Arquivos grandes lidos** | Alto | Ler trechos especificos (offset+limit), nao arquivo inteiro |
| **Skill references carregados** | Alto | Progressive loading — carregar so quando necessario |
| **Git diffs extensos** | Alto | Focar em arquivos relevantes, nao `git diff` inteiro |
| **Grep/Glob com muitos resultados** | Medio-alto | Usar filtros (glob, type) para reduzir resultados |
| **Historico de conversa** | Medio | Exchanges acumulam. /clear em breakpoints naturais |
| **System prompts e skills** | Medio | Fixo — nao controlavel pelo usuario |
| **Tool call overhead** | Baixo | Cada call adiciona metadata. Agrupar quando possivel |

## Sinais de Degradacao

O usuario nem sempre percebe que a qualidade esta caindo. Fique atento a:

1. **Respostas mais curtas que o usual** — modelo cortando corners
2. **Repeticao de informacao ja dita** — modelo "esquecendo" inicio da conversa
3. **Instrucoes ignoradas** — regras definidas no inicio sendo violadas
4. **Outputs mais genericos** — menos especifico ao contexto do projeto
5. **Erros de referencia** — confundir nomes de arquivos, funcoes, variaveis
6. **Demora anormal** — processamento mais lento com contexto grande

## Estrategias de Mitigacao

### Preventivas (antes de ficar pesado)

1. **Ler trechos, nao arquivos inteiros**
   ```
   # Ruim: le o arquivo todo (500+ linhas)
   Read file.tsx

   # Bom: le so a parte relevante
   Read file.tsx offset=42 limit=30
   ```

2. **Filtrar outputs de ferramentas**
   ```
   # Ruim: grep sem filtro
   grep "pattern" src/

   # Bom: grep com filtros
   grep "pattern" src/ --glob="*.tsx" --type=ts
   ```

3. **Usar CLI ao inves de MCP quando possivel**
   - CLI: retorna 5-20 linhas de texto curto
   - MCP: retorna JSON com metadata, schemas, etc. (10-50x mais tokens)

4. **Progressive loading em skills**
   - So carregar `references/` quando o step precisa
   - Nao carregar todas as references no inicio

### Reativas (quando ja esta pesado)

1. **Parar e gerar handoff** — usar `--handoff` antes que piore
2. **/clear e retomar** — com handoff document como primeiro prompt
3. **Dividir tarefa** — se implementacao e grande, fazer em batches
4. **Simplificar tool calls** — reduzir outputs, ser mais especifico

## Regra dos 40-50% (Videos 2 e 4)

"Nunca ultrapassar 40-50% da context window" — Deborah Folloni / DevGPT

| Fase | Budget ideal | Justificativa |
|------|:-----------:|---------------|
| SDD Research | ~30% | Precisa ler muitos arquivos |
| SDD Spec | ~25% | Le prd.md + gera spec |
| SDD Implement | ~40% | Le spec + escreve codigo |
| Trident Review | ~35% | Le diff + analisa |
| Skill chain (3+) | ~20% cada | /clear entre skills |

Se a tarefa precisa de mais que 50%, e sinal de que precisa ser dividida.

## CLI vs MCP — Impacto na Context Window

| Operacao | Via CLI | Via MCP | Diferenca |
|----------|:-------:|:-------:|:---------:|
| Buscar arquivo | ~50 tokens | ~200 tokens | 4x |
| Ler dados | ~100 tokens | ~500 tokens | 5x |
| Listar items | ~80 tokens | ~800 tokens | 10x |
| Query complexa | ~150 tokens | ~1500 tokens | 10x |

Recomendacao: se uma operacao pode ser feita via CLI ou MCP, preferir CLI.
A skill `cli-skill-wrapper` ajuda a converter APIs em CLIs otimizados.
