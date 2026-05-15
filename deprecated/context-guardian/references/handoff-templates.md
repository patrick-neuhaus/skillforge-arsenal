# Handoff Templates — Templates por Cenario

Consulte este arquivo no **Step 3** quando for gerar um handoff document.

---

## Template 1: Handoff entre Fases do SDD

```markdown
# Handoff: SDD [Phase N → Phase N+1]
**Data:** [YYYY-MM-DD]
**Feature:** [nome da feature]

## Fase Completada: [nome da fase]
**Output gerado:** [prd.md / spec.md / codigo]
**Arquivo de referencia:** [path do output]

## Decisoes Tomadas
- [decisao 1]: [justificativa]
- [decisao 2]: [justificativa]

## Proxima Fase: [nome]
1. Ler [arquivo de output da fase anterior]
2. [passo seguinte especifico]
3. [passo seguinte especifico]

## Como Retomar
```
Estou implementando [feature]. Acabei a fase [N] do SDD.
O output esta em [path]. Leia e continue com a fase [N+1].
```
```

## Template 2: Handoff Mid-Implementation

```markdown
# Handoff: Implementacao em Andamento
**Data:** [YYYY-MM-DD]
**Feature/Task:** [nome]
**Spec:** [path do spec.md]

## Progresso
- [x] [item do spec ja implementado]
- [x] [item do spec ja implementado]
- [ ] [proximo item a implementar] ← RETOMAR AQUI
- [ ] [item pendente]
- [ ] [item pendente]

## Arquivos Modificados
| Arquivo | Status | O que foi feito |
|---------|:------:|----------------|
| src/components/X.tsx | Completo | Criado com props A, B, C |
| src/lib/queries/Y.ts | Parcial | Query de listagem OK, falta mutation |
| src/app/page.tsx | Pendente | Nao tocado ainda |

## Problemas Encontrados
- [problema 1]: [como foi resolvido ou se esta pendente]
- [problema 2]: [workaround usado]

## Como Retomar
```
Estou implementando [feature] seguindo o spec em [path].
Ja completei [N] de [M] items. O proximo e [descricao].
Leia o spec e continue de onde parei.
```
```

## Template 3: Handoff de Auditoria/Review

```markdown
# Handoff: Auditoria em Andamento
**Data:** [YYYY-MM-DD]
**Tipo:** [Trident / Security / Architecture / UX]
**Escopo:** [o que esta sendo auditado]

## Findings Ate Agora
| ID | Severity | Arquivo | Descricao | Status |
|----|:--------:|---------|-----------|:------:|
| F001 | P0 | src/X.tsx:42 | [descricao] | Confirmado |
| F002 | P1 | src/Y.ts:15 | [descricao] | Pendente |

## Areas Ainda Nao Escaneadas
- [ ] [area/modulo 1]
- [ ] [area/modulo 2]

## Como Retomar
```
Estou fazendo auditoria [tipo] no projeto. Ja encontrei [N] findings.
Falta escanear [areas]. Continue de onde parei.
```
```

## Template 4: Handoff Generico (qualquer tarefa)

```markdown
# Handoff: [Titulo da Tarefa]
**Data:** [YYYY-MM-DD]

## O que Estamos Fazendo
[1-2 frases descrevendo a tarefa]

## Estado Atual
- **Progresso:** [X]% completo
- **Ultimo passo concluido:** [descricao]
- **Proximo passo:** [descricao]

## Decisoes Tomadas (que nao estao nos arquivos)
- [decisao verbal do usuario que seria perdida no /clear]
- [trade-off discutido e conclusao]

## Arquivos Relevantes
- [path 1] — [o que e / o que foi feito]
- [path 2] — [o que e / o que foi feito]

## Contexto Critico
[Informacao que NAO esta em nenhum arquivo e seria perdida.
Ex: "O usuario disse que o campo X vai ser removido na proxima sprint,
entao nao gastar tempo otimizando ele"]

## Como Retomar
```
[Instrucao de 2-3 linhas para colar como primeiro prompt apos /clear]
```
```

## Regras para Bons Handoffs

1. **Referencie arquivos, nao copie conteudo** — o handoff deve ser curto
2. **Inclua decisoes verbais** — a unica coisa que se perde no /clear e o que nao esta em arquivo
3. **"Como Retomar" e obrigatorio** — o usuario precisa saber exatamente o que colar
4. **Nomeie o arquivo com data** — `handoff-2026-04-03-invoice-feature.md`
5. **Maximo 50 linhas** — handoff longo consome o contexto que voce esta tentando liberar

## Onde Salvar

| Cenario | Local |
|---------|-------|
| Projeto com SDD | Raiz do projeto (junto com prd.md, spec.md) |
| Skill development | Raiz do repo de skills |
| Generico | Working directory atual |

Nome: `handoff-[YYYY-MM-DD]-[descricao-curta].md`
