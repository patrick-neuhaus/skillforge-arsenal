# Find Skills Analysis — Como o Algoritmo Ranqueia

Consulte este arquivo no **Step 1** para entender como skills sao encontradas.

---

## Como o Find Skills Funciona

O Find Skills da Vercel e o principal mecanismo de descoberta do skills.sh. O codigo e open source no GitHub.

### Fatores de Ranking

| Fator | Peso | Como otimizar |
|-------|:----:|---------------|
| **Keyword match na description** | Alto | Keyword bombing — cobrir verbos, substantivos, frases naturais |
| **Nome da skill** | Alto | Nome descritivo e buscavel (kebab-case) |
| **Popularidade (installs)** | Medio | First-mover advantage — publicar cedo importa |
| **Recencia** | Baixo-Medio | Atualizar periodicamente mantem relevancia |
| **Tamanho/completude** | Baixo | Skills com references/ e scripts/ ranqueiam melhor |

### Anatomia de uma Busca por Agente

Quando o Claude Code recebe um pedido do usuario, ele:
1. Parseia o intent do usuario em keywords
2. Busca skills cujas descriptions casam com essas keywords
3. Ranqueia por relevancia (match de keywords + popularidade)
4. Carrega o SKILL.md da skill mais relevante

O ponto critico: **a description e a UNICA coisa que o agente le antes de decidir**. O body do SKILL.md carrega DEPOIS. Toda informacao de "quando usar" deve estar na description.

### Concorrencia e Diferenciacao

No skills.sh, skills com dominios similares competem pelo mesmo espaco de keywords:
- `ui-ux-pro-max` (222K installs) vs `frontend-design` (73K) vs `web-design-guidelines` (213K)
- Todas cobrem "design" e "UI" — o que diferencia e a **especificidade** e **completude** das keywords

Estrategia: nao tente competir em keywords genericas. Domine keywords especificas do seu nicho.

## Insights do Video 1 (Omer)

### O Agente como Cliente

"The agents are the customers for skills" — a mentalidade de otimizacao muda quando voce entende que:
- O "usuario" da description e um LLM, nao um humano
- LLMs processam tokens, nao scaneiam visualmente
- Keywords precisas > formatacao bonita
- Verbos de acao > adjetivos descritivos

### First-Mover Advantage

O skills.sh ainda e relativamente novo. Publicar skills de qualidade agora da vantagem desproporcional porque:
- Menos concorrencia por keywords
- Installs acumulam ao longo do tempo (compound effect)
- Skills populares aparecem em "trending" e "featured"

### CLI-First vs MCP

Skills CLI-first tem vantagem na descoberta porque:
- O agente pode explorar comandos via `--help` (autodiscovery)
- Cada comando e uma keyword potencial
- MCPs retornam JSON pesado que degrada o ranking de usabilidade

## Metricas de Referencia

| Metrica | Top Skills | Skills Medianas | Skills Ruins |
|---------|:---------:|:--------------:|:------------:|
| Installs | 50K+ | 1K-10K | <100 |
| Description length | 300-800 chars | 100-300 chars | <50 chars |
| Action verbs | 8+ | 3-5 | 0-2 |
| Domain nouns | 8+ | 3-5 | 0-2 |
| Natural phrases | 5+ | 1-3 | 0 |
| GEO Score (/15) | 12+ | 7-11 | <7 |
