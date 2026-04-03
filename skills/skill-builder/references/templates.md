# Templates e Exemplos — Referência pra Escrita de Skills

Última atualização: 2026-03-26

Consulte este arquivo quando precisar de **modelos concretos** durante a Fase 3 (Escrita). Contém templates pra diferentes tipos de skill e exemplos reais de padrões que funcionam.

---

## Templates por tipo de skill

### Tipo 1: Skill de processo (mais comum)

Skills que guiam o modelo por um processo em fases. Ex: PRD, UX Audit, Discovery.

```markdown
---
name: nome-da-skill
description: "[descrição pushy com triggers]"
---

# Nome da Skill

## Visão geral
[O que faz + problema que resolve + quando usar]

## Princípios
1. **[Princípio]** — [Porquê]
2. **[Princípio]** — [Porquê]
3. **[Princípio]** — [Porquê]

## Fluxo de trabalho

### Fase 1: [Coleta/Entendimento]
[Perguntas organizadas em blocos de 2-3]

**Bloco 1 — [Tema]:**
- [Pergunta]
- [Pergunta]

**Bloco 2 — [Tema]:**
- [Pergunta]
- [Pergunta]

### Fase 2: [Análise/Estruturação]
[O que fazer com o que coletou]

### Fase 3: [Geração do output]
[Template do output + regras]

### Fase 4: [Validação]
[Checklist + apresentação pro usuário]

## Regras do output
[Formato, linguagem, restrições]

## Exemplo de interação
**Usuário:** "[input típico]"
**Skill:** "[resposta ideal]"

## Integração com outras skills
[Quais skills complementam]

## Quando NÃO usar
[Situações em que outra skill é mais apropriada]
```

### Tipo 2: Skill técnica (geração de artefato)

Skills que geram um arquivo ou artefato específico. Ex: XLSX generator, PPTX.

```markdown
---
name: nome-da-skill
description: "[triggers focados no tipo de artefato]"
---

# Nome da Skill

## Visão geral
[O que gera + formatos suportados]

## Requisitos
- [Dependência 1]
- [Dependência 2]

## Processo

### 1. Identificar o que o usuário precisa
[Perguntas rápidas — skills técnicas precisam de menos discovery]

### 2. Gerar o artefato
[Passo a passo técnico]
[Script a executar, se houver]

### 3. Validar e entregar
[Verificações de qualidade]
[Como apresentar o output]

## Templates de output
[Template 1 — quando usar]
[Template 2 — quando usar]

## Erros comuns e como evitar
[Lista de problemas frequentes com solução]
```

### Tipo 3: Skill de análise/auditoria

Skills que analisam algo existente e geram diagnóstico. Ex: Repo Review, UX Audit.

```markdown
---
name: nome-da-skill
description: "[triggers focados em análise/revisão]"
---

# Nome da Skill

## Visão geral
[O que analisa + que tipo de diagnóstico gera]

## Framework de análise
[O framework/metodologia usada — ex: Heurísticas de Nielsen, OWASP]

### Dimensão 1: [Nome]
- [O que avaliar]
- [Critérios de qualidade]
- [Escala de severidade]

### Dimensão 2: [Nome]
...

## Processo

### 1. Coletar o input
[O que precisa receber: screenshots, código, URL, etc]

### 2. Analisar
[Ordem de análise — o que olhar primeiro]
[Como classificar os achados]

### 3. Gerar relatório
[Template do relatório com escala de severidade]

## Escala de severidade
[Definição clara de cada nível — ex: Cosmético, Menor, Maior, Crítico]

## Exemplo de achado
**Achado:** [descrição]
**Severidade:** [nível]
**Evidência:** [o que comprova]
**Recomendação:** [como corrigir]
```

---

## Padrões de description que funcionam

### Padrão básico (funciona pra maioria)
```
"Skill para [O QUE FAZ]. Use esta skill SEMPRE que o usuário mencionar: 
[lista de 5-8 triggers]. Também use quando [2-3 triggers implícitos]. 
Se [situação ambígua], USE esta skill."
```

### Padrão com diferenciação (quando há overlap com outra skill)
```
"Skill para [O QUE FAZ]. Use esta skill SEMPRE que [triggers]. 
Se houver dúvida entre esta skill e [skill X], pergunte: 
'[pergunta que diferencia]'"
```

### Padrão com threshold (quando a skill só deve acionar em certos contextos)
```
"Skill para [O QUE FAZ]. Use SEMPRE que [triggers]. 
NÃO use pra [situações triviais que não precisam de skill]. 
Se o pedido é simples e pode ser resolvido em <5 linhas, 
responda direto sem acionar a skill."
```

---

## Exemplos de bons princípios (extraídos de skills reais)

### Com porquê claro:
> **Extrair, não inventar.** O objetivo é tirar da cabeça do usuário o que ele já sabe. Não assume nada. Pergunta. Porque skill que assume gera output baseado em achismo, não em dados.

### Com regra prática:
> **MVP primeiro, sempre.** Cortar escopo é mais valioso do que adicionar. Se o usuário quer 10 features, a skill deve ajudar a identificar as 3 que importam. Porque LLMs tendem a expandir escopo, não cortar.

### Com anti-pattern:
> **Honestidade sobre limitações.** Se o conhecimento sobre um tema é superficial ou potencialmente desatualizado, USE WEB SEARCH. Não invente referências. Nunca cite um livro que você não tem certeza que existe. Porque uma referência inventada destrói a credibilidade do output inteiro.

---

## Exemplo de bloco de perguntas bem estruturado

```markdown
**Bloco 1 — O problema (não a solução):**

IMPORTANTE: O usuário vai chegar falando da SOLUÇÃO ("quero um app que faz X"). 
Seu trabalho é voltar pro PROBLEMA. Faça isso com firmeza mas sem arrogância.

- O que você quer construir? (deixe ele falar livremente primeiro)
- Agora me conta: qual o problema que isso resolve? 
  O que acontece HOJE sem essa solução?
- Quem sofre com esse problema? Com que frequência?
- Por que agora? O que muda se não fizer?
```

**Por que funciona:**
- Começa com instrução META (o que fazer com as respostas)
- Perguntas vão do geral ao específico
- Cada pergunta tem propósito claro
- Há parentéticos que guiam o tom

---

## Padrão de integração entre skills

```markdown
## Integração com outras skills

Esta skill pode ser acionada POR DENTRO de outras skills:

- **[Skill X]:** "[situação em que faz sentido combinar]"
- **[Skill Y]:** "[situação]"

Quando acionada por outra skill, seja breve — traga o essencial inline, 
não faça o processo completo de todas as fases.
```

---

## Anti-padrões de output (o que NÃO fazer)

### ❌ Template com placeholders genéricos
```
## Seção 1
[Insira conteúdo aqui]

## Seção 2
[TODO: completar]
```
**Problema:** O modelo tende a gerar texto pra preencher placeholders, mesmo quando a seção não se aplica.

### ❌ Regras contraditórias
```
Seja breve e direto.
...
Detalhe cada ponto com exemplos extensos e explicações completas.
```
**Problema:** O modelo oscila entre os dois e não é consistente.

### ❌ Lista infinita de MUST/NEVER
```
DEVE SEMPRE fazer X
NUNCA faça Y
OBRIGATORIAMENTE faça Z
JAMAIS esqueça de W
```
**Problema:** Perde o impacto. Se tudo é obrigatório, nada é prioridade.

### ✅ Versão correta
```
Regras fundamentais (quebre qualquer outra regra antes destas):
1. [Regra 1] — [porquê]
2. [Regra 2] — [porquê]

Preferências (siga quando possível, mas use bom senso):
- [Preferência 1]
- [Preferência 2]
```
