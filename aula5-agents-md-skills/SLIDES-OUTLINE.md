# SLIDES-OUTLINE — Semana 3 (Aula 5): AGENTS.md e Skills

Arquivo: `P [M2] - S3 - AGENTS.md e Skills.pptx` · **41 slides** · template PDA
(fundo `2A042E`, amarelo `EDDC11`, Dela Gothic One / IBM Plex Sans / IBM Plex Mono,
estrela real extraída do deck do Módulo 1).

Aula 6 não tem deck: é red team em duplas, roda no Excalidraw
(`excalidraw/aula6-red-team.excalidraw`).

**Fio condutor:** *"Até você contar pra ela."* — S2 planta, S14 aplica à regra, S37 fecha.

## Rastreio dos objetivos

| objetivo | slides dedicados |
|---|---|
| 1 · AGENTS.md/CLAUDE.md curto, específico e verificável | **S17**, S15, S16, S21 (Lab 1) |
| 2 · por que a IA não deve gerar sozinha o arquivo de regras | **S10–S16** (demo do `/init` + erro proposital) |
| 3 · rules sempre carregadas vs skills sob demanda + custo | **S22–S26**, S29, S30 |
| 4 · hierarquia projeto / global / pessoal | **S18**, S19 (CLAUDE.md) · **S34** (skills) |
| 5 · skill com Progressive Disclosure + validar a de outra pessoa | **S25**, S30, S35, S36 (Lab 2), S39 (aula 6) |
| 6 · Skill (conhecimento) vs MCP/Tool (capacidade) | **S31** |

Teto de 3 slides consecutivos sem recurso visual: respeitado. Terminais, cards,
tabelas, diagramas de hierarquia e os 3 slots de print contam; a estrela não.

## Slots a preencher (nenhuma imagem foi inventada)

| slide | o que vai ali |
|---|---|
| S12 | print do `CLAUDE.md` que o `/init` gerou ao vivo |
| S28 | print da skill `ajuda-geral` disparando numa tarefa sem relação |
| S29 | GIF ou print da barra do `/context` antes e depois da skill gorda |

Também precisa: trocar `<org>` no S41.

---

## Mapa dos slides

### Bloco 0 — Abertura e Giro das IAs (0–10)

| # | slide | componente |
|---|---|---|
| S1 | Capa — `</MÓDULO 2 · AULA 5>` AGENTS.MD E SKILLS | painel amarelo + estrela grande |
| S2 | Fio condutor: **ATÉ VOCÊ CONTAR PRA ELA.** | frase isolada Dela 60pt |
| S3 | Giro das IAs — as 3 manchetes | 3 cards + infoBox |
| S4 | Giro 1 · CLAUDE.md e AGENTS.md, agora os dois valem | infoBox TL;DR + steps + ref |
| S5 | Giro 2 · O aumento de 25% que é queda de 17% | infoBox + terminal com a conta |
| S6 | Giro 3 · O relógio do GPT-5.5 começou a contar | infoBox + steps |

### Bloco 0.5 — Recap ativo, conduzido por eles (10–25)

| # | slide | componente |
|---|---|---|
| S7 | Antes de seguir: o que ficou da semana passada? | frase grande |
| S8 | 3 perguntas, quem responde é sorteado | 3 cards (o 3º em destaque) |
| S9 | **Hoje você toma 4 decisões** — o mapa dos objetivos | tabela decisão / pergunta / onde aparece |

### Bloco 1 — Quem escreve a regra (27–55)

| # | slide | componente |
|---|---|---|
| S10 | Kicker: ELE LÊ SEU CÓDIGO. ELE NUNCA VIU VOCÊ ERRANDO NELE. | frase-âncora |
| S11 | Demo · `/init` ao vivo + a pergunta pra turma | terminal + infoBox |
| S12 | O CLAUDE.md genérico que voltou | **slot de print** + steps |
| S13 | ⚠ **Agora eu deixo quebrar** — o erro proposital | 2 cards (sem a regra / com a regra) |
| S14 | Ninguém sabe qual é a regra antes do erro acontecer | infoBox + steps |
| S15 | Regra é memória de erro — o CLAUDE.md com origem citada | terminal |
| S16 | Mesmo arquivo, histórico diferente | 2 cards + infoBox |
| S17 | **Objetivo 1** · curto, específico, verificável + entra/fica de fora | 3 cards + tabela |
| S18 | **Objetivo 4** · hierarquia: quem ganha o conflito | 4 faixas + seta lateral |
| S19 | Em qual arquivo você escreve a exceção? | 2 cards + infoBox |
| S20 | AGENTS.md e CLAUDE.md — o que mudou na quinta | terminal + steps (gancho do Giro 1) |
| S21 | **LAB 1 · REGRA OU RUÍDO?** — 15 min | labPanel + 5 passos |

### Bloco 2 — Sempre carregado ou sob demanda (70–90)

| # | slide | componente |
|---|---|---|
| S22 | Kicker: CLAUDE.MD CUSTA TOKEN EM TODA SESSÃO | frase-âncora |
| S23 | A pergunta certa não é "isso é importante?" | 2 infoBox |
| S24 | **Objetivo 3** · o que cada coisa custa na janela | tabela oficial de custo |
| S25 | Três níveis, como um manual (progressive disclosure) | 3 cards com os números |
| S26 | Mede antes de opinar — `/context` linha de base | terminal + infoBox |
| S27 | A skill gorda, ao vivo | terminal (frontmatter errado) + steps |
| S28 | Falso positivo | **slot de print** + steps |
| S29 | O salto, medido | **slot de GIF** + 3 cards |
| S30 | A mesma skill, enxuta | 3 cards (antes / corpo / apêndice) |
| S31 | **Objetivo 6** · Skill é conhecimento. MCP é capacidade | 2 cards + infoBox |
| S32 | O arquivo inteiro — anatomia do SKILL.md | terminal + tabela de campos |
| S33 | **Faz X. Use quando Y.** — falso positivo / calibrada / falso negativo | 3 cards |
| S34 | **Objetivo 4** · duas skills com o mesmo nome: qual roda? | 4 faixas + alerta de inversão |
| S35 | Três cenários. Sempre os três | 3 cards |
| S36 | **LAB 2 · A SUA PRIMEIRA SKILL** — 25 min | labPanel + 5 passos |

### Fechamento (115–120)

| # | slide | componente |
|---|---|---|
| S37 | O que fica — 6 cards de recap | grade 2×3 + infoBox do fio condutor |
| S38 | Atividade de fixação — mínima e completa | 2 cards |
| S39 | `</DEMO DAY>` · **RED TEAM EM DUPLAS** (aula 6) | frase grande + steps + infoBox |
| S40 | Links (7) | lista numerada |
| S41 | Dúvidas e suporte | painel amarelo + contato |

---

## Decisões de construção

- **Aula 6 virou red team em duplas**, substituindo o lab guiado paralelo que estava no
  mapeamento de formatos da skill `pda-aula`. Decisão da Iasmim neste brief.
- **S20 existe porque o material estava desatualizado.** A afirmação "o Claude Code não
  lê AGENTS.md" era verdade quando o material foi escrito e deixou de ser em 18/09
  (v2.1.277). Em vez de só corrigir em silêncio, a mudança virou conteúdo: a facilitadora
  assume o erro em sala e usa pra ensinar o hábito de conferir a versão.
- **S34 é uma pegadinha proposital.** Na hierarquia de skills, pessoal vence projeto —
  o contrário do `CLAUDE.md`. Perguntar antes de mostrar.
- Nenhum slide menciona a Alura (ela vive no `ENTREGAVEL.md` e no roteiro).
- Nenhum lab exige API key. Tudo roda com a conta Claude Pro (semana ≤ 10).
