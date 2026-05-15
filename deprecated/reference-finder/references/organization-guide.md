# Sistema de Organização de Referências

Consulte este arquivo no **Step 5** do workflow quando for salvar referências.

---

## Table of Contents

1. Modelo Hub-and-Spoke (PARA + Zettelkasten)
2. MOCs (Maps of Content)
3. Scoring (ByteRover-inspired)
4. Formato de arquivo
5. Formato de MOC
6. Archive
7. Obsidian (opcional)

---

## 1. Modelo Hub-and-Spoke

A base de referências usa dois sistemas complementares:

### PARA (Tiago Forte) como Hub — organização por acionabilidade

- **Projects** — referências ativamente sendo usadas num projeto atual
- **Areas** — referências de responsabilidades contínuas (liderança, arquitetura, vendas)
- **Resources** — referências de interesse futuro ou aprendizado
- **Archives** — referências de projetos concluídos

Na prática: arquivos em `references/` organizados por domínio (= Areas). Nome indica a área: `lideranca-references.md`, `vendas-references.md`, `infra-references.md`.

### Zettelkasten como Spoke — conexões

- Cada referência tem pelo menos uma **conexão** com outra referência existente
- Conexões são bidirecionais: "A complementa B" e "B é complementado por A"
- Com o tempo, conexões revelam padrões e insights não-óbvios

## 2. MOCs — Maps of Content

MOCs são índices temáticos que conectam referências de múltiplos domínios.

### Quando criar um MOC

- Um tema cruza 3+ domínios diferentes (ex: "escalar operação" cruza liderança + infra + produto)
- O usuário toma decisão estratégica envolvendo múltiplas áreas
- Referências de domínios diferentes se complementam de forma não-óbvia

### Onde salvar

`references/moc-[tema].md`

## 3. Scoring (ByteRover-inspired)

Cada referência salva recebe:

### Importance (0-100)
- **80-100**: Seminal, core do domínio. Obra que todo profissional deveria conhecer.
- **50-79**: Útil, complementar. Framework prático ou referência recente relevante.
- **30-49**: Complementar. Artigo, talk, ou recurso secundário.
- **0-29**: Marginal. Menção para completude, não é essencial.

Ajustes: +3 quando buscada por necessidade, +5 quando curada manualmente.

### Maturity
- **draft**: Recém-encontrada, não foi aplicada ainda.
- **validated**: Aplicada pelo usuário em contexto real, confirmada como útil.
- **core**: Referência base do domínio, citada repetidamente.

### Recency decay
- Referências com maturity=draft AND importance<35 são candidatas a archive após 21 dias sem uso.
- Referências com maturity=core nunca decaem.

## 4. Formato de Arquivo de Referências

```markdown
# [Domínio] — Base de Referências

Última atualização: [data]

## Obras seminais
- **[Livro]** — [Autor] ([Ano]): [1 frase] | importance: [score] | maturity: [tier]
  - Conexões: → [outra referência no mesmo ou outro arquivo]

## Frameworks
- **[Framework]** — [Autor/Origem]: [1 frase] | importance: [score] | maturity: [tier]
  - Conexões: → [framework complementar ou alternativo]

## Pessoas
- **[Nome]**: [quem é]

## Conexões cruzadas
- Este domínio se conecta com: [lista de outros arquivos e por quê]

## Notas
- [Observações relevantes pro contexto do usuário]
```

Se o arquivo já existia, ATUALIZE em vez de recriar. Adicione novas referências e atualize conexões.

## 5. Formato de MOC

```markdown
# MOC: [Tema transversal]

Última atualização: [data]

## Por que este MOC existe
[1-2 frases: por que essas referências precisam ser vistas juntas]

## Referências por domínio

### De [dominio]-references.md
- [Referência] — relevância pro tema: [como se conecta]

### De [outro-dominio]-references.md
- [Referência] — relevância pro tema: [como se conecta]

## Insight da conexão
[O que emerge quando essas referências são vistas juntas — insight não-óbvio]
```

## 6. Archive

Referências que caem abaixo do threshold (draft + importance<35 + 21d sem uso):
- Movidas pra seção `## Archived` no final do arquivo de domínio
- Mantidas como stub de 1 linha (searchable) com link pro conteúdo original
- Conteúdo completo pode ser recuperado via git history

## 7. Obsidian (opcional)

Sugerir APENAS se o usuário demonstrar interesse em organização fora do Claude.

**Por que Obsidian:**
- Markdown puro (compatível com `references/`)
- Links bidirecionais nativos (`[[referência]]`) — perfeito pro Zettelkasten
- Graph view mostra conexões visualmente
- Plugins: Dataview (queries), Templates, Daily Notes
- Offline-first, dados locais, free

**Não force.** A maioria das vezes, `references/` dentro das skills é suficiente.
