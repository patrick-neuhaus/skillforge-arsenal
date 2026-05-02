# `references/wcag-ux-checklist.md`

> WCAG 2.2 AA aplicado ao fluxo de audit. Consultado a partir da Fase 4 do SKILL.md. Esta skill é dona canônica do **checklist WCAG**; outras skills (`ui-design-system`, `react-patterns`) referenciam estes limiares sem reabrir teoria.

## 1. Como esta checklist é usada no audit

WCAG 2.2 AA é **baseline**, não capítulo separado. Atravessa todo o audit:
- Fase 2 (fluxos): teste com teclado, screen reader, zoom 200%.
- Fase 3 (heurísticas): contraste, foco, hierarquia já são WCAG.
- Fase 4 (esta): varredura sistemática dos critérios.
- Fase 5 (estados): cada estado precisa atender contraste e ser anunciado.

**axe e Lighthouse pegam ~30–40% dos problemas de a11y.** Teste manual com teclado e screen reader é obrigatório para baseline AA.

## 2. Critérios novos no WCAG 2.2 (outubro/2023)

### Nível A

| Critério | O que verificar | Exemplo de violação | Como testar |
|----------|-----------------|---------------------|-------------|
| **3.2.6 Consistent Help** | Mecanismo de ajuda na mesma posição em todas as páginas | Chat aparece no footer em uma página, no header em outra | Visual, navegação |
| **3.3.7 Redundant Entry** | Não pedir info já fornecida no mesmo processo | Checkout pede endereço já cadastrado | Percorrer fluxo end-to-end |

### Nível AA

| Critério | O que verificar | Exemplo de violação | Como testar |
|----------|-----------------|---------------------|-------------|
| **2.4.11 Focus Not Obscured (Minimum)** | Elemento com foco não pode ser totalmente coberto | Input com foco fica atrás de banner fixo | Tab pela página com banners visíveis |
| **2.5.7 Dragging Movements** | Alternativa sem arrastar para drag-and-drop | Kanban só com DnD, sem botão "mover para" | Tentar realizar tarefa só com clique |
| **2.5.8 Target Size (Minimum)** | Alvos interativos ≥ 24×24 CSS px | Botão de fechar 16×16 | DevTools, medir elemento |
| **3.3.8 Accessible Authentication (Minimum)** | Login sem teste cognitivo obrigatório | CAPTCHA sem alternativa (áudio, reconhecimento) | Tentar login sem mouse / com leitor de tela |

### Nível AAA (informativo, não obrigatório)

- 2.4.12 Focus Not Obscured (Enhanced)
- 2.4.13 Focus Appearance
- 3.3.9 Accessible Authentication (Enhanced)

## 3. Critérios clássicos que mais falham

Em apps gerados por IA (Lovable, Bolt, Cursor) e em produtos sem QA de a11y, esses são os recorrentes.

| Critério | Nível | O que verificar | Teste rápido |
|----------|-------|-----------------|--------------|
| **1.1.1 Non-text Content** | A | Alt em imagens informativas | Screenreader: a imagem é descrita? |
| **1.3.1 Info and Relationships** | A | Labels associados via `for`/`id` ou aria-label | Inspecionar campos do form |
| **1.4.3 Contrast (Minimum)** | AA | Texto normal 4.5:1, texto grande 3:1 | DevTools > Accessibility, ou axe |
| **1.4.10 Reflow** | AA | Conteúdo funciona em 320 CSS px de largura sem scroll bidimensional | Resize para 320px, percorrer fluxos críticos |
| **1.4.11 Non-text Contrast** | AA | UI components e gráficos 3:1 | Borda de input, ícones de status, focus ring |
| **1.4.12 Text Spacing** | AA | Texto continua legível com espaçamento ajustado | DevTools, simular line-height 1.5, letter-spacing 0.12em |
| **1.4.13 Content on Hover or Focus** | AA | Conteúdo que aparece em hover/focus é dispensável, hoverable, persistente | Tooltip não pode forçar mouse fora; deve ser fechável com Esc |
| **2.1.1 Keyboard** | A | Tudo funciona sem mouse | Tab pela página inteira, ativar com Enter/Space |
| **2.3.1 Three Flashes** | A | Sem flashes acima de 3/segundo | Inspecionar animações |
| **2.3.3 Animation from Interactions (AAA, mas prática AA)** | AAA | Animação não-essencial pode ser desabilitada | `prefers-reduced-motion: reduce` é respeitado? |
| **2.4.3 Focus Order** | A | Ordem do foco segue a ordem visual e lógica | Tab da página inteira; ordem faz sentido? |
| **2.4.7 Focus Visible** | AA | Indicador de foco visível ao navegar por teclado | `outline: none` sem substituto é violação |
| **3.3.1 Error Identification** | A | Erro identificado em texto | Submeter form com dados inválidos |
| **3.3.3 Error Suggestion** | AA | Erro vem com sugestão acionável | "Email inválido" → "use formato nome@dominio.com" |
| **3.3.4 Error Prevention (Legal/Financial)** | AA | Reversão / verificação / confirmação para ações de risco | Pagamento, exclusão de dado |
| **4.1.2 Name, Role, Value** | A | Componentes custom com roles ARIA corretos | Div clicável sem `role="button"` e `tabindex="0"` |
| **4.1.3 Status Messages** | AA | Mudanças dinâmicas anunciadas a screen reader | Toast de "Salvo" usa `role="status"` ou live region? |

## 4. Teste obrigatório por fluxo

### 4.1 Teclado

1. **Tab** pela página inteira do início ao fim.
2. **Shift+Tab** para verificar ordem reversa.
3. **Enter / Space** ativam botões e links.
4. **Setas** navegam dentro de componentes (menus, radios, listas).
5. **Esc** fecha modais, menus, popovers.
6. **Tab trap** em modal: foco circula dentro, retorna ao trigger ao fechar.

### 4.2 Screen reader (teste rápido)

- VoiceOver (Mac, Safari) ou NVDA (Windows, Firefox/Chrome).
- Percorrer fluxo crítico com SR ligado.
- Verificar: nomes acessíveis em botões, labels em campos, anúncio de erros e sucessos, headings descritivos, landmarks (`<main>`, `<nav>`, `<header>`).

### 4.3 Zoom e reflow

- **Zoom 200%** (Cmd/Ctrl + +): conteúdo continua legível, sem scroll bidirecional desnecessário.
- **Zoom 400%**: idem (exceções: tabelas e mapas podem manter scroll horizontal).
- **Reflow 320 CSS px**: redimensionar viewport e verificar fluxos críticos. Modal não pode quebrar; toolbar não pode sumir sem alternativa.

> Nota: Zoom/reflow é referência cruzada com `ui-design-system` (matriz de QA visual) e `react-patterns` (testes Playwright multi-viewport). `ux-audit` audita o **resultado observável**.

### 4.4 Reduced motion

- Sistema operacional → preferência por menos movimento.
- App respeita `prefers-reduced-motion: reduce`?
- Animações de loading, transições de modal, parallax, autoplay de carousel devem ser reduzidas ou desligadas.

### 4.5 Não dependência só de cor (1.4.1)

- Desaturar mentalmente (ou via filter): o significado persiste?
- Campo obrigatório só em vermelho → violação (precisa de asterisco/texto).
- Link só por cor → violação (precisa de underline ou outro signifier).

## 5. Formato canônico de finding de a11y

```
Problema: [descrição específica do que foi observado]
WCAG: [número] [nome] — Nível [A/AA/AAA]
Princípio Nielsen relacionado (opcional): [H1...H10]
Severidade: [0–4 Nielsen]
Impacto: [quem é excluído / qual fricção sofre]
Recomendação: [ação concreta com medida específica]
Critério de aceite: [como QA valida — teste manual + ferramenta]
```

### Exemplo

```
Problema: Botão de fechar modal mede 16×16 px.
WCAG: 2.5.8 Target Size (Minimum) — AA
Princípio Nielsen: H5 (prevenção de erros — toque acidental)
Severidade: 3
Impacto: Usuários com motor fino reduzido erram o alvo; usuários de touch precisam de múltiplas tentativas.
Recomendação: Aumentar para mínimo 24×24 CSS px (ideal 44×44 para touch). Aumentar área clicável via padding sem alterar visual.
Critério de aceite: Medição em DevTools confirma ≥ 24×24 px; teste em mobile real (iPhone SE, viewport 375 px) confirma toque consistente; axe não reporta violação 2.5.8.
```

## 6. Ferramentas de verificação

| Ferramenta | Cobre | Não cobre |
|-----------|-------|-----------|
| **axe DevTools / extensão** | Contraste, ARIA, labels, structure (~30–40%) | Ordem lógica, intenção, fluxo, copy de erro |
| **Lighthouse a11y** | Subset do axe + alguns checks de mobile | Idem; score ≠ conformidade |
| **DevTools > Accessibility** | Árvore de a11y, contraste, nome computado | Fluxo, teclado completo |
| **VoiceOver / NVDA** | Experiência real de SR | Mensuração quantitativa |
| **Teclado manual** | Foco, ordem, traps, atalhos | — |
| **Zoom / reflow** | Critérios 1.4.10, 1.4.4 | — |

**Regra:** axe + Lighthouse são complemento, não prova de conformidade. Auditar manualmente os fluxos críticos é obrigatório. (`react-patterns` é dono da estratégia de tooling automatizado em CI.)

## 7. Conflitos de interpretação a registrar

- **Tabelas e reflow:** WCAG admite que partes podem exigir layout 2D. Não absolve de oferecer alternativas (column management, export, sticky identifiers, views compactas).
- **Reduced motion:** AA exige controlar movimento automático e evitar que atrapalhe; AAA cobre remoção por interação. Para web app moderno, tratar como prática padrão, não compliance mínima.
- **CAPTCHA:** se obrigatório por requisito legal/segurança, oferecer alternativa acessível (áudio, reconhecimento de objeto, magic link).

## 8. Checklist mínimo por audit

Em todo audit (mesmo focado), verificar pelo menos:

- [ ] Contraste de texto (1.4.3) e não-texto (1.4.11) em todos os estados.
- [ ] Foco visível (2.4.7) em todos os elementos interativos.
- [ ] Teclado (2.1.1) — fluxo crítico operável sem mouse.
- [ ] Target size (2.5.8) — ≥ 24×24, idealmente 44×44 em touch.
- [ ] Labels (1.3.1) em todos os campos de formulário.
- [ ] Reflow (1.4.10) em 320 CSS px.
- [ ] Status messages (4.1.3) — sucessos e erros anunciados.
- [ ] Error suggestion (3.3.3) — toda mensagem de erro tem orientação.
- [ ] Reduced motion respeitado.
- [ ] Não dependência só de cor (1.4.1).
