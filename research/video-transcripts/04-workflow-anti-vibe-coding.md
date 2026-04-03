Aqui esta a analise completa da transcrição do Video 4: "Como eu uso o Claude Code (Workflow Anti-Vibe Coding)".

---

# Analise Completa -- Video 4: "Como eu uso o Claude Code (Workflow Anti-Vibe Coding)"

**Canal/Autora:** Criadora do app "Epic" (3.000+ usuarios, lançado sem escrever uma linha de codigo manualmente). Usa Claude Code desde abril (quase 10 meses de uso diario na epoca da gravação).

**URL:** https://www.youtube.com/watch?v=BcLtqQ3JlMU

---

## 1. Resumo Completo

O video apresenta a metodologia **SDD (Spec Driven Development)** como alternativa ao "vibe coding" puro. A autora argumenta que vibe coding (jogar prompts aleatorios e torcer para dar certo) realmente nao funciona e produz codigo de baixa qualidade. Porem, com um metodo estruturado, e possivel construir aplicações inteiras com IA -- como ela fez com o app Epic.

O video cobre:
- **Por que o codigo gerado por IA costuma ser ruim** (5 problemas-chave)
- **A raiz do problema:** a context window e como ela e desperdiçada
- **O metodo SDD em 3 passos:** Pesquisa, Spec, Implementação
- **Como cada passo funciona na pratica** com exemplos reais
- **Resultados esperados** ao aplicar o metodo

---

## 2. Workflow Anti-Vibe Coding (SDD) -- Cada Passo Detalhado

### Passo 1: PESQUISA (Research)

**Objetivo:** Buscar todo o contexto necessario para a IA fazer uma implementação efetiva.

O que fazer:
1. **Pesquisar na base de codigo existente** -- identificar quais arquivos serao afetados pela nova implementação e encontrar padroes de implementação de coisas similares ja feitas
2. **Buscar documentações externas** -- ler documentação relevante das tecnologias/bibliotecas usadas (ex: NextAuth docs)
3. **Buscar padroes de implementação externos** -- Stack Overflow, GitHub, documentações oficiais

**Tecnica especial mencionada:** Clonar um repo do GitHub que tenha o padrao desejado, importar dentro do projeto numa pasta `.tmp`, pedir pro Claude Code analisar aquele padrao, e depois deletar a pasta. Isso serve para trazer padroes comprovados de implementação.

**Output do Passo 1:** Gerar um arquivo `prd.md` -- um resumo filtrado de tudo que foi encontrado na pesquisa. So vai pro PRD o que e relevante (informações inuteis sao descartadas). Contem:
- Arquivos da base de codigo relevantes para a implementação
- Trechos relevantes das documentações externas
- Code snippets / padroes de implementação encontrados

**Depois:** `/clear` -- limpar a context window completamente.

### Passo 2: SPEC (Especificação)

**Objetivo:** Gerar um plano tatico e especifico de implementação.

O que fazer:
1. Abrir uma conversa nova (context window limpa)
2. Pedir pro Claude Code ler o `prd.md` gerado no passo anterior
3. Pedir para gerar uma `spec.md` que contenha:
   - **Todos os arquivos que precisam ser CRIADOS** (com path completo)
   - **Todos os arquivos que precisam ser MODIFICADOS** (com path completo)
   - **O que precisa ser criado ou modificado em CADA arquivo**
   - **Code snippets / pseudocodigo** para cada arquivo quando aplicavel

**Formato critico da spec:** Sempre seguir o padrao:
```
[path do arquivo] -> [o que criar ou modificar nele]
```

A spec e essencialmente o "prompt de implementação" -- e o mais tatico e especifico possivel.

**Depois:** `/clear` -- limpar a context window novamente.

### Passo 3: IMPLEMENTAÇÃO (Code)

**Objetivo:** Executar o plano com o maximo de context window disponivel.

O que fazer:
1. Abrir uma conversa nova (context window limpa)
2. Anexar a `spec.md` como prompt
3. Pedir para implementar a spec

A vantagem: como a spec ja e um resumo compacto de toda a pesquisa e planejamento, a context window fica quase toda livre para a IA fazer a implementação real.

---

## 3. CLAUDE.md -- Configuração

O video **nao entra em detalhes sobre CLAUDE.md especificamente**. O foco e no workflow de 3 passos (PRD -> Spec -> Implementação). Porem, o conceito central e que voce deve informar a IA sobre:
- Padroes de arquitetura que voce usa
- Como separar arquivos (responsabilidades)
- Quais componentes ja existem na base de codigo
- Documentações relevantes

Isso se aplica diretamente ao que poderia ir num CLAUDE.md.

---

## 4. Commands Mostrados

O video **nao menciona commands customizados** como `research_codebase`, `create_plan`, ou `implement_plan` pelo nome. O que a autora descreve sao **3 prompts manuais** que ela faz em conversas separadas:

1. **Prompt de Pesquisa** -- "Preciso implementar X. Pesquise na base de codigo, leia documentações, busque padroes e gere um prd.md"
2. **Prompt de Spec** -- "Leia o prd.md e gere uma spec com todos os arquivos a criar/modificar e o que fazer em cada um"
3. **Prompt de Implementação** -- "Implemente a spec.md"

Ela menciona que os prompts exatos estao disponiveis na newsletter dela (DevGPT no Substack).

O unico command nativo mencionado e o `/clear` do Claude Code para limpar a context window entre cada passo.

---

## 5. Thoughts/Documentação -- Sistema de Notas

O video **nao menciona um sistema de thoughts/notas** especificamente. O sistema de "memoria" que ela usa entre conversas sao os **arquivos .md** gerados em cada passo:
- `prd.md` -- memoria da pesquisa
- `spec.md` (ou `my-spec.md`) -- memoria do planejamento

Esses arquivos funcionam como "handoff" entre conversas, preservando o conhecimento quando a context window e limpa.

---

## 6. Ferramentas Usadas

- **Claude Code** -- ferramenta principal, usada via CLI no terminal
- **`/clear`** -- comando nativo do Claude Code para limpar context window
- **Web search/MCP** -- mencionado que MCPs consomem context window (Jason blob enorme) e que ela pede para buscar na internet
- **Newsletter DevGPT (Substack)** -- onde os prompts exatos estao disponiveis
- **HumanLayer** -- **nao mencionado neste video**

---

## 7. Padroes de Organização

### Problemas que o metodo resolve (diagnosticados pela autora):

| Problema | Causa Raiz |
|---|---|
| **Over-engineering** | IA nao sabe que existe forma mais simples (nao esta na context window) |
| **Reinventar a roda** | IA nao sabe que ja existe solução pronta |
| **Nao saber implementar** | Documentação mais recente que o training cutoff |
| **Repetir codigo** | Context window estourou, IA esqueceu que ja fez aquilo |
| **Juntar tudo no mesmo arquivo** | Voce nao disse como quer separar os arquivos |

### Regras de ouro para context window:
- **Trabalhar com no maximo 40-50% da context window** -- quando passar disso, `/clear`
- **Informações incorretas, incompletas, inuteis ou excessivas** destroem a qualidade do output
- **Qualidade do input = qualidade do output** -- "quem transforma agua em vinho e Jesus, nao a IA"
- **Cada ação consome context window:** buscar arquivos, ler arquivos, editar, escrever, rodar MCPs, prompts

### Tecnica da pasta `.tmp`:
- Clonar um repo do GitHub com o padrao desejado
- Importar numa pasta `.tmp` dentro do projeto
- Pedir pro Claude Code analisar e extrair o padrao
- Deletar a pasta depois

---

## 8. Insights Acionaveis -- O que Aplicar

### A. Criar Commands Customizados para os 3 passos
O workflow dela pode ser transformado em 3 slash commands:
1. `/research` -- pesquisa na base de codigo + docs + padroes -> gera `prd.md`
2. `/spec` -- le o `prd.md` -> gera `spec.md` com plano tatico
3. `/implement` -- le a `spec.md` -> implementa

### B. Sempre dar `/clear` entre passos
Nunca fazer pesquisa + spec + implementação na mesma conversa. O "handoff" entre conversas sao os arquivos .md.

### C. A Spec deve ser ultra-especifica
Nao e um documento vago. E um plano tatico com:
- Path exato de cada arquivo
- O que criar ou modificar em cada um
- Code snippets / pseudocodigo quando necessario

### D. Pesquisa antes de implementação -- SEMPRE
Mesmo para tarefas "simples", buscar na base de codigo primeiro evita codigo duplicado, over-engineering e reinvenção de roda.

### E. Documentações externas sao obrigatorias
Se a implementação usa qualquer biblioteca/serviço externo, a documentação TEM que ser passada. A IA nao vai pesquisar sozinha na maioria das vezes.

### F. Tecnica `.tmp` para importar padroes
Quando nao tem experiencia com um padrao especifico, clonar um repo de referencia, importar temporariamente, e pedir pra IA aprender o padrao antes de implementar.

### G. Regra dos 40-50%
Monitorar uso da context window. Nunca deixar passar de 50%. Isso e mais importante do que parece -- a qualidade degrada drasticamente quando a window enche.

### H. A velocidade "real" nao e no inicio
Vibe coding parece rapido no começo mas trava cedo. SDD parece mais lento no inicio mas vai muito mais longe sem travar. E uma inversao de curva de produtividade.

---

**Resumo em uma frase:** O metodo SDD e basicamente "pesquise, resuma, limpe, planeje, resuma, limpe, implemente" -- usando arquivos .md como memoria persistente entre conversas com context window limpa, garantindo que a IA sempre tenha contexto relevante e compacto em vez de uma window poluida.