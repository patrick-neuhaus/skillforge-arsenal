# Remotion Patterns — Componentes para Video Programatico

Consulte este arquivo quando criando componentes para projetos Remotion.

---

## Anatomia de um Projeto Remotion

```
src/
├── remotion/
│   ├── Root.tsx              # Entry point — registra composicoes
│   ├── compositions/         # Videos (Composition = um video)
│   │   ├── MyVideo.tsx       # Composicao principal
│   │   └── Intro.tsx         # Composicao de intro
│   ├── components/           # Componentes de cena
│   │   ├── Title.tsx         # Componente animado de titulo
│   │   ├── Logo.tsx          # Logo animado
│   │   └── Chart.tsx         # Data visualization animada
│   ├── sequences/            # Sequencias (cenas dentro de video)
│   │   ├── IntroSequence.tsx
│   │   └── OutroSequence.tsx
│   └── lib/
│       ├── design-tokens.ts  # Cores, fontes, spacing do video
│       └── spring-configs.ts # Configuracoes de animacao
```

## Padroes de Componentes Remotion

### Composicao (Video)
```typescript
// Uma Composition = um video renderizavel
export const MyVideo: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: tokens.bg }}>
      <Sequence from={0} durationInFrames={90}>
        <IntroSequence />
      </Sequence>
      <Sequence from={90} durationInFrames={120}>
        <ContentSequence />
      </Sequence>
    </AbsoluteFill>
  );
};
```

### Componente Animado
```typescript
// Cada componente recebe frame via useCurrentFrame()
export const AnimatedTitle: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 30], [0, 1]);
  const translateY = spring({ frame, fps: 30, from: 50, to: 0 });

  return (
    <h1 style={{ opacity, transform: `translateY(${translateY}px)` }}>
      {text}
    </h1>
  );
};
```

## Regras de Componentes Remotion

1. **Tudo e funcao de frame** — nao use useState/useEffect pra animacao. Use useCurrentFrame()
2. **Sequences organizam tempo** — cada Sequence e uma cena com inicio e duracao
3. **AbsoluteFill e o container** — preenche todo o viewport do video
4. **Design tokens separados** — cores/fontes em arquivo dedicado, nao inline
5. **Props tipadas** — cada componente recebe dados via props (titulo, dados, config)
6. **Composicao = atomic design** — atoms (textos), molecules (cards), organisms (cenas)
