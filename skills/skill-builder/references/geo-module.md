# GEO Module — Otimizacao Avancada para Descoberta por Agentes

Consulte este arquivo no **Step 4** apos escrever a description inicial. O description-guide.md cobre keyword bombing basico; este modulo vai alem.

---

## O Conceito: Agentes sao os Clientes

"The agents are the customers for skills" (Omer, criador da skill mais baixada do skills.sh). Nao otimize pra humanos lerem — otimize pra agentes encontrarem.

## Processo GEO em 3 Etapas

### Etapa 1: Gerar Keywords via Claude

Peca ao proprio Claude Code:

```
"Se voce fosse buscar uma skill que [descricao do que a skill faz],
quais termos voce usaria? Liste 20+ termos incluindo:
- Verbos de acao (criar, analisar, revisar...)
- Substantivos de dominio (componente, schema, API...)
- Frases naturais que um dev digitaria
- Sinonimos em PT-BR e EN
- Erros comuns de digitacao que levariam ao mesmo intent"
```

O agente gera keywords melhores que o humano porque ELE e o cliente da skill.

### Etapa 2: Analisar Find Skills (Opcional mas Recomendado)

O Find Skills da Vercel e open source. O algoritmo de ranking considera:
- **Match de keywords** na description (peso mais alto)
- **Nome da skill** (peso alto)
- **Popularidade** (instalacoes)
- **Recencia** (ultima atualizacao)

Tecnica: clone o repo do Find Skills, analise o codigo de ranking, e otimize a description pra casar com os criterios.

### Etapa 3: Reescrever e Validar

Com as keywords geradas, reescreva a description seguindo o formato:
1. **Primeira frase:** Core capability (o que faz)
2. **Bloco de triggers:** "Use when/SEMPRE que:" + lista de frases naturais
3. **Bloco de diferenciacao:** "Nao use pra X, use Y" (evita acionamento falso)

**Checklist de validacao:**
- [ ] 5+ verbos de acao
- [ ] 5+ substantivos de dominio
- [ ] Pelo menos 3 frases naturais PT-BR
- [ ] Pelo menos 3 frases naturais EN
- [ ] Under 1024 caracteres
- [ ] Diferenciacao clara com skills similares
- [ ] Core capability na primeira frase

## Anti-Patterns GEO

- **Marketing speak:** "A powerful tool for..." — agentes nao se impressionam com adjetivos
- **Descricao vaga:** "Helps with development" — nao tem keywords buscaveis
- **So EN:** Perder triggers PT-BR que sao o contexto primario do usuario
- **So acao, sem objeto:** "Criar, melhorar, analisar" o que? Falta o substantivo
- **Copy-paste de outro skill:** Cada skill tem keywords unicas. Nao reutilize cegamente

## Exemplo: Antes e Depois

**Antes (generico):**
```yaml
description: "A skill for building other Claude Code skills."
```

**Depois (GEO-otimizado):**
```yaml
description: "Create, improve, and optimize Claude Code skills with battle-tested techniques. Expert guidance on skill architecture, progressive loading, workflow design, description optimization (GEO), and packaging. Use when user wants to: create skill, build skill, new skill, improve skill, refactor skill, debug skill, package skill, evolve skill, write SKILL.md, 'transforma isso numa skill', 'quero automatizar esse processo'..."
```
