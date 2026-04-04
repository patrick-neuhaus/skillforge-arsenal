# Guia de Design para Apresentações

## Antes de Começar

- **Paleta audaciosa e específica pro tema**: Se trocar suas cores pra outra apresentação e "funcionar", você não foi específico o bastante.
- **Dominância sobre igualdade**: Uma cor domina (60-70% do peso visual), com 1-2 tons de suporte e um acento marcante. Nunca distribua peso igual entre cores.
- **Contraste claro/escuro**: Fundos escuros pra título + conclusão, claros pra conteúdo (estrutura "sanduíche"). Ou escuro o deck inteiro pra sensação premium.
- **Comprometa-se com um motivo visual**: Escolha UM elemento distinto e repita — frames de imagem arredondados, ícones em círculos coloridos, bordas grossas de um lado só. Leve em todos os slides.

## Paletas de Cores

Escolha cores que combinem com seu tema — não caia no azul genérico.

| Tema | Primária | Secundária | Acento |
|------|----------|------------|--------|
| **Midnight Executive** | `1E2761` (navy) | `CADCFC` (ice blue) | `FFFFFF` (white) |
| **Forest & Moss** | `2C5F2D` (forest) | `97BC62` (moss) | `F5F5F5` (cream) |
| **Coral Energy** | `F96167` (coral) | `F9E795` (gold) | `2F3C7E` (navy) |
| **Warm Terracotta** | `B85042` (terracotta) | `E7E8D1` (sand) | `A7BEAE` (sage) |
| **Ocean Gradient** | `065A82` (deep blue) | `1C7293` (teal) | `21295C` (midnight) |
| **Charcoal Minimal** | `36454F` (charcoal) | `F2F2F2` (off-white) | `212121` (black) |
| **Teal Trust** | `028090` (teal) | `00A896` (seafoam) | `02C39A` (mint) |
| **Berry & Cream** | `6D2E46` (berry) | `A26769` (dusty rose) | `ECE2D0` (cream) |
| **Sage Calm** | `84B59F` (sage) | `69A297` (eucalyptus) | `50808E` (slate) |
| **Cherry Bold** | `990011` (cherry) | `FCF6F5` (off-white) | `2F3C7E` (navy) |

## Layouts por Slide

**Todo slide precisa de elemento visual** — imagem, gráfico, ícone ou shape. Slides só de texto são esquecíveis.

### Opções de Layout
- Duas colunas (texto esquerda, ilustração direita)
- Linhas de ícone + texto (ícone em círculo colorido, header bold, descrição abaixo)
- Grid 2x2 ou 2x3 (imagem de um lado, blocos de conteúdo do outro)
- Imagem half-bleed (full left ou right) com overlay de conteúdo

### Display de Dados
- Callouts de estatística (números grandes 60-72pt com labels pequenos abaixo)
- Colunas de comparação (antes/depois, prós/contras, lado a lado)
- Timeline ou fluxo de processo (passos numerados, setas)

### Polish Visual
- Ícones em pequenos círculos coloridos ao lado de headers de seção
- Texto itálico de acento para stats-chave ou taglines

## Tipografia

**Escolha um par interessante** — não caia no Arial. Header com personalidade + body limpo.

| Font Header | Font Body |
|-------------|-----------|
| Georgia | Calibri |
| Arial Black | Arial |
| Calibri | Calibri Light |
| Cambria | Calibri |
| Trebuchet MS | Calibri |
| Impact | Arial |
| Palatino | Garamond |
| Consolas | Calibri |

| Elemento | Tamanho |
|----------|---------|
| Título do slide | 36-44pt bold |
| Header de seção | 20-24pt bold |
| Texto body | 14-16pt |
| Captions | 10-12pt muted |

## Spacing

- 0.5" margens mínimas
- 0.3-0.5" entre blocos de conteúdo
- Deixe espaço pra respirar — não preencha cada centímetro

## Erros Comuns (Evite)

- **Não repita o mesmo layout** — varie colunas, cards e callouts entre slides
- **Não centralize texto body** — left-align parágrafos e listas; centralize só títulos
- **Não economize em contraste de tamanho** — títulos precisam de 36pt+ pra se destacar de 14-16pt body
- **Não caia no azul genérico** — escolha cores que reflitam o tema específico
- **Não misture spacing** — escolha 0.3" ou 0.5" e use consistentemente
- **Não estilize um slide e deixe o resto plain** — comprometa-se totalmente ou mantenha simples em tudo
- **Não crie slides só de texto** — adicione imagens, ícones, gráficos ou elementos visuais
- **Não esqueça padding de text box** — ao alinhar linhas ou shapes com bordas de texto, use `margin: 0` no text box
- **Não use elementos de baixo contraste** — ícones E texto precisam de contraste forte contra o fundo
- **NUNCA use linhas de acento sob títulos** — marca registrada de slides gerados por IA; use whitespace ou cor de fundo
