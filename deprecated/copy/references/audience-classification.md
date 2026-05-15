<!--
  audience-classification.md — Sistema de classificacao por modo + Schwartz awareness + sophistication + Tom BR vs US
  Carregado em: Phase 0.2 (Audience Context classification)
  v3 — 2026-05-03 (Wave 1: Schwartz sophistication levels separados + Tom BR vs US deep)
-->

# Audience Classification System (por modo)

> **Load this file** in Phase 0.2 (Audience Context classification). Provides the full classification system for each of the 9 copy modes, including Schwartz 5 awareness levels + 5 sophistication levels for landing/cold-email/ads/review-site.

## Classification by mode

A classificacao de audiencia depende do modo. Schwartz classico (1-5 awareness) se aplica diretamente a **landing**, **cold-email**, **review-site**. Os outros modos usam sistemas proprios:

| Modo | Sistema de Classificacao | O que perguntar/classificar |
|------|--------------------------|----------------------------|
| **landing** | Schwartz Awareness 1-5 + Sophistication 1-5 | Nivel consciencia + estagio mercado |
| **cold-email** | Schwartz Awareness 1-5 | Nivel consciencia do prospect |
| **social** | Content Pillar + Formato | Qual pilar? (Industry 30%, BTS 25%, Educational 25%, Personal 15%, Promotional 5%). Qual formato? (Story, Contrarian, Value, Carousel, Thread) |
| **email** (sequence) | Schwartz Progressivo | Schwartz de ENTRADA (ex: 2) e Schwartz de SAIDA (ex: 4). Cada email progride a audiencia um nivel. |
| **whatsapp** | Estado do Lead | Frio? Morno? Quente? No-show? Follow-up? + tecnica Chris Voss |
| **blog-seo** | Buyer Stage | Awareness, Consideration, Decision, Implementation (ver copy-blog-seo.md) |
| **review-site** | Buyer Intent + Schwartz 3-5 | "X review", "is X worth it", "X vs Y" — leads em consideration→decision |
| **ux** | Estado da Interface | Onboarding, Erro, Empty State, Sucesso, Confirmacao Destrutiva (NAO usar Schwartz) |
| **ads** | Tipo de Trafego → Schwartz | Perguntar: "Trafego frio ou remarketing?" Frio → Schwartz 1-2. Remarketing → 3-4. Carrinho → 5. |

---

## Schwartz Awareness Levels (1-5)

> Regra de ouro: quanto mais inconsciente → mais indireto. Quanto mais consciente → mais direto.

| Nivel | Nome | Sinal | Framework padrao | Alternativa |
|-------|------|-------|-----------------|-------------|
| 1 | Unaware | Nao sabe que tem o problema | Story / SB7 | Epiphany Bridge |
| 2 | Problem Aware | Sabe do problema, nao da solucao | PAS | PASTOR |
| 3 | Solution Aware | Sabe que solucoes existem, nao conhece voce | AIDA | FAB, 4Ps |
| 4 | Product Aware | Conhece voce, ainda nao comprou | Value Equation | BAB |
| 5 | Most Aware | Pronto pra comprar, so precisa de motivo | Closing Framework | — |

**Regra critica:** urgencia e escassez so funcionam no nivel 4-5. Em niveis 1-2, afastam.

---

## Schwartz Sophistication Levels (1-5) — NOVO v3

**ATENCAO:** sophistication levels sao DIFERENTES de awareness levels. Awareness = quanto o LEITOR sabe. Sophistication = quanto o MERCADO esta saturado de promessas.

Os dois sao escalas independentes — copy precisa diagnosticar AMBOS antes de escolher framework.

| Nivel | Estado do Mercado | Estrategia de Copy | Exemplo |
|-------|-------------------|--------------------|---------|
| **1** | Mercado virgem (poucos players, pouca propaganda) | Afirme beneficio simples, direto | "Perca 5kg em 30 dias" — primeiro produto na categoria |
| **2** | Concorrentes copiam (promessa basica saturada) | Amplifique a MESMA promessa com mais forca, dados, autoridade | "Perca 10kg em 30 dias" + "Estudo da Harvard prova" |
| **3** | Promessas saturadas (todos prometem o mesmo) | Introduza **mecanismo unico** que renova credibilidade | "Perca 10kg em 30 dias com o protocolo cetogenico de 16 horas" |
| **4** | Mecanismos saturados (todos tem mecanismo) | **Refine/sub-mecanismo** ou amplifique sub-aspecto | "Perca 10kg com cetogenico noturno (so apos 18h)" |
| **5** | Mercado totalmente saturado (todo mecanismo ja viu) | **Identification > Concentration** — foque tribo/identidade | "Cetogenico para maes acima de 40 que trabalham fora" |

### Como diagnosticar sophistication

**Sinais de saturacao do mercado:**
- Quantos players competem direto? (Google: "[seu produto]" — paginas?)
- Que promessas dominam? (Headlines competidores se parecem?)
- Quanto custa CPC/CPM? (Alto = saturado)
- Cliente jaq tem ceticismo no nicho? ("ja tentei N coisas")

**Combine awareness + sophistication:**
- Awareness 2 + Sophistication 1: "Voce sabia que [problema]? Aqui e a solucao." (basico funciona)
- Awareness 2 + Sophistication 4: "Voce sabia que [problema]? A solucao especifica e [sub-mecanismo refinado]" (precisa de novo angulo)
- Awareness 4 + Sophistication 5: "Voce ja tentou X, Y, Z. Mas isso e diferente porque [identification + tribo]"

### Aplicar em copy

**Headlines por sophistication:**

| Sophistication | Headline pattern | Exemplo |
|---|---|---|
| 1 | Promessa simples direta | "Aprenda ingles" |
| 2 | Promessa amplificada | "Aprenda ingles fluente em 90 dias" |
| 3 | Promessa + mecanismo | "Aprenda ingles fluente em 90 dias com o metodo das 4 imersoes" |
| 4 | Sub-mecanismo refinado | "Aprenda ingles fluente em 90 dias com 4 imersoes de 25min/dia (sem gramatica)" |
| 5 | Identidade/tribo | "Para empresarios brasileiros: aprenda ingles em 90 dias mesmo trabalhando 12h" |

⚠️ **Erro comum:** usar headline sophistication 1 em mercado sophistication 4 → lead acha "promessa rasa, ja vi mil vezes" e ignora.

---

## Schwartz 5 — Closing Framework

Para audiencia Most Aware (trial usado, carrinho abandonado, remarketing quente):

1. Lembrete do valor — o que ja experimentaram/viram/receberam
2. Objecao final enderecada — a unica coisa que ainda impede
3. Incentivo — desconto, bonus, extensao de trial, upgrade
4. CTA direto + urgencia real — prazo ou escassez verdadeira
5. Guarantee + risk reversal — transferir risco pro vendedor

Tom: assertivo, direto, sem rodeios. Nao re-educar — o lead ja sabe tudo.

## Schwartz 3 — Comparacao Competitiva

Para Schwartz 3 (Solution Aware), o lead esta comparando alternativas. O copy deve incluir diferenciacao: secao de comparacao (vs. concorrentes), posicionamento claro, prova especifica.

## Audiencia Mista / Stack de Frameworks

Se a audiencia cobre multiplos niveis Schwartz (ex: sales page longa, remarketing misto):

1. Classificar Schwartz de ENTRADA e de SAIDA
2. Usar Stack de Frameworks:
   - Secoes 1-3: framework do nivel de entrada (ex: PAS pra nivel 2)
   - Secoes 4-6: framework intermediario (ex: FAB/AIDA pra nivel 3)
   - Secoes 7+: framework do nivel de saida (ex: Value Equation pra nivel 4-5)

---

## Tom BR vs US (NOVO v3 — DR-brasil)

100% dos clientes Patrick sao BR → tom BR e default, nao excecao. Detalhe abaixo:

### Diferencas estruturais

| Dimensao | Copy BR | Copy US |
|----------|---------|---------|
| **Distancia leitor** | Caloroso, proximo ("amigao", "voce") | Distante, formal ("you" institucional) |
| **Humor** | Autoironia, situacional, popular (BBB, futebol, novela, memes) | Sarcastico, understatement, dry |
| **Promessa** | Superlativo aceito ("O melhor!", "Imperdivel!", "Maior do Brasil!") | Understatement com brincadeira |
| **Hiperboles** | Aceitas com lastro de prova | Evitadas (soa "as seen on TV") |
| **Referencias culturais** | Datadas (BBB 2024, novela atual) — vida util ~6 meses | Universais (Star Wars, Friends) — anos |
| **Storytelling** | Personal, emocional, "minha historia" | Estruturado, "case study" |
| **CTA tom** | Direto + emocional ("Quero comecar agora!") | Funcional ("Get started") |
| **Religiosidade** | Implicita aceita (gratidao, fe, milagre — cuidado) | Quase ausente em copy comercial |
| **Regional** | Sul, NE, SE com girias proprias — segmenta | Pouco regional (English uniforme) |

### Quando usar tom BR puro

- 100% audiencia BR
- B2C (sempre)
- Influencer/criador BR
- Local business (bar, restaurante, salao)
- Coaching/infoproduto BR

### Quando neutralizar (BR mais sobrio)

- B2B SaaS BR (CFO/diretor pode estranhar gerundismo + "amigao")
- Audiencia mista BR + LATAM
- Marca premium aspiracional

### Quando usar tom US (em PT-BR)

- Copy traduzido US (mas adapte! tradução literal soa frio)
- Marca global posicionada como "international" (Apple-like)
- Audiencia tech/dev BR (acostumada a ingles)

### Pegadinhas de tom

⚠️ **Religiosidade:** "Deus ilumine seu negocio" funciona em alguns nichos (saude/familia), afasta em outros (tech). Default: usar valores universais (gratidao, solidariedade) sem mencionar deidades.

⚠️ **Regionalismos fortes:** "Mainha", "tchê", "uai" — segmenta pra regiao. Em campanha nacional, neutralize. Em remarketing geo-tagged, intensifique.

⚠️ **Gerundismo:** "Estamos preparando o seu pedido pra estar entregando" — soa fraco e robotico. Prefira: "Preparamos seu pedido. Entregamos hoje."

⚠️ **Promessa milagrosa:** copy BR DR (info-produto) tende ao "transforme sua vida em 7 dias!". Anvisa/CVM regulam pesado em saude/financas. Sempre adicionar disclaimer quando categoria exige (ver foundations.md Compliance).

---

## B2B vs B2C (mantido — referencia rapida)

| Dimensao | B2B | B2C |
|----------|-----|-----|
| Decisor | Comite, multiplos stakeholders | Individual ou familia |
| Ciclo | Longo (semanas a meses) | Curto (minutos a dias) |
| Driver | ROI, eficiencia, compliance, risk-to-career | Emocao, desejo, status |
| Tom | Profissional, baseado em dados | Conversacional, emocional |
| Prova | Cases com ROI, logos, TCO comparison | Reviews, testemunhos pessoais |
| CTA | "Agende demo", "Fale com vendas" | "Compre agora", "Comece gratis" |
| Schwartz tipico | 3-4 (avaliando alternativas) | 1-3 (descobrindo problema/solucao) |