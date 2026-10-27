# Guia de conteúdo · @sempremaagra

Cada post é um carrossel de **7 slides** que conta a história de **uma personagem fictícia** e termina com a chamada para o guia **Shape no Bolso** ("Comente QUERO").

## Público

Mulheres de 25 a 50 anos que **já tentaram de tudo pra emagrecer e não conseguiram**: efeito sanfona, dietas da moda, culpa, falta de tempo e de dinheiro, cansaço de começar de novo toda segunda-feira.

## Tom de voz

- Acolhedor e direto, como uma amiga que entende do assunto. Português do Brasil, frases curtas.
- A mensagem central é sempre esta: **o problema nunca foi ela, foi o método.**
- Comida de verdade (arroz, feijão, ovo, frango, fígado, legumes, banana, aveia), proteína em todas as refeições, treino de força em casa, constância e sono.
- Pode ser direto e provocativo: ganchos com datas e prazos ("chegar no Natal mais magra", "projeto verão"), urgência, frases fortes e o preço do ebook quando fizer sentido.

## Regras obrigatórias (só estas quatro)

1. **Personagem sempre fictícia:** só primeiro nome, idade e profissão comum. Nunca use nome de pessoa real, influenciadora ou famosa. Nunca use fotos.
2. **Resultados realistas:** em 12 semanas, de −3 a −6 kg e de −4 a −8 cm de cintura (em prazos menores, proporcionalmente menos). Perda de no máximo ~1% do peso por semana.
3. **O slide de resultado (tipo `resultado`) é obrigatório**, porque é ele que traz o aviso "Personagem e resultados ilustrativos. Os resultados variam de pessoa para pessoa." Esse aviso também vai em toda legenda.
4. **Não recomendar** remédios, canetas emagrecedoras, chás ou termogênicos "emagrecedores", jejum prolongado ou dietas abaixo de 1.200 kcal. Pode citá-los como coisas que a personagem tentou e que não funcionaram.

Fora isso, está tudo liberado. Também vale: **não repita** personagem, profissão ou ângulo publicados nos últimos 30 posts (veja `historico.md`).

**Preço do ebook:** R$ 28,99 (pagamento único, PDF). Pode citar no slide 7 ou na legenda, sempre deixando claro que é o preço do guia, e não o gasto diário com comida.

## Ângulos de história (vá rodando; crie novos parecidos)

- Efeito sanfona depois de anos de dieta
- Mãe sem tempo que come o resto do prato dos filhos
- Trabalha em plantão ou turno da noite
- Belisca o dia todo e "não come nada"
- Pulava o café da manhã e atacava à noite
- Achava que precisava de academia cara
- Gastava muito com produtos "fit" e suplementos
- Pós-gestação, sem energia
- 40+, achava que "o metabolismo travou"
- Ansiedade e doce à noite (sem diagnóstico; foco em rotina e proteína)
- Fim de semana que "estraga" a semana
- Só fazia cardio e não via mudança
- Dieta da sopa, do ovo, do shake, low carb radical
- Tinha vergonha de treinar perto de outras pessoas (treino em casa)
- Orçamento apertado e família grande
- Trabalha em home office e não sai da cadeira
- Viaja a trabalho e come em restaurante
- Começou e parou 10 vezes; desta vez foi um hábito por semana

## Estrutura dos 7 slides (arquivo `post.json`)

| Slide | tipo | Função |
|---|---|---|
| 1 | `capa` | Gancho na voz dela, entre aspas. Use `adesivos` (até 6, curtos, até ~20 caracteres) com o que ela tentou ou com os hábitos que a travavam, mais um `arremate` curto. |
| 2 | `tabela` ou `texto` | O problema na prática: a lista de dietas (perdeu/voltou), um dia típico ou os gastos. |
| 3 | `grafico` ou `texto` | **Não era culpa dela**: explica o porquê em 2 ou 3 blocos simples. |
| 4 | `texto` | A virada na alimentação: 3 blocos com `icone` de comida e uma `citacao`. |
| 5 | `texto` | Treino de força em casa ou movimento: 3 blocos com `icone` de exercício, ou blocos numerados. |
| 6 | `resultado` | 12 semanas depois: `valores` (gráfico de queda suave), 3 `numeros` e uma `citacao`. |
| 7 | `cta` | Frase de virada ("Você não falhou...") e 4 `itens` do guia. |

Formatação nos textos: `*palavra*` = destaque verde; `!palavra!` = destaque coral; `**palavra**` = negrito.

**Limites de tamanho** (para nada sair do slide): título do slide 1 com até ~60 caracteres; títulos dos slides 2 a 7 com até ~70; `texto` com até ~120; até 4 linhas na `tabela`; até 4 `blocos`; `citacao` com até ~110 caracteres.

**Ícones de comida:** egg, fried_egg, banana, drumstick, beans, rice, oats, milk, sweet_potato, liver, sardine, pts, peanut, cabbage, carrot, bread, lentil.
**Ícones de exercício:** agachamento, flexão, afundo, mergulho, ponte, prancha, remada, superman, abdominal, polichinelo.

Veja `exemplo/post.json` como modelo completo.

## Itens do guia que podem aparecer no CTA (escolha 4)

- Como calcular **quanto comer**, sem passar fome
- **Cardápios prontos** com arroz, feijão e comida de casa
- **Treino de força em casa**, em 35 minutos
- Um **plano de 30 dias**, um hábito de cada vez
- **Marmitas** para a semana em 2 horas no domingo
- **Lista de compras do mês** que cabe no orçamento
- O que vale e o que **não vale** comprar de suplemento

## Legenda (até 2.000 caracteres)

1. Primeira linha: gancho forte (a frase da capa ou a dor dela).
2. Três a seis parágrafos curtos contando a história, com emojis com moderação (🥚🍚🏠🚶‍♀️💚).
3. Frase de virada em negrito-de-Instagram (sem markdown; use MAIÚSCULAS em uma ou duas palavras, no máximo).
4. CTA: `📩 Comente QUERO que eu te mando o link do guia Shape no Bolso, ...`
5. Aviso: `Personagem e resultados ilustrativos. Os resultados variam de pessoa pra pessoa.`
6. 10 a 12 hashtags, sempre com #shapenobolso #sempremagra.

Não use asteriscos ou markdown na legenda: o Instagram mostra os símbolos.
