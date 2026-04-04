# Design Review Checklist — 3 Camadas

Consulte este arquivo no modo `--design` para review de output visual/frontend.

---

## Camada 1: Visual Consistency

### Layout & Spacing
- [ ] Espacamento consistente (usa scale, nao valores arbitrarios)
- [ ] Alinhamento correto (grid, flexbox alignment)
- [ ] Hierarquia visual clara (titulos > subtitulos > body)
- [ ] Responsividade (breakpoints mobile/tablet/desktop)

### Color & Typography
- [ ] Cores seguem paleta definida (design tokens, nao hex hardcoded)
- [ ] Contraste suficiente (texto sobre background)
- [ ] Tipografia consistente (max 2 familias: display + body)
- [ ] Font weights usados com proposito (nao aleatorio)

### Components
- [ ] Botoes seguem variantes definidas (primary, secondary, ghost)
- [ ] Inputs tem estados (default, focus, error, disabled)
- [ ] Cards/containers tem sombras e bordas consistentes
- [ ] Icons de uma unica source (Lucide, Heroicons — nao misturar)

### Anti-AI Design
- [ ] Nao tem gradientes roxo-rosa cliche ("selo de AI generico")
- [ ] Tem identidade visual propria (nao generico bonito)
- [ ] Micro-interactions presentes (hover, focus, transitions)
- [ ] Imagens/ilustracoes sao proprias ou de alta qualidade (nao stock generico)

## Camada 2: Acessibilidade (WCAG)

### Nivel A (minimo)
- [ ] Todas as imagens tem alt text
- [ ] Formularios tem labels associados
- [ ] Links tem texto descritivo (nao "clique aqui")
- [ ] Navegacao via teclado funciona (tab order logico)
- [ ] Contraste minimo 4.5:1 pra texto normal, 3:1 pra texto grande

### Nivel AA (recomendado)
- [ ] Focus indicators visiveis em todos elementos interativos
- [ ] Error messages identificam o campo com erro
- [ ] Nao depende apenas de cor pra comunicar informacao
- [ ] Touch targets >= 44x44px em mobile
- [ ] Skip navigation link presente

### Semantic HTML
- [ ] Headings em ordem (h1 > h2 > h3, sem pular)
- [ ] Landmarks semanticos (nav, main, aside, footer)
- [ ] Botoes sao `<button>`, links sao `<a>` (nao divs clicaveis)
- [ ] Listas sao `<ul>`/`<ol>`, nao divs com bullet chars

## Camada 3: Performance

### Loading
- [ ] Imagens otimizadas (WebP/AVIF, lazy loading)
- [ ] Fontes com font-display: swap (evitar FOIT)
- [ ] CSS critico inline ou preloaded
- [ ] Componentes pesados com lazy import / dynamic()

### Runtime
- [ ] Nao re-renderiza desnecessariamente (check React DevTools)
- [ ] Listas grandes usam virtualizacao (>100 items)
- [ ] Animacoes usam transform/opacity (nao width/height/top/left)
- [ ] Event listeners tem cleanup (useEffect return)

### Bundle
- [ ] Nao importa libs inteiras quando precisa de 1 funcao
- [ ] Tree-shaking funciona (named imports, nao default)
- [ ] Imagens nao estao no bundle JS (usar public/ ou CDN)

## Severity de Findings

| Camada | Severity padrao | Override |
|--------|:--------------:|----------|
| Visual inconsistency | P2 | P1 se landing page / face publica |
| Accessibility violation | P1 | P0 se app publico / regulado |
| Performance issue | P2 | P1 se impacta UX percetivelmente |
| Anti-AI design | P3 | P2 se cliente esta pagando pelo design |
