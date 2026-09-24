# PACOTE.md — Semana 3: AGENTS.md e skills

Leitura interna (Iasmim / próximo subagente). Não é material de aluno.

---

## 0. Divergência entre a grade e a doc oficial — leia isso primeiro

O `_BRIEF.md` e o `_GANCHOS.md` chamam esta semana de "AGENTS.md e skills". Abri a doc
oficial (`code.claude.com/docs/en/memory`) antes de escrever qualquer coisa, como
instruído, e a doc diverge do que a grade assume:

> **O Claude Code não lê `AGENTS.md` diretamente. Ele lê `CLAUDE.md`.**
> Se o projeto já usa `AGENTS.md` (convenção de outro agente), a ponte é um import
> (`@AGENTS.md` na primeira linha do `CLAUDE.md`) ou um symlink
> (`ln -s AGENTS.md CLAUDE.md`).

`AGENTS.md` é um padrão aberto, mantido pela Agentic AI Foundation (Linux Foundation),
pensado pra funcionar em vários agentes (Codex, Cursor, Copilot etc.) — não é um
arquivo que o Claude Code carrega sozinho.

**Resolução que tomei (não é renegociação de decisão aprovada, é fidelidade à doc real):**
ensinei os dois, nomeando a diferença explicitamente como conteúdo da aula, em vez de
tratar os nomes como sinônimos. Isso vira parte do conteúdo, não um rodapé: o aluno sai
sabendo que "arquivo de regras" é um conceito (hierarquia, progressive disclosure) que
tem uma implementação vendor-neutra (`AGENTS.md`) e uma implementação específica do
harness que ele usa (`CLAUDE.md`), e que a ponte entre as duas é uma linha de import ou
um symlink. Acho que isso é estritamente melhor pedagogicamente do que fingir que são a
mesma coisa — a turma vai trabalhar com mais de um agente ao longo da carreira.
Documentado nos slides S1 e S8, no `README.md` e no `GUIA-DO-ALUNO.md`.

Todas as demais afirmações técnicas do pacote (frontmatter de skill, campos, hierarquia
de `CLAUDE.md`, progressive disclosure, `.claude/rules/`) foram verificadas contra
`code.claude.com/docs/en/skills`, `code.claude.com/docs/en/memory`,
`code.claude.com/docs/en/best-practices` e
`platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices` — nenhuma
veio de memória. Ver `REFERENCIAS.md`.

---

## 1. Mapeamento Alura

| Curso | Sustenta | O que sai do síncrono por causa disso |
|---|---|---|
| Context Engineering: otimização da janela de contexto de IAs | Progressive disclosure, orçamento de contexto | O síncrono não explica do zero o que é uma janela de contexto nem estratégias gerais de compressão/isolamento — assume que a turma já viu isso e vai direto pra decisão prática "isso é regra ou é skill". |
| Engenharia de software na era da IA: segurança de aplicações com agentes, MCPs e código gerado por IA (dentro da formação AI-Native Software Engineering) | `allowed-tools`, por que restringir o que a skill pode rodar | O síncrono não reexplica a motivação de segurança por trás de escopar ferramentas — só mostra o campo e o padrão de uso. Ameaças específicas de MCP ficam pra semana 4. |

Os dois cursos de LangChain do catálogo geral da Alura foram verificados mas **não
mapeados nesta semana** — não são o tema. Ver a seção "O que eu procurei e decidi não
usar" em `REFERENCIAS.md`.

## 2. O que foi cortado em relação à grade antiga

- **Explicação de tokenização e temperatura** — já foi coberta na aula 1 e não volta
  aqui. Esta semana assume que o vocabulário básico de janela de contexto já existe.
- **MCP** — a grade antiga descrevia esta semana com formato de red team, que na
  verdade é o mapeamento da semana 4 (MCP na prática). Não toquei em MCP como tema
  além de citar `allowed-tools` de passagem — MCP como protocolo é conteúdo da semana 4.
- **Profundidade em hooks e subagentes** — a doc de best practices menciona os dois
  como alternativas a CLAUDE.md pra "isso precisa acontecer sempre, sem exceção" e
  "isso precisa de contexto isolado". Citei de passagem no roteiro (bloco de
  hierarquia) mas não abri lab — não é o assunto desta semana, evita diluir o foco
  regra-vs-skill.
- **Red team como formato de aula inteira** — a grade antiga descrevia esta semana como
  red team. Resolução (já dada pela Iasmim, ver `_BRIEF.md` "Uma inconsistência na spec
  que eu já resolvi"): aula 2 é red team em duplas (mudado no brief de 21/09; antes era lab guiado paralelo); a validação cruzada (que é o
  núcleo do red team) acontece só no último checkpoint da aula 6, e se completa no
  entregável assíncrono. Motivo pedagógico respeitado: ninguém quebra uma skill antes
  de ter escrito uma.

## 3. Ganchos para frente

- **Semana 4 (MCP na prática, red team em duplas)** retoma `allowed-tools` — agora a
  ferramenta que a skill restringe é uma tool de MCP, não só `Bash`/`Read`/`Grep`. O
  red team da semana 4 quebra o *server* MCP do colega; esta semana treinou o
  vocabulário e o reflexo de "tentar quebrar a coisa do colega" em escala pequena (uma
  skill), não em escala de servidor.
- **Semana 4** também pode reusar o mecanismo de pareamento por sorteio com prioridade
  a domínios diferentes — já testado nesta semana, funciona, documentado em
  `ROTEIRO-FACILITADORA.md`.
- **Semana 5 e 6 (Excalidraw coletivo)** podem desenhar a hierarquia
  managed/usuário/projeto/local como zona de diagrama coletivo, já que a turma viu a
  versão em slide/tabela nesta semana — não precisa reintroduzir o conceito, só a
  representação visual.
- **`.claude/rules/` com escopo por `paths`** foi citado mas não praticado (fora do
  escopo desta semana). Fica disponível como gancho pra qualquer semana futura que
  precise de "regra que só vale pra uma parte do código" — especialmente semana 5
  (engenharia de software) ou semana 9 (code review e subagentes).
- **O parágrafo pro dono do negócio** desta semana usa o exemplo de "a IA não inventa
  dado que não foi dado" — esse framing (regra permanente vs. custo de token) pode ser
  reaproveitado literalmente na semana 4 pra explicar por que um MCP server também
  precisa de permissão restrita, não só a skill.
- **O `RELATORIO-VALIDACAO.md` em três cenários** (dispara quando deve / não dispara
  quando não deve / falso positivo) é um formato que qualquer semana com red team pode
  reaproveitar diretamente — inclusive semana 8 (Verificadores), que é sobre
  exatamente esse tipo de teste em escala maior.

## 4. Ganchos para trás

`_GANCHOS.md` estava vazio na seção "Ganchos declarados pelos lotes anteriores" (esta
semana é do lote 1 — não havia gancho anterior pra puxar). Segui a instrução do
`_BRIEF.md`: assumi que a turma tem um `CLAUDE.md` funcional no repositório do projeto
próprio, escrito/completado na semana 2, e tornei isso pré-requisito explícito de
entrada (ver `README.md` e `ENTREGAVEL.md`, seção Pré-requisitos). Também retomei o
padrão de skill introduzido como "Desafio 2" da aula 1 (`_referencia-aula1/
ENTREGAVEL.md`) — lá a skill era read-only e opcional/bônus; aqui ela vira o entregável
central, com frontmatter completo e progressive disclosure forçada, não mais opcional.

## 5. Cobertura dos 7 domínios do catálogo

| Domínio | Funciona? | Como |
|---|---|---|
| 1. Listagem de perfis de alunos da PDA | Sim | Skill: gerar card de perfil a partir de briefing solto. Regra candidata: nunca preencher campo sem dado de origem. |
| 2. Captação de clientes / automações freelancer | Sim | Skill: montar proposta comercial a partir de 3 perguntas. Regra candidata: sempre incluir disclaimer de preço variável. |
| 3. Quiz conectado ao Claude | Sim | Skill: gerar pergunta nova no formato exato do schema de exportação. Regra candidata: nunca alterar o schema sem confirmação. |
| 4. Avaliação automatizada de projetos por IA | Sim | Skill: aplicar rubrica fixa e devolver notas por critério. Regra candidata: nunca aprovar sem rodar os testes do projeto avaliado. |
| 5. Agente de revisão de código com a voz da PDA | Sim | Skill: comentar PR no tom e nas regras do curso. Regra candidata: nunca aprovar PR com `tests/` alterado. |
| 6. Problema real da ONG | Sim | Skill: gerar rascunho de e-mail/relatório no tom institucional. Regra candidata: nunca incluir dado de aluno sem anonimizar. |
| 7. Domínio próprio do aluno | Sim | A regra nasce, por definição, do primeiro erro real que o aluno já teve com o agente nesse domínio — é o caso mais direto de todos. |

**7 de 7 domínios cobertos** — a atividade (escrever uma regra a partir de erro real +
uma skill com progressive disclosure) é um mecanismo de projeto, não de conteúdo
específico de um domínio, então generaliza para todos.

## 6. Soma dos minutos

**Aula 5:** Giro (10) + Recap (15) + Teoria/demo 1 (30) + Lab 1 (15) + Teoria/demo 2
(20) + Lab 2 (25) + Fechamento (5) = **120 min.**

**Aula 6:** Abertura + sorteio (10) + Bloco 1 (20) + Bloco 2 (20) + Bloco 3 (20) +
Bloco 4 (20) + Bloco 5/validação cruzada (20) + Fechamento (10) = **120 min.**

**Total da semana: 240 min síncronos**, mais o bloco de Alura assíncrono (pré-requisito
de entrada na aula 6, não contado nos 240).

## 7. Onde o julgamento do aluno é indispensável

Dois pontos, um por aula — nomeados explicitamente no roteiro, não implícitos:

- **Aula 5, Lab 1:** decidir se uma regra candidata *realmente* muda o comportamento do
  agente ou é redundante com o que ele já faz sozinho. O agente não pode fazer essa
  parte por ele — ele não tem acesso ao histórico de erro específico do aluno a menos
  que o aluno descreva, e mesmo descrito, só o teste antes/depois (rodado pelo próprio
  aluno, em duas sessões) prova a diferença. Uma regra que soa bem mas não muda nada é
  o erro mais fácil de cometer aqui, e é exatamente o que a rubrica do `ENTREGAVEL.md`
  pune ("o que não pontua: uma regra que soa bem mas não muda nada").
- **Aula 6, validação cruzada (checkpoint 5):** decidir, ao ler a skill do colega —
  que documenta um domínio que o aluno validador não conhece — quais cenários realmente
  testam o limite da `description` escrita. O agente que roda o teste não sabe, por si
  só, o que conta como "não deveria disparar aqui" no domínio do colega; isso exige o
  aluno entender rápido o escopo pretendido da skill alheia antes de tentar quebrá-la.
  É o mesmo tipo de julgamento que sustenta code review de verdade, e é reaproveitado
  deliberadamente como ensaio pra semana 4 (red team em MCP).

## 8. Por que esta semana não usa Excalidraw

`_GANCHOS.md` e `_BRIEF.md` mapeiam Excalidraw coletivo pras semanas 5 e 6. A semana 3
usa red team em duplas desde o brief de 21/09 (ver seção "Uma inconsistência na spec que eu já resolvi" do
`_BRIEF.md`). Não há zona de diagrama coletivo a preencher ao vivo nesta semana — os
diagramas que aparecem (hierarquia de CLAUDE.md, ponte AGENTS.md↔CLAUDE.md, analogia do
manual) são artefatos de slide, prontos, não quadros que a turma desenha junto. Por
isso não há pasta `excalidraw/` neste pacote.

## 9. Pendências pra orquestradora decidir

- Confirmar com a Alura a URL exata (fora da formação) e a contagem de aulas do curso
  "Engenharia de software na era da IA: segurança de aplicações com agentes, MCPs e
  código gerado por IA" — só achei confirmado dentro da formação
  `AI-Native Software Engineering`. Marcado `[CONFIRMAR NA ALURA]` em `README.md` e
  `REFERENCIAS.md`.
- O "Módulo 2" no cabeçalho do `ENTREGAVEL.md` é um chute de numeração de módulo —
  não há um mapeamento aula→módulo no `_BRIEF.md`. Ajustar se a Iasmim já tiver uma
  numeração de módulos definida em outro lugar.
