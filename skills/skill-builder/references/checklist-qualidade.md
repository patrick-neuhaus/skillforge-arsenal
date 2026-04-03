# Checklist de Qualidade — Validação de Skills

Última atualização: 2026-03-26

Consulte este arquivo na **Fase 5 (Validação)** do fluxo de criação de skill. Passe por TODOS os itens antes de considerar a skill pronta.

---

## A. Estrutura e metadata

- [ ] **Frontmatter completo** — tem `name` e `description` no YAML?
- [ ] **Name consistente** — name no frontmatter = nome da pasta da skill?
- [ ] **Description pushy** — cobre triggers explícitos ("quando o usuário mencionar X") E implícitos ("também use quando...")?
- [ ] **Description com near-misses** — inclui instrução de quando NÃO acionar? ("Se for Y, use a skill Z em vez desta")
- [ ] **SKILL.md < 500 linhas** — se passou, moveu conteúdo pra references/?

## B. Seções essenciais

- [ ] **Visão geral** — explica o que faz, pra que serve, em 2-3 parágrafos?
- [ ] **Princípios** — tem pelo menos 3 princípios com explicação do porquê?
- [ ] **Fluxo de trabalho** — processo passo a passo claro?
- [ ] **Regras do output** — formato, linguagem, tom, restrições definidos?
- [ ] **Quando NÃO usar** — lista clara de situações que NÃO são pra esta skill?
- [ ] **Integração** — menciona skills complementares e como combinar?

## C. Qualidade das instruções

- [ ] **Imperativo** — instruções usam forma imperativa ("Faça", "Pergunte"), não sugestiva ("Seria bom se")?
- [ ] **Porquês** — cada regra importante tem explicação do motivo?
- [ ] **Exemplos** — tem pelo menos 2 exemplos concretos de input/output?
- [ ] **Edge cases** — trata pelo menos 2-3 situações atípicas?
- [ ] **Sem redundância** — não repete comportamento base do Claude (ser educado, admitir erros, etc)?
- [ ] **Tom consistente** — linguagem e nível de formalidade uniformes em toda a skill?
- [ ] **PT-BR** — toda a skill em português brasileiro, exceto termos técnicos universais?

## D. Context engineering

- [ ] **Progressive disclosure** — conteúdo organizado nos 3 níveis (metadata → body → references)?
- [ ] **Ponteiros claros** — cada reference file tem instrução no SKILL.md de QUANDO ler?
- [ ] **Sem lixo** — não tem informação irrelevante competindo por atenção do modelo?
- [ ] **Ordem importa** — informações mais importantes primeiro em cada seção?
- [ ] **Seções auto-contidas** — cada fase/seção funciona mesmo se o modelo perdeu contexto anterior?
- [ ] **Referências grandes** — arquivos >300 linhas têm table of contents?

## E. Fundamentação

- [ ] **Domínio pesquisado** — se o domínio tem corpo de conhecimento, foi pesquisado antes de escrever?
- [ ] **Referências incorporadas** — frameworks e princípios do domínio viraram instruções (não só citações)?
- [ ] **Fontes documentadas** — tem seção ou nota indicando quais referências foram usadas?
- [ ] **Referências salvas** — se pesquisou, salvou em references/ pra uso futuro?

## F. Testes e validação

- [ ] **Testou** — rodou pelo menos 2-3 cenários reais?
- [ ] **Cenários variados** — testes cobrem caminho feliz + edge case + input vago?
- [ ] **Feedback aplicado** — feedback do usuário foi incorporado na skill?
- [ ] **Output consistente** — múltiplas rodadas do mesmo input geram output de qualidade similar?

## G. Anti-patterns (red flags)

Se qualquer um desses aparecer, a skill precisa de revisão:

- [ ] **Sem MUST/NEVER excessivo** — tem mais de 5 restrições em caps lock? Reescreva explicando o porquê.
- [ ] **Sem copy-paste** — copiou documentação externa inteira pra dentro? Extraia princípios.
- [ ] **Sem contradições** — seções diferentes dão instruções conflitantes?
- [ ] **Sem placeholder** — tem [insira aqui] ou [TODO] no output? Remova ou preencha.
- [ ] **Sem scope creep** — a skill tenta fazer mais do que deveria? Quebre em skills menores.
- [ ] **Sem instruções mortas** — tem instruções que nunca seriam acionadas no uso real?

---

## Escala de prioridade pra correções

Se encontrou vários problemas, corrija nessa ordem:

1. **Description** — se não aciona, nada mais importa
2. **Fluxo de trabalho** — se o processo tá confuso, output vai ser ruim
3. **Exemplos** — se não tem exemplos, modelo inventa formato
4. **Princípios e porquês** — se não tem fundamentação, instruções viram arbitrárias
5. **Edge cases** — se não trata exceções, falha nos 20% de casos atípicos
6. **Polish** — tom, formatação, organização

---

## Template de relatório de validação

Use esse formato pra apresentar o resultado da validação pro usuário:

```
## Validação da skill [nome] — v[X]

### Status: [APROVADA / APROVADA COM RESSALVAS / REQUER REVISÃO]

### O que tá bom:
- [ponto forte 1]
- [ponto forte 2]

### O que precisa ajustar:
- [prioridade 1]: [descrição + sugestão de correção]
- [prioridade 2]: [descrição + sugestão de correção]

### Itens do checklist que falharam:
- [item]: [motivo]
```
