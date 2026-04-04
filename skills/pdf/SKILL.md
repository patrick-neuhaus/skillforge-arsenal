---
name: pdf
description: "Create, read, edit, merge, split, convert, extract, generate, combine, and manipulate PDF files. Use this skill whenever the user wants to do anything with PDFs — including extracting text or tables, merging multiple PDFs into one, splitting pages apart, rotating, adding watermarks, creating new PDFs from scratch, filling forms (fillable or non-fillable), encrypting/decrypting, extracting images, OCR on scanned documents, cropping, and batch processing. Triggers EN: 'PDF', '.pdf', 'merge PDFs', 'split PDF', 'extract text from PDF', 'fill PDF form', 'create PDF', 'convert to PDF', 'PDF watermark', 'OCR PDF'. Triggers PT-BR: 'juntar PDFs', 'dividir PDF', 'extrair texto do PDF', 'preencher formulario PDF', 'criar PDF', 'converter pra PDF', 'marca dagua PDF', 'OCR em PDF', 'combinar PDFs', 'editar PDF', 'manipular PDF', 'gerar PDF'."
license: Proprietary. LICENSE.txt has complete terms
---

# PDF — Processamento Completo de PDFs

IRON LAW: NUNCA sobrescreva o PDF original sem criar backup primeiro. Operacoes em PDF sao destrutivas — sempre confirme antes de gravar. `cp original.pdf original.backup.pdf` ANTES de qualquer escrita.

## Quick Reference

| Tarefa | Ferramenta | Referencia |
|--------|-----------|------------|
| Ler/extrair texto | pdfplumber | references/python-libs.md |
| Extrair tabelas | pdfplumber + pandas | references/python-libs.md |
| Merge PDFs | pypdf | references/python-libs.md |
| Split PDF | pypdf | references/python-libs.md |
| Criar PDF novo | reportlab | references/python-libs.md |
| Rotacionar paginas | pypdf | references/python-libs.md |
| Watermark | pypdf | references/python-libs.md |
| OCR (scanned) | pytesseract + pdf2image | references/python-libs.md |
| Extrair imagens | pdfimages (poppler) | references/cli-tools.md |
| Criptografia | pypdf ou qpdf | references/cli-tools.md |
| Preencher formulario | scripts/ (ver FORMS.md) | FORMS.md |
| Operacoes CLI | qpdf, pdftk, pdftotext | references/cli-tools.md |
| JavaScript (pdf-lib) | pdf-lib, pdfjs-dist | references/javascript-libs.md |
| Render PDF to image | pypdfium2 | references/javascript-libs.md |
| Batch processing | pypdf + logging | references/workflows-avancados.md |
| Otimizacao/reparo | qpdf | references/cli-tools.md |
| Troubleshooting | Multiplas | references/workflows-avancados.md |

## Workflow

```
PDF Processing Progress:

- [ ] Phase 1: Identificar Operacao ⚠️ REQUIRED
  - [ ] 1.1 Qual operacao? (ler, criar, editar, merge, split, form, OCR, etc.)
  - [ ] 1.2 PDF existe? Verificar se arquivo esta acessivel
  - [ ] 1.3 PDF tem senha? Verificar criptografia
  - [ ] 1.4 Escolher ferramenta certa (ver Quick Reference)
- [ ] Phase 2: Preparar ⛔ BLOCKING
  - [ ] ⛔ GATE: Criar backup do PDF original antes de qualquer modificacao
  - [ ] 2.1 Instalar dependencias necessarias
  - [ ] 2.2 Se formulario: rodar check_fillable_fields primeiro
  - [ ] 2.3 Se OCR: verificar se pytesseract + poppler estao instalados
- [ ] Phase 3: Executar
  - [ ] 3.1 Carregar referencia relevante (Load references/X.md)
  - [ ] 3.2 Implementar operacao
  - [ ] 3.3 Se formulario: seguir FORMS.md passo a passo
- [ ] Phase 4: Validar ⛔ BLOCKING
  - [ ] ⛔ GATE: Confirmar com usuario antes de sobrescrever arquivo original
  - [ ] 4.1 Verificar output (abrir, contar paginas, checar texto)
  - [ ] 4.2 Se formulario: converter output pra imagem e validar posicionamento
  - [ ] 4.3 Confirmar que backup existe
```

## Quick Start

```python
from pypdf import PdfReader, PdfWriter

# Ler PDF
reader = PdfReader("document.pdf")
print(f"Paginas: {len(reader.pages)}")

# Extrair texto
text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Operacoes Basicas (pypdf)

### Merge PDFs
```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

### Split PDF
```python
reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as output:
        writer.write(output)
```

### Rotacionar Paginas
```python
reader = PdfReader("input.pdf")
writer = PdfWriter()
page = reader.pages[0]
page.rotate(90)  # 90 graus no sentido horario
writer.add_page(page)
with open("rotated.pdf", "wb") as output:
    writer.write(output)
```

## Extracao de Texto e Tabelas (pdfplumber)

```python
import pdfplumber

# Texto
with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)

# Tabelas -> Excel
import pandas as pd
with pdfplumber.open("document.pdf") as pdf:
    all_tables = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)
    if all_tables:
        combined_df = pd.concat(all_tables, ignore_index=True)
        combined_df.to_excel("extracted_tables.xlsx", index=False)
```

## Criacao de PDFs (reportlab)

**IMPORTANTE**: Nunca use caracteres Unicode de subscrito/sobrescrito (tipo 0-9 pequenos) no reportlab — as fontes built-in nao suportam e renderizam como caixas pretas. Use tags `<sub>` e `<super>` em objetos Paragraph.

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []
story.append(Paragraph("Titulo do Relatorio", styles['Title']))
story.append(Spacer(1, 12))
story.append(Paragraph("Conteudo aqui. " * 20, styles['Normal']))
doc.build(story)
```

## Formularios PDF

Se precisar preencher formulario PDF, leia FORMS.md e siga as instrucoes passo a passo. O processo depende de o PDF ter campos fillaveis ou nao.

## Progressive Loading — Referencias Detalhadas

Para codigo completo e exemplos avancados, carregue a referencia relevante:

- **Load `references/python-libs.md`** — pypdf, pdfplumber, reportlab, pytesseract, pypdfium2
- **Load `references/cli-tools.md`** — pdftotext, qpdf, pdftk, pdfimages, poppler-utils
- **Load `references/javascript-libs.md`** — pdf-lib, pdfjs-dist, operacoes JS
- **Load `references/workflows-avancados.md`** — batch processing, otimizacao, troubleshooting, performance

## Anti-Patterns

| Anti-Pattern | Por que e ruim | Faca isso |
|-------------|---------------|-----------|
| Sobrescrever PDF original sem backup | Operacao destrutiva irreversivel | `cp original.pdf original.backup.pdf` primeiro |
| Usar `pypdf.extract_text()` pra PDFs grandes | Lento e impreciso | Use `pdftotext` CLI ou pdfplumber |
| Carregar PDF inteiro na memoria | Estoura RAM em arquivos grandes | Processe em chunks (ver workflows-avancados.md) |
| Unicode subscript/superscript no reportlab | Renderiza como caixas pretas | Use tags `<sub>` e `<super>` em Paragraph |
| Ignorar que PDF e scanned/imagem | extract_text() retorna vazio | Detecte e use OCR (pytesseract) |
| Pular validacao de formulario preenchido | Texto fora de posicao | Converta output pra imagem e verifique |
| Usar PyMuPDF/fitz sem checar licenca | AGPL — contaminacao viral | Use pypdfium2 (Apache/BSD) como alternativa |
| Tentar editar texto inline no PDF | PDF nao e formato editavel | Extraia, modifique, recrie |
| Rodar OCR sem poppler instalado | pdf2image depende de poppler | `apt install poppler-utils` ou equivalente |

## Pre-Delivery Checklist

Antes de entregar qualquer resultado PDF ao usuario:

- [ ] Output PDF abre corretamente?
- [ ] Numero de paginas esta correto?
- [ ] Texto extraido/inserido esta legivel e bem posicionado?
- [ ] Backup do original existe (se houve modificacao)?
- [ ] Se formulario: campos preenchidos estao nas posicoes corretas?
- [ ] Se merge: ordem das paginas esta correta?
- [ ] Se criptografia: senha funciona pra abrir?
- [ ] Arquivo de saida tem tamanho razoavel (nao corrompido)?

## Quando NAO usar esta skill

- **Editar texto inline no PDF** — PDF nao e formato editavel. Extraia o conteudo, modifique, e recrie. Ou use a skill `docx` se o formato final puder ser Word.
- **Criar documento formatado com estilos complexos** — Use `docx` (Word) ou `pptx` (apresentacao) e converta pra PDF depois.
- **Planilhas/dados tabulares como output principal** — Use `xlsx`. Se precisa extrair tabelas DE um PDF, ai sim use esta skill.
- **Visualizacao/apresentacao de dados** — Use `pptx` pra slides.
- **O usuario quer Google Docs/Sheets** — Esta skill e pra arquivos locais .pdf.

## Integracao com Outras Skills

| Skill | Quando usar junto |
|-------|-------------------|
| `docx` | Criar doc Word → converter pra PDF (melhor pra docs com estilos complexos) |
| `pptx` | Apresentacao → export PDF, ou extrair conteudo de PDF pra slides |
| `xlsx` | Extrair tabelas de PDF → Excel, ou dados de planilha → PDF report |
| `sdd` | Quando a feature envolve processamento de PDF como parte de um sistema maior |
| `maestro` | Quando nao sabe qual skill usar — maestro roteia pra ca se envolver PDF |

## Dependencias

| Ferramenta | Instalacao | Uso |
|-----------|-----------|-----|
| pypdf | `pip install pypdf` | Merge, split, rotate, encrypt |
| pdfplumber | `pip install pdfplumber` | Extrair texto e tabelas |
| reportlab | `pip install reportlab` | Criar PDFs novos |
| pytesseract | `pip install pytesseract` + Tesseract instalado | OCR |
| pdf2image | `pip install pdf2image` + poppler | Converter PDF → imagem |
| pypdfium2 | `pip install pypdfium2` | Render PDF, alternativa a PyMuPDF |
| poppler-utils | `apt install poppler-utils` | pdftotext, pdfimages, pdftoppm |
| qpdf | `apt install qpdf` | CLI: merge, split, encrypt, repair |
| pandas | `pip install pandas` | Processar tabelas extraidas |

## Licencas

- pypdf: BSD | pdfplumber: MIT | pypdfium2: Apache/BSD | reportlab: BSD
- poppler-utils: GPL-2 | qpdf: Apache | pdf-lib: MIT | pdfjs-dist: Apache
- **ATENCAO**: PyMuPDF/fitz e AGPL. Use pypdfium2 como alternativa segura.
