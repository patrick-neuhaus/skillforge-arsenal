# Edicao de Documentos DOCX Existentes via XML

Um .docx e um arquivo ZIP contendo XMLs. Para editar, desempacote, edite o XML, reempacote.

**Siga os 3 passos em ordem.**

---

## Step 1: Unpack

```bash
python scripts/office/unpack.py document.docx unpacked/
```

Extrai XML, pretty-prints, mescla runs adjacentes e converte smart quotes para entidades XML (`&#x201C;` etc.) para sobreviverem a edicao. Use `--merge-runs false` para pular merge de runs.

---

## Step 2: Editar XML

Edite arquivos em `unpacked/word/`.

**Use "Claude" como autor** para tracked changes e comentarios, a menos que o usuario peca outro nome.

**Use a ferramenta Edit diretamente para string replacement. NAO escreva scripts Python.** Scripts introduzem complexidade desnecessaria. A ferramenta Edit mostra exatamente o que esta sendo substituido.

**CRITICAL: Use smart quotes para conteudo novo.** Quando adicionar texto com apostrofos ou aspas, use entidades XML:

```xml
<!-- Use these entities for professional typography -->
<w:t>Here&#x2019;s a quote: &#x201C;Hello&#x201D;</w:t>
```

| Entidade | Caractere |
|----------|-----------|
| `&#x2018;` | ' (left single) |
| `&#x2019;` | ' (right single / apostrophe) |
| `&#x201C;` | " (left double) |
| `&#x201D;` | " (right double) |

### Adicionando Comentarios

Use `comment.py` para lidar com boilerplate em multiplos XMLs (texto deve ser XML pre-escaped):

```bash
python scripts/comment.py unpacked/ 0 "Comment text with &amp; and &#x2019;"
python scripts/comment.py unpacked/ 1 "Reply text" --parent 0  # reply to comment 0
python scripts/comment.py unpacked/ 0 "Text" --author "Custom Author"  # custom author name
```

Depois adicione markers ao document.xml (veja secao Comments abaixo).

---

## Step 3: Pack

```bash
python scripts/office/pack.py unpacked/ output.docx --original document.docx
```

Valida com auto-repair, condensa XML e cria DOCX. Use `--validate false` para pular.

**Auto-repair corrige:**
- `durableId` >= 0x7FFFFFFF (regenera ID valido)
- `xml:space="preserve"` faltando em `<w:t>` com whitespace

**Auto-repair NAO corrige:**
- XML malformado, nesting invalido, relationships faltando, violacoes de schema

---

## Pitfalls Comuns

- **Substitua elementos `<w:r>` inteiros**: Ao adicionar tracked changes, substitua todo o bloco `<w:r>...</w:r>` com `<w:del>...<w:ins>...` como siblings. Nao injete tags de tracked change dentro de um run.
- **Preserve formatacao `<w:rPr>`**: Copie o bloco `<w:rPr>` do run original para seus runs de tracked change para manter bold, font size, etc.

---

## XML Reference

### Schema Compliance

- **Ordem dos elementos em `<w:pPr>`**: `<w:pStyle>`, `<w:numPr>`, `<w:spacing>`, `<w:ind>`, `<w:jc>`, `<w:rPr>` por ultimo
- **Whitespace**: Adicione `xml:space="preserve"` a `<w:t>` com espacos no inicio/fim
- **RSIDs**: Devem ser hex de 8 digitos (ex: `00AB1234`)

---

### Tracked Changes

**Insercao:**
```xml
<w:ins w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
  <w:r><w:t>inserted text</w:t></w:r>
</w:ins>
```

**Delecao:**
```xml
<w:del w:id="2" w:author="Claude" w:date="2025-01-01T00:00:00Z">
  <w:r><w:delText>deleted text</w:delText></w:r>
</w:del>
```

**Dentro de `<w:del>`**: Use `<w:delText>` ao inves de `<w:t>`, e `<w:delInstrText>` ao inves de `<w:instrText>`.

**Edicoes minimas** — marque apenas o que muda:
```xml
<!-- Change "30 days" to "60 days" -->
<w:r><w:t>The term is </w:t></w:r>
<w:del w:id="1" w:author="Claude" w:date="...">
  <w:r><w:delText>30</w:delText></w:r>
</w:del>
<w:ins w:id="2" w:author="Claude" w:date="...">
  <w:r><w:t>60</w:t></w:r>
</w:ins>
<w:r><w:t> days.</w:t></w:r>
```

**Deletando paragrafos/itens de lista inteiros** — quando remover TODO o conteudo de um paragrafo, marque tambem o paragraph mark como deletado para que ele se mescle com o proximo. Adicione `<w:del/>` dentro de `<w:pPr><w:rPr>`:

```xml
<w:p>
  <w:pPr>
    <w:numPr>...</w:numPr>  <!-- list numbering if present -->
    <w:rPr>
      <w:del w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z"/>
    </w:rPr>
  </w:pPr>
  <w:del w:id="2" w:author="Claude" w:date="2025-01-01T00:00:00Z">
    <w:r><w:delText>Entire paragraph content being deleted...</w:delText></w:r>
  </w:del>
</w:p>
```

Sem o `<w:del/>` em `<w:pPr><w:rPr>`, aceitar changes deixa um paragrafo/item de lista vazio.

**Rejeitando insercao de outro autor** — aninhe delecao dentro da insercao:
```xml
<w:ins w:author="Jane" w:id="5">
  <w:del w:author="Claude" w:id="10">
    <w:r><w:delText>their inserted text</w:delText></w:r>
  </w:del>
</w:ins>
```

**Restaurando delecao de outro autor** — adicione insercao depois (nao modifique a delecao):
```xml
<w:del w:author="Jane" w:id="5">
  <w:r><w:delText>deleted text</w:delText></w:r>
</w:del>
<w:ins w:author="Claude" w:id="10">
  <w:r><w:t>deleted text</w:t></w:r>
</w:ins>
```

---

### Comments

Apos rodar `comment.py` (Step 2), adicione markers ao document.xml. Para replies, use flag `--parent` e aninhe markers dentro do pai.

**CRITICAL: `<w:commentRangeStart>` e `<w:commentRangeEnd>` sao siblings de `<w:r>`, NUNCA dentro de `<w:r>`.**

```xml
<!-- Comment markers are direct children of w:p, never inside w:r -->
<w:commentRangeStart w:id="0"/>
<w:del w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
  <w:r><w:delText>deleted</w:delText></w:r>
</w:del>
<w:r><w:t> more text</w:t></w:r>
<w:commentRangeEnd w:id="0"/>
<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="0"/></w:r>

<!-- Comment 0 with reply 1 nested inside -->
<w:commentRangeStart w:id="0"/>
  <w:commentRangeStart w:id="1"/>
  <w:r><w:t>text</w:t></w:r>
  <w:commentRangeEnd w:id="1"/>
<w:commentRangeEnd w:id="0"/>
<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="0"/></w:r>
<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="1"/></w:r>
```

---

### Imagens via XML

1. Adicione arquivo de imagem a `word/media/`
2. Adicione relationship a `word/_rels/document.xml.rels`:
```xml
<Relationship Id="rId5" Type=".../image" Target="media/image1.png"/>
```
3. Adicione content type a `[Content_Types].xml`:
```xml
<Default Extension="png" ContentType="image/png"/>
```
4. Referencie no document.xml:
```xml
<w:drawing>
  <wp:inline>
    <wp:extent cx="914400" cy="914400"/>  <!-- EMUs: 914400 = 1 inch -->
    <a:graphic>
      <a:graphicData uri=".../picture">
        <pic:pic>
          <pic:blipFill><a:blip r:embed="rId5"/></pic:blipFill>
        </pic:pic>
      </a:graphicData>
    </a:graphic>
  </wp:inline>
</w:drawing>
```
