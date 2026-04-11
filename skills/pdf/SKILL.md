---
name: pdf
description: "Create, read, edit, merge, split, convert, extract, generate, combine, and manipulate PDF files. Use this skill whenever the user wants to do anything with PDFs — including extracting text or tables, merging multiple PDFs into one, splitting pages apart, rotating, adding watermarks, creating new PDFs from scratch, filling forms (fillable or non-fillable), encrypting/decrypting, extracting images, OCR on scanned documents, cropping, and batch processing. Triggers EN: 'PDF', '.pdf', 'merge PDFs', 'split PDF', 'extract text from PDF', 'fill PDF form', 'create PDF', 'convert to PDF', 'PDF watermark', 'OCR PDF'. Triggers PT-BR: 'juntar PDFs', 'dividir PDF', 'extrair texto do PDF', 'preencher formulário PDF', 'criar PDF', 'converter pra PDF', 'marca d'água PDF', 'OCR em PDF', 'combinar PDFs', 'editar PDF', 'manipular PDF', 'gerar PDF'."
license: Proprietary. LICENSE.txt has complete terms
---

# PDF — Processamento Completo de PDFs

**Iron Law:** Nunca sobrescreva o PDF original sem criar backup primeiro. Operações em PDF são destrutivas — sempre confirme antes de gravar. `cp original.pdf original.backup.pdf` ANTES de qualquer escrita.

## Quick Reference

| Tarefa | Ferramenta | Referência |
|--------|-----------|------------|
| Ler/extrair texto | pdfplumber | references/python-libs.md |
| Extrair tabelas | pdfplumber + pandas | references/python-libs.md |
| Merge PDFs | pypdf | references/python-libs.md |
| Split PDF | pypdf | references/python-libs.md |
| Criar PDF novo | reportlab | references/python-libs.md |
| Rotacionar páginas | pypdf | references/python-libs.md |
| Watermark | pypdf | references/python-libs.md |
| OCR (scanned) | pytesseract + pdf2image | references/python-libs.md |
| Extrair imagens | pdfimages (poppler) | references/cli-tools.md |
| Criptografia | pypdf ou qpdf | references/cli-tools.md |
| Preencher formulário | scripts/ (ver FORMS.md) | FORMS.md |
| Operações CLI | qpdf, pdftk, pdftotext | references/cli-tools.md |
| JavaScript (pdf-lib) | pdf-lib, pdfjs-dist | references/javascript-libs.md |
| Render PDF to image | pypdfium2 | references/javascript-libs.md |
| Batch processing | pypdf + logging | references/workflows-avancados.md |
| Otimização/reparo | qpdf | references/cli-tools.md |
| Troubleshooting | Múltiplas | references/workflows-avancados.md |

## Workflow

```
PDF Processing Progress:

- [ ] Phase 1: Identificar Operação ⚠️ REQUIRED
  - [ ] 1.1 Qual operação? (ler, criar, editar, merge, split, form, OCR, etc.)
  - [ ] 1.2 PDF existe? Verificar se arquivo está acessível
  - [ ] 1.3 PDF tem senha? Verificar criptografia
  - [ ] 1.4 Escolher ferramenta certa (ver Quick Reference)
- [ ] Phase 2: Preparar ⛔ BLOCKING
  - [ ] ⛔ GATE: Criar backup do PDF original antes de qualquer modificação
  - [ ] 2.1 Instalar dependências necessárias
  - [ ] 2.2 Se formulário: rodar check_fillable_fields primeiro
  - [ ] 2.3 Se OCR: verificar se pytesseract + poppler estão instalados
- [ ] Phase 3: Executar
  - [ ] 3.1 Carregar referência relevante (Load references/X.md)
  - [ ] 3.2 Implementar operação
  - [ ] 3.3 Se formulário: seguir FORMS.md passo a passo
- [ ] Phase 4: Validar ⛔ BLOCKING
  - [ ] ⛔ GATE: Confirmar com usuário antes de sobrescrever arquivo original
  - [ ] 4.1 Verificar output (abrir, contar páginas, checar texto)
  - [ ] 4.2 Se formulário: converter output pra imagem e validar posicionamento
  - [ ] 4.3 Confirmar que backup existe
```

## Quick Start

```python
from pypdf import PdfReader, PdfWriter

# Ler PDF
reader = PdfReader("document.pdf")
print(f"Páginas: {len(reader.pages)}")

# Extrair texto
text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Operações Básicas (pypdf)

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

### Rotacionar Páginas
```python
reader = PdfReader("input.pdf")
writer = PdfWriter()
page = reader.pages[0]
page.rotate(90)  # 90 graus no sentido horário
writer.add_page(page)
with open("rotated.pdf", "wb") as output:
    writer.write(output)
```

## Extração de Texto e Tabelas (pdfplumber)

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

## Criação de PDFs (reportlab)

**IMPORTANTE**: Nunca use caracteres Unicode de subscrito/sobrescrito (tipo 0-9 pequenos) no reportlab — as fontes built-in não suportam e renderizam como caixas pretas. Use tags `<sub>` e `<super>` em objetos Paragraph.

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []
story.append(Paragraph("Título do Relatório", styles['Title']))
story.append(Spacer(1, 12))
story.append(Paragraph("Conteúdo aqui. " * 20, styles['Normal']))
doc.build(story)
```

## Formulários PDF

Se precisar preencher formulário PDF, leia FORMS.md e siga as instruções passo a passo. O processo depende de o PDF ter campos preenchíveis ou não.

## Progressive Loading — Referências Detalhadas

Para código completo e exemplos avançados, carregue a referência relevante:

- **Load `references/python-libs.md`** — pypdf, pdfplumber, reportlab, pytesseract, pypdfium2
- **Load `references/cli-tools.md`** — pdftotext, qpdf, pdftk, pdfimages, poppler-utils
- **Load `references/javascript-libs.md`** — pdf-lib, pdfjs-dist, operações JS
- **Load `references/workflows-avancados.md`** — batch processing, otimização, troubleshooting, performance

## Anti-Patterns

| Anti-Pattern | Por que é ruim | Faça isso |
|-------------|---------------|-----------|
| Sobrescrever PDF original sem backup | Operação destrutiva irreversível | `cp original.pdf original.backup.pdf` primeiro |
| Usar `pypdf.extract_text()` pra PDFs grandes | Lento e impreciso | Use `pdftotext` CLI ou pdfplumber |
| Carregar PDF inteiro na memória | Estoura RAM em arquivos grandes | Processe em chunks (ver workflows-avancados.md) |
| Unicode subscript/superscript no reportlab | Renderiza como caixas pretas | Use tags `<sub>` e `<super>` em Paragraph |
| Ignorar que PDF é scanned/imagem | extract_text() retorna vazio | Detecte e use OCR (pytesseract) |
| Pular validação de formulário preenchido | Texto fora de posição | Converta output pra imagem e verifique |
| Usar PyMuPDF/fitz sem checar licença | AGPL — contaminação viral | Use pypdfium2 (Apache/BSD) como alternativa |
| Tentar editar texto inline no PDF | PDF não é formato editável | Extraia, modifique, recrie |
| Rodar OCR sem poppler instalado | pdf2image depende de poppler | `apt install poppler-utils` ou equivalente |

## Pre-Delivery Checklist

Antes de entregar qualquer resultado PDF ao usuário:

- [ ] Output PDF abre corretamente?
- [ ] Número de páginas está correto?
- [ ] Texto extraído/inserido está legível e bem posicionado?
- [ ] Backup do original existe (se houve modificação)?
- [ ] Se formulário: campos preenchidos estão nas posições corretas?
- [ ] Se merge: ordem das páginas está correta?
- [ ] Se criptografia: senha funciona pra abrir?
- [ ] Arquivo de saída tem tamanho razoável (não corrompido)?

## Quando NÃO usar esta skill

- **Editar texto inline no PDF** — PDF não é formato editável. Extraia o conteúdo, modifique, e recrie. Ou use a skill `docx` se o formato final puder ser Word.
- **Criar documento formatado com estilos complexos** — Use `docx` (Word) ou `pptx` (apresentação) e converta pra PDF depois.
- **Planilhas/dados tabulares como output principal** — Use `xlsx`. Se precisa extrair tabelas DE um PDF, aí sim use esta skill.
- **Visualização/apresentação de dados** — Use `pptx` pra slides.
- **O usuário quer Google Docs/Sheets** — Esta skill é pra arquivos locais .pdf.

## Integração com Outras Skills

| Skill | Quando usar junto |
|-------|-------------------|
| `docx` | Criar doc Word → converter pra PDF (melhor pra docs com estilos complexos) |
| `pptx` | Apresentação → export PDF, ou extrair conteúdo de PDF pra slides |
| `xlsx` | Extrair tabelas de PDF → Excel, ou dados de planilha → PDF report |
| `sdd` | Quando a feature envolve processamento de PDF como parte de um sistema maior |
| `maestro` | Quando não sabe qual skill usar — maestro roteia pra cá se envolver PDF |

## Dependências

| Ferramenta | Instalação | Uso |
|-----------|-----------|-----|
| pypdf | `pip install pypdf` | Merge, split, rotate, encrypt |
| pdfplumber | `pip install pdfplumber` | Extrair texto e tabelas |
| reportlab | `pip install reportlab` | Criar PDFs novos |
| pytesseract | `pip install pytesseract` + Tesseract instalado | OCR |
| pdf2image | `pip install pdf2image` + poppler | Converter PDF → imagem |
| pypdfium2 | `pip install pypdfium2` | Render PDF, alternativa a PyMuPDF |
| poppler-utils | `apt install poppler-utils` | pdftotext, pdfimages, pdftoppm |
| qpdf | `apt install qpdf` | CLI: merge, split, encrypt, repair |
| pandas | `pip install pandas` | Processar tabelas extraídas |

## Licenças

- pypdf: BSD | pdfplumber: MIT | pypdfium2: Apache/BSD | reportlab: BSD
- poppler-utils: GPL-2 | qpdf: Apache | pdf-lib: MIT | pdfjs-dist: Apache
- **ATENÇÃO**: PyMuPDF/fitz é AGPL. Use pypdfium2 como alternativa segura.
