# Guia do aluno — Semana 3: AGENTS.md e skills

Este guia acompanha os slides da aula 5 e o red team em duplas da aula 6. Quando aparecer
**MÃO NA MASSA**, é a sua vez. Terminal aberto do lado o tempo todo.

Travou? Manda o erro no chat, segue em dupla — a solução não pode esperar o fim da
aula.

---

## Antes da aula 5 (confira, não refaça)

```bash
cd <pasta-do-seu-projeto-proprio>
git status                 # devia estar limpo ou com mudanças que você reconhece
cat CLAUDE.md               # devia existir e não ter nenhum TODO
claude
```

Dentro do Claude Code:

```
/context
```

Anote o número que aparece pro seu `CLAUDE.md` (linhas e % da janela). Você vai comparar
com esse número várias vezes hoje.

---

## AULA 5 — LAB 1: Regra ou ruído? (15 min)

O objetivo aqui não é escrever uma regra qualquer. É provar, com um teste antes/depois,
que a regra muda o comportamento do agente. Se não muda, ela não entra.

### 1. Escolha um erro real

Abra o Mural da Alucinação da turma (ou a sua própria lista de "coisas que o agente já
fez errado no meu projeto"). Escolha **um** erro concreto — algo que aconteceu de
verdade, não uma preocupação hipotética.

Exemplos do tipo de erro que vale (não copie — use o seu):
- O agente inventou o nome de uma biblioteca que não existe.
- Ele editou um arquivo de teste pra fazer o teste passar.
- Ele usou `let` onde o resto do projeto usa `const`, ou `==` onde o projeto usa `===`.
- Ele assumiu um formato de resposta de API que não é o real.

### 2. Escreva a regra candidata

Uma frase, verificável, no mesmo padrão do `CLAUDE.md` que você já tem. Teste rápido
antes de escrever: **"se essa linha sumir, o agente volta a errar do mesmo jeito?"**
Se a resposta for "não teria diferença", a regra não vale a pena — é coisa que o agente
já faz certo sozinho, e cada linha aqui custa token em toda sessão.

> ref: <https://code.claude.com/docs/en/best-practices#write-an-effective-claude-md> —
> a tabela ✅ incluir / ❌ excluir e o teste "removeria isso causaria erro?" são de lá.

### 3. Teste causal — antes e depois

```
# sessão 1: SEM a regra nova (comente a linha ou use uma cópia do CLAUDE.md sem ela)
peça exatamente a mesma tarefa que gerou o erro original
```

Anote o que o agente faz.

```
# sessão 2: COM a regra nova no CLAUDE.md
/clear
peça exatamente a mesma tarefa de novo
```

Anote se o comportamento mudou de verdade. **Só commita a regra se mudou.**

### 4. Se não mudou

Duas saídas possíveis, e a escolha é sua:
- **Descartar.** Não virou regra por bom motivo — não valia o token.
- **Virar skill, não regra.** Se o que você queria é um procedimento que só importa
  às vezes (não em toda sessão), isso é o assunto do Lab 2. Regra é o que precisa estar
  sempre lá. Skill é o que só precisa estar lá quando você for usar.

---

## AULA 5 — LAB 2: Sua primeira skill com progressive disclosure (25 min)

### 1. Escolha algo que você repete

Não é sobre a tarefa mais impressionante — é sobre a que você já fez mais de duas vezes
do mesmo jeito. Ideias por domínio (adapte pro seu projeto):

| domínio do catálogo | exemplo de skill |
|---|---|
| Listagem de perfis de alunos | gerar um card de perfil a partir de um briefing em texto solto |
| Captação de clientes / automações freelancer | montar uma proposta comercial a partir de 3 perguntas |
| Quiz conectado ao Claude | gerar uma nova pergunta no formato exato do seu schema |
| Avaliação automatizada de projetos | aplicar uma rubrica fixa a um repositório e devolver notas |
| Agente de revisão de código da PDA | comentar um PR no tom e nas regras do curso |
| Problema real da ONG | gerar um rascunho de e-mail ou relatório no tom institucional |
| Domínio próprio | qualquer tarefa do seu negócio que você já fez do mesmo jeito 2+ vezes |

### 2. Copie o esqueleto

```bash
mkdir -p .claude/skills/<seu-nome-de-skill>
cp starter/skill-skeleton/SKILL.md .claude/skills/<seu-nome-de-skill>/SKILL.md
cp starter/skill-skeleton/reference.md .claude/skills/<seu-nome-de-skill>/reference.md
```

Abra `SKILL.md` e complete os `TODO`. Preste atenção especial no `description`: é o
campo que faz o Claude decidir sozinho quando invocar a skill. Siga o padrão
`[o que faz]. Use quando [gatilho específico].` — vago demais e ela não dispara nunca
ou dispara sempre (falso positivo).

> ref: <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>
> — exemplos de description boa e ruim são de lá.

### 3. Force a progressive disclosure

Regra prática: se um pedaço do conteúdo só faz sentido **depois** que a skill já foi
invocada (um exemplo longo, um checklist grande, o formato exato de uma saída), ele vai
pro `reference.md`, não pro `SKILL.md`. O `SKILL.md` fica com o "o quê" e o "quando";
o `reference.md` fica com o "como, em detalhe".

### 4. Meça o contexto, antes e depois

```
/context
```

Anote o número. Agora invoque a skill:

```
/<seu-nome-de-skill>
```

```
/context
```

Anote de novo. **A diferença entre os dois números é a prova de que progressive
disclosure funciona** — o `reference.md` só entrou na janela quando você invocou, não
antes.

### 5. Rode uma vez de verdade

Use a skill numa tarefa real do seu projeto. Ela dispara? O resultado é o que você
esperava? Guarde esse primeiro teste — ele volta na aula 6.

---

## AULA 6 — RED TEAM EM DUPLAS (120 min)

Hoje você não constrói: você **quebra**. Nos primeiros 40 minutos você fecha a sua
própria skill. Depois, as duplas são sorteadas ao vivo e você passa o resto da aula
tentando fazer a skill **do seu colega** errar.

**Antes de começar:** você precisa da skill do Lab 2 (aula 5) **invocável**. Não precisa
estar bonita, nem completa. Precisa rodar quando alguém chama. Sem isso, a pessoa que
for sorteada com você fica sem o que testar.

### As 3 regras do jogo

1. **Você testa a skill do colega, não a sua.** É muito mais fácil ver o furo na skill
   de quem não escreveu ela — você não sabe o que ela "deveria" fazer, então só sobra o
   que está escrito.
2. **Sessão limpa em cada cenário.** `/clear` antes de cada um. O contexto que sobrou de
   quando a skill foi escrita esconde exatamente o furo que você está procurando.
3. **Cola o comando e a saída bruta, não a conclusão.** "Funcionou" não é evidência.

### Como a aula corre

| min | o que acontece |
|---|---|
| 0–10 | Abertura, as regras do jogo, você confirma que a sua skill invoca |
| 10–40 | **Fechamento individual** — você termina a sua skill até ela ficar invocável |
| 40–50 | **Sorteio das duplas ao vivo.** Você senta com quem foi sorteado e troca o caminho do repositório |
| 50–70 | **Cenários 1 e 2** na skill do colega |
| 70–90 | **Cenário 3** — o falso positivo, o difícil |
| 90–105 | **Relatório cruzado** — você preenche o relatório da skill dele e entrega pra ele |
| 105–115 | **Mural de achados** — alguns leem o achado mais surpreendente |
| 115–120 | Fechamento: o que falta pro entregável, prazo |

O sorteio é ao vivo de propósito. Se você soubesse com quem ia trocar, escreveria a
skill pensando na pessoa — e aí o teste não valeria nada.

### Como trocar as skills

Copie a pasta `.claude/skills/<nome>/` inteira do colega pro seu projeto — **não** o
repositório inteiro dele. Você vai rodar a skill dele no **seu** contexto, com o seu
projeto em volta. Isso é proposital: uma skill que só funciona no repositório de origem
tem a `description` amarrada em coisa que não está escrita nela.

### Os três cenários

Template completo em `starter/relatorio-validacao/TEMPLATE.md`. Em resumo:

**Cenário 1 — dispara quando deve.** Um pedido real, com as palavras que alguém usaria
de verdade. Não copie a frase de exemplo do `SKILL.md` dele: escreva do seu jeito.

**Cenário 2 — não dispara quando não deve.** Um pedido sem nenhuma relação com o que a
skill faz. Não disparar aqui é o resultado **certo**, não uma falha.

**Cenário 3 — o falso positivo.** O difícil. Pegue uma frase que usa as **mesmas
palavras** da `description` dele, mas num domínio completamente diferente. Se ela
disparar aqui, você achou o furo.

> **Bônus (não conta nota, conta na vida):** um quarto cenário, do seu próprio jeito de
> quebrar, que nenhum dos três cobre. Cole no relatório mesmo que não tenha quebrado.

### Se você chegou sem skill invocável

Você não fica de fora. Entra num trio como **validador extra** e entrega dois relatórios
em vez de um. Avise a facilitadora no começo da aula, não no min 40.

### O que você leva pra casa

- O relatório que **você** escreveu sobre a skill do colega.
- O relatório que **ele** escreveu sobre a sua.
- E a parte que é só sua: o que você vai mudar na sua skill depois de ler o relatório
  dele. Isso entra no entregável.

---

## Checklist de saída da semana

- [ ] `CLAUDE.md` do seu projeto tem pelo menos uma regra nova nascida de um erro real,
      testada antes/depois.
- [ ] `.claude/skills/<nome>/SKILL.md` com frontmatter completo e `reference.md`
      separado (ou justificativa escrita de por que não precisa de um).
- [ ] Print ou trecho de `/context` mostrando a diferença de tokens antes/depois de
      invocar a skill.
- [ ] Pelo menos um cenário de validação cruzada rodado na skill do colega, anotado.
- [ ] Commit feito, com `CLAUDE.md` e a skill dentro do repositório do seu projeto.

---

## Se algo deu errado

| sintoma | tenta isso |
|---|---|
| `/context` não existe ou dá erro | atualize o Claude Code (`claude update` ou reinstale pelo instalador da aula 1); confirme com `claude --version` |
| a skill não aparece em `/context` nem dispara sozinha | confira o caminho: tem que ser `.claude/skills/<nome>/SKILL.md`, dentro da raiz do seu projeto (ou de uma pasta acima dele) |
| a skill dispara em tarefas que não têm nada a ver | a `description` está genérica demais — reescreva com o padrão "o que faz + quando usar", com termos-chave específicos do seu domínio |
| a skill nunca dispara sozinha, só com `/nome` | normal se você marcou `disable-model-invocation: true` de propósito; se não marcou, o `description` provavelmente está vago |
| `allowed-tools` bloqueia a skill toda hora | ela está pedindo mais ferramenta do que você liberou — decida se a ferramenta é mesmo necessária antes de simplesmente liberar tudo |
| criei `AGENTS.md` mas o Claude Code não usa | rode `claude --version`: da **2.1.277** (18/09/2026) em diante ele lê `AGENTS.md` quando **não existe** `CLAUDE.md` no projeto. Se você tem os dois, ele lê o `CLAUDE.md` — a ponte é `@AGENTS.md` na primeira linha dele, ou `ln -s AGENTS.md CLAUDE.md` (no Windows sem WSL, use o import: symlink pede administrador). Também dá pra ligar/desligar o comportamento em `/config` |
| Windows: `ln -s` não funciona | rode o Git Bash ou PowerShell como Administrador, ou simplesmente use o import `@AGENTS.md` em vez do symlink — funciona igual e não pede privilégio nenhum |
| meu par faltou e não sei quem valida minha skill | fala com a facilitadora depois da aula — você entra no banco de reposição, não fica sem validação |
| `/context` mostra número diferente do esperado depois do `/clear` | esperado — `/clear` reseta a conversa, mas o `CLAUDE.md` do projeto recarrega sozinho na próxima leitura |
