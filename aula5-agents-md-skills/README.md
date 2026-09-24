# aula5-agents-md-skills

Semana 3 — **AGENTS.md e skills**
Especialização em Desenvolvimento com IA · Programadores do Amanhã · Turma 2

> Aula 5 (conceito + demo) e aula 6 (**red team em duplas**). A numeração é por aula,
> não por semana — semana 3 = aulas 5 e 6.

Essa semana responde a uma pergunta que a semana 2 deixou em aberto: você já tem um
`CLAUDE.md` no seu projeto próprio. Ele funciona? Ele resolve alguma coisa de verdade,
ou é decoração? E o que você faz quando uma instrução não deveria ficar carregada o
tempo todo, mas só quando você precisa dela?

## Pré-requisito não negociável

**Você chega no lab da aula 6 com:**
1. O bloco da Alura desta semana concluído (seção "Alura" abaixo).
2. Um `CLAUDE.md` funcional no repositório do **seu projeto próprio** (o que você
   escreveu/completou na semana 2, com o esqueleto gerado pelo agente).

Sem os dois, você não tem base pro lab e atrapalha a dupla na validação cruzada do
final da aula 6. Isso não é regra por regra — é o motivo pelo qual a Alura é
pré-requisito de entrada, não conteúdo complementar.

## O que você vai fazer

- **Aula 5** — a facilitadora pede pro agente gerar sozinho um arquivo de regras do
  zero, mostra o resultado (genérico, e você vai entender por quê), e contrasta com um
  escrito a partir de erros reais. Depois, o mesmo tratamento para skills: uma skill
  mal-feita que carrega tudo de uma vez vs. uma que carrega só o essencial e busca o
  resto sob demanda. Dois labs curtos no seu próprio projeto.
- **Aula 6** — red team em duplas: você fecha a sua skill nos primeiros 40 minutos, as
  duplas são sorteadas ao vivo, e o resto da aula você **valida a skill do colega** em
  três cenários (dispara quando deve, não dispara quando não deve, e o falso positivo).
  No fim, relatório cruzado: você entrega o relatório da skill dele, ele entrega o da
  sua.

## Alura (obrigatório antes da aula 6)

- **Context Engineering: otimização da janela de contexto de IAs** —
  <https://www.alura.com.br/curso-online-context-engineering-otimizacao-da-janela-de-contexto-de-ias>.
  Cobre compressão, isolamento e gestão de memória de contexto. **O síncrono não repete
  o que esse curso já explica sobre orçamento de contexto** — ele assume que você já viu
  isso e vai direto pra decisão prática (regra vs. skill).
- **Engenharia de software na era da IA: segurança de aplicações com agentes, MCPs e
  código gerado por IA** (dentro da formação AI-Native Software Engineering) —
  <https://www.alura.com.br/formacao-ai-native-software-engineering>. Cobre por que
  restringir o que um agente pode executar é uma prática de segurança, não excesso de
  cautela. **O síncrono não reexplica a motivação de segurança de `allowed-tools`** —
  só mostra o campo e como usar. `[CONFIRMAR NA ALURA]` a URL do curso avulso e a
  contagem exata de aulas — só achamos o curso listado dentro da formação.

## O que tem aqui

```
.
|-- README.md                    <- este arquivo
|-- GUIA-DO-ALUNO.md              <- passo a passo dos labs e do red team
|-- ENTREGAVEL.md                 <- a atividade de fixação + rubrica
|-- starter/
|   |-- skill-skeleton/
|   |   |-- SKILL.md              <- esqueleto INCOMPLETO com TODOs — você completa no lab
|   |   `-- reference.md          <- onde vai o material de referência (progressive disclosure)
|   `-- relatorio-validacao/
|       `-- TEMPLATE.md           <- o formato do relatório dos 3 cenários de validação
`-- (ROTEIRO-FACILITADORA.md, SLIDES-OUTLINE.md, REFERENCIAS.md, PACOTE.md
     são material da facilitadora — não fazem parte do que você usa no lab)
```

## Pré-requisitos técnicos

- Tudo que você já tinha pronto desde a aula 1: Node 18+, git, Claude Code instalado
  e logado.
- O seu projeto próprio, do jeito que ficou na semana 2, com o `CLAUDE.md` completo
  (sem `TODO`) e um repositório git de verdade (init + pelo menos um commit).
- **Windows:** os mesmos comandos de sempre. Se você não configurou o terminal na aula
  1, volte na tabela "Terminal: qual usar" do `GUIA-DO-ALUNO.md` da aula 1 antes de
  começar — ela não muda essa semana.

## Regra da casa (continua valendo)

> **Você é responsável por cada linha que commita.**
> O agente executa. Você especifica, lê o diff, roda os testes e decide.

Essa semana ela ganha uma segunda camada: você também é responsável por cada linha do
seu `CLAUDE.md` e de cada `SKILL.md`. Se uma regra não muda o comportamento do agente,
ela não é regra — é ruído que você paga em token toda sessão.

## Uma nota sobre nomes: AGENTS.md, CLAUDE.md e a skill

Você vai ouvir os dois nomes esta semana e eles não são a mesma coisa:

- **`AGENTS.md`** é um formato aberto, mantido pela Agentic AI Foundation (Linux
  Foundation), pensado pra funcionar em qualquer agente de código — Codex, Cursor,
  Copilot, Claude Code, etc. Mais de 60 mil projetos open source usam.
  Ver <https://agents.md/>.
- **Desde a versão 2.1.277 do Claude Code (18/09/2026), ele lê `AGENTS.md` quando não
  existe um `CLAUDE.md` no projeto.** Dá pra ligar e desligar no `/config`. Confira a
  sua versão com `claude --version` antes de assumir qualquer coisa.
- **Se você tem os dois arquivos, ele lê o `CLAUDE.md`.** A ponte, nesse caso, é um
  import (`@AGENTS.md` na primeira linha do `CLAUDE.md`) ou um symlink
  (`ln -s AGENTS.md CLAUDE.md`). Ver
  <https://code.claude.com/docs/en/memory#agentsmd>.

Na prática: escreva as regras uma vez, no formato que fizer sentido pro seu time. Se o
time usa mais de um agente de código, o `AGENTS.md` é a escolha mais segura por padrão,
porque funciona em mais ferramentas sem duplicar arquivo.

> **Uma versão anterior deste arquivo dizia que o Claude Code não lia `AGENTS.md`.**
> Era verdade quando foi escrito e deixou de ser em 18/09. Isso virou conteúdo da aula 5
> (slide 20): doc de ferramenta muda debaixo do pé, e conferir a versão é hábito, não
> paranoia.

---

## Registro da sessão de 21/09 (produção do deck)

**O que foi produzido nesta sessão:**

- `P [M2] - S3 - AGENTS.md e Skills.pptx` — 41 slides, aula 5. Template PDA com os
  tokens extraídos do deck real do Módulo 1 (`P M1 - A2 - Coding Agents.pptx`),
  incluindo as duas estrelas como imagem, não como autoshape.
- `ROTEIRO-FACILITADORA.md` — reescrito: aula 5 minuto a minuto com slide por bloco, e
  aula 6 no novo formato.
- `SLIDES-OUTLINE.md` — reescrito pra bater com o deck construído.
- `excalidraw/aula6-red-team.excalidraw` — andaime da aula 6 (mesa de pareamento, três
  zonas de cenário em branco, relatório cruzado, mural de achados). O que a turma
  preenche ao vivo está tracejado e vazio.

**Decisões tomadas:**

1. **Aula 6 virou red team em duplas** (era lab guiado paralelo). Mudança pedida no
   brief. `README.md`, `GUIA-DO-ALUNO.md`, `ENTREGAVEL.md` e `PACOTE.md` foram
   ajustados; a rubrica somava 105% depois da mudança e foi recalibrada pra 100%.
2. **O relatório de validação saiu da entrega completa e entrou na mínima**, porque
   agora ele é produzido dentro da própria aula 6. A entrega completa ganhou
   `RESPOSTA-AO-RED-TEAM.md`: o relatório que o par escreveu sobre a sua skill, mais o
   que você mudou por causa dele.
3. **A afirmação "o Claude Code não lê AGENTS.md" foi corrigida** — mudou na v2.1.277,
   em 18/09. Em vez de corrigir em silêncio, virou conteúdo: notícia 1 do Giro das IAs
   (S4) e slide 20, onde a facilitadora assume o erro em sala e usa pra ensinar o hábito
   de conferir a versão antes de acreditar em tutorial.
4. **Objetivo 6 (Skill vs MCP) ganhou slide próprio** (S31), fechando os 6 objetivos do
   brief com rastreio no `SLIDES-OUTLINE.md`.

**Pendências pra Iasmim:**

- [ ] Preencher os 3 slots de print/GIF: **S12** (`CLAUDE.md` do `/init`), **S28**
      (skill `ajuda-geral` disparando errado), **S29** (barra do `/context` antes/depois).
- [ ] Trocar `<org>` no **S41**.
- [ ] Rodar `claude --version` e confirmar 2.1.277+ antes da aula (o S20 mostra ao vivo).
- [ ] Ensaiar a demo do erro proposital (**S13**) e confirmar que o agente edita
      `tests/` com o fraseado "faz esse teste passar".
- [ ] Conferir as 3 perguntas do recap (**S8**) contra o que a semana 2 de fato cobriu.
- [ ] Conferir se as 3 notícias do Giro ainda são as mais relevantes no dia da aula.
- [ ] `[CONFIRMAR NA ALURA]` a URL do curso avulso de segurança (pendência antiga).
