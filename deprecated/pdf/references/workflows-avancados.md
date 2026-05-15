# Workflows Avancados — Referencia Detalhada

## Batch Processing com Error Handling

```python
import os
import glob
from pypdf import PdfReader, PdfWriter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def batch_process_pdfs(input_dir, operation='merge'):
    pdf_files = glob.glob(os.path.join(input_dir, "*.pdf"))

    if operation == 'merge':
        writer = PdfWriter()
        for pdf_file in pdf_files:
            try:
                reader = PdfReader(pdf_file)
                for page in reader.pages:
                    writer.add_page(page)
                logger.info(f"Processed: {pdf_file}")
            except Exception as e:
                logger.error(f"Failed to process {pdf_file}: {e}")
                continue

        with open("batch_merged.pdf", "wb") as output:
            writer.write(output)

    elif operation == 'extract_text':
        for pdf_file in pdf_files:
            try:
                reader = PdfReader(pdf_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()

                output_file = pdf_file.replace('.pdf', '.txt')
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                logger.info(f"Extracted text from: {pdf_file}")

            except Exception as e:
                logger.error(f"Failed to extract text from {pdf_file}: {e}")
                continue
```

## Extracao de Figuras/Imagens

### Metodo 1: pdfimages (mais rapido)
```bash
pdfimages -all document.pdf images/img
```

### Metodo 2: pypdfium2 + Image Processing
```python
import pypdfium2 as pdfium
from PIL import Image
import numpy as np

def extract_figures(pdf_path, output_dir):
    pdf = pdfium.PdfDocument(pdf_path)

    for page_num, page in enumerate(pdf):
        # Render em alta resolucao
        bitmap = page.render(scale=3.0)
        img = bitmap.to_pil()

        # Converter pra numpy pra processamento
        img_array = np.array(img)

        # Deteccao simples de figuras (regioes nao-brancas)
        mask = np.any(img_array != [255, 255, 255], axis=2)

        # Salvar pagina renderizada
        img.save(f"{output_dir}/page_{page_num+1}.png")
```

---

## Performance — Dicas de Otimizacao

### 1. PDFs Grandes
- Use streaming ao inves de carregar PDF inteiro na memoria
- Use `qpdf --split-pages` pra dividir arquivos grandes
- Processe paginas individualmente com pypdfium2

### 2. Extracao de Texto
- `pdftotext -bbox-layout` e o mais rapido pra texto puro
- Use pdfplumber pra dados estruturados e tabelas
- Evite `pypdf.extract_text()` pra documentos muito grandes

### 3. Extracao de Imagens
- `pdfimages` e muito mais rapido que renderizar paginas
- Use baixa resolucao pra previews, alta pra output final

### 4. Formularios
- pdf-lib mantem estrutura de formulario melhor que a maioria das alternativas
- Pre-valide campos antes de processar

### 5. Gerenciamento de Memoria
```python
# Processar PDFs em chunks
def process_large_pdf(pdf_path, chunk_size=10):
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)

    for start_idx in range(0, total_pages, chunk_size):
        end_idx = min(start_idx + chunk_size, total_pages)
        writer = PdfWriter()

        for i in range(start_idx, end_idx):
            writer.add_page(reader.pages[i])

        with open(f"chunk_{start_idx//chunk_size}.pdf", "wb") as output:
            writer.write(output)
```

---

## Troubleshooting

### PDFs Criptografados
```python
from pypdf import PdfReader

try:
    reader = PdfReader("encrypted.pdf")
    if reader.is_encrypted:
        reader.decrypt("password")
except Exception as e:
    print(f"Failed to decrypt: {e}")
```

### PDFs Corrompidos
```bash
# Verificar integridade
qpdf --check corrupted.pdf

# Tentar reparar
qpdf --replace-input corrupted.pdf
```

### Texto Nao Extraido (PDF scanned/imagem)
```python
import pytesseract
from pdf2image import convert_from_path

def extract_text_with_ocr(pdf_path):
    """Fallback pra OCR quando extract_text() retorna vazio."""
    images = convert_from_path(pdf_path)
    text = ""
    for i, image in enumerate(images):
        text += pytesseract.image_to_string(image)
    return text
```

### Diagnostico: PDF e texto ou imagem?
```python
from pypdf import PdfReader

def is_scanned_pdf(pdf_path):
    """Verifica se o PDF e scanned (sem texto extraivel)."""
    reader = PdfReader(pdf_path)
    for page in reader.pages[:3]:  # Checar primeiras 3 paginas
        text = page.extract_text()
        if text and text.strip():
            return False
    return True
```
