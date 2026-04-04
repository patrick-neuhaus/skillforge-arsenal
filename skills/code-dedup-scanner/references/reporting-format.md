# Reporting Format — Como Apresentar Resultados

Consulte este arquivo no **Step 3** para formatar o report.

---

## Template de Report Completo (--report)

```markdown
# Code Dedup Report — [Projeto]
**Data:** [YYYY-MM-DD]
**Escopo:** [diretorio/modulo escaneado]

## Resumo
- **Arquivos escaneados:** [N]
- **Matches encontrados:** [N]
- **Recomendacao:** [N] reuse, [N] extend, [N] create

## Matches

### 1. [Nome do match] — [REUSE ✅ / EXTEND 🔄 / EXTRACT 🔀]

**Location:** [path:line]
**What it does:** [descricao breve]
**Current usage:** [onde e importado, quantas vezes]
**Similarity to need:** [alta/media/baixa + justificativa]

**Recommendation:**
[Acao especifica: "Importe de X" ou "Adicione prop Y ao componente existente"]

---

### N+1. [Nome] — CREATE 🆕

**What:** [o que precisa ser criado]
**Suggested path:** [path sugerido seguindo convencoes do projeto]
**Rationale:** [nenhum match encontrado — justificar]
**Dependencies:** [libs necessarias, se alguma]

## Acoes Sugeridas
1. [ ] [Acao 1]
2. [ ] [Acao 2]
3. [ ] [Acao 3]
```

## Template de Report Rapido (--check)

```markdown
## Dedup Check: [descricao do que vai criar]

| Match | Location | Action | Similarity |
|-------|----------|--------|:----------:|
| ButtonVariant | components/ui/Button.tsx | EXTEND 🔄 | Alta |
| useFormSubmit | hooks/useFormSubmit.ts | REUSE ✅ | Media |
| — | — | CREATE 🆕 | — |

**Recommendation:** Extend Button with new variant, reuse useFormSubmit, create InvoiceForm.
```

## Regras de Apresentacao

1. **Matches primeiro, creates depois** — o usuario quer saber o que ja existe antes do que precisa criar
2. **Um match por bloco** — nao misturar multiplos matches num paragrafo
3. **Evidencia obrigatoria** — todo match tem path, line number, e usage context
4. **Acao especifica** — "Reuse" nao basta. "Importe Button de components/ui/ e adicione variant='danger'" sim
5. **Sem false positives** — se nao tem certeza, nao reporte. Melhor perder 1 match que gerar 3 falsos

## Criterios de Match

| Tipo | Criterio | Exemplo |
|------|----------|---------|
| **Exato** | Mesmo nome + mesma funcionalidade | `formatDate()` em utils/ = o que voce quer |
| **Parcial** | Funcionalidade similar com gap | `DataTable` existe mas sem sort |
| **Conceitual** | Padrao similar em dominio diferente | `UserCard` → poderia virar `EntityCard<T>` |
| **Dependencia** | Lib instalada resolve | `date-fns` ja instalado, nao precisa criar formatDate |

Apenas report **Exato** e **Parcial** como matches concretos.
**Conceitual** mencionar como sugestao de generalizacao.
**Dependencia** sempre checar (o usuario pode nao saber que a lib esta instalada).
