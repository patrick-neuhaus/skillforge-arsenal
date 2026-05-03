<!--
  copy-blog-seo.md — Framework artigo SEO + E-E-A-T + buyer stage + AI Overview citation + GEO + topical authority
  Carregado em: tasks de copy pra blog, conteudo editorial, SEO on-page, estrategia de conteudo
  v3 — 2026-05-03 (Wave 2: AI Overview citation + Schema for LLM + GEO + E-E-A-T pos-AI flood + Topical authority Pillar/Hub/Cluster)
-->

# Copy — Blog & SEO

**Referencias:** Brian Dean / Backlinko, Henneke Duistermaat, Ann Handley, Google Search Quality Guidelines

## E-E-A-T pos-AI flood (NOVO v3)

E-E-A-T sempre foi importante. Pos-AI flood (2024+), virou filtro PRIMARIO de ranqueamento.

| Letra | Significado | Como demonstrar (2026) |
|-------|-------------|----------------|
| **E** | Experience | Cases pessoais reais, "quando eu fiz X em [empresa] em [ano]", videos/screenshots |
| **E** | Expertise | Formacao + historico publico (LinkedIn, palestras, artigos citados) |
| **A** | Authoritativeness | Backlinks de sites autoritativos, mencoes externas, premios |
| **T** | Trustworthiness | HTTPS, autor identificado, fontes citadas, atualizacao recente, privacy clara |

### Sinais de "Experience" diferenciados (NOVO)

Google em 2025 aumentou peso do "E" (Experience) pra distinguir conteudo humano de IA.

**Experience signals que elevam ranking:**

- **Voz primeira pessoa:** "Em 2024, eu migrei nosso site de X para Y. O resultado foi..."
- **Numeros especificos vividos:** "Aumentei trafego em 47% em 6 meses fazendo Z"
- **Erros documentados:** "Tentei A. Falhou. Mudei pra B. Aqui porque..."
- **Anedota concreta:** "Quando o cliente C disse [frase exata], percebi que..."
- **Foto/video proprio:** screenshot do dashboard, video do processo
- **Data atualizada:** "Atualizado em 03/05/2026" (Google rebaixa conteudo desatualizado)

⚠️ **AI nao consegue gerar isso autentico:** especificidade temporal + emocional + referencial. Diferenca real entre humano e IA.

---

## Framework de Artigo SEO (6 componentes)

```
1. Headline (H1)
   → keyword primaria + beneficio claro
   → ex: "Como Reduzir Churn em SaaS: 9 Estrategias com Dados Reais"

2. Introducao
   → keyword no primeiro paragrafo (posicao natural, nao forcada)
   → promessa clara: "voce vai aprender [resultado especifico]"
   → gancho: dado surpreendente, pergunta, ou afirmacao contrarian

3. Body — H2s/H3s seguindo search intent
   → cada H2 = subtopico que o leitor espera ver
   → H3s detalham sub-pontos dentro do H2
   → responda as perguntas "People Also Ask" como H2 ou H3

4. Conteudo original
   → experiencia real: cases, dados proprios, perspectiva unica
   → nao reescreva o que ja esta ranqueando — adicione algo novo
   → citacoes de especialistas + fontes primarias

5. Internal links estrategicos
   → link para paginas de produto/servico quando relevante
   → link para outros artigos relacionados (cluster de conteudo)
   → anchor text descritivo, nao "clique aqui"

6. CTA no final
   → call-to-action alinhado com o estagio do funil do artigo
   → Awareness → conteudo gratuito | Decision → demo/trial
```

---

## AI Overview / ChatGPT Search / Perplexity Citation (NOVO v3)

AI Overview (Google), Perplexity, ChatGPT Search citam fontes quando respondem. Aparecer nessas citacoes = trafego novo + autoridade.

### Como ser citado

**1. Estruture pra ser parseavel:**

- Perguntas claras como H2/H3 (que LLMs vao buscar como query match)
- Respostas concisas logo apos a pergunta (1-3 paragrafos)
- Listas numeradas/bullets (LLMs preferem extrair de listas)
- Tabelas comparativas (ranqueia bem em "X vs Y" queries)

**2. Schema markup pra LLM:**

LLMs leem JSON-LD pra contexto.

| Schema | Quando usar |
|---|---|
| `Article` | Posts de blog (sempre) |
| `FAQPage` | FAQ section ou artigo Q&A |
| `HowTo` | Tutoriais passo-a-passo |
| `Product` | Pages de produto |
| `Review` | Reviews afiliados (ver copy-review-site.md) |
| `Organization` | Pagina sobre/footer |

**3. Entity Linking (NOVO):**

Mais que rich snippets, entities = "sistema nervoso" pra AI. Empresas que implementaram entity linking viram +69% cliques organicos e +19.7% visibilidade em AI Overview.

Pratica:
- Linke entidades mencionadas (produtos, pessoas, lugares) a Wikipedia, Wikidata
- Use schema `sameAs` apontando pra perfis autoritativos
- Mencione marca + categoria juntos ("Notion (productivity software)")

**4. First-person experience signals:**

LLMs preferem citar conteudo com **autoridade pessoal experiencial**. Inclua:
- Anedotas datadas
- Stats coletados pelo autor
- Casos de cliente especificos com numero
- Citacoes diretas de entrevistados

---

## GEO — Generative Engine Optimization (NOVO v3)

SEO classico = otimizar pra Google search. GEO = otimizar pra AI engines (ChatGPT, Perplexity, Gemini, Claude search).

### Padroes GEO

**1. FAQ verdadeiro, nao keyword stuffed:**
- Perguntas que pessoas REAIS fazem (Reddit, AlsoAsked, AnswerThePublic)
- Respostas diretas (1-3 paragrafos)
- Cada FAQ standalone (LLM extrai isolado)

**2. Titulos/subtitulos interrogativos:**
- "Qual o melhor [X] em 2026?"
- "Como funciona [Y]?"
- LLMs match query do user com title literal

**3. Linguagem que sinaliza expertise:**
- Passo-a-passo ("Primeiro X, depois Y")
- Citar fontes com data ("Estudo da Harvard 2024 mostra...")
- Exemplos pessoais datados
- Numeros especificos

**4. Atualizacao constante:**
- Date stamps visiveis ("Atualizado: 03/05/2026")
- Conteudo evergreen + revisao trimestral
- LLMs rebaixam conteudo "stale"

**5. Long-tail conversacional:**
- "Como [X] em [Y]" > "[X]"
- Queries naturais em texto > keywords agressivas

---

## Buyer Stage Keywords

| Estagio | Intent | Modificadores | CTA ideal |
|---------|--------|---------------|-----------|
| **Awareness** | Aprender | "what is", "how to", "guide", "o que e", "como" | Lead magnet, newsletter |
| **Consideration** | Comparar | "best", "vs", "alternatives", "melhor", "comparativo" | Webinar, case study, demo |
| **Decision** | Comprar | "pricing", "reviews", "demo", "preco", "contratar" | Trial, demo, contato |
| **Implementation** | Usar | "templates", "tutorial", "how to use", "configurar" | Onboarding, upsell |

**Aplicacao:**
- Artigo "o que e [conceito]" → Awareness → CTA pra newsletter ou guia
- Artigo "melhor [solucao] para [perfil]" → Consideration → CTA pra demo
- Artigo "[produto] preco" → Decision → CTA direto pra contato

---

## Topical Authority — Pillar/Hub/Cluster atualizado (NOVO v3)

Estrutura semantica pra Google + AI engines reconhecerem voce como autoridade no tema.

### Estrutura

```
PILLAR PAGE (artigo amplo, 3000-5000 palavras)
   "Manual de SEO 2026"
        |
        +-- HUB POSTS (subtopicos, 1500-3000 palavras)
        |     "Schema Markup pra AI"
        |     "E-E-A-T pos-AI explicado"
        |     "GEO: o que mudou em 2026"
        |
        +-- CLUSTER POSTS (long-tail, 800-1500 palavras)
              "Como configurar JSON-LD em Webflow"
              "Lista de schemas suportados pelo Google"
              ...
```

### Regras

- Cada cluster post linka pro hub (ancora descritiva)
- Hub linka pro pillar
- Pillar linka pra hubs principais
- Cluster pode linkar entre si lateral (so quando faz sentido)

### Beneficios

- Google entende "topical authority" no tema
- AI engines mapeiam relacoes (entity graph)
- Trafego long-tail soma com pillar autoritativo
- Internal linking forte (cresce DA das paginas)

⚠️ **Anti-padrao:** canibalizacao. Multiplos posts atacando mesma keyword. Use canonical ou consolide.

---

## Content Prioritization — Scoring

Antes de criar um artigo, pontue em 4 fatores:

| Fator | Peso | Como avaliar |
|-------|------|-------------|
| **Customer Impact** | 40% | Qual o impacto direto pra cliente / negocio? |
| **Content-Market Fit** | 30% | Temos autoridade real nesse tema? |
| **Search Potential** | 20% | Volume de busca + dificuldade keyword (KD) |
| **Resources** | 10% | Quanto custa produzir vs beneficio esperado? |

**Score final = Impact × 0.4 + Fit × 0.3 + Search × 0.2 + Resources × 0.1**

> Priorize artigos com score alto em Customer Impact + Content-Market Fit. SEO sem autoridade real no tema nao ranqueia mais (E-E-A-T).

---

## Checklist de Artigo SEO 2026

**Antes de escrever:**
- [ ] Keyword primaria definida (volume + KD pesquisados)?
- [ ] Search intent mapeado (informacional? transacional?)?
- [ ] Top 5 resultados atuais analisados?
- [ ] "People Also Ask" levantadas?
- [ ] AI Overview/Perplexity testado pra query? (que sites citam?)

**Ao escrever:**
- [ ] Keyword no H1, primeiro paragrafo, pelo menos 1 H2?
- [ ] Introducao com promessa clara em ate 3 linhas?
- [ ] Cada H2 cobre um subtopico esperado pelo leitor?
- [ ] Ha perspectiva ou dado original (nao apenas curadoria)?
- [ ] Internal links pra produto/servico e artigos relacionados?
- [ ] First-person experience signals incluidos? (E-E-A-T pos-AI)
- [ ] FAQ verdadeira pra GEO?

**Antes de publicar:**
- [ ] Meta description com keyword + beneficio (150-160 chars)?
- [ ] URL curta com keyword?
- [ ] Imagem com alt text descritivo?
- [ ] CTA no final alinhado com estagio do funil?
- [ ] Autor identificado com bio (E-E-A-T)?
- [ ] Schema markup apropriado (Article, FAQ, HowTo, Review)?
- [ ] Date stamp visivel?
- [ ] Entity linking nas mencoes principais?

---

## Skyscraper Technique (Brian Dean) — atualizado 2026

1. Encontre conteudo ranqueando alto com muitos backlinks
2. Crie algo 10x melhor (mais completo, mais atual, mais visual, mais acionavel)
3. **NOVO 2026:** adicione first-person experience que original nao tem
4. Contate quem linkava para o original

> Skyscraper sem experience signals = bate Google qualidade rebaix. Pos-2024, "10x better" precisa incluir perspectiva pessoal real.

---

## Anti-padroes 2026

- ❌ Conteudo IA sem revisao humana (Google detecta + rebaixa)
- ❌ Keyword stuffing
- ❌ Multiplos H1
- ❌ FAQ generica copiada de PAA sem resposta
- ❌ Sem schema markup
- ❌ Sem date stamp
- ❌ Sem autor identificado
- ❌ Canibalizacao (multiplos posts pra mesma keyword)
- ❌ Internal links com "clique aqui" (anchor descritivo sempre)
- ❌ Sem perspective/experience signals (gera "AI smell")