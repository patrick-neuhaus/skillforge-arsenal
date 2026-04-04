# Dark Patterns, UX de IA e Mobile Ergonomics

Verificacoes complementares que nao sao heuristicas nem WCAG, mas impactam diretamente a experiencia.

---

## Dark Patterns — Categorias (Purdue University Framework)

| Categoria | O que e | Exemplo | Status legal |
|-----------|---------|---------|--------------|
| **Nagging** | Interrupcoes persistentes | Pop-up de newsletter que aparece toda pagina | Pode violar DSA |
| **Obstruction** | Dificultar tarefas que nao beneficiam o negocio | Cancelamento em 15 passos vs assinatura em 2 | Ilegal (FTC, DSA) |
| **Sneaking** | Esconder informacao relevante | Custo extra revelado so no checkout | Ilegal (CPRA, DSA) |
| **Interface Interference** | Manipular interface pra favorecer uma acao | "Aceitar" em verde grande, "Recusar" em cinza pequeno | Pode violar CPRA |
| **Forced Action** | Obrigar acao nao relacionada | Criar conta pra ver preco | Depende do contexto |
| **Confirmshaming** | Texto manipulativo na opcao de recusar | "Nao, eu nao quero economizar dinheiro" | Anti-etico |
| **Roach Motel** | Facil de entrar, dificil de sair | Free trial que exige ligacao pra cancelar | Ilegal (FTC) |

### Contexto legal

- **EU Digital Services Act (2024+):** Dark patterns explicitamente proibidos. Consent obtido via manipulacao e INVALIDO.
- **California CPRA:** Interface interference em dados pessoais e violacao.
- **FTC Enforcement:** Acoes contra empresas usando obstruction e sneaking em larga escala.

### Checklist rapido

- [ ] Cancelamento e tao facil quanto assinatura?
- [ ] Todos os custos estao visiveis antes do checkout?
- [ ] Opcoes de aceitar e recusar tem peso visual equivalente?
- [ ] Pre-selecoes (checkboxes marcados) beneficiam o usuario ou o negocio?
- [ ] Pop-ups interrompem o fluxo principal do usuario?
- [ ] O usuario consegue completar a tarefa principal sem criar conta?
- [ ] Texto de opcoes nao usa manipulacao emocional?

---

## UX de IA — Checklist

Aplicar quando o app tem features de IA/LLM (chatbot, geracao de conteudo, agentes, recomendacao).

### Transparencia e confianca

- [ ] O usuario sabe que esta interagindo com IA (e nao com humano)?
- [ ] Tem indicadores de confianca (certeza vs "chute")?
- [ ] Respostas citam fontes/referencias quando aplicavel?
- [ ] O usuario entende POR QUE a IA sugeriu algo (explainability)?

### Loading e feedback

- [ ] Respostas de LLM mostram streaming progressivo (nao tela em branco)?
- [ ] Spinner tem estimativa de tempo ou indicacao de progresso?
- [ ] Se a resposta e longa, mostra conteudo parcial enquanto processa?

### Controle do usuario

- [ ] Acoes destrutivas sugeridas pela IA passam por confirmacao humana?
- [ ] Tem override facil (corrigir/rejeitar sugestao da IA)?
- [ ] Tem botao de like/dislike ou feedback pra melhorar respostas?
- [ ] Se e chat, mantem contexto entre turnos?
- [ ] Historico e acessivel e pesquisavel?

### Error handling

- [ ] O que acontece quando a IA falha? Mensagem generica ou orientacao clara?
- [ ] Timeout tem fallback (sugestao de tentar novamente, alternativa manual)?
- [ ] Rate limiting e comunicado de forma amigavel?

---

## Mobile Ergonomics — Thumb Zone

### Dados de referencia (Steven Hoober, 2013 + atualizacoes)

- 49% usam celular com uma mao
- 75% das interacoes sao com polegar
- Em telas 6.5"+, zona confortavel e significativamente menor

### Zonas do polegar

| Zona | Localizacao | Usar pra |
|------|-------------|----------|
| **Confortavel** | Centro e centro-baixo | CTAs primarios, navegacao principal |
| **Esticar** | Bordas e parte superior | Acoes secundarias |
| **Dificil** | Cantos superiores (especialmente top-left) | Acoes destrutivas (evita toque acidental) |

### Checklist mobile

- [ ] CTAs primarios estao na zona confortavel (centro-baixo)?
- [ ] Navegacao e por bottom nav (acessivel) ou top menu (requer esticar)?
- [ ] Modais e acoes destrutivas NAO estao em zonas faceis de tocar?
- [ ] Targets de toque tem pelo menos 44x44px? (WCAG pede 24px, mas 44px e melhor pra touch)
- [ ] Em telas grandes (6.5"+), acoes no topo-esquerdo sao alcancaveis?
- [ ] Gestos de swipe tem alternativa em botao?
- [ ] Formularios usam teclado correto (numerico pra telefone, email pra email)?

### Core Web Vitals — Referencia rapida

| Metrica | O que mede | Bom | Precisa melhorar | Ruim |
|---------|-----------|-----|-------------------|------|
| **LCP** | Loading — tempo ate o maior elemento visivel | <= 2.5s | 2.5s-4s | > 4s |
| **INP** | Responsividade — tempo entre interacao e proximo paint | <= 200ms | 200ms-500ms | > 500ms |
| **CLS** | Estabilidade visual — quanto o layout muda | <= 0.1 | 0.1-0.25 | > 0.25 |

**INP substituiu FID em marco 2024.** INP mede TODAS as interacoes na pagina (nao so a primeira como FID).

### Avaliacao sem ferramentas

Percepcao subjetiva e valida em UX audit:
- "A pagina principal demora visivelmente pra carregar o conteudo principal" → possivel LCP alto
- "Ao clicar num botao, o feedback demora" → possivel INP alto
- "Ao carregar, o botao pula de posicao" → CLS
