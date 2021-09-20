jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
n_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, n_partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {n_partidas} partidas.')
for pos, v in enumerate(jogador['gols']):
    print(f'    -> Na partida {pos + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
