from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
maior = 0
for c in range(0, 4):
    jogadores[f'jogador{c+1}'] = randint(1, 6)
ranking = list()
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{f"O {k} tirou {v} no dado.":>20}')
    sleep(1)
print('-=' * 30)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{" < Ranking dos jogadores > ":=^35}')
for i, j in enumerate(ranking):
    print(f"{f'{i + 1}º lugar: {j[0]} com {j[1]}.':^35}")
    sleep(1)
