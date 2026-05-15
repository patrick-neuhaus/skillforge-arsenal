<!--
  copy-review-site.md — Mode review-site standalone: review afiliado, comparison 3rd-party, best-of, buying guide
  Carregado em: tasks de copy pra review afiliado, comparison page de 3rd-party, best-of round-up, buying guide
  v3 — 2026-05-03 (NOVO ref Wave 3: mode 9 review-site standalone)
-->

# Copy — Review Site & Afiliado

**Referencias:** Pat Flynn (Smart Passive Income), Wirecutter, NerdWallet, Authority Hacker

## Quando usar este modo (vs blog-seo)

| Caso | Mode |
|---|---|
| Artigo informacional ("o que e X?") | **blog-seo** |
| Comparison "vs" da PROPRIA marca | **competitor-alternatives** (skill separada) |
| Review de produto 3rd-party com link afiliado | **review-site** (este) |
| "Best [X] for [Y]" round-up afiliado | **review-site** |
| Buying guide com afiliado | **review-site** |
| "Is X worth it" review | **review-site** |

⚠️ **Boundary critica:**
- **competitor-alternatives** = "We vs Them" — voce posiciona SUA marca contra concorrente
- **review-site** = review/comparison de produtos 3rd-party (afiliado) — voce nao vende, recomenda

---

## 4 Sub-tipos de Review

### 1. Single Product Review

Review profundo de UM produto especifico.

**Estrutura:**
1. Hook (problema que produto resolve OU resultado/transformacao)
2. Quem deveria comprar (perfil ideal)
3. Quem NAO deveria comprar (anti-perfil — credibilidade)
4. Background do produto (empresa, historia, posicionamento)
5. Pros (4-6 com exemplos concretos)
6. Cons (2-3 honestos — sem cons = parece ad)
7. Comparison rapido com 1-2 alternativas
8. Verdict (recomenda? pra quem? quando?)
9. CTA afiliado + Pricing + Disclosure FTC

### 2. Comparison 3rd-party ("X vs Y")

Compara 2 produtos terceiros. Voce nao vende nenhum.

**Estrutura:**
1. Hook ("Voce esta entre X e Y? Aqui o veredicto")
2. Quick verdict (1 frase: "Pra A, escolha X. Pra B, escolha Y")
3. Tabela comparativa side-by-side
4. Deep dive em 5-7 dimensoes (preco, features, suporte, etc)
5. Cenarios de uso ("Se voce e [persona], escolha [produto]")
6. CTA afiliado pra cada + Disclosure

### 3. Best-of Round-up ("Os 5 melhores X")

Lista ranqueada de N produtos pra um caso de uso.

**Estrutura:**
1. Hook (criterio de escolha + autoridade)
2. Metodologia ("Avaliei 23 produtos durante 6 meses")
3. Resumo executivo (top 3 numa frase cada)
4. Detalhe produto #1 (vencedor geral) — review profundo
5. Detalhe produto #2-5 — review medio
6. Tabela comparativa final
7. Como escolher pra seu caso (cenarios)
8. CTA afiliado por produto + Disclosure

### 4. Buying Guide ("Como comprar X")

Guia educacional + recomendacao de produtos.

**Estrutura:**
1. Hook (decisao + custo do erro)
2. O que considerar antes de comprar (5-8 fatores)
3. Tipos/categorias de [produto]
4. Faixas de preco
5. Top picks por categoria/preco
6. Erros comuns ao comprar
7. CTAs afiliados nas recomendacoes + Disclosure

---

## Disclosure FTC + ANPD/LGPD (OBRIGATORIO)

### FTC (US) — disclosure rule

Reviews afiliados PRECISAM disclosure visivel:

**Padrao:**
- Topo do artigo (antes de qualquer link)
- Linguagem clara: "Este artigo contem links de afiliado. Se voce comprar atraves dos links, podemos ganhar comissao sem custo adicional pra voce."
- Visivel sem scroll (acima do fold)
- Cor/font legivel (nao cinza minusculo)

**Anti-padroes (FTC penaliza):**
- ❌ Disclosure escondido no rodape
- ❌ Linguagem ambigua ("podemos ter relacao com...")
- ❌ Cor cinza-claro pequena
- ❌ Sem disclosure (multa pesada nos EUA)

### LGPD/ANPD (BR)

Brasil regula menos pesado que FTC, MAS:
- Codigo de Defesa do Consumidor exige propaganda identificavel
- ANPD pode atuar se review enganoso induz erro
- Boa pratica: usar mesmo padrao FTC

**Template disclosure BR:**
> "Este artigo contem links de afiliado. Se voce comprar atraves dos links, recebemos comissao sem custo adicional. Isso nao influencia nossa opiniao — recomendamos so produtos que testamos e gostamos."

---

## Schema.org Review Markup (OBRIGATORIO)

Review deve incluir schema JSON-LD pra Google + AI engines reconhecerem:

```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "Product",
    "name": "[nome do produto]",
    "image": "[url da imagem]",
    "brand": "[marca]"
  },
  "author": {
    "@type": "Person",
    "name": "[seu nome]"
  },
  "datePublished": "[YYYY-MM-DD]",
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "4.5",
    "bestRating": "5"
  },
  "reviewBody": "[trecho do review]"
}
```

**Beneficios:**
- Aparece em rich snippets do Google (estrelas)
- AI engines (Perplexity, ChatGPT) citam como fonte
- Aumenta CTR organico

---

## Tom: Critique Honesto (NAO Venda Direta)

Review afiliado vende mais quando soa **independente**, nao promotional.

### Padroes que funcionam

**Honestidade calibrada:**
- "X tem [pro], MAS [contra real]"
- "Eu recomendo X pra [perfil A], mas Y e melhor pra [perfil B]"
- "Quem nao deveria comprar: [anti-perfil]"

**Especificidade:**
- "Usei por 6 meses em meu projeto Z"
- "Comparei com Y e Z — esse e o que escolhi porque..."
- Numeros: "Reduziu meu tempo de [task] em 40%"

**Storytelling pessoal:**
- "Antes de descobrir X, eu tentei A, B, C — e por que essas falharam"
- "O momento que percebi que X resolveria foi quando..."

### Anti-padroes

- ❌ "X e o MELHOR produto do mercado!" (sem prova/comparacao)
- ❌ Sem cons (todo produto tem cons reais)
- ❌ Linguagem promocional ("amazing", "revolutionary")
- ❌ Apenas features, sem experiencia de uso
- ❌ Stack de bonus exagerado (parece ad)

---

## Estrutura de Review High-Conversion

```
1. HEADLINE
   "Review de [Produto] [Ano]: Vale a pena? Eu testei por [tempo]"

2. DISCLOSURE (acima do fold)
   "Este artigo contem links de afiliado..."

3. QUICK VERDICT (1 paragrafo)
   "[Produto] e [recomendacao] pra [perfil] que precisa [resultado].
   Nao recomendo pra [anti-perfil]. Score: [N/10]."

4. AUTHORITY (1 paragrafo)
   "Eu sou [seu papel/credencial]. Testei [Produto] durante [tempo]
   no contexto de [uso real]."

5. PROBLEMA QUE [PRODUTO] RESOLVE
   "Antes de [Produto], eu tinha [dor especifica]..."

6. PROS (4-6 com exemplos)
   - "[Pro 1]: por exemplo, [caso concreto vivido]"
   - "[Pro 2]: ..."

7. CONS (2-3 honestos)
   - "[Con 1]: [problema real, com cenario]"
   - "[Con 2]: ..."

8. COMPARISON RAPIDO (1-2 alternativas)
   "Vs [alternativa]: [diferenca chave]"

9. CENARIOS DE USO
   - "Pra [perfil A]: vai resolver porque..."
   - "Pra [perfil B]: melhor escolher [outro]"

10. PRICING
    Preco atualizado + comparacao com alternativa
    "Pix copia e cola" se aplicavel pra mercado BR

11. CTA AFILIADO
    "[Produto] no [link afiliado]" — botao destacado
    "Garanta seu acesso" (no nome de venda direta — review e neutro)

12. FAQ (3-5 objecoes comuns)
    - "Vale o preco?"
    - "Como cancelar?"
    - "Tem versao gratuita?"

13. SCHEMA REVIEW MARKUP (no head do HTML)
```

---

## Scoring/Rating System (consistencia)

Review precisa de rating system **consistente** entre artigos do site:

### Sistema 5 estrelas
| Stars | Significado |
|---|---|
| ⭐⭐⭐⭐⭐ | Excelente, recomendo amplamente |
| ⭐⭐⭐⭐ | Muito bom, recomendo com ressalvas |
| ⭐⭐⭐ | OK, depende muito do uso |
| ⭐⭐ | Tem problemas, evite a menos que [caso] |
| ⭐ | Nao recomendo |

### Sistema 10 pontos (Wirecutter style)
| Score | Significado |
|---|---|
| 9-10 | Top picks (raro) |
| 7-8 | Recomendo |
| 5-6 | OK pra perfil especifico |
| <5 | Evite |

### Multi-dimensional (NerdWallet style)
- Preco (1-5)
- Features (1-5)
- Suporte (1-5)
- UX (1-5)
- Valor geral (calculado)

---

## SEO Intent: keywords de review afiliado

| Intent | Keyword pattern | CTA principal |
|---|---|---|
| Pre-buying research | "[produto] review", "[produto] vale a pena" | Verdict + comparison |
| Comparison shopping | "[X] vs [Y]" | Decision matrix |
| Best-of search | "best [categoria] [ano]", "melhor [X]" | Lista ranqueada |
| Buying guide | "como escolher [produto]" | Educacao + recommendation |
| Anti-purchase research | "is [X] worth it", "[produto] vale a pena" | Veredicto critico |

---

## Aspectos Eticos (CRITICOS)

### Nao recomende algo que nao usou

- Use o produto pelo menos 30 dias antes de review
- Documenta com screenshots/videos
- Cita casos de uso reais

### Nao esconda relacao financeira

- Disclosure visivel sempre
- Mencione se recebeu o produto gratis pra review
- Mencione se tem qualquer relacao adicional (parceiro, afiliado, embaixador)

### Nao manipule rating pra comissao

Se 2 produtos sao similares mas X paga 30% comissao e Y paga 5%:
- ❌ ANTI-ETICO: ranquear X em primeiro porque paga mais
- ✅ ETICO: ranquear pelo merito, mencionar comissoes diferentes na disclosure

---

## Cases benchmark (estudar)

- **Wirecutter (NYT):** review profundo, metodologia transparente, baseado em testes reais
- **NerdWallet:** finance, multi-dimensional rating, foco em "best for [perfil]"
- **The Sweet Setup:** apps Apple, recomendacoes opinativas mas honestas
- **Authority Hacker:** SEO + afiliado, content marketing
- **Pat Flynn / Smart Passive Income:** podcast + blog, transparency total

---

## Quick Test pre-publish

Antes de publicar review afiliado:

- [ ] Disclosure visivel acima do fold?
- [ ] Pros + Cons (sem cons = ad disfarcado)?
- [ ] Schema.org Review markup no head?
- [ ] Date stamp visivel?
- [ ] Autor identificado com credenciais?
- [ ] Storytelling pessoal (testei por X tempo)?
- [ ] Anti-perfil mencionado (quem NAO deveria comprar)?
- [ ] Comparison com pelo menos 1 alternativa?
- [ ] Rating consistente com outros reviews do site?
- [ ] CTA afiliado com link rastreavel?
- [ ] FAQ com 3+ objecoes?
- [ ] Sweep #8 Anti-AI rodado (ver copy-process.md)?