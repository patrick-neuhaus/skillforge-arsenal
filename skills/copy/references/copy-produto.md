<!--
  copy-produto.md — UX writing checklist por componente: botões, forms, erros, empty states, success states
  Carregado em: tasks de copy para interface de produto, microcopy, onboarding, mensagens de sistema
-->

# Copy — UX Writing & Microcopy

**Referências:** Kinneret Yifrah (Microcopy: The Complete Guide), Nicole Fenton, Erika Hall

## Princípios Fundamentais

1. **Clareza > Criatividade** — o usuário precisa entender em zero esforço cognitivo
2. **Verbo + benefício** — todo elemento de ação diz o que o usuário faz E o que ele ganha
3. **Contexto = confiança** — microcopy que explica o "por quê" reduz abandono
4. **Consistência de voz** — tom do produto deve ser o mesmo em todos os estados da interface
5. **Escreva para o estado emocional do momento** — erro → empático; sucesso → celebratório

---

## Checklist por Componente

### Botões (CTAs)

| Padrão ruim | Padrão bom |
|-------------|------------|
| Submit | Enviar formulário |
| OK | Entendido |
| Click here | Baixar relatório |
| Register | Criar minha conta |
| Buy | Garantir meu acesso |
| Delete | Excluir permanentemente |
| Next | Próximo: revisar pedido |

**Regras:**
- [ ] Verbo no imperativo ou primeira pessoa
- [ ] Diz o que acontece DEPOIS do clique
- [ ] Ação destrutiva (delete, cancel) tem confirmação e linguagem clara
- [ ] Botão primário = ação desejada. Botão secundário = escape. Nunca os dois iguais.

---

### Formulários

| Elemento | Regra | Exemplo |
|----------|-------|---------|
| Labels | Visíveis sempre (não apenas placeholder) | "E-mail" acima do campo |
| Placeholder | Exemplo de preenchimento, não repetir o label | "ex: joao@empresa.com" |
| Campos obrigatórios | Indicar claramente (asterisco + legenda) | "* Campos obrigatórios" |
| Sequência | Ordem lógica = como a pessoa pensa | Nome → E-mail → Empresa → Cargo |
| Campos opcionais | Marcar como "(opcional)" — não assumir | "Telefone (opcional)" |
| Submit | CTA específico, não "Enviar" genérico | "Criar minha conta gratuita" |

**Checklist:**
- [ ] Cada campo tem label visível (não só placeholder)?
- [ ] Placeholder tem exemplo concreto?
- [ ] Campo obrigatório está sinalizado?
- [ ] O CTA do submit diz o que acontece depois?
- [ ] Formulário pede só o que é estritamente necessário?

---

### Mensagens de Erro

**Estrutura:** O que deu errado + Por que aconteceu + Como resolver

| Ruim | Bom |
|------|-----|
| "Erro" | "E-mail inválido. Use o formato joao@empresa.com" |
| "Falha na operação" | "Não conseguimos processar. Tente novamente ou entre em contato." |
| "Campo obrigatório" | "Por favor, insira seu e-mail para continuar" |
| "Senha incorreta" | "E-mail ou senha incorretos. [Esqueceu a senha?]" |
| "Erro 404" | "Página não encontrada. [Voltar para início]" |

**Checklist:**
- [ ] Explica o que deu errado (não só "erro")?
- [ ] Tom é empático, não acusatório ("você errou" → "não encontramos")?
- [ ] Oferece caminho de saída (link, botão, sugestão)?
- [ ] Usa linguagem humana, não código técnico?

---

### Empty States

Empty state = quando não há dados ainda (lista vazia, busca sem resultado, primeiro acesso).

**Não deixe vazio. Use como oportunidade:**

| Contexto | O que escrever |
|----------|---------------|
| Lista vazia (primeiro acesso) | Contexto do que aparecerá + CTA para criar o primeiro item |
| Busca sem resultado | "Nenhum resultado para '[termo]'" + sugestão de busca alternativa |
| Notificações vazias | "Tudo certo por aqui! Você será notificado quando X acontecer." |
| Feed vazio | "Ainda não há conteúdo. [Siga X pessoas] para começar a ver posts." |

**Checklist:**
- [ ] Explica por que está vazio?
- [ ] Tem CTA para resolver o vazio?
- [ ] Tom é positivo/encorajador, não neutro ou negativo?

---

### Success States

**Nunca apenas "Sucesso!" — celebre E direcione o próximo passo:**

| Contexto | O que escrever |
|----------|---------------|
| Cadastro concluído | "Conta criada! Verifique seu e-mail para ativar." |
| Pagamento aprovado | "Pagamento confirmado. Você receberá o acesso em até 5 minutos." |
| Formulário enviado | "Recebemos seu contato! Retornaremos em até 24h." |
| Upload concluído | "Arquivo enviado com sucesso. [Ver arquivo]" |
| Configuração salva | "Alterações salvas." (sem rodeio — confirmação direta) |

**Checklist:**
- [ ] Confirma o que aconteceu?
- [ ] Define expectativa de próximo passo?
- [ ] Tom é proporcional (não exagerado para ações rotineiras)?

---

## Tom por Estado da Interface

| Estado | Tom | Palavras-chave |
|--------|-----|----------------|
| Onboarding | Encorajador, guia | "vamos", "fácil", "passo a passo" |
| Erro | Empático, orientado à solução | "não se preocupe", "isso acontece", "veja como" |
| Empty state | Positivo, motivador | "ainda", "em breve", "comece aqui" |
| Sucesso | Celebratório mas conciso | "pronto", "feito", "ótimo" |
| Confirmação destrutiva | Neutro, claro, sem alarme | "isso não pode ser desfeito" |
