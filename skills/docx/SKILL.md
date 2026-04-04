---
name: docx
description: "Create, read, edit, generate, format, build, convert, extract, write, and produce Word documents (.docx). Expert in professional document generation with tables of contents, headings, page numbers, headers, footers, images, tables, tracked changes, and comments. Use when user wants to: create Word doc, edit .docx, generate report, build proposal, write memo, format letter, extract text from docx, insert images in document, find-and-replace in Word file, work with tracked changes or comments, convert content to Word, produce professional document, read docx content, manipulate Word file, add table of contents, create template. Triggers: 'Word doc', 'word document', '.docx', 'relatório Word', 'proposta em Word', 'documento formatado', 'gerar documento', 'editar documento', 'criar relatório', 'template Word', 'tracked changes', 'revisão de documento'. Do NOT use for PDFs (use pdf), spreadsheets (use xlsx), presentations (use pptx), or Google Docs."
license: Proprietary. LICENSE.txt has complete terms
---

# DOCX — Criacao, Edicao e Analise de Documentos Word

IRON LAW: NUNCA gere um documento sem antes perguntar qual formato/estrutura o usuario precisa. Um relatorio e uma proposta precisam de layouts completamente diferentes. Pergunte ANTES de escrever uma unica linha.

## Quick Reference

| Tarefa | Abordagem | Referencia |
|--------|-----------|------------|
| Ler/analisar conteudo | `pandoc` ou unpack para XML raw | - |
| Criar documento novo | `docx-js` via JavaScript | Load `references/docxjs-guide.md` |
| Editar documento existente | Unpack -> edit XML -> repack | Load `references/xml-editing-guide.md` |
| Converter .doc para .docx | `soffice.py --convert-to docx` | - |
| Converter para imagens | soffice -> PDF -> pdftoppm | - |
| Aceitar tracked changes | `scripts/accept_changes.py` | - |
| Regras criticas do docx-js | Gotchas que quebram renderizacao | Load `references/critical-rules.md` |

## Workflow

Copie este checklist e acompanhe o progresso:

```
DOCX Progress:

- [ ] Step 1: Entender Necessidade ⚠️ REQUIRED
  - [ ] 1.1 Perguntar tipo de documento (relatorio, proposta, carta, memo, template?)
  - [ ] 1.2 Perguntar formato de pagina (A4, US Letter, landscape?)
  - [ ] 1.3 Perguntar se tem template/modelo existente
  - [ ] 1.4 Perguntar elementos necessarios (TOC, headers, footers, imagens, tabelas?)
  - [ ] ⛔ GATE: Confirmar escopo com usuario antes de comecar
- [ ] Step 2: Escolher Abordagem ⚠️ REQUIRED
  - [ ] 2.1 Documento novo? -> Load references/docxjs-guide.md
  - [ ] 2.2 Editar existente? -> Load references/xml-editing-guide.md
  - [ ] 2.3 Apenas ler/extrair? -> pandoc direto
- [ ] Step 3: Construir
  - [ ] 3.1 Implementar estrutura base (pagina, margens, fontes)
  - [ ] 3.2 Adicionar conteudo principal
  - [ ] 3.3 Adicionar elementos especiais (TOC, imagens, tabelas)
  - [ ] 3.4 Load references/critical-rules.md antes de finalizar
- [ ] Step 4: Validar ⛔ BLOCKING
  - [ ] 4.1 Rodar python scripts/office/validate.py no arquivo
  - [ ] 4.2 Se falhou: unpack, corrigir XML, repack
  - [ ] ⛔ GATE: Se vai sobrescrever arquivo existente, CONFIRMAR com usuario
- [ ] Step 5: Entregar
  - [ ] Rodar pre-delivery checklist
  - [ ] Informar ao usuario o que foi gerado e onde esta
```

## Step 1: Entender Necessidade ⚠️ REQUIRED

Antes de qualquer codigo, pergunte:
- "Que tipo de documento voce precisa?" (relatorio, proposta, carta, contrato, memo, template)
- "Tamanho de pagina?" (A4 e o padrao do docx-js, US Letter precisa de config explicita)
- "Tem algum modelo/template existente pra seguir?"
- "Quais elementos especiais?" (sumario, cabecalho com logo, numeracao de pagina, tabelas)

Se o usuario ja deu contexto suficiente, nao repita perguntas obvias. Use bom senso.

## Step 2: Escolher Abordagem

### Criar documento novo
Load `references/docxjs-guide.md` — contem: setup, page size, styles, listas, tabelas, imagens, page breaks, hyperlinks, footnotes, tab stops, multi-column, TOC, headers/footers.

### Editar documento existente
Load `references/xml-editing-guide.md` — contem: unpack/edit/pack workflow, tracked changes, comments, imagens via XML, schema compliance, smart quotes.

### Apenas ler/extrair
```bash
# Extracao de texto com tracked changes
pandoc --track-changes=all document.docx -o output.md

# Acesso ao XML raw
python scripts/office/unpack.py document.docx unpacked/
```

### Converter .doc para .docx
```bash
python scripts/office/soffice.py --headless --convert-to docx document.doc
```

### Converter para imagens
```bash
python scripts/office/soffice.py --headless --convert-to pdf document.docx
pdftoppm -jpeg -r 150 document.pdf page
```

### Aceitar tracked changes
```bash
python scripts/accept_changes.py input.docx output.docx
```

## Step 3: Construir

Siga a referencia carregada no Step 2. Sempre consulte `references/critical-rules.md` antes de finalizar — contem as gotchas que quebram renderizacao em diferentes plataformas.

## Step 4: Validar ⛔ BLOCKING

```bash
python scripts/office/validate.py doc.docx
```

Se falhar:
1. Unpack: `python scripts/office/unpack.py doc.docx unpacked/`
2. Corrigir o XML com base no erro reportado
3. Repack: `python scripts/office/pack.py unpacked/ output.docx --original doc.docx`

### ⛔ Confirmation Gate — Sobrescrita de Arquivos

**NUNCA sobrescreva um arquivo .docx existente sem confirmacao explicita do usuario.** Sempre pergunte:
- "O arquivo X.docx ja existe. Quer que eu sobrescreva ou crie um novo arquivo?"

Se o usuario pediu para "editar" o arquivo, o padrao seguro e criar `output.docx` separado.

## Anti-Patterns

| Anti-Pattern | Por que e ruim | Faca isso |
|-------------|---------------|-----------|
| Gerar documento sem perguntar estrutura | Relatorio != proposta != carta | Pergunte o tipo ANTES (Iron Law) |
| Usar `\n` para quebra de linha | Cria XML invalido | Use Paragraph separados |
| Usar unicode bullets (`\u2022`) | Renderiza como texto, nao como lista | Use `LevelFormat.BULLET` com numbering config |
| `WidthType.PERCENTAGE` em tabelas | Quebra no Google Docs | Use sempre `WidthType.DXA` |
| `ShadingType.SOLID` em celulas | Fundo preto | Use `ShadingType.CLEAR` |
| Tabelas como divisores/regras | Altura minima, renderiza como caixa vazia | Use `border.bottom` em Paragraph |
| `PageBreak` fora de Paragraph | XML invalido | Sempre dentro de `new Paragraph({ children: [new PageBreak()] })` |
| `ImageRun` sem `type` | Crash | Sempre especifique png/jpg/etc |
| Escrever scripts Python para editar XML | Complexidade desnecessaria | Use a ferramenta Edit diretamente |
| Sobrescrever arquivo sem perguntar | Perda de dados | Crie arquivo separado ou confirme |

## Pre-Delivery Checklist

Antes de entregar QUALQUER documento, verifique:

```
- [ ] Validacao passou sem erros (validate.py)
- [ ] Tamanho de pagina esta correto (A4 vs US Letter)
- [ ] Fontes sao universais (Arial, Times New Roman)
- [ ] Tabelas tem dual widths (columnWidths + cell width)
- [ ] Imagens tem o parametro `type` definido
- [ ] TOC usa HeadingLevel (nao custom styles)
- [ ] Heading styles incluem outlineLevel (necessario pro TOC)
- [ ] Nenhum unicode bullet foi usado (tudo via numbering config)
- [ ] Smart quotes usadas para tipografia profissional
- [ ] Arquivo nao sobrescreveu original sem confirmacao
```

## Integracoes

| Skill | Quando usar juntas |
|-------|-------------------|
| **pdf** | Converter .docx para PDF (`soffice --convert-to pdf`), ou extrair conteudo de PDF para gerar .docx |
| **pptx** | Quando o conteudo do documento tambem precisa virar apresentacao, ou vice-versa |
| **xlsx** | Quando tabelas vem de planilhas ou dados do documento vao para Excel |
| **comunicacao-clientes** | Quando o documento e um entregavel pra cliente (proposta, relatorio) — a skill ajuda no tom |
| **maestro** | Quando o pedido envolve multiplos formatos (ex: "gera relatorio em Word e PDF") — maestro orquestra |

## Quando NAO Usar Esta Skill

- **PDF puro** — use a skill `pdf` (pypdf, pdfplumber)
- **Google Docs** — esta skill gera .docx local, nao interage com Google Docs API
- **Planilhas/tabelas de dados** — use `xlsx` mesmo que o usuario diga "documento com tabela"
- **Apresentacoes** — use `pptx`
- **Markdown/texto simples** — nao precisa de skill, Claude ja faz nativamente
- **Edicao de PDF existente** — use `pdf`, nao converta para .docx e de volta

## Dependencias

- **pandoc**: Extracao de texto
- **docx**: `npm install -g docx` (documentos novos)
- **LibreOffice**: Conversao PDF (auto-configurado via `scripts/office/soffice.py`)
- **Poppler**: `pdftoppm` para imagens
