<!--
  copy-produto.md — UX writing checklist por componente + voice/tone matrices + AI features + error handling + a11y + push/SMS
  Carregado em: tasks de copy pra interface de produto, microcopy, onboarding, mensagens de sistema
  v3 — 2026-05-03 (Wave 2: voice/tone matrices Mailchimp/Atlassian + AI features UX + error fluxos criticos + a11y + push/SMS)
-->

# Copy — UX Writing & Microcopy

**Referencias:** Kinneret Yifrah (Microcopy Complete Guide), Nicole Fenton, Erika Hall, Mailchimp/Shopify/Atlassian style guides

## Principios Fundamentais

1. **Clareza > Criatividade** — usuario precisa entender em zero esforco cognitivo
2. **Verbo + beneficio** — todo elemento de acao diz o que usuario faz E o que ganha
3. **Contexto = confianca** — microcopy que explica o "por que" reduz abandono
4. **Consistencia de voz** — tom do produto deve ser o mesmo em todos estados da interface
5. **Escreva pro estado emocional do momento** — erro → empatico; sucesso → celebratorio

---

## Voice & Tone Matrices (NOVO v3)

Voice = personalidade da marca (constante). Tone = como aplica a voice em situacoes especificas (varia).

### Mailchimp pattern (pubico)

**Voice base:** clara, sincera, com humor sutil, autentica.

**Tone matrix (situacao → tom):**

| Situacao | Tone ajustado | Exemplo |
|---|---|---|
| Welcome onboarding | Encorajador, leve | "Vamos juntos!" |
| Erro de configuracao | Empatico + solucao | "Algo nao deu certo. Vamos resolver?" |
| Pagamento aprovado | Celebratorio mas direto | "Pagamento feito. Continue de onde parou." |
| Limite atingido | Direto + ROI | "Voce ja usou 80%. Mantenha [beneficio]: [upgrade]" |

### 4 Dimensoes de Voice (Nielsen Norman Group)

Avalia cada microcopy em 4 eixos:

1. **Formal ↔ Casual** — banco = formal | jogo = casual
2. **Serio ↔ Engracado** — saude = serio | viagem = engracado leve
3. **Respeitoso ↔ Irreverente** — institucional = respeitoso | streetwear = irreverente
4. **Seco ↔ Entusiastico** — B2B tech = seco | consumer app = entusiastico

**Aplicacao:**
- App bancario: Formal + Serio + Respeitoso + Seco
- Game pra adolescente: Casual + Engracado + Irreverente + Entusiastico
- SaaS B2B: Casual leve + Serio + Respeitoso + Moderado

⚠️ **Erro comum:** voice inconsistente entre canais. Email formal + UI casual = quebra confianca.

### Style guides publicos pra estudar

- **Mailchimp:** mailchimp.com/help/style-guide (acessivel, claro, voz humana)
- **Shopify:** polaris.shopify.com (UX voice + tone deep)
- **Atlassian:** atlassian.design/foundations (matriz pratica)

---

## Checklist por Componente

### Botoes (CTAs)

| Padrao ruim | Padrao bom |
|-------------|------------|
| Submit | Enviar formulario |
| OK | Entendido |
| Click here | Baixar relatorio |
| Register | Criar minha conta |
| Buy | Garantir meu acesso |
| Delete | Excluir permanentemente |
| Next | Proximo: revisar pedido |

**Regras:**
- [ ] Verbo no imperativo ou primeira pessoa
- [ ] Diz o que acontece DEPOIS do clique
- [ ] Acao destrutiva (delete, cancel) tem confirmacao e linguagem clara
- [ ] Botao primario = acao desejada. Botao secundario = escape. Nunca os dois iguais.

---

### Formularios

| Elemento | Regra | Exemplo |
|----------|-------|---------|
| Labels | Visiveis sempre (nao apenas placeholder) | "E-mail" acima do campo |
| Placeholder | Exemplo de preenchimento, nao repetir o label | "ex: joao@empresa.com" |
| Campos obrigatorios | Indicar claramente (asterisco + legenda) | "* Campos obrigatorios" |
| Sequencia | Ordem logica = como a pessoa pensa | Nome → E-mail → Empresa → Cargo |
| Campos opcionais | Marcar como "(opcional)" — nao assumir | "Telefone (opcional)" |
| Submit | CTA especifico, nao "Enviar" generico | "Criar minha conta gratuita" |

---

### Mensagens de Erro (Fluxos Criticos NOVO v3)

**Estrutura:** O que deu errado + Por que aconteceu + Como resolver

| Ruim | Bom |
|------|-----|
| "Erro" | "E-mail invalido. Use o formato joao@empresa.com" |
| "Falha na operacao" | "Nao conseguimos processar. Tente novamente ou entre em contato." |
| "Campo obrigatorio" | "Por favor, insira seu e-mail para continuar" |
| "Senha incorreta" | "E-mail ou senha incorretos. [Esqueceu a senha?]" |
| "Erro 404" | "Pagina nao encontrada. [Voltar para inicio]" |

### Erros em Pagamento (CRITICO)

Pagamento e fluxo de maxima ansiedade. Copy errada = perde venda + churn.

**Padrao:**
- Tom: empatico, NAO acusatorio (nao culpe usuario)
- Identifique problema especifico (cartao expirado vs saldo vs antifraude)
- Ofereca proximo passo CLARO (tentar outro cartao, contatar suporte, retry)
- Nao perca contexto (carrinho/produto continua)

**Ex bom:**
> "Ops, nao conseguimos processar seu cartao 1234. Pode tentar outro cartao ou usar Pix. Seu pedido continua salvo."

**Ex ruim:**
> "Pagamento recusado. Erro PA-203."

### Erros em Auth (login/signup)

**Tom:** seguro mas amigavel. Nunca revele se email existe (security).

**Ex bom:**
> "E-mail ou senha incorretos. [Esqueceu a senha?]"

**Ex ruim:**
> "Esse email nao existe na nossa base" (vaza info pra atacante)

### Erros em Acoes Destrutivas (delete/cancel)

**Padrao:**
- Confirmacao explicita ("Voce vai apagar X. Isso e permanente.")
- Tom neutro, sem alarme exagerado
- Botao destrutivo VISIVELMENTE diferente do escape
- Sem possibilidade de "desfazer" (undo) → reforce permanencia

**Ex bom:**
> "Voce vai excluir o projeto 'Cliente X'. Isso apaga 47 tarefas, 3 documentos e nao pode ser desfeito.
> [Cancelar] [Sim, excluir permanentemente]"

---

### Empty States

Empty state = quando nao ha dados ainda (lista vazia, busca sem resultado, primeiro acesso).

**Nao deixe vazio. Use como oportunidade:**

| Contexto | O que escrever |
|----------|---------------|
| Lista vazia (primeiro acesso) | Contexto do que aparecera + CTA para criar primeiro item |
| Busca sem resultado | "Nenhum resultado para '[termo]'" + sugestao de busca alternativa |
| Notificacoes vazias | "Tudo certo por aqui! Voce sera notificado quando X acontecer." |
| Feed vazio | "Ainda nao ha conteudo. [Siga X pessoas] para comecar a ver posts." |

---

### Success States

**Nunca apenas "Sucesso!" — celebre E direcione o proximo passo:**

| Contexto | O que escrever |
|----------|---------------|
| Cadastro concluido | "Conta criada! Verifique seu e-mail para ativar." |
| Pagamento aprovado | "Pagamento confirmado. Voce recebera o acesso em ate 5 minutos." |
| Formulario enviado | "Recebemos seu contato! Retornaremos em ate 24h." |
| Upload concluido | "Arquivo enviado com sucesso. [Ver arquivo]" |
| Configuracao salva | "Alteracoes salvas." (sem rodeio — confirmacao direta) |

---

## AI Features UX (NOVO v3)

IA virou feature comum em produtos. Copy especifica pra IA tem 3 obrigacoes: **transparencia, controle, calibragem**.

### Transparencia

- **Sempre identifique IA:** "✨ Gerado por IA" ou "✨ AI-generated"
- **Explique limites:** "Este assistente usa IA e pode nao saber tudo"
- **Diferencie origem:** "Resposta humana" vs "Sugestao da IA"

### Controle

- **Consentimento explicito antes de acoes:** "Voce quer que eu gere um resumo com IA?" → [Sim] [Nao]
- **Botao de override:** "Editar resposta da IA" sempre visivel
- **Opt-out:** "Nao quero ver sugestoes da IA"

### Calibragem

- **Sugestoes como botoes (NAO texto solto):** "Perguntas sugeridas: [Voltar para...] [Ver detalhes...]"
- **Confianca explicita:** "Tenho 80% de certeza" > nao apresentar como fato
- **Resposta vaga? Empatia:** "Ainda estou aprendendo sobre isso. Pode reformular?"

### Erros em IA

**Nao mencionar:**
- "Erro do modelo"
- "Hallucination"
- "Contexto insuficiente" (jargao tecnico)

**Mencionar:**
- "Nao consegui processar agora. Tente reformular?"
- "Hmm, isso e novo pra mim. [Sugestao de busca alternativa]"

### Padroes Mailchimp/Notion/Linear pra IA

- Notion: "✨ Ask AI" — botao discreto, contexto-aware
- Linear: AI suggestions inline + botao "Apply" / "Reject"
- Mailchimp: AI-generated copy marcada com badge sutil

---

## Acessibilidade (a11y) Copy (NOVO v3)

Texto pra screen readers + baixa escolaridade = curto e explicito.

### Alt text (imagens)

- **Descritivo + breve:** "Grafico de barras mostrando 60% de conversao em Q3"
- **NAO:** "imagem" / "foto" / "graph"
- **Decorativo:** alt="" (vazio) pra screen reader pular

### Buttons / links

- **Texto claro com alvo:** "Baixar relatorio anual" > "Clique aqui"
- **Sem "Saiba mais" solto:** "Saiba mais sobre [topico]"
- **Aria labels:** botoes com so icone precisam aria-label="Fechar modal"

### Reading level

- **Voz ativa:** "Salve o arquivo" > "O arquivo deve ser salvo"
- **Frases curtas:** <20 palavras por frase
- **Sem jargao:** "Cancele a qualquer momento" > "Termine sua subscription"
- **Linguagem 6a serie:** ferramentas (Hemingway, language tool) pra checar nivel

### Cores + contraste

Copy depende de:
- Texto sempre visivel sem depender de cor (nao "campos vermelhos sao obrigatorios")
- Status icones com texto ("✓ Salvo" nao so verde)

---

## Push Notifications (NOVO v3)

Push tem 1-2 segundos de atencao. Copy precisa ser instantaneamente clara.

### Estrutura

```
[Title — 30-50 chars]
[Body — 100-200 chars max]
[Action button (opcional)]
```

### Padroes

| Tipo | Title | Body |
|---|---|---|
| Lembrete acao | "Esqueceu o carrinho?" | "[Produto] ainda esta esperando. 10% off ate amanha." |
| Update | "Pedido a caminho 📦" | "Seu pedido sera entregue ate 18h hoje" |
| Engagement | "[Nome do amigo] te marcou" | "Veja o que [amigo] disse no comentario" |
| Educacao | "Dica do dia 💡" | "Como aumentar conversao em 5 minutos" |

### Anti-padroes

- ❌ All caps ("URGENTE!!!")
- ❌ Generico ("Algo novo!")
- ❌ Sem contexto ("Voce tem 1 mensagem")
- ❌ Multipla por hora (gera silenciamento)

### Personalizacao

- Use nome do usuario quando possivel
- Refira a acao recente do usuario
- Timing: respeite fuso, evite madrugada

---

## SMS (NOVO v3)

SMS = canal critico (98% open rate, mas alta friccao por ser intrusivo).

### Estrutura

```
[Identificacao remetente] [Mensagem 160 chars max] [CTA + link]
```

**Ex bom:**
> "Banco X: Compra de R$450 aprovada no cartao final 1234. Nao foi voce? Bloqueie em [link]"

**Ex ruim:**
> "Compra realizada. [link]"

### Quando usar

- Transacional critico (confirmacao pagamento, codigo 2FA, entrega)
- Lembretes time-sensitive (consulta, evento)
- Marketing SO com opt-in explicito (LGPD/GDPR)

### Anti-padroes

- ❌ SMS marketing sem opt-in claro (LGPD violation)
- ❌ Multiplos SMS/dia
- ❌ Linguagem promocional sem identificacao
- ❌ Links encurtados suspeitos (parece phishing)

---

## Tom por Estado da Interface

| Estado | Tom | Palavras-chave |
|--------|-----|----------------|
| Onboarding | Encorajador, guia | "vamos", "facil", "passo a passo" |
| Erro | Empatico, orientado a solucao | "nao se preocupe", "isso acontece", "veja como" |
| Empty state | Positivo, motivador | "ainda", "em breve", "comece aqui" |
| Sucesso | Celebratorio mas conciso | "pronto", "feito", "otimo" |
| Confirmacao destrutiva | Neutro, claro, sem alarme | "isso nao pode ser desfeito" |
| AI feature | Transparente, controlavel | "Gerado por IA", "Voce pode editar", "Ainda aprendendo" |
| Push notif | Direto, contextual | nome, acao especifica, valor |