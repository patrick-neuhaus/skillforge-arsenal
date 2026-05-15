---
name: pptx
description: "Cria, edita, lê, analisa, converte e inspeciona apresentações PowerPoint (.pptx). Gera decks profissionais do zero ou a partir de templates, extrai texto e dados de slides, faz QA visual automatizado, combina e reestrutura apresentações. Use quando: criar apresentação, montar deck, pitch deck, slides, editar pptx, extrair texto de apresentação, converter slides pra imagens, fazer QA visual, criar do zero com PptxGenJS, editar template XML. Triggers: 'deck', 'slides', 'apresentação', 'presentation', '.pptx', 'pitch deck', 'slide deck', 'montar apresentação', 'criar slides'. NÃO use para PDFs (use pdf), planilhas (use xlsx), ou documentos Word (use docx)."
license: Proprietary. LICENSE.txt has complete terms
---

# PPTX Skill

IRON LAW: NUNCA crie slides sem perguntar sobre a audiência e o propósito primeiro. Um pitch de vendas e uma revisão técnica precisam de estruturas completamente diferentes.

## Quick Reference

| Tarefa | Guia |
|--------|------|
| Ler/analisar conteúdo | `python -m markitdown presentation.pptx` |
| Editar ou criar de template | Load [editing.md](editing.md) |
| Criar do zero | Load [pptxgenjs.md](pptxgenjs.md) |
| Design e paletas | Load [references/design-guide.md](references/design-guide.md) |
| QA visual | Load [references/qa-visual.md](references/qa-visual.md) |

## Checklist do Workflow

```
PPTX Skill Progress:

- [ ] 1. Entender o contexto ⚠️ REQUIRED
  - [ ] 1.1 Quem é a audiência? (cliente, diretoria, técnico, investidor)
  - [ ] 1.2 Qual o propósito? (vender, ensinar, reportar, convencer)
  - [ ] 1.3 Existe template/marca? (cores, logo, guideline)
  - [ ] 1.4 Quantos slides? (estimativa)
  - [ ] 1.5 Conteúdo: tem texto pronto ou precisa criar?
- [ ] 2. Planejar estrutura
  - [ ] 2.1 Definir roteiro de slides (título → problema → solução → CTA)
  - [ ] 2.2 Escolher paleta de cores. Load `references/design-guide.md`
  - [ ] 2.3 Escolher fluxo: template (editing.md) ou do zero (pptxgenjs.md)?
  - [ ] ⛔ GATE: Confirmar estrutura com o usuário antes de gerar
- [ ] 3. Construir (em waves)
  - [ ] 3.1 Wave 1: Estrutura + conteúdo principal
  - [ ] 3.2 Wave 2: Design, ícones, gráficos, polish visual
  - [ ] 3.3 Wave 3: QA visual completo. Load `references/qa-visual.md`
- [ ] 4. QA ⚠️ REQUIRED
  - [ ] 4.1 Conteúdo: markitdown → verificar texto, ordem, typos
  - [ ] 4.2 Visual: converter pra imagens → subagent review
  - [ ] 4.3 Fix + re-verify (mínimo 1 ciclo)
  - [ ] ⛔ GATE: Confirmar com usuário antes de sobrescrever arquivo original
- [ ] 5. Entregar
  - [ ] 5.1 Rodar pre-delivery checklist
  - [ ] 5.2 Nomear arquivo corretamente
```

## Leitura de Conteúdo

```bash
# Extração de texto
python -m markitdown presentation.pptx

# Overview visual (grid de thumbnails)
python scripts/thumbnail.py presentation.pptx

# XML bruto
python scripts/office/unpack.py presentation.pptx unpacked/
```

## Workflow de Edição

**Load [editing.md](editing.md) para detalhes completos.**

1. Analisar template com `thumbnail.py`
2. Unpack → manipular slides → editar conteúdo → clean → pack

## Criação do Zero

**Load [pptxgenjs.md](pptxgenjs.md) para detalhes completos.**

Usar quando não há template ou apresentação de referência disponível.

## Ideias de Design

**Load [references/design-guide.md](references/design-guide.md)** para paletas de cores, tipografia, layouts e regras visuais.

Resumo rápido:
- **Paleta audaciosa e específica pro tema** — se trocar as cores pra outra apresentação e "funcionar", você não foi específico o bastante
- **Dominância, não igualdade** — uma cor domina (60-70%), 1-2 de suporte, 1 de acento
- **Todo slide precisa de elemento visual** — imagem, gráfico, ícone ou shape. Slides só de texto são esquecíveis
- **Nunca use linhas de acento abaixo de títulos** — marca registrada de slide gerado por IA

## Conversão para Imagens

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
rm -f slide-*.jpg
pdftoppm -jpeg -r 150 output.pdf slide
ls -1 "$PWD"/slide-*.jpg
```

Passe os caminhos absolutos diretamente para a ferramenta de visualização. O `rm` limpa imagens de rodadas anteriores.

**Após correções, rode os 4 comandos novamente** — o PDF precisa ser regenerado do `.pptx` editado.

## Confirmation Gates

⛔ **Antes de sobrescrever arquivo existente:** "O arquivo [nome] já existe. Confirma substituição?"

⛔ **Antes de gerar slides:** "Confirma a estrutura proposta (X slides, tema Y, audiência Z) antes de eu começar?"

⛔ **Antes de aplicar design radical:** "Vou usar [paleta/estilo]. Quer ver preview de 1-2 slides antes de eu fazer todos?"

## Anti-Patterns

| Anti-pattern | Por que é ruim | O que fazer |
|---|---|---|
| Mesmo layout em todos os slides | Apresentação monótona, audiência desliga | Variar: colunas, cards, callouts, imagens |
| Texto centralizado no body | Parece amador, difícil de ler | Left-align parágrafos e listas; centralizar só títulos |
| Paleta genérica azul | Sem identidade, parece template gratuito | Cores específicas pro tema/marca |
| Slides só de texto | Esquecíveis, sem impacto visual | Sempre ter imagem, ícone, gráfico ou shape |
| Pular QA visual | "Funciona no código" ≠ "funciona no slide" | Converter pra imagem + subagent review |
| Linhas de acento sob títulos | Marca de slide AI-generated | Whitespace ou cor de fundo |
| Unicode bullets (•) | Cria bullets duplos no PowerPoint | Usar `bullet: true` (PptxGenJS) ou `<a:buChar>` (XML) |
| Reusar objetos de opção | PptxGenJS muta objetos in-place, corrompe o 2o uso | Factory function `() => ({...})` pra cada chamada |
| Ignorar audiência | Pitch de vendas ≠ review técnico | Perguntar propósito antes de criar |

## Pre-Delivery Checklist

Antes de considerar a apresentação pronta:

- [ ] Todos os slides revisados com markitdown (sem placeholder text)
- [ ] QA visual feito (converter pra imagens + subagent)
- [ ] Mínimo 1 ciclo de fix + re-verify completo
- [ ] Layouts variados (não repetir o mesmo em slides consecutivos)
- [ ] Paleta consistente em todos os slides
- [ ] Tipografia: títulos 36pt+, body 14-16pt, captions 10-12pt
- [ ] Margens mínimas de 0.5" respeitadas
- [ ] Sem texto cortado ou overflow
- [ ] Contraste adequado (texto E ícones vs fundo)
- [ ] Speaker notes adicionadas (se solicitado)
- [ ] Nome do arquivo descritivo

## Quando NÃO Usar Esta Skill

- **PDF puro** → use `pdf`
- **Documento Word** → use `docx`
- **Planilha/dados tabulares** → use `xlsx`
- **Só extrair texto de PDF que era apresentação** → use `pdf`
- **Google Slides** → esta skill é pra .pptx local
- **Confuso sobre qual skill usar** → invoque `maestro`

## Integração

| Skill | Quando combinar |
|-------|----------------|
| `pdf` | Converter apresentação pra PDF final. Ou extrair conteúdo de PDF pra montar slides. |
| `docx` | Conteúdo vem de um Word doc. Ou gerar handout/resumo da apresentação em Word. |
| `xlsx` | Dados de planilha viram gráficos nos slides. Ou exportar tabela da apresentação. |
| `maestro` | Projeto envolve múltiplos formatos. Maestro orquestra a sequência. |
| `prompt-engineer` | Gerar conteúdo dos slides com IA antes de montar. |
| `product-discovery-prd` | Apresentação é parte de discovery — PRD vira deck de pitch. |

## Referências

| Arquivo | Conteúdo |
|---------|----------|
| [editing.md](editing.md) | Workflow completo de edição via template (unpack/pack/XML) |
| [pptxgenjs.md](pptxgenjs.md) | Tutorial PptxGenJS: texto, shapes, imagens, ícones, charts, masters |
| [references/design-guide.md](references/design-guide.md) | Paletas de cores, tipografia, layouts, spacing, erros comuns |
| [references/qa-visual.md](references/qa-visual.md) | Processo de QA visual completo com subagents |

## Dependências

- `pip install "markitdown[pptx]"` — extração de texto
- `pip install Pillow` — grids de thumbnails
- `npm install -g pptxgenjs` — criação do zero
- LibreOffice (`soffice`) — conversão pra PDF (auto-configurado via `scripts/office/soffice.py`)
- Poppler (`pdftoppm`) — PDF pra imagens
