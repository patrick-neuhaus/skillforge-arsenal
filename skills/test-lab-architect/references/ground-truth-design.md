# Ground Truth Design — Step 3 reference

Carrega no Step 3 do `test-lab-architect`. Este é o gate ⛔ BLOCKING — sem gabarito viável, recusa arquitetar.

## Por que gabarito é blocking

Lab de teste mede assertividade da IA contra uma referência. Sem referência confiável, "assertividade" vira número aleatório. Pior: vira viés confirmado — IA aprende a chutar a classe majoritária do pseudo-gabarito e dá 95%, gestor confia, manda pra prod, dá merda em produção.

Resumo brutal: **lab sem gabarito real não é validação, é teatro com gráfico bonito**.

## Perguntas blocking (Step 3.1)

Faça em sequência. Cada uma tem alert se a resposta não bate o threshold:

### 1. Existe base validada por humano?
- ✅ Sim, com N casos por tipo → segue
- ⚠️ Parcial (alguns tipos sim, outros não) → arquiteta lab cobrindo só os tipos com gabarito; explicita no output
- ❌ Não existe → vai pro Step 3.3 (educa + estrutura coleta)

### 2. Volume por tipo
- < 30 casos: **alert crítico**. Skin precisa pelo menos 30 pra ter mínimo de poder estatístico. Pergunta: dá pra coletar mais antes de arquitetar?
- 30-100: aceitável pra MVP do lab, com nota de "expandir conforme uso"
- 100+: bom, segue

### 3. Balanceamento
- Classe majoritária > 70%: **alert**. IA aprende a chutar a maioria, dá 95% sem aprender nada. Pergunta: tem casos da minoria pra incluir? Se não tem, fala que assertividade vai mentir.
- Entre 30/70 e 70/30: aceitável
- Próximo de 50/50: ideal

Para multi-classe (>2 saídas possíveis): nenhuma classe deve representar mais de 60% do gabarito.

### 4. Quem validou
- Especialista único: **red flag de viés**. Validador único reproduz seus próprios padrões — IA pode acertar 100% imitando o viés do validador, e errar tudo na vida real. Pergunta: tem como ter 2+ validadores ou consenso?
- Múltiplos validadores com critério explícito: bom
- Validador anônimo / origem desconhecida: red flag — gabarito não confiável

### 5. Como vai ser atualizada quando critério mudar
- "Vamos ver" / não pensou: pause. Critério muda (regulação, política), gabarito velho fica errado. Pergunta: quem é responsável por re-validar? Quando? Como sinaliza que casos antigos viraram inválidos?
- Tem processo definido (mesmo que simples): aceitável

## Step 3.2: Alerts de viés

Independente das respostas, levante red flags:

- **Volume baixo**: < 30 por tipo → assertividade vira ruído estatístico
- **Imbalance**: classe majoritária > 70% → IA aprende a chutar
- **Validador único**: 1 humano validou tudo → reproduz vieses dele
- **Casos só fáceis**: gabarito tem só casos óbvios → assertividade alta sem capacidade real
- **Casos só de uma fonte**: todos validados em janela curta de tempo, ou de um cliente só → não generaliza
- **Gabarito = treino**: se o gabarito foi usado pra ajustar prompt, não pode ser teste — vazamento de dados

Reporte cada um que achar. Não suaviza.

## Step 3.3: Se não existe gabarito — educa + estrutura coleta

Antes de qualquer coisa: **educa sobre por que importa**, com 1 frase. Exemplo: "sem gabarito real validado por humano, qualquer prompt vai parecer bom pra IA porque ela tá comparando consigo mesma — você precisa de verdade externa pra medir acerto."

Depois ajuda estruturar coleta:

1. **Mínimo viável pra começar**: 30 casos por tipo, balanceamento ≥ 30/70, validador qualificado.
2. **Onde tirar os casos**:
   - Histórico real de produção (amostragem aleatória, não casos curados)
   - Casos sintéticos (só se domínio permite — ex: gerar CPF é OK, gerar análise médica é desastre)
   - Casos consensuais com cliente (workshop com domain expert)
3. **Quem valida**: 2+ humanos qualificados, com critério escrito de aprovação/reprovação. Se discordarem, incluir o caso ou descartar (não fazer média).
4. **Formato de armazenamento**: tabela com `id`, `input`, `expected_output`, `validador`, `data_validacao`, `criterio_aplicado`, `notas`. Critério aplicado é importante porque muda com o tempo.

## Quando aceitar prosseguir mesmo com gap

Patrick pode insistir em rodar mesmo sem gabarito ideal. Aceita, mas:

1. Documenta no output: "lab arquitetado com gap conhecido de gabarito — assertividade reportada não é confiável até [coletar mais N casos / balancear / validar com 2º humano]"
2. Coloca "fix gabarito" como Wave 1 do roadmap pós-implementação
3. Reforça uma vez: "sem isso resolvido, qualquer melhoria de prompt vai parecer real e pode não ser"

## Exemplo: caso Athié (CPF)

Input do Willy: tabela com 10 casos CPF, todos com IA = humano. 8 OK, 2 divergência.

Análise:
- Volume 10 (< 30) ❌
- Balanceamento: 8 aprovados / 2 reprovados (80/20) ⚠️
- Validador: não declarado ⚠️
- Atualização: não pensada ⚠️

Recomendação ao arquitetar lab da Athié: antes de qualquer coisa, plano de coleta — alvo 50 casos por tipo de doc, 30/70 minimum, validados por 2 pessoas da equipe SST com critério escrito do que é aprovado/reprovado pra cada tipo.