# Design Skill Template — Skills com Identidade Visual

Consulte este arquivo no **Step 3** quando a skill envolve output visual ou design.

---

## Quando Usar Este Template

- Skill que gera UI, componentes visuais, ou landing pages
- Skill que aplica branding (cores, fontes, logo) em outputs
- Skill que combina IA (decisoes criativas) com assets de marca

## O Diferencial: Skill + Identidade Visual

Skill sozinha = output generico, "cara de AI"
Skill + identidade visual = output profissional e distinto

O insight do Video 5 (DevGPT): a melhoria dramatica vem de combinar instrucoes da skill com assets concretos de marca.

## Pre-requisitos de Identidade Visual

Antes de usar a skill, o usuario deve ter:

| Asset | Obrigatorio | Formato |
|-------|:-----------:|---------|
| Logo (dark + light) | Sim | SVG ou PNG transparente |
| Paleta de cores | Sim | 3-5 hex codes (primary, accent, neutral) |
| 2 fontes | Sim | Display (titulos) + Body (texto) |
| Conceito visual | Recomendado | 1 palavra/frase (ex: "montanhas", "tech minimal") |
| Imagem de fundo | Opcional | Alinhada ao conceito |

## Anatomia da Design Skill

```
design-skill/
├── SKILL.md           # Workflow + instrucoes
├── references/
│   ├── design-json-schema.md    # Schema do design.json
│   ├── brand-checklist.md       # Checklist de assets necessarios
│   └── micro-interactions.md    # Padroes de hover, transicao, animacao
└── assets/                      # Exemplos de output
```

## Workflow em 2 Fases

### Fase 1: Baseline (sem skill)
1. Gerar versao funcional basica do output
2. Documentar o "antes" — resultado generico serve como controle

### Fase 2: Refinamento (com skill + assets)
1. Prompt: "Melhore o design usando a skill + essas cores/fontes/assets"
2. Anexar screenshots da paleta e tipografia (assets concretos > descricoes)
3. A skill automaticamente adiciona micro-interactions (hover, transitions)
4. 2 prompts ja produzem diferenca dramatica

## Template de design.json

A skill de design deve gerar um `design.json` com:

```json
{
  "designPrinciples": ["..."],
  "colorPalette": {
    "primary": "#hex",
    "accent": "#hex",
    "neutral": ["#light", "#mid", "#dark"]
  },
  "typography": {
    "headings": { "family": "...", "weights": [...] },
    "body": { "family": "...", "weights": [...] }
  },
  "spacing": { "unit": "rem", "scale": [...] },
  "components": { "button": {...}, "card": {...} },
  "effects": { "shadows": [...], "transitions": [...] }
}
```

## Anti-Patterns de Design Skills

- **Descrever cores com adjetivos:** "Use uma cor quente" → usar hex code exato
- **Ignorar dark/light mode:** Sempre ter variantes
- **Micro-interactions ausentes:** UI estatica parece "morta" — adicionar hover, focus, transition
- **Generico bonito:** Bonito mas sem identidade = ainda "cara de AI". Precisa dos assets de marca
- **Gradientes cliche:** Gradientes roxo-rosa sao o "selo de AI generico". Evitar

## Roteiro de Perguntas

Perguntas que a skill deve fazer ao usuario:

1. "Tem logo? Em quais formatos (SVG, PNG)? Tem versao dark e light?"
2. "Quais sao as cores da marca? (hex codes)"
3. "Quais fontes usar? (nome + onde encontrar — Google Fonts, CDN, local)"
4. "Qual o conceito visual? (1-2 palavras: elegante, tech, natural, bold...)"
5. "Tem alguma referencia visual que voce gosta? (URL ou screenshot)"
