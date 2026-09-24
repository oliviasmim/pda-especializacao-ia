# 🤖 Semana 3 — AGENTS.md e skills: Atividade Prática (Entregável)

**Módulo 2 — AI Orchestrator / Contexto**

|  |  |
| :---- | :---- |
| **Material da aula** | `aula5-agents-md-skills/` no seu fork de pda-especializacao-ia |
| **Repositório do projeto** | seu repositório próprio (criado na semana 2) |
| **Formulário de entrega** | https://forms.gle/PSd6i65g44GwBMgq6 |
| **Prazo de entrega** | Antes da aula 1 da semana 4 |

O que você entrega no formulário é o **link do repositório do seu projeto próprio no
GitHub**, com a skill já commitada (e, na faixa completa, publicada — ver passo 4 do
passo a passo).

---

## O que você vai entregar

**Mínima:**
1. Uma skill própria (`SKILL.md` com `name`, `description` e `allowed-tools`
   preenchidos, nada de `TODO`), invocável.

**Completa (tudo da mínima +):**
2. A mesma skill com progressive disclosure de verdade: um `reference.md` (ou mais de
   um arquivo) separado do `SKILL.md`.
3. A skill **publicada no GitHub**, seguindo a documentação oficial de criação de
   skills — ver "Como publicar sua skill no GitHub" no passo a passo.

---

## Material de apoio (sem Alura)

Turmas sem acesso à Alura: comece por aqui em vez do bloco indicado no `README.md`.
São leituras em português que cobrem o mesmo terreno — a decisão entre regra
permanente e skill sob demanda, e como uma skill é estruturada de verdade:

- [Engenharia de contexto para agentes de IA: 3 arquivos que apresentam sua empresa ao Claude](https://interney.net/engenharia-de-contexto-agentes-ia/) — as técnicas de engenharia de contexto (retrieval just-in-time, compactação, notas estruturadas, subagentes) e por que isso muda como você organiza `AGENTS.md`/`CLAUDE.md`.
- [AGENTS.md: Context Engineering para Agentes de IA](https://blog.codedimension.com.br/post/agents-md-context-engineering-skills-rules/) — a diferença prática entre `AGENTS.md`, skills e regras.
- [Agent Skills: o que são e como criar para agentes de IA](https://www.distrito.me/blog/agent-skills-o-que-sao-como-funcionam-como-criar-habilidades-para-agentes-de-ia) — estrutura de uma skill, frontmatter, exemplos de `SKILL.md`.
- [Extend Claude with skills — documentação oficial](https://code.claude.com/docs/en/skills) — a referência que vale mais: todos os campos do frontmatter (`name`, `description`, `allowed-tools` etc.), progressive disclosure com arquivos de apoio, e como skills são compartilhadas via git. Em inglês, mas é a fonte primária — use como consulta, não como leitura corrida.

## Pré-requisitos

- Ter lido pelo menos um material da lista acima (ou o bloco da Alura, se você tiver
  acesso).
- `CLAUDE.md` funcional no repositório do seu projeto próprio, sem `TODO`, commitado.
- Ter feito o Lab 1 e o Lab 2 da aula 5.
- **Chegar na aula 6 com a skill invocável** — sem ela, o seu par fica sem o que testar.

## Passo a passo

1. Feche o `SKILL.md` da sua skill (Lab 2, aula 5): `name` claro, `description` que
   nomeia o gatilho específico do seu domínio (não copiada de exemplo), `allowed-tools`
   restrito ao mínimo necessário — nada de liberar tudo. Nada de `TODO`.
2. Rode a skill numa tarefa real do seu projeto e confirme que ela dispara sozinha (ou,
   se `disable-model-invocation: true`, que dispara ao ser chamada por nome). Guarde o
   comando e o resultado — vale como prova em caso de dúvida.
3. **(Completa)** Separe o material de referência do `SKILL.md`: crie um `reference.md`
   (ou mais de um arquivo) na pasta da skill com o conteúdo detalhado, e deixe no
   `SKILL.md` só o essencial pra decidir se/quando disparar, com um link pro
   `reference.md`. Se você decidir que **nada** merece sair do `SKILL.md`, tudo bem —
   mas escreva por quê, isso também é uma decisão válida.
4. **(Completa) Como publicar sua skill no GitHub:**
   - Confirme que a pasta da skill está em `.claude/skills/<nome-da-skill>/` dentro do
     repositório do seu projeto — é o local que a
     [documentação oficial](https://code.claude.com/docs/en/skills) descreve como
     "compartilhado com o time via git", porque qualquer pessoa que clonar o repo já
     recebe a skill.
   - Adicione um `README.md` curto **dentro da pasta da skill** (ou uma seção no
     README do projeto) explicando em 2-3 frases o que ela faz e como alguém de fora
     poderia usá-la: copiar a pasta pra dentro do próprio `.claude/skills/` de outro
     projeto e reiniciar o Claude Code.
   - Commite e dê push pro repositório do seu projeto no GitHub. Confira, num
     navegador anônimo (ou pedindo pra alguém abrir o link), que a pasta
     `.claude/skills/<nome-da-skill>/` aparece no repositório.
   - Pra ver como fica uma skill pensada pra ser reaproveitada por outras pessoas,
     dê uma olhada no [repositório público de skills da Anthropic](https://github.com/anthropics/skills) — não pra copiar conteúdo, só pra ver o padrão de organização.
5. Cole o link do repositório do seu projeto (com a skill já commitada e, na faixa
   completa, publicada) no formulário de entrega.

**Exemplo modelo (domínio 1 do catálogo — Listagem de perfis de alunos da PDA):**

> Quando a gente pede pra uma IA genérica montar o perfil de um aluno, ela às vezes
> inventa informação que não foi dada — um curso que a pessoa não fez, uma habilidade
> que ela não tem. Isso já aconteceu aqui. A correção não foi "pedir com mais cuidado"
> toda vez: foi ensinar pro sistema, de forma permanente, a regra "nunca preencha um
> campo do perfil que não veio no briefing — deixe em branco e avise". Agora, toda vez
> que alguém gera um perfil, essa regra vale, sem precisar lembrar de repetir o pedido.
> E quando a tarefa é mais específica — gerar o perfil num formato exato pro site —
> o sistema só carrega essas instruções detalhadas na hora de usar, não o tempo todo.
> Isso significa respostas mais confiáveis e um sistema mais barato de rodar.

## Checklist antes de entregar

- [ ] O `SKILL.md` não tem `TODO`, tem `name` e `description` específicos (nomeia o
      gatilho), `allowed-tools` restrito (não liberou tudo).
- [ ] A skill dispara pelo menos uma vez de verdade, numa tarefa real do seu projeto —
      não um teste de brinquedo.
- [ ] (Completa) Existe `reference.md` separado, ou a decisão de não ter um está
      justificada por escrito.
- [ ] (Completa) A pasta `.claude/skills/<nome>/` está commitada e com push feito no
      GitHub, com o README curto explicando o que a skill faz.
- [ ] O link colado no formulário é do repositório do **seu projeto**, não do fork do
      curso.

---

## Rubrica

| critério | peso | o que eu olho |
|---|---|---|
| Skill própria válida | 50% | frontmatter completo, `description` com gatilho específico do domínio, `allowed-tools` restrito, dispara pelo menos uma vez de verdade |
| Progressive disclosure | 30% | `reference.md` separado com uso real, ou justificativa honesta de por que não precisa |
| Skill publicada no GitHub | 20% | `.claude/skills/<nome>/` commitada e com push no repositório do projeto, com README curto explicando o que ela faz |

O que **não** pontua: uma skill com `description` copiada de exemplo sem adaptar ao
seu domínio; "funciona" sem mostrar o comando que você rodou; `allowed-tools` liberando
tudo porque "deu preguiça de restringir".

## Bônus (sem peso na nota, com peso na vida)

- Se você fez o red team em duplas da aula 6, tente um **quarto cenário** na skill do
  seu colega — um jeito de quebrá-la que nenhum dos três padrão cobre. Vale a pena
  registrar, mesmo que não tenha quebrado nada.
- Crie o `AGENTS.md` do seu projeto (o formato aberto). Se o seu Claude Code é 2.1.277
  ou mais novo e você **não** tem `CLAUDE.md`, ele já lê o `AGENTS.md` direto. Se tem os
  dois, aponte o `CLAUDE.md` pra ele com `@AGENTS.md`. Depois teste com outro agente
  (Cursor, Codex, o que você tiver à mão) e veja se os dois leem a mesma regra sem
  duplicar arquivo.
