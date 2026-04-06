---
name: copy
description: "Write, review, improve, and optimize copy for any channel. 8 modes: Landing Page, Social, Email, Cold Email, WhatsApp, Blog/SEO, UX/Microcopy, Ads. Frameworks: AIDA, PAS, StoryBrand SB7, Hormozi Value Equation. Schwartz 5 awareness levels. Seven Sweeps editing. Use when: 'escreve copy', 'melhora esse texto', 'headline pra landing', 'email sequence', 'copy de anúncio', 'write copy', 'improve this copy'."
---

# Copy v1

IRON LAW: NUNCA escreva copy sem antes classificar o nível de consciência da audiência (Schwartz). Copy nível 1 com táticas de nível 5 (oferta direta + urgência) é a causa #1 de campanhas que não convertem. Classifique ANTES de escolher framework.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--mode <m>` | landing, social, email, cold-email, whatsapp, blog-seo, ux, ads | auto-detect |
| `--edit` | Revisar/editar copy existente (Seven Sweeps) | false |
| `--brief` | Gerar copy brief antes de escrever | false |
| `--framework <f>` | Forçar framework: aida, pas, bab, sb7, pastor, value-eq | auto por awareness |

## Workflow

```
Copy Progress:

- [ ] Phase 0: Contexto ⚠️ REQUIRED
  - [ ] 0.1 Identificar modo (Landing/Social/Email/etc.) ou auto-detect
  - [ ] 0.2 Classificar nível de consciência da audiência (Schwartz 1-5)
  - [ ] 0.3 Definir objetivo (converter? nutrir? educar?)
- [ ] Phase 1: Pesquisa ⚠️ REQUIRED
  - [ ] 1.1 Load references/foundations.md (sempre)
  - [ ] 1.2 Load arquivo de referência do modo específico
  - [ ] 1.3 Se --brief: gerar copy brief antes de escrever
  - [ ] 1.4 Se VoC disponível: minerar linguagem do cliente
- [ ] Phase 2: Escrever ⚠️ REQUIRED
  - [ ] 2.1 Selecionar framework pelo nível de consciência + modo
  - [ ] 2.2 Escrever primeiro rascunho seguindo estrutura do framework
  - [ ] 2.3 Load references/headlines.md para opções de headline/hook
  - [ ] 2.4 Gerar 2-3 alternativas de headline
- [ ] Phase 3: Editar ⛔ BLOQUEANTE
  - [ ] 3.1 Load references/copy-process.md (Seven Sweeps)
  - [ ] 3.2 Rodar sweeps: Clareza → Voz → E daí? → Prove → Especificidade → Emoção → Zero Risco
  - [ ] 3.3 Load references/power-words.md para polish no nível de palavra
- [ ] Phase 4: Apresentar ⛔ BLOQUEANTE
  - [ ] 4.1 Apresentar copy com anotações explicando as escolhas
  - [ ] 4.2 Apresentar alternativas de headline
  - [ ] ⛔ GATE: Aprovação do usuário antes de qualquer publicação/envio
```

## Phase 0: Detect Mode

Identifique o modo antes de qualquer coisa:

| Contexto | Modo |
|---------|------|
| "landing page", "página de vendas", "LP" | landing |
| "post", "LinkedIn", "Instagram", "TikTok", "carrossel" | social |
| "email", "sequence", "nurture", "welcome" | email |
| "cold email", "outbound", "prospecção" | cold-email |
| "WhatsApp", "mensagem", "follow-up" | whatsapp |
| "blog", "artigo", "SEO", "conteúdo" | blog-seo |
| "botão", "erro", "onboarding", "microcopy", "UX" | ux |
| "anúncio", "ad", "Meta", "Google Ads", "criativo" | ads |

**Se ambíguo:** pergunte. Não assuma.

## Phase 1: Awareness Level (Schwartz)

Classifique ANTES de escolher framework:

| Nível | Nome | Sinal | Framework padrão | Alternativa |
|-------|------|-------|-----------------|-------------|
| 1 | Unaware | Não sabe que tem o problema | Story / SB7 | Epiphany Bridge |
| 2 | Problem Aware | Sabe do problema, não da solução | PAS | PASTOR |
| 3 | Solution Aware | Sabe que existe solução, não conhece você | AIDA | FAB, 4Ps |
| 4 | Product Aware | Conhece você, ainda não comprou | Value Equation | BAB |
| 5 | Most Aware | Pronto pra comprar, só precisa de motivo | Direto (oferta + CTA) | — |

**Regra crítica:** urgência e escassez só funcionam no nível 4-5. Em níveis 1-2, afastam.

## Phase 2: Framework Reference

**AIDA** — Atenção → Interesse → Desejo → Ação. Nível 3.

**PAS** — Problema → Agitação → Solução. Nível 2. Aprofunde a dor antes de resolver.

**BAB** — Before → After → Bridge. Nível 4. Foco na transformação.

**SB7 / StoryBrand** — Personagem → Problema → Guia → Plano → Ação → Evitar falha → Sucesso. Nível 1-2.

**PASTOR** — Problem → Amplify → Story → Testimony → Offer → Response. Nível 2-3.

**Value Equation (Hormozi)** — (Sonho × Probabilidade) / (Tempo × Esforço). Nível 4. Maximize numerador, minimize denominador.

## Phase 3: Reference Loading Rules

- SEMPRE load: `references/foundations.md`
- Por modo: load `references/copy-[mode].md`
- Se `--edit`: load `references/copy-process.md`
- Para headlines: load `references/headlines.md`
- Para polish: load `references/power-words.md`
- Para psicologia: load `references/copy-psychology.md`

## Anti-Patterns

- Escrever copy sem saber o nível de consciência
- Usar urgência/escassez pra audiências Unaware
- Corporativês ("alavancar", "solução robusta", "seamless")
- Feature dump sem benefício (teste "o que significa que..." )
- CTA ausente ou enterrado no fim
- Tom inconsistente entre seções
- Claims genéricas sem prova ("o melhor do mercado", "world-class")
- Escrever pra todo mundo = não escrever pra ninguém

## Quando NÃO usar

| Situação | Use em vez disso |
|-----------|-----------------|
| Estratégia de marca / posicionamento | **product-discovery-prd** |
| Auditoria SEO / SEO técnico | **seo** |
| Auditoria de fluxo UX (não microcopy) | **ux-audit** |
| Comunicação com clientes | **comunicacao-clientes** |
| Prompt engineering pra IA | **prompt-engineer** |

## Integrations

- **SEO** — copy escreve o conteúdo, seo otimiza a estrutura e os metadados
- **UX Audit** — ux-audit revisa fluxos, copy escreve a microcopy
- **Comunicação Clientes** — comunicação cuida das mensagens com clientes, copy cuida do marketing
- **Product Discovery PRD** — PRD define o que construir, copy vende

## Design Principles

1. Nível de consciência Schwartz ANTES da escolha do framework
2. VoC (Voz do Cliente) > linguagem inventada — use as palavras do seu cliente
3. Clareza > criatividade — sempre
4. Especificidade > generalidade — números, nomes, datas
5. Benefícios > features — ponte "o que significa que..."
6. Teste > opinião — A/B é o único árbitro
7. Edição não é opcional — Seven Sweeps é o padrão mínimo
