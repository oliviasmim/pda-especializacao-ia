import io, os, sys, re
D = os.path.expanduser("~/mnt/pda-especializacao-ia/aula5-agents-md-skills")

def rd(f): return io.open(os.path.join(D,f), encoding='utf-8').read()
def wr(f,s): io.open(os.path.join(D,f),'w',encoding='utf-8').write(s)
def sub(s, a, b, label):
    assert a in s, "NAO ACHOU: " + label
    return s.replace(a, b, 1)

# ───────────────────────── README.md
r = rd('README.md')
r = sub(r,
"""> Aula 5 (conceito + demo) e aula 6 (lab guiado paralelo). A numeração é por aula, não
> por semana — semana 3 = aulas 5 e 6.""",
"""> Aula 5 (conceito + demo) e aula 6 (**red team em duplas**). A numeração é por aula,
> não por semana — semana 3 = aulas 5 e 6.""", "readme header")

r = sub(r,
"""- **Aula 6** — lab guiado paralelo: a facilitadora escreve uma skill ao vivo, do zero,
  e você acompanha construindo a sua, no seu projeto, checkpoint a cada 20 minutos. No
  último checkpoint, você troca de skill com a sua dupla e tenta quebrar a dela.""",
"""- **Aula 6** — red team em duplas: você fecha a sua skill nos primeiros 40 minutos, as
  duplas são sorteadas ao vivo, e o resto da aula você **valida a skill do colega** em
  três cenários (dispara quando deve, não dispara quando não deve, e o falso positivo).
  No fim, relatório cruzado: você entrega o relatório da skill dele, ele entrega o da
  sua.""", "readme aula6")

r = sub(r,
"""- **`AGENTS.md`** é um formato aberto, mantido pela Agentic AI Foundation (Linux
  Foundation), pensado pra funcionar em qualquer agente de código — Codex, Cursor,
  Copilot, Claude Code, etc. Ver <https://agents.md/>.
- **O Claude Code não lê `AGENTS.md` diretamente. Ele lê `CLAUDE.md`.** Se o seu
  repositório já tem um `AGENTS.md` (de outro agente, ou porque seu time decidiu
  padronizar nele), a ponte é um import (`@AGENTS.md` dentro do `CLAUDE.md`) ou um
  symlink (`ln -s AGENTS.md CLAUDE.md`). Isso está documentado, com exemplo, em
  <https://code.claude.com/docs/en/memory#agentsmd>.

Na prática: você escreve as regras uma vez, no formato que fizer sentido pro seu time,
e decide se aponta pra elas com import ou com symlink. O `GUIA-DO-ALUNO.md` mostra os
dois jeitos.""",
"""- **`AGENTS.md`** é um formato aberto, mantido pela Agentic AI Foundation (Linux
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
> paranoia.""", "readme agents")
wr('README.md', r)

# ───────────────────────── GUIA-DO-ALUNO.md
g = rd('GUIA-DO-ALUNO.md')
g = sub(g,
"""| criei `AGENTS.md` mas o Claude Code não usa | ele não lê `AGENTS.md` direto — crie `CLAUDE.md` com `@AGENTS.md` na primeira linha, ou `ln -s AGENTS.md CLAUDE.md` (no Windows sem WSL, use o import, não o symlink — symlink pede administrador) |""",
"""| criei `AGENTS.md` mas o Claude Code não usa | rode `claude --version`: da **2.1.277** (18/09/2026) em diante ele lê `AGENTS.md` quando **não existe** `CLAUDE.md` no projeto. Se você tem os dois, ele lê o `CLAUDE.md` — a ponte é `@AGENTS.md` na primeira linha dele, ou `ln -s AGENTS.md CLAUDE.md` (no Windows sem WSL, use o import: symlink pede administrador). Também dá pra ligar/desligar o comportamento em `/config` |""", "guia faq agents")

i = g.index("## AULA 6 — Lab guiado paralelo")
j = g.index("## Checklist de saída da semana")
novo = """## AULA 6 — RED TEAM EM DUPLAS (120 min)

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

"""
g = g[:i] + novo + g[j:]
wr('GUIA-DO-ALUNO.md', g)

# ───────────────────────── ENTREGAVEL.md
e = rd('ENTREGAVEL.md')
e = sub(e,
"""Duas faixas, como sempre: a **mínima** você fecha ainda no dia da aula 6. A **completa**
é a que prova progressive disclosure de verdade e fecha a validação cruzada.""",
"""Duas faixas, como sempre: a **mínima** você fecha ainda no dia da aula 6 — o red team
em duplas produz o relatório cruzado dentro da própria aula. A **completa** é a que
prova progressive disclosure em número e mostra o que você mudou depois de ler o
relatório que o seu par escreveu sobre a sua skill.""", "entregavel intro")

e = sub(e,
"""**Mínima:**
1. Uma regra nova no `CLAUDE.md` do seu projeto, nascida de um erro real observado —
   com a prova do teste antes/depois (o que o agente fez sem a regra, o que fez com ela).
2. Uma skill própria (`SKILL.md` com `name`, `description` e `allowed-tools`
   preenchidos, nada de `TODO`).
3. O parágrafo pro dono do negócio (ver modelo abaixo).

**Completa (tudo da mínima +):**
4. A mesma skill com progressive disclosure de verdade: um `reference.md` (ou mais de
   um arquivo) separado do `SKILL.md`, e a prova em número — `/context` antes e depois
   de invocar a skill, mostrando a diferença.
5. `RELATORIO-VALIDACAO.md` da skill do **seu colega de dupla**, cobrindo os três
   cenários (ver `starter/relatorio-validacao/TEMPLATE.md`):
   - dispara quando deve
   - não dispara quando não deve
   - falso positivo (um cenário parecido, mas que não deveria disparar)""",
"""**Mínima:**
1. Uma regra nova no `CLAUDE.md` do seu projeto, nascida de um erro real observado —
   com a prova do teste antes/depois (o que o agente fez sem a regra, o que fez com ela).
2. Uma skill própria (`SKILL.md` com `name`, `description` e `allowed-tools`
   preenchidos, nada de `TODO`), invocável.
3. `RELATORIO-VALIDACAO.md` da skill do **seu par no red team**, cobrindo os três
   cenários (ver `starter/relatorio-validacao/TEMPLATE.md`):
   - dispara quando deve
   - não dispara quando não deve
   - falso positivo (mesmas palavras da `description`, domínio diferente)
4. O parágrafo pro dono do negócio (ver modelo abaixo).

**Completa (tudo da mínima +):**
5. A mesma skill com progressive disclosure de verdade: um `reference.md` (ou mais de
   um arquivo) separado do `SKILL.md`, e a prova em número — `/context` antes e depois
   de invocar a skill, mostrando a diferença.
6. `RESPOSTA-AO-RED-TEAM.md`: o relatório que o **seu par** escreveu sobre a **sua**
   skill, e embaixo, em 3 a 6 linhas, o que você mudou por causa dele — ou por que
   decidiu não mudar. Essa parte é sua, não dele.""", "entregavel o que entregar")

e = sub(e,
"""3. Rode a skill do seu colega de dupla (ou trio, se for o caso — ver pareamento no
   `GUIA-DO-ALUNO.md`) contra os três cenários do template. Cole comando + resultado
   bruto pra cada um, não só a conclusão.
4. Escreva o parágrafo pro dono do negócio.""",
"""3. Na aula 6, rode a skill do seu par (ou dos dois, se você caiu num trio como
   validador extra — ver `GUIA-DO-ALUNO.md`) contra os três cenários do template. Cole
   comando + resultado bruto pra cada um, não só a conclusão. **Sessão limpa em cada
   cenário.**
4. Leia o relatório que o seu par escreveu sobre a sua skill e escreva o que você mudou
   por causa dele (ou por que não mudou).
5. Escreva o parágrafo pro dono do negócio.""", "entregavel passo 3")

e = sub(e,
"""5. Copie os artefatos pra `aula5-agents-md-skills/entrega/` no seu fork:
   ```
   entrega/
   |-- CLAUDE-md-diff.md        # a regra nova + o teste antes/depois
   |-- skill/                   # cópia de .claude/skills/<nome>/ do seu projeto
   |-- RELATORIO-VALIDACAO.md   # a validação da skill do colega
   `-- paragrafo-dono-negocio.md
   ```
6. Commit, push, cole o link do repositório do seu projeto próprio no formulário.""",
"""6. Copie os artefatos pra `aula5-agents-md-skills/entrega/` no seu fork:
   ```
   entrega/
   |-- CLAUDE-md-diff.md         # a regra nova + o teste antes/depois
   |-- skill/                    # cópia de .claude/skills/<nome>/ do seu projeto
   |-- RELATORIO-VALIDACAO.md    # a validação que VOCÊ fez na skill do seu par
   |-- RESPOSTA-AO-RED-TEAM.md   # (completa) o relatório dele sobre a sua + o que você mudou
   `-- paragrafo-dono-negocio.md
   ```
7. Commit, push, cole o link do repositório do seu projeto próprio no formulário.""", "entregavel arvore")

e = sub(e,
"""| Validação cruzada nos 3 cenários | 25% | dispara quando deve / não dispara quando não deve / falso positivo — cada um com evidência bruta |
| Parágrafo pro dono do negócio | 15% | sem jargão, nomeia o problema resolvido e o que evita de errado |""",
"""| Validação cruzada nos 3 cenários | 25% | dispara quando deve / não dispara quando não deve / falso positivo — cada um com evidência bruta, sessão limpa |
| Resposta ao red team | 10% | o que você mudou depois de ler o relatório sobre a sua skill, ou por que não mudou |
| Parágrafo pro dono do negócio | 10% | sem jargão, nomeia o problema resolvido e o que evita de errado |""", "entregavel rubrica")

e = sub(e,
"""- Bloco da Alura desta semana concluído (Context Engineering — ver `README.md`).
- `CLAUDE.md` funcional no repositório do seu projeto próprio, sem `TODO`, commitado.
- Ter feito o Lab 1 e o Lab 2 da aula 5, e os checkpoints da aula 6.""",
"""- Bloco da Alura desta semana concluído (Context Engineering — ver `README.md`).
- `CLAUDE.md` funcional no repositório do seu projeto próprio, sem `TODO`, commitado.
- Ter feito o Lab 1 e o Lab 2 da aula 5.
- **Chegar na aula 6 com a skill invocável** — sem ela, o seu par fica sem o que testar.""", "entregavel prereq")

e = sub(e,
"""- [ ] (Completa) Os três cenários do relatório de validação têm comando + resultado
      bruto colado, não só "funcionou" / "não funcionou".""",
"""- [ ] Os três cenários do relatório de validação têm comando + resultado bruto colado,
      não só "funcionou" / "não funcionou".
- [ ] O relatório é sobre a skill do **seu par**, não sobre a sua.""", "entregavel checklist")

e = sub(e,
"""- Crie o `AGENTS.md` do seu projeto (o formato aberto) e aponte seu `CLAUDE.md` pra
  ele com `@AGENTS.md`. Teste se outro agente (Cursor, Codex, o que você tiver à mão)
  consegue ler o mesmo arquivo sem duplicar regra nenhuma.""",
"""- Crie o `AGENTS.md` do seu projeto (o formato aberto). Se o seu Claude Code é 2.1.277
  ou mais novo e você **não** tem `CLAUDE.md`, ele já lê o `AGENTS.md` direto. Se tem os
  dois, aponte o `CLAUDE.md` pra ele com `@AGENTS.md`. Depois teste com outro agente
  (Cursor, Codex, o que você tiver à mão) e veja se os dois leem a mesma regra sem
  duplicar arquivo.""", "entregavel bonus")
wr('ENTREGAVEL.md', e)

print("patch aplicado: README.md, GUIA-DO-ALUNO.md, ENTREGAVEL.md")
