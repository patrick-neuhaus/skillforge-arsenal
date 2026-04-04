# Audit Templates — Formatos de Output

Templates pra cada modo de audit. Copie a estrutura e preencha.

---

## Template: Audit Completo

```markdown
## Resumo Executivo

**Produto:** [nome]
**Plataforma:** [web desktop / mobile / responsivo / nativo]
**Usuario-alvo:** [persona resumida]
**Data:** [data]

**Heuristicas com falha:** [H1, H3, H5...]
**WCAG 2.2 violacoes:** [criterios violados]
**Dark patterns encontrados:** [sim/nao — quais]

**Findings totais:** [N]
- Severidade 4 (catastrofico): [N]
- Severidade 3 (maior): [N]
- Severidade 2 (menor): [N]
- Severidade 1 (cosmetico): [N]

---

## Analise de Fluxos

### Fluxo: [nome do fluxo]
**Passos:** [passo 1] → [passo 2] → [passo 3] → ...
**Veredicto:** ✅ Fluido | ⚠️ Tem friccao | ❌ Quebrado
**Observacao:** [2-3 linhas sobre o que funciona e o que nao funciona]

[repetir pra cada fluxo]

---

## Findings Priorizados

### Severidade 4 — Corrigir imediatamente
| # | Problema | Principio violado | Evidencia | Recomendacao |
|---|---------|-------------------|-----------|--------------|
| 1 | [desc] | [heuristica/law/WCAG] | [elemento especifico] | [acao concreta] |

### Severidade 3 — Corrigir antes do proximo release
| # | Problema | Principio violado | Evidencia | Recomendacao |
|---|---------|-------------------|-----------|--------------|

### Severidade 2 — Prioridade baixa
| # | Problema | Principio violado | Evidencia | Recomendacao |
|---|---------|-------------------|-----------|--------------|

### Severidade 1 — Cosmetico
| # | Problema | Principio violado | Evidencia | Recomendacao |
|---|---------|-------------------|-----------|--------------|

---

## Acessibilidade (WCAG 2.2)

**Conformidade geral:** [boa / parcial / baixa]

| Criterio | Nivel | Status | Detalhe |
|----------|-------|--------|---------|
| [numero] [nome] | [A/AA] | ✅/❌ | [evidencia] |

---

## O que esta funcionando bem

- [Acerto 1 — por que funciona]
- [Acerto 2 — por que funciona]
- [Acerto 3 — por que funciona]

---

## Oportunidade criativa

[Uma ideia fora do obvio que transformaria a experiencia — nao obrigatorio, mas se existir, vale registrar]
```

---

## Template: Audit Focado

Formato compacto pra tela ou fluxo especifico.

```markdown
## Audit Focado: [nome da tela/fluxo]

**Objetivo da tela:** [o que o usuario vem fazer aqui]
**Contexto:** [plataforma, usuario-alvo]

### Fluxo analisado
[passo 1] → [passo 2] → [passo 3] → ...
**Veredicto:** ✅ | ⚠️ | ❌

### Findings

| # | Problema | Principio | Severidade | Recomendacao |
|---|---------|-----------|------------|--------------|
| 1 | [desc] | [heuristica/law/WCAG] | [0-4] | [acao] |
| 2 | [desc] | [heuristica/law/WCAG] | [0-4] | [acao] |

### O que funciona bem
- [acerto]

### Proximos passos sugeridos
- [acao 1]
- [acao 2]
```

---

## Template: Cognitive Walkthrough

Metodo focado em learnability pra novos usuarios. Baseado em Wharton, Rieman, Lewis, Polson (1994).

### Quando usar
- Apps walk-up-and-use (kiosks, onboarding, ferramentas publicas)
- Avaliacao de learnability pra usuarios de primeiro uso
- Quando o publico-alvo e nao-tecnico

### Metodo

1. **Defina o perfil do usuario** (experiencia, motivacao, contexto)
2. **Defina as tarefas** (3-5 tarefas mais importantes)
3. **Pra cada passo de cada tarefa, pergunte as 4 perguntas:**
   - O usuario vai TENTAR fazer a acao correta? (sabe o que quer fazer?)
   - O usuario vai NOTAR que a acao correta esta disponivel? (e visivel?)
   - O usuario vai ASSOCIAR a acao com o efeito desejado? (o label faz sentido?)
   - Apos executar, o usuario vai PERCEBER que progrediu? (tem feedback?)
4. **Documente falhas** como findings com severidade

### Template

```markdown
## Cognitive Walkthrough: [nome do app/feature]

**Perfil do usuario:** [experiencia, motivacao, contexto]
**Data:** [data]

### Tarefa: [nome da tarefa]

| Passo | Acao esperada | Tentativa? | Visivel? | Associacao? | Feedback? | Problema |
|-------|---------------|------------|----------|-------------|-----------|----------|
| 1 | [acao] | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | [se houver] |
| 2 | [acao] | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | [se houver] |

**Veredicto:** [completavel sem ajuda? / precisa de guia? / bloqueado?]
**Findings:** [lista de problemas com severidade]

[repetir pra cada tarefa]

### Resumo de learnability
- **Tarefas completaveis sem ajuda:** [N de M]
- **Problemas de visibilidade:** [N]
- **Problemas de associacao (label confuso):** [N]
- **Problemas de feedback:** [N]
```

---

## Template: Varredura Heuristica (por heuristica)

Formato detalhado pra documentar cada heuristica no audit completo.

```markdown
### H[N]: [Nome da heuristica]
**Veredicto:** ✅ Passa | ⚠️ Parcial | ❌ Viola

**Evidencias:**
- [Elemento X] faz/nao faz [comportamento] — Severidade: [0-4]
- [Elemento Y] faz/nao faz [comportamento] — Severidade: [0-4]

**Recomendacao:** [Acao concreta]
```

---

## Geracao de tarefas (se solicitado)

Se o usuario pedir, transforme findings em tarefas pro ClickUp:
- 1 tarefa por finding
- Titulo: `[Sev-N] [Area] - Descricao curta`
- Descricao: Problema → Principio violado → Recomendacao
- Tag de severidade pra priorizacao
