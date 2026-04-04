# WCAG 2.2 — Checklist de Acessibilidade

Criterios organizados por prioridade de impacto em auditorias de UX.

---

## Criterios novos do WCAG 2.2 (outubro 2023)

### Nivel A

| Criterio | O que verificar | Exemplo de violacao |
|----------|-----------------|---------------------|
| **3.2.6 Consistent Help** | Mecanismo de ajuda na mesma posicao em todas as paginas | Chat de suporte aparece no footer em uma pagina e no header em outra |
| **3.3.7 Redundant Entry** | Nao pedir ao usuario pra redigitar informacao ja fornecida | Formulario de checkout pede endereco de novo depois do cadastro |

### Nivel AA

| Criterio | O que verificar | Exemplo de violacao |
|----------|-----------------|---------------------|
| **2.4.11 Focus Not Obscured (Minimum)** | Elemento com foco nao pode ser totalmente coberto | Input com foco fica atras de um banner fixo |
| **2.5.7 Dragging Movements** | Alternativa sem arrastar pra toda funcionalidade de drag | Kanban so funciona com drag-and-drop, sem botao de mover |
| **2.5.8 Target Size (Minimum)** | Alvos interativos >= 24x24 CSS pixels | Botao de fechar modal com 16x16px |
| **3.3.8 Accessible Authentication (Minimum)** | Login sem teste cognitivo obrigatorio | CAPTCHA sem alternativa acessivel (audio, objeto recognition) |

### Nivel AAA

| Criterio | O que verificar |
|----------|-----------------|
| **2.4.12 Focus Not Obscured (Enhanced)** | Foco nunca coberto por nenhum conteudo |
| **2.4.13 Focus Appearance** | Indicador de foco com contraste e tamanho suficiente |
| **3.3.9 Accessible Authentication (Enhanced)** | Versao mais restritiva de 3.3.8 |

---

## Criterios classicos que mais falham

Esses sao os que falham com mais frequencia em apps gerados por IA (Lovable, Bolt, Cursor).

| Criterio | Nivel | O que verificar | Teste rapido |
|----------|-------|-----------------|--------------|
| **1.1.1 Non-text Content** | A | Alt text em imagens informativas | Imagem sem alt ou com alt="" quando e informativa |
| **1.3.1 Info and Relationships** | A | Labels em todos os campos de formulario | Input sem `<label>` associado via `for`/`id` |
| **1.4.3 Contrast (Minimum)** | AA | Texto normal: 4.5:1, texto grande: 3:1 | Texto cinza claro em fundo branco |
| **1.4.11 Non-text Contrast** | AA | Componentes UI e graficos: 3:1 | Borda de input que some no fundo |
| **2.1.1 Keyboard** | A | Tudo funciona sem mouse | Tab nao navega entre elementos, Enter nao ativa botao |
| **2.4.7 Focus Visible** | AA | Indicador de foco visivel ao navegar por teclado | `outline: none` sem substituto |
| **4.1.2 Name, Role, Value** | A | Componentes custom com roles ARIA corretos | Div clicavel sem `role="button"` e sem `tabindex` |

---

## Formato de finding de acessibilidade

```
**Problema:** [descricao especifica]
**WCAG:** [numero] [nome] — [nivel]
**Severidade:** [0-4 Nielsen]
**Recomendacao:** [acao concreta com medidas especificas]
```

### Exemplo

```
**Problema:** Botao de fechar modal tem 16x16px
**WCAG:** 2.5.8 Target Size (Minimum) — AA
**Severidade:** 3
**Recomendacao:** Aumentar pra minimo 24x24px (ideal 44x44px pra touch)
```

---

## Ferramentas de verificacao rapida

Se o usuario tiver acesso ao app rodando:
- **Contraste:** DevTools > Accessibility panel ou extensao axe
- **Teclado:** Tab through da pagina inteira, verificar focus visible
- **Screen reader:** VoiceOver (Mac), NVDA (Windows) — testar fluxo principal
- **Target size:** DevTools > medir elemento com ruler
