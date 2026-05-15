# Regras Criticas do docx-js

Consulte esta referencia ANTES de finalizar qualquer documento. Estas gotchas quebram renderizacao em diferentes plataformas.

---

## Page Size

- **Defina tamanho de pagina explicitamente** — docx-js padrao e A4; use US Letter (12240 x 15840 DXA) para documentos US
- **Landscape: passe dimensoes portrait** — docx-js troca width/height internamente; passe a borda curta como `width`, longa como `height`, e defina `orientation: PageOrientation.LANDSCAPE`

## Texto e Conteudo

- **Nunca use `\n`** — use elementos Paragraph separados
- **Nunca use unicode bullets** — use `LevelFormat.BULLET` com numbering config
- **PageBreak deve estar dentro de Paragraph** — standalone cria XML invalido
- **ImageRun requer `type`** — sempre especifique png/jpg/etc

## Tabelas

- **Sempre defina table `width` com DXA** — nunca use `WidthType.PERCENTAGE` (quebra no Google Docs)
- **Tabelas precisam de dual widths** — array `columnWidths` E `width` na celula, ambos devem bater
- **Table width = soma de columnWidths** — para DXA, garanta que somam exatamente
- **Sempre adicione cell margins** — use `margins: { top: 80, bottom: 80, left: 120, right: 120 }` para padding legivel
- **Use `ShadingType.CLEAR`** — nunca SOLID para shading de tabela
- **Nunca use tabelas como divisores/regras** — celulas tem altura minima e renderizam como caixas vazias (incluindo em headers/footers); use `border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "2E75B6", space: 1 } }` em Paragraph. Para footers com duas colunas, use tab stops, nao tabelas

## TOC e Headings

- **TOC requer HeadingLevel apenas** — sem custom styles em heading paragraphs
- **Override built-in styles** — use IDs exatos: "Heading1", "Heading2", etc.
- **Inclua `outlineLevel`** — obrigatorio para TOC (0 para H1, 1 para H2, etc.)

## Unidades de Medida — Referencia Rapida

| Contexto | Unidade | Conversao |
|----------|---------|-----------|
| Page size, margins, table widths | DXA | 1440 DXA = 1 inch |
| Font size | Half-points | 24 = 12pt |
| Image dimensions (XML) | EMU | 914400 EMU = 1 inch |
| Image dimensions (docx-js) | Pixels | Usa transformation: { width, height } |
| Spacing | Twips | 240 twips = 12pt |

## Compatibilidade Cross-Platform

| Feature | Word | Google Docs | LibreOffice |
|---------|------|-------------|-------------|
| `WidthType.DXA` | OK | OK | OK |
| `WidthType.PERCENTAGE` | OK | QUEBRA | Parcial |
| `ShadingType.CLEAR` | OK | OK | OK |
| `ShadingType.SOLID` | Fundo preto | Fundo preto | Fundo preto |
| TOC com HeadingLevel | OK | OK | OK |
| TOC com custom styles | OK | QUEBRA | QUEBRA |
| Tabelas em headers/footers | Altura minima | Renderiza vazio | Inconsistente |
