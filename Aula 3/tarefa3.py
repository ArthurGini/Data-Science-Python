"""
@Author: Arthur Briganti Gini
RA: 213253
e-mail: a213253@dac.unicamp.br


Analisando os dados do jogo de dados CRAPS

Você deverá simular diversas rodadas do CRAPS rastreando o número total de jogos ganhos e perdidos no primeiro lançamento,
 no segundo lançamento, no terceiro lançamento, etc. Resuma os resultados do seguinte modo:

    Exibir um gráfico de barra horizontal indicando quantos jogos foram ganhos e como muitos são perdidos no primeiro lançamento,
    segundo lançamento,terceiro lançamento, etc. Uma vez que o jogo poderia continuar indefinidamente,
    você pode acompanhar as vitórias e derrotas na primeira dúzia lançamentos (de um par de dados),
      em seguida, manter dois contadores que controlam as vitórias e perdas após 12 lançamentos -
      não importa quanto tempo o jogo lee. Crie barras separadas para vitórias e derrotas.
    Quais são as chances de ganhar no craps? [Nota: Você deve descobrir que craps é um dos jogos de casino mais justos.
    O que você acha que isso significa?]
    Qual é a média para a duração de um jogo de dados? A mediana? O modo?
    As chances de vitória aumentam com a duração do jogo?
    
dados = {
  "primeira": [
    {
      "win": ,
      "loser": ,
  }],
  "segunda": 0,
}
"""


import random as rd
import json

for i in range(1,10):
  #rd.seed(32)
  rodada = rd.randrange(1, 7)
  win = rd.randrange(1, 7)
  loose = rd.randrange(1, 7)

print("win = ", win)
print("Loose = ", loose)


dados = [rodada [win, loose],
         rodada [win, loose]]

rodada.insert(1, win)
rodada.insert(2, loose)

dados.insert()

dados.append(rodada)




#Rodada, wins, loose, Rodada
dados = []
for i in range(1,10):
  if (i == rodada):
    dados.insert(i, rodada)
    dados.insert(i+1, win)
    dados.insert(i+2, loose)


"""
#inserindo as rodadas
for i in range(1,10, 3):
  dados.insert(3, rodada)
  #dados.insert(i, rodada)

#inserindo as wins
for i in range(1,10, 2):
  dados.insert(i, win)

#inserindo as loose
for i in range(1,10, 1):
  dados.insert(i, loose)

"""