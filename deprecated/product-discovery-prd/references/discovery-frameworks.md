# Discovery Frameworks — Referência Rápida

Consulte este arquivo quando precisar de detalhes sobre frameworks mencionados no SKILL.md.

---

## Assumption Mapping (David Bland — Testing Business Ideas)

### Quando usar
- Antes de investir tempo/dinheiro em construir algo
- Quando o projeto tem suposições críticas não validadas
- Quando o usuário diz "meu cliente quer X" sem evidência concreta

### Matriz 2×2

```
                    POUCA EVIDÊNCIA          MUITA EVIDÊNCIA
ALTA IMPORTÂNCIA    🔴 LEAP OF FAITH        ✅ VALIDADO
                    (testar ANTES)           (pode construir)

BAIXA IMPORTÂNCIA   ⚪ IGNORAR               ✅ OK
                    (não vale o esforço)     (baixo risco)
```

### 3 tipos de suposição

1. **Desirability** — "Eles querem isso?"
   - Evidência forte: entrevistas, comportamento observado, dados de uso
   - Evidência fraca: "meu cliente disse que quer" (Mom Test fail)

2. **Feasibility** — "Conseguimos fazer?"
   - Evidência forte: POC testada, benchmark medido
   - Evidência fraca: "acho que dá" sem ter testado

3. **Viability** — "O negócio se sustenta?"
   - Evidência forte: modelo de receita validado, pricing testado
   - Evidência fraca: "vamos monetizar depois"

### Template prático

| Suposição | Tipo | Importância | Evidência | Ação |
|-----------|------|-------------|-----------|------|
| OCR extrai campos SST com >90% precisão | Feasibility | Alta | Fraca | POC antes de construir |
| Equipe adota sistema no dia a dia | Desirability | Alta | Fraca | Entrevista + protótipo |
| Volume justifica investimento | Viability | Média | Alguma | Calcular ROI com dados reais |

---

## Impact Mapping (Gojko Adzic)

### Quando usar
- Projetos com múltiplos stakeholders
- Quando precisa conectar features a resultados de negócio
- Quando o escopo está crescendo sem critério

### Estrutura

```
GOAL (objetivo de negócio mensurável)
├── ACTOR 1 (quem influencia o goal)
│   ├── IMPACT (mudança de comportamento esperada)
│   │   ├── DELIVERABLE (feature/entrega)
│   │   └── DELIVERABLE
│   └── IMPACT
│       └── DELIVERABLE
└── ACTOR 2
    └── IMPACT
        └── DELIVERABLE
```

### Exemplo

```
Reduzir tempo de conferência SST de 5h → 30min/semana
├── Técnico de segurança (usuário direto)
│   ├── Parar de abrir PDFs manualmente
│   │   ├── Upload em lote de documentos
│   │   └── OCR automático com extração de campos
│   └── Validar dados sem planilha
│       └── Dashboard de status por documento
└── Gerente (stakeholder)
    └── Ter visibilidade sem pedir relatório
        └── Relatório automático semanal
```

### Relação com OST (Teresa Torres)

- Impact Mapping: "Que mudança de comportamento gera valor?" (top-down, do negócio pro user)
- OST: "Que dor do cliente cria essa oportunidade?" (bottom-up, do user pro negócio)
- Juntas: cadeia completa de discovery → delivery

---

## Lean UX Canvas (Jeff Gothelf)

### Quando usar
- Quando precisa alinhar OKRs com JTBD
- Times cross-funcionais que precisam de framework compartilhado
- Quando o projeto precisa de métricas claras desde o início

### Boxes do Canvas

| Box | Conteúdo | Exemplo |
|-----|----------|---------|
| 1 | Business Problem (Objective) | "Tempo excessivo gasto em conferência manual de documentos SST" |
| 2 | Success Metrics (Key Results) | "Reduzir tempo de 5h → 30min/semana com <5% erro" |
| 3 | Assumptions | "OCR funciona pra documentos SST, equipe adota" |
| 4 | JTBD + Métricas de comportamento | "Quando recebo documentos SST, quero validá-los automaticamente para não errar e não perder tempo" |

### OKR resultante

O = Box 1 (Business Problem)
KRs = Box 2 (Success Metrics)

---

## Pre-mortem

### Quando usar
- Antes de iniciar qualquer projeto não-trivial
- Quando a equipe parece otimista demais
- Quando ninguém menciona riscos

### Script

1. "Imagina que passaram 3 meses e esse projeto fracassou completamente."
2. "O que deu errado? Liste TUDO que pode ter causado o fracasso."
3. Categorize:
   - 🔴 **Project killers** — impedem o lançamento
   - 🟡 **Known-but-unsaid** — todo mundo sente mas ninguém fala
   - 🟠 **Execution risks** — "será que conseguimos?"
4. Pra cada risco: mitigação possível ou sinal de alerta a monitorar

### Regra

Se o pre-mortem revelar um project killer sem mitigação, isso precisa ser resolvido ANTES de continuar o discovery. Não adianta fazer PRD bonito se o fundamento é frágil.

---

## North Star Metric

### Quando usar
- Todo projeto que vai pra produção (não é exercício acadêmico)
- Quando precisa de uma métrica única pra alinhar time e stakeholders

### 3 categorias

| Tipo | Quando usar | Exemplos |
|------|-------------|----------|
| Atenção (engagement) | Produtos de uso recorrente | DAU, sessões/dia, tempo de uso |
| Transação (revenue) | Produtos de venda/conversão | Pedidos/dia, GMV, conversão |
| Produtividade (output) | Ferramentas de trabalho | Docs processados, tarefas completadas |

### Regras

- Deve ser uma taxa ou ratio, não contagem absoluta
- Deve representar VALOR pro usuário, não só métrica de negócio
- Deve ser influenciável pelo time (não "receita total da empresa")
- Uma por projeto. Se tem duas, escolha a mais importante.

---

## Shape Up — Appetite (Ryan Singer, Basecamp)

### Conceito

O appetite define QUANTO tempo/esforço gastar. O escopo se adapta ao appetite, NÃO o contrário.

### Tamanhos

| Appetite | Duração | Quando usar |
|----------|---------|-------------|
| Small batch | 1-2 semanas | Feature isolada, bug fix significativo |
| Big batch | 6 semanas | Projeto novo, refatoração grande |
| Micro | 1-3 dias | Prova de conceito, spike técnico |

### Implicação pro PRD

Se o appetite é 1 semana, o MVP precisa ser BRUTALMENTE cortado. Se é 6 semanas, pode ser mais completo. Perguntar appetite ANTES de definir escopo evita o clássico "projeto infinito que nunca lança".
