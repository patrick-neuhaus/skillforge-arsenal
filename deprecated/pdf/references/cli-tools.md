# CLI Tools — Referencia Detalhada

## pdftotext (poppler-utils)

```bash
# Extrair texto
pdftotext input.pdf output.txt

# Preservar layout
pdftotext -layout input.pdf output.txt

# Paginas especificas
pdftotext -f 1 -l 5 input.pdf output.txt  # Paginas 1-5

# Bounding box com coordenadas (essencial pra dados estruturados)
pdftotext -bbox-layout document.pdf output.xml
```

## qpdf

### Merge e Split
```bash
# Merge PDFs
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf

# Split paginas
qpdf input.pdf --pages . 1-5 -- pages1-5.pdf
qpdf input.pdf --pages . 6-10 -- pages6-10.pdf

# Split em grupos
qpdf --split-pages=3 input.pdf output_group_%02d.pdf

# Paginas especificas com ranges complexos
qpdf input.pdf --pages input.pdf 1,3-5,8,10-end -- extracted.pdf

# Merge paginas especificas de multiplos PDFs
qpdf --empty --pages doc1.pdf 1-3 doc2.pdf 5-7 doc3.pdf 2,4 -- combined.pdf
```

### Rotacionar
```bash
qpdf input.pdf output.pdf --rotate=+90:1  # Rotacionar pagina 1 em 90 graus
```

### Criptografia
```bash
# Proteger com senha + permissoes especificas
qpdf --encrypt user_pass owner_pass 256 --print=none --modify=none -- input.pdf encrypted.pdf

# Verificar status de criptografia
qpdf --show-encryption encrypted.pdf

# Remover senha (requer a senha)
qpdf --password=mypassword --decrypt encrypted.pdf decrypted.pdf
```

### Otimizacao e Reparo
```bash
# Otimizar pra web (linearize pra streaming)
qpdf --linearize input.pdf optimized.pdf

# Remover objetos nao usados e comprimir
qpdf --optimize-level=all input.pdf compressed.pdf

# Tentar reparar PDF corrompido
qpdf --check input.pdf
qpdf --fix-qdf damaged.pdf repaired.pdf

# Mostrar estrutura detalhada pra debug
qpdf --show-all-pages input.pdf > structure.txt
```

## pdftk

```bash
# Merge
pdftk file1.pdf file2.pdf cat output merged.pdf

# Split (burst = uma pagina por arquivo)
pdftk input.pdf burst

# Rotacionar
pdftk input.pdf rotate 1east output rotated.pdf
```

## poppler-utils — Imagens

### Extrair imagens embarcadas
```bash
# Extrair como JPEG
pdfimages -j input.pdf output_prefix
# Resultado: output_prefix-000.jpg, output_prefix-001.jpg, etc.

# Extrair com metadata
pdfimages -j -p document.pdf page_images

# Listar info das imagens sem extrair
pdfimages -list document.pdf

# Extrair no formato original
pdfimages -all document.pdf images/img
```

### Converter PDF para imagens
```bash
# PNG com resolucao especifica
pdftoppm -png -r 300 document.pdf output_prefix

# Range de paginas em alta resolucao
pdftoppm -png -r 600 -f 1 -l 3 document.pdf high_res_pages

# JPEG com qualidade customizada
pdftoppm -jpeg -jpegopt quality=85 -r 200 document.pdf jpeg_output
```
