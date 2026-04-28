---
name: docx
description: "Word documents (.docx) — create, read, edit, generate, format, build, convert, extract. TOC, headings, page numbers, headers/footers, images, tables, tracked changes, comments. Use em: 'Word doc', 'word document', '.docx', 'relatório Word', 'proposta em Word', 'documento formatado', 'gerar documento', 'editar documento', 'criar relatório', 'template Word', 'tracked changes', 'revisão de documento', extract text from docx, find-and-replace Word, professional document. NOT for PDFs (use pdf), spreadsheets (xlsx), presentations (pptx), Google Docs."
license: Proprietary. LICENSE.txt has complete terms
---

# DOCX — Criação, Edição e Análise de Documentos Word

**Iron Law:** Nunca gere um documento sem antes perguntar qual formato/estrutura o usuário precisa. Um relatório e uma proposta precisam de layouts completamente diferentes. Pergunte ANTES de escrever uma única linha.

## Quick Reference

| Tarefa | Abordagem | Referência |
|--------|-----------|------------|
| Ler/analisar conteúdo | `pandoc` ou unpack para XML raw | - |
| Criar documento novo | `docx-js` via JavaScript | Load `references/docxjs-guide.md` |
| Editar documento existente | Unpack → edit XML → repack | Load `references/xml-editing-guide.md` |
| Converter .doc para .docx | `soffice.py --convert-to docx` | - |
| Converter para imagens | soffice → PDF → pdftoppm | - |
| Aceitar tracked changes | `scripts/accept_changes.py` | - |
| Regras críticas do docx-js | Gotchas que quebram renderização | Load `references/critical-rules.md` |

## Workflow

Copie este checklist e acompanhe o progresso:

```
DOCX Progress:

- [ ] Step 1: Entender Necessidade ⚠️ REQUIRED
  - [ ] 1.1 Perguntar tipo de documento (relatório, proposta, carta, memo, template?)
  - [ ] 1.2 Perguntar formato de página (A4, US Letter, landscape?)
  - [ ] 1.3 Perguntar se tem template/modelo existente
  - [ ] 1.4 Perguntar elementos necessários (TOC, headers, footers, imagens, tabelas?)
  - [ ] ⛔ GATE: Confirmar escopo com usuário antes de começar
- [ ] Step 2: Escolher Abordagem ⚠️ REQUIRED
  - [ ] 2.1 Documento novo? → Load references/docxjs-guide.md
  - [ ] 2.2 Editar existente? → Load references/xml-editing-guide.md
  - [ ] 2.3 Apenas ler/extrair? → pandoc direto
- [ ] Step 3: Construir
  - [ ] 3.1 Implementar estrutura base (página, margens, fontes)
  - [ ] 3.2 Adicionar conteúdo principal
  - [ ] 3.3 Adicionar elementos especiais (TOC, imagens, tabelas)
  - [ ] 3.4 Load references/critical-rules.md antes de finalizar
- [ ] Step 4: Validar ⛔ BLOCKING
  - [ ] 4.1 Rodar python scripts/office/validate.py no arquivo
  - [ ] 4.2 Se falhou: unpack, corrigir XML, repack
  - [ ] ⛔ GATE: Se vai sobrescrever arquivo existente, confirmar com usuário
- [ ] Step 5: Entregar
  - [ ] Rodar pre-delivery checklist
  - [ ] Informar ao usuário o que foi gerado e onde está
```

## Step 1: Entender Necessidade ⚠️ REQUIRED

Antes de qualquer código, pergunte:
- "Que tipo de documento você precisa?" (relatório, proposta, carta, contrato, memo, template)
- "Tamanho de página?" (A4 é o padrão do docx-js, US Letter precisa de config explícita)
- "Tem algum modelo/template existente pra seguir?"
- "Quais elementos especiais?" (sumário, cabeçalho com logo, numeração de página, tabelas)

Se o usuário já deu contexto suficiente, não repita perguntas óbvias. Use bom senso.

## Step 2: Escolher Abordagem

### Criar documento novo
Load `references/docxjs-guide.md` — contém: setup, page size, styles, listas, tabelas, imagens, page breaks, hyperlinks, footnotes, tab stops, multi-column, TOC, headers/footers.

### Editar documento existente
Load `references/xml-editing-guide.md` — contém: unpack/edit/pack workflow, tracked changes, comments, imagens via XML, schema compliance, smart quotes.

### Apenas ler/extrair
```bash
# Extração de texto com tracked changes
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

Siga a referência carregada no Step 2. Sempre consulte `references/critical-rules.md` antes de finalizar — contém as gotchas que quebram renderização em diferentes plataformas.

## Step 4: Validar ⛔ BLOCKING

```bash
python scripts/office/validate.py doc.docx
```

Se falhar:
1. Unpack: `python scripts/office/unpack.py doc.docx unpacked/`
2. Corrigir o XML com base no erro reportado
3. Repack: `python scripts/office/pack.py unpacked/ output.docx --original doc.docx`

### ⛔ Confirmation Gate — Sobrescrita de Arquivos

**Nunca sobrescreva um arquivo .docx existente sem confirmação explícita do usuário.** Sempre pergunte:
- "O arquivo X.docx já existe. Quer que eu sobrescreva ou crie um novo arquivo?"

Se o usuário pediu para "editar" o arquivo, o padrão seguro é criar `output.docx` separado.

## Anti-Patterns

| Anti-Pattern | Por que é ruim | Faça isso |
|-------------|---------------|-----------|
| Gerar documento sem perguntar estrutura | Relatório ≠ proposta ≠ carta | Pergunte o tipo antes (Iron Law) |
| Usar `\n` para quebra de linha | Cria XML inválido | Use Paragraph separados |
| Usar unicode bullets (`\u2022`) | Renderiza como texto, não como lista | Use `LevelFormat.BULLET` com numbering config |
| `WidthType.PERCENTAGE` em tabelas | Quebra no Google Docs | Use sempre `WidthType.DXA` |
| `ShadingType.SOLID` em células | Fundo preto | Use `ShadingType.CLEAR` |
| Tabelas como divisores/regras | Altura mínima, renderiza como caixa vazia | Use `border.bottom` em Paragraph |
| `PageBreak` fora de Paragraph | XML inválido | Sempre dentro de `new Paragraph({ children: [new PageBreak()] })` |
| `ImageRun` sem `type` | Crash | Sempre especifique png/jpg/etc |
| Escrever scripts Python para editar XML | Complexidade desnecessária | Use a ferramenta Edit diretamente |
| Sobrescrever arquivo sem perguntar | Perda de dados | Crie arquivo separado ou confirme |

## Pre-Delivery Checklist

Antes de entregar qualquer documento, verifique:

```
- [ ] Validação passou sem erros (validate.py)
- [ ] Tamanho de página está correto (A4 vs US Letter)
- [ ] Fontes são universais (Arial, Times New Roman)
- [ ] Tabelas têm dual widths (columnWidths + cell width)
- [ ] Imagens têm o parâmetro `type` definido
- [ ] TOC usa HeadingLevel (não custom styles)
- [ ] Heading styles incluem outlineLevel (necessário pro TOC)
- [ ] Nenhum unicode bullet foi usado (tudo via numbering config)
- [ ] Smart quotes usadas para tipografia profissional
- [ ] Arquivo não sobrescreveu original sem confirmação
```

## Integrações

| Skill | Quando usar juntas |
|-------|-------------------|
| **pdf** | Converter .docx para PDF (`soffice --convert-to pdf`), ou extrair conteúdo de PDF para gerar .docx |
| **pptx** | Quando o conteúdo do documento também precisa virar apresentação, ou vice-versa |
| **xlsx** | Quando tabelas vêm de planilhas ou dados do documento vão para Excel |
| **comunicacao-clientes** | Quando o documento é um entregável pra cliente (proposta, relatório) — a skill ajuda no tom |
| **maestro** | Quando o pedido envolve múltiplos formatos (ex: "gera relatório em Word e PDF") — maestro orquestra |

## Quando NÃO Usar Esta Skill

- **PDF puro** — use a skill `pdf` (pypdf, pdfplumber)
- **Google Docs** — esta skill gera .docx local, não interage com Google Docs API
- **Planilhas/tabelas de dados** — use `xlsx` mesmo que o usuário diga "documento com tabela"
- **Apresentações** — use `pptx`
- **Markdown/texto simples** — não precisa de skill, Claude já faz nativamente
- **Edição de PDF existente** — use `pdf`, não converta para .docx e de volta

## Dependências

- **pandoc**: Extração de texto
- **docx**: `npm install -g docx` (documentos novos)
- **LibreOffice**: Conversão PDF (auto-configurado via `scripts/office/soffice.py`)
- **Poppler**: `pdftoppm` para imagens
