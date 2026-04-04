# QA Visual de Apresentações

## Filosofia

**Assuma que existem problemas. Seu trabalho é encontrá-los.**

Seu primeiro render quase nunca está correto. Encare QA como uma caçada de bugs, não um passo de confirmação. Se você encontrou zero problemas na primeira inspeção, você não olhou direito.

## QA de Conteúdo

```bash
python -m markitdown output.pptx
```

Verifique: conteúdo faltando, typos, ordem errada.

**Quando usar templates, verifique texto placeholder restante:**

```bash
python -m markitdown output.pptx | grep -iE "\bx{3,}\b|lorem|ipsum|\bTODO|\[insert|this.*(page|slide).*layout"
```

Se o grep retornar resultados, corrija antes de declarar sucesso.

## QA Visual

**USE SUBAGENTS** — mesmo pra 2-3 slides. Você ficou olhando o código e vai ver o que espera, não o que está lá. Subagents têm olhos frescos.

Converta slides pra imagens (ver Conversão para Imagens no SKILL.md), depois use este prompt:

```
Visually inspect these slides. Assume there are issues — find them.

Look for:
- Overlapping elements (text through shapes, lines through words, stacked elements)
- Text overflow or cut off at edges/box boundaries
- Decorative lines positioned for single-line text but title wrapped to two lines
- Source citations or footers colliding with content above
- Elements too close (< 0.3" gaps) or cards/sections nearly touching
- Uneven gaps (large empty area in one place, cramped in another)
- Insufficient margin from slide edges (< 0.5")
- Columns or similar elements not aligned consistently
- Low-contrast text (e.g., light gray text on cream-colored background)
- Low-contrast icons (e.g., dark icons on dark backgrounds without a contrasting circle)
- Text boxes too narrow causing excessive wrapping
- Leftover placeholder content

For each slide, list issues or areas of concern, even if minor.

Read and analyze these images — run `ls -1 "$PWD"/slide-*.jpg` and use the exact absolute paths it prints:
1. <absolute-path>/slide-N.jpg — (Expected: [brief description])
2. <absolute-path>/slide-N.jpg — (Expected: [brief description])
...

Report ALL issues found, including minor ones.
```

## Loop de Verificação

1. Gerar slides → Converter pra imagens → Inspecionar
2. **Listar problemas encontrados** (se nenhum, olhe de novo mais criticamente)
3. Corrigir problemas
4. **Re-verificar slides afetados** — um fix frequentemente cria outro problema
5. Repetir até uma passagem completa não revelar novos problemas

**Não declare sucesso até completar pelo menos um ciclo de fix + re-verify.**

## Conversão para Imagens

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
rm -f slide-*.jpg
pdftoppm -jpeg -r 150 output.pdf slide
ls -1 "$PWD"/slide-*.jpg
```

O `rm` limpa imagens de rodadas anteriores. `pdftoppm` faz zero-pad baseado na contagem de páginas: `slide-1.jpg` pra decks com menos de 10 páginas, `slide-01.jpg` pra 10-99, `slide-001.jpg` pra 100+.

**Após fixes, rode os 4 comandos novamente** — o PDF deve ser regenerado do `.pptx` editado antes do `pdftoppm` refletir suas mudanças.
