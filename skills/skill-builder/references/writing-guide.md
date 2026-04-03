# Writing Guide — Princípios e Técnicas para Escrever Skills

Consulte este arquivo no **Step 2** (pesquisa) e **Step 5** (escrita) do workflow.

---

## Table of Contents

1. Context Engineering — o conceito central
2. Hierarquia de eficácia (Anthropic)
3. Técnica: Iron Law
4. Técnica: Question-Style Instructions
5. Técnica: Anti-Pattern Documentation
6. Regras de escrita para skills
7. Progressive Loading — 3 níveis
8. Pesquisa de domínio
9. Armadilhas comuns

---

## 1. Context Engineering

Skill não é prompt. Skill é **curadoria de contexto**: decidir o que o modelo precisa ver, quando, e em qual formato.

**Princípio do orçamento de atenção:** cada token na skill compete com todos os outros tokens no contexto. Informação irrelevante DILUI a atenção disponível.

Implicações:
- Corte frases que não adicionam informação nova
- Se pode ser inferido do contexto, não escreva
- 3 linhas precisas > 10 linhas vagas
- Informação importante no início de cada seção (primacy bias)

## 2. Hierarquia de Eficácia (Anthropic)

Técnicas ordenadas por impacto — respeite a ordem:

**Nível 1 — Clareza e direção (maior impacto)**
Instruções claras, específicas, sem ambiguidade. Teste do colega: se um colega inteligente não entenderia na primeira leitura, reescreva.

**Nível 2 — Exemplos (few-shot)**
Um exemplo de input → output vale mais que 10 linhas de explicação. Mínimo 2 exemplos por formato de output importante.

**Nível 3 — Chain of thought**
Pra tarefas de análise/decisão, descreva OS passos. "Antes de recomendar: 1) Qual o problema real? 2) Quais opções? 3) Tradeoffs?" — não "pense cuidadosamente".

**Nível 4 — Estrutura**
Organize em blocos claros: headers Markdown ou XML tags. Claude responde bem a ambos.

**Nível 5 — Papel/persona**
Atribuir papel ajuda, mas MENOS que clareza e exemplos. Não comece por aqui.

## 3. Técnica: Iron Law

Uma regra inquebrável no topo do SKILL.md, após frontmatter. Previne o atalho mais provável do modelo.

**Como escrever:** Pergunte: "Qual o ÚNICO erro que o modelo mais provavelmente vai cometer?" Escreva uma regra que previna.

Exemplos:
- Debugging: `IRON LAW: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.`
- TDD: `IRON LAW: NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.`
- Skill Builder: `IRON LAW: NEVER generate a skill without reading 2+ existing skills first.`

**Red Flags (mecanismo de rollback):**
Paire a Iron Law com sinais de que o modelo está desviando:
```
Red Flags (volte ao Step 1 se qualquer um aparecer):
- "Acho que o problema pode ser..." (chutando, não analisando)
- Fazendo mudanças sem entender a causa raiz
- Fix funciona mas você não consegue explicar por quê
```

## 4. Técnica: Question-Style Instructions

Dê perguntas específicas, não diretivas vagas. Modelos são excelentes em "responder perguntas específicas" mas sofrem com instruções abstratas.

```markdown
# Ruim — diretiva vaga
Verifique se o código viola SRP.

# Bom — pergunta específica
Pergunte: Quantas razões distintas esse módulo teria pra mudar?
Se mais de uma, provavelmente viola SRP.
```

```markdown
# Ruim
Cuidado com race conditions.

# Bom
Pergunte: O que acontece se dois requests chegam nesse código simultaneamente?
```

**Padrão:** Transforme diretiva → pergunta que um sênior faria → inclua o que a resposta implica.

## 5. Técnica: Anti-Pattern Documentation

Liste explicitamente o que o modelo NÃO deve fazer. Modelos têm "defaults de treinamento" — se não proibir, vão usar.

**Como encontrar:** Pergunte: "Qual seria o default preguiçoso do Claude pra essa tarefa?"

Exemplos:
- Frontend: "Não use gradientes purple/blue como default, não use Inter pra tudo"
- Code: "Não adicione try-catch com console.log desnecessário"
- Copy: "Evite CTAs genéricos: Submit, Sign Up, Learn More"

Coloque anti-patterns no SKILL.md perto do step relevante, ou em referência separada pra listas longas.

## 6. Regras de Escrita

### Imperativo, não sugestivo
- ✅ "Pergunte o contexto técnico antes de sugerir solução"
- ❌ "Seria bom se você perguntasse sobre o contexto técnico"

### Explique o porquê
- ✅ "Sempre inclua seção 'Fora do escopo' — sem ela, o LLM pode inventar features que não foram pedidas"
- ❌ "Sempre inclua seção 'Fora do escopo'"

### Específico com escape
- ✅ "Use shadcn/ui pra componentes. Se o projeto já usa outra lib, mantenha a existente."
- ❌ "Use uma biblioteca de componentes moderna"

### Evite caps lock como muleta
Se precisa gritar (SEMPRE, NUNCA), é sinal de que não explicou o porquê. Reserve caps pra restrições de segurança reais, não preferências.

### Não repita o sistema
Claude já sabe: ser educado, pensar antes de responder, admitir quando não sabe. Gaste tokens em conhecimento NOVO.

### Seções opcionais, nunca vazias
Se uma seção não se aplica, REMOVA. `[placeholder]` é pior que nada — o modelo inventa conteúdo pra preencher.

### Calibre pra Claude 4.x
Opus 4.5+/4.6 são mais responsivos — instruções que forçavam triggering em modelos antigos agora causam overtriggering. Instruição clara e direta > caps lock.

## 7. Progressive Loading — 3 Níveis

### Nível 1: Description (~100 palavras)
- Sempre no contexto. Único mecanismo de triggering.
- Deve ser pushy — melhor acionar demais que nunca acionar.

### Nível 2: SKILL.md body (<250 linhas)
- Carregado quando a skill aciona.
- Contém o workflow completo.
- Se passar de 250 linhas, mova pra references/.

### Nível 3: References (sem limite)
- Carregados sob demanda com ponteiro claro: "Consulte `references/X.md` quando [situação]"
- Arquivos >100 linhas precisam de table of contents.

**Quando mover pro nível 3:**
- Detalhes técnicos de sub-domínio
- Templates extensos
- Checklists detalhados
- Exemplos longos
- Referências bibliográficas

## 8. Pesquisa de Domínio

### Quando pesquisar
Sempre que o domínio tenha corpo de conhecimento (UX → Nielsen, Segurança → OWASP, Vendas → SPIN Selling).

### Quando NÃO pesquisar
Skills operacionais (converte CSV), integração técnica (doc oficial é a fonte), formatação/template trivial.

### Como pesquisar (camadas)
1. **Obras seminais:** "[domínio] best books framework seminal"
2. **Frameworks práticos:** "[domínio] methodology practical steps"
3. **Pessoas-chave:** "[domínio] expert thought leader"
4. **Evolução recente:** "[domínio] 2025 2026 latest"

### O que fazer com as referências
- Incorpore frameworks como INSTRUÇÕES, não como citações
- Se a referência é rica, crie arquivo em `references/` com resumo curado
- "Aplique as 10 heurísticas de Nielsen" vira um checklist executável, não uma menção ao Nielsen

## 9. Armadilhas Comuns

1. **Skill que tenta fazer tudo** → Quebre em 2+ skills com escopos claros
2. **Instruções contraditórias** → Se seção A diz "seja breve" e seção B diz "detalhe tudo", modelo fica confuso
3. **Excesso de MUST/NEVER** → Cada restrição forte reduz flexibilidade. Poucas e justificadas.
4. **Sem exemplos** → Modelo inventa o formato. Sempre dê exemplos de output.
5. **Description fraca** → Skill excelente que nunca aciona é skill inútil.
6. **Copy-paste de docs** → Não copie doc inteira. Extraia princípios e transforme em instruções.
7. **Repetir o que Claude já sabe** → Não ensine a pesquisar ou ser educado. Ensine o domínio.

---

## Fontes

- Anthropic Prompt Engineering Guide — hierarquia de 5 níveis
- Anthropic Context Engineering for AI Agents — curadoria de contexto
- Skill Forge (sanyuan0704) — 12 técnicas battle-tested
- Martin Fowler / Thoughtworks "Context Engineering for Coding Agents"
- Paper "Agentic Context Engineering" (ACE)
