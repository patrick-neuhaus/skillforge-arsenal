# `references/11-validation-prompts.md` — Validation Prompts "X porque Y" (Wave 9)

> **Frases template embasamento teórico** byte-perfect pra Phase 3 do `--full`. Skill consulta esta ref pra gerar proposta com justificativa explícita estilo "Vou X aqui porque Y, não Z aqui porque W atrapalha atenção".
> **Quando usar:** Phase 3 `--full`. Output Patrick lê em < 30s e cita em vendas como diferencial.
> **Boundary:** frases JÁ PRONTAS pra copy-paste em proposta. Foundations conceptuais em `06-theoretical-foundations.md`. Discovery prompts em `10-discovery-prompts.md`.

---

## 1. Estrutura template Phase 3 (literal byte-perfect)

```
=== Proposta motion ===

Vou colocar <padrão nome> em <section>.

Por quê AQUI:
- <Princípio teórico A>: <X porque Y>
- <Princípio teórico B>: <X porque Y>
- Easing semantics: <CustomEase escolhido> transmite <sensação>
- Anti-pattern evitado: <Z porque atrapalha W>

Por quê NÃO usaria <alternativa rejeitada>:
- <Razão técnica/perceptiva curta>

Por quê NÃO faria <outra alternativa rejeitada>:
- <Razão>

Spec técnico segue Phase 5 se aprovas.
======================
```

---

## 2. Frases prontas — Por quê AQUI (afirmação + justificativa)

### 2.1 Gestalt continuity

- "Stagger 40ms entre palavras porque continuity gestalt mantém olho do user em trajetória horizontal de leitura, evitando saltos cognitivos."
- "FLIP layout animation porque elementos viajam entre posições preservando continuidade visual — sem FLIP, items 'saltam' = perda rastreabilidade."
- "Shared element route change porque card → detalhe mantém continuity espacial — user não 'perde' o item entre rotas."
- "Self-drawing path no logo porque closure gestalt completa forma na cabeça do user antes terminar = sensação de descoberta + memorabilidade."
- "Stagger uniforme em cards porque common fate gestalt sinaliza grupo coeso — user percebe categoria, não items isolados."

### 2.2 Attention economy

- "Hero reveal em 800ms porque attention economy primeiro contato — user precisa entender mensagem em ≤1s. Motion mais lento atrasa decisão."
- "Press feedback em 80ms porque user clica isso 100+ vezes/dia. Motion mais longo = distraction tax acumulado."
- "Microinteraction discreta no hover de card porque SaaS operacional precisa motion FUNCIONAL, não decorativo competindo atenção da tarefa."
- "Skeleton loading sem shimmer chamativo porque user vai esperar 1-2s e voltar pra tarefa — motion ornamental aqui = ruído."
- "Background ambient com amplitude baixa porque hero tem mensagem-chave + CTA — motion de fundo NÃO pode competir."

### 2.3 Scroll psychology

- "Section reveal staggered curto (250ms) porque user em modo skimming precisa percepção rápida 'tem section aqui' — reveal lento perde ancora."
- "Parallax range ≤ 30px porque vestibular WCAG 2.3.3 — deslocamentos maiores disparam náusea em ~5% dos users."
- "ScrollTrigger com scrub: 0.5 porque user scroll velocity varia 6x entre input methods — smoothing previne jitter visual."
- "Sticky narrative com 3 capítulos porque scroll psychology — mais que 5 = fadiga; menos que 2 = motion overhead sem benefício."
- "Reading progress bar discreta porque user em modo reading não pode ser distraído — ele só quer saber 'estou na metade?'."

### 2.4 Easing semantics

- "CustomEase osmo-ease (0.625, 0.05, 0, 1) porque tom session narrative = cinematic premium — curve orgânica não-mecânica match Awwwards-tier."
- "Power3.out porque interaction precisa sentir punchy/decisivo — ease-out genérico parece fraco em CTA highlight."
- "Linear easing intencional em skeleton loading porque ciclo contínuo deve ser invisível mecânico (não competir com expectativa do conteúdo chegando)."
- "Spring suave em toggle thumb porque física simulada transmite tato — toggle sem física parece 'snap on/off' digital frio."
- "easeReverse com exit power3.in porque saída de modal deve ser MAIS rápida que entrada — Carbon/Material guidelines convergem nisso."

### 2.5 Reduced motion + a11y

- "Reduced motion fallback snap-to-end porque user com vestibular sensitivity precisa OUTPUT funcional sem animação — não pode 'perder' o estado."
- "Aria-label descrevendo motion porque screen reader user precisa equivalente narrativo do que vê — animação puramente visual exclui."
- "Pause control porque kinetic typography > 5s viola WCAG 2.2.2 — texto em movimento contínuo precisa OFF switch acessível."
- "Keyboard equivalent pra orbit 3D porque mouse-only navigation exclui power user keyboard + screen reader users."

### 2.6 Performance

- "Animar transform + opacity APENAS porque GPU compositor processa essas properties sem layout/paint pipeline — 60fps garantido."
- "Lazy load Three.js porque scene 3D fora hero crítico não pode atrasar LCP do conteúdo principal."
- "PixelRatio cap em 2 porque retina displays renderizam 4x pixels — sem cap, mobile high-DPI fica < 30fps."
- "gsap.quickTo em mousemove porque cria/destruir tween a cada move = GC pressure + frame drops — quickTo reusa instance."

---

## 3. Frases prontas — Por quê NÃO (alternativa rejeitada)

### 3.1 Rejeitar motion ornamental em SaaS

- "Não usaria character animation Rive aqui porque audiência é dev sênior B2B — character lúdico quebra confiança técnica do contexto."
- "Não usaria parallax pesado em dashboard porque LCP atrasado + risco vestibular WCAG + contexto operacional pede previsibilidade."
- "Não usaria hero loop ambient + kinetic typography simultâneos porque cada motion compete pela atenção limitada — resultado: user abandona antes entender."
- "Não usaria 3D Three.js em SaaS landing porque ROI duvidoso (B2B audience valoriza clareza > espetáculo) + bundle cost alto."
- "Não usaria glassmorphism animado aqui porque contraste em frames intermediários quebra (WCAG AA falha)."

### 3.2 Rejeitar motion lento demais

- "Não usaria reveal 1500ms na hero porque attention economy primeira dobra — user decide em 3s, motion lento atrasa decisão."
- "Não usaria spinner instantâneo porque delay < 200ms = ruído (Doherty law) — usa skeleton ou nada."
- "Não usaria stagger > 80ms em headline porque vira 'uma palavra de cada vez', quebra fluxo de leitura."
- "Não usaria modal entrance 600ms porque user quer ler conteúdo modal AGORA — entrance > 320ms parece bloqueio."
- "Não usaria page transition 800ms porque user navega 3+ vezes/sessão — soma fricção exponencial."

### 3.3 Rejeitar motion mecânico/genérico

- "Não usaria linear easing em UI feedback porque parece mecânico/quebrado — ease-out é baseline mínimo."
- "Não usaria default ease (sem especificar) porque GSAP usa power1.out genérico — perde diferencial premium award-grade."
- "Não usaria bounce/elastic em SaaS sério porque quebra confiança — tom corporate pede calmness."
- "Não usaria CustomEase complexo em microinteraction press porque overhead injustificado — power2.out simples basta."

### 3.4 Rejeitar motion sem contexto

- "Não usaria self-drawing path em parágrafo body porque path animation serve descoberta — em texto corrido vira distração."
- "Não usaria FLIP em lista 500+ items porque custo paint > benefício continuity — vira lentidão visual."
- "Não usaria scrollytelling em landing curta (1-2 viewports) porque pattern serve narrativa progressiva — em landing curta vira overhead sem narrative."
- "Não usaria character mascot em página financeira/legal porque tom lúdico fora de contexto — quebra trust signal crítico."

### 3.5 Rejeitar motion fora do tom

- "Não usaria motion brutalist em SaaS B2B conservador porque tom session narrative exige minimal técnico — brutalist conflita expectativa cliente."
- "Não usaria motion cinematic premium em editorial blog porque tom session narrative = brutalist editorial — cinematic compete com texto crítico."
- "Não usaria motion lúdico criativo em compliance/legal porque contexto exige seriedade — lúdico quebra trust crítico do mercado."

---

## 4. Sintaxe das frases — convenções

### 4.1 Estrutura sempre

```
[Padrão proposto] porque [princípio teórico] [consequência observável].
```

OU

```
Não usaria [alternativa rejeitada] porque [razão técnica/perceptiva].
```

### 4.2 Tom

- **Direto:** "Vou X porque Y" não "Provavelmente seria interessante usar X considerando Y"
- **Específico:** "stagger 40ms" não "stagger pequeno"
- **Causal:** "porque Y" sempre presente — sem causa, frase é vazia
- **Brevidade:** ≤ 25 palavras por frase

### 4.3 Anti-pattern frases

- **Vaga:** "Esse motion vai ficar legal porque é elegante" → vazio.
- **Sem causa:** "Stagger 40ms" → faltou "porque Y".
- **Jargão sem aplicação:** "Aplico continuity gestalt aqui" → falta "para que isso ajuda na prática?"
- **Causa errada:** "Linear easing porque é mais smooth" → linear NÃO é smooth, é mecânico.

---

## 5. Customização Patrick (frases adicionadas conforme uso)

Adicionar frases novas só quando:
- 3+ Phase 3 propostas usaram a mesma justificativa não listada
- Frase virou padrão recorrente em vendas Patrick

Formato adição:
```
- "[Frase nova literal]" — adicionada Wave X, motivo: <contexto>
```

---

## 6. Boundary com outras skills

- **`copy`** — frases de venda/marketing. Esta ref tem frases TÉCNICAS de motion. Sem overlap.
- **`product-marketing-context`** — frases posicionamento produto. Esta ref tem frases PRINCÍPIOS motion.
- **`sales-enablement`** — material vendas. Patrick PODE usar frases desta ref EM vendas, mas a ref é técnica primária.

---

## 7. Manutenção desta ref

- Wave 1 lock-in 30 dias após criação (cooldown frases serem testadas em `--full` real)
- ADD frase nova só com 3+ usos reais documentados
- Remover frase nunca usada em 60 dias
- Revisar trimestralmente alinhamento com `06-theoretical-foundations.md`
