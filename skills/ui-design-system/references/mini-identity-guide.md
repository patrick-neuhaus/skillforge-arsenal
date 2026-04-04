# Mini Identity Guide — Criar Identidade Visual Minima

Consulte este arquivo no modo `--identity`.

---

## O que e Necessario (Minimo Viavel)

| Asset | Obrigatorio | Onde conseguir |
|-------|:-----------:|----------------|
| Logo (dark + light) | Sim | Designer, Canva, ou AI (DALL-E, Midjourney) |
| 3-5 cores hex | Sim | Coolors.co, Realtime Colors, Adobe Color |
| 2 fontes | Sim | Google Fonts (gratis, CDN-ready) |
| Conceito visual (1 palavra) | Recomendado | Workshop com cliente ou brainstorm |
| Imagem de referencia | Opcional | Dribbble, Behance, Awwwards |

## Passo a Passo

### 1. Logo
- **Se nao tem:** Usar iniciais/nome em fonte marcante como placeholder
- **Formatos:** SVG (ideal) ou PNG transparente
- **Versoes:** Dark background (logo claro) + Light background (logo escuro)
- **Onde colocar:** `public/brands/` ou `public/images/`

### 2. Paleta de Cores
Minimo 3 cores, ideal 5:

| Funcao | O que e | Exemplo |
|--------|---------|---------|
| **Primary** | Cor principal da marca | #2563EB (azul) |
| **Accent** | Destaque, CTAs, links | #F59E0B (amarelo) |
| **Neutral Dark** | Textos, backgrounds escuros | #1E293B |
| **Neutral Mid** | Bordas, separadores | #94A3B8 |
| **Neutral Light** | Backgrounds claros | #F8FAFC |

**Ferramentas:**
- Coolors.co — gera paletas harmonicas
- Realtime Colors — preview cores numa landing page
- Adobe Color — roda de cores com teoria

**Regra:** Se o cliente NAO tem cores definidas, peca referencia visual (site/app que gosta) e extraia a paleta.

### 3. Tipografia
Duas fontes:

| Funcao | Tipo | Exemplos |
|--------|------|----------|
| **Display** (titulos) | Serif ou marcante | Playfair Display, Merriweather, Space Grotesk |
| **Body** (textos) | Sans-serif legivel | Inter, DM Sans, Nunito, Source Sans 3 |

**Combos testados:**
- Playfair Display + Inter (elegante)
- Space Grotesk + DM Sans (tech moderno)
- Merriweather + Source Sans 3 (editorial)
- Inter + Inter (minimalista — so muda weight)

**Regra:** Na duvida, use Inter pra tudo. E a fonte mais segura e versatil.

### 4. Conceito Visual
Uma palavra/frase que guia TODAS as decisoes visuais:

| Conceito | Implicacao |
|----------|-----------|
| "Tech minimal" | Cores frias, sans-serif, muito whitespace |
| "Natureza" | Verdes, formas organicas, texturas |
| "Luxo" | Serif, dourado/preto, sombras suaves |
| "Energia" | Cores vibrantes, gradientes, animacoes |
| "Corporativo" | Azul/cinza, sans-serif, grid rigido |

### 5. Checklist Final

Antes de usar os assets na skill de design:
- [ ] Logo existe em pelo menos 1 formato (SVG ou PNG)
- [ ] 3+ cores hex definidas (primary, accent, neutral)
- [ ] 2 fontes escolhidas com fallbacks
- [ ] Conceito visual em 1-2 palavras
- [ ] Assets colocados em pasta acessivel (public/brands/)
- [ ] Screenshot da paleta + tipografia (pra anexar ao prompt)

## Insight do Video 5

"A skill sozinha melhora a qualidade visual, mas sem assets de marca proprios, o resultado ainda sera bonito generico. O diferencial real e skill + identidade visual, por menor que seja."

Assets concretos (hex codes, nomes de fonte, screenshots) sao MAIS eficazes que descricoes textuais. Sempre que possivel, anexe screenshots.
