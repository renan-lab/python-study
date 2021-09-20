jogador = dict()
gols = list()
jogadores = list()
resp = 's'
while resp in 'Ss':
    jogador['nome'] = str(input('Nome do jogador: '))
    n_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, n_partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Inválida. Quer continuar? [S/N] ')).strip()[0]
print('-=' * 30)
# print(f'{"cod.":<12}{"nome":<12}{"gols":<12}{"total":<12}')
print('cod. ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for pos, j in enumerate(jogadores):
    print(f'{pos:<5}', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod == 999:
        break
    if cod >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {cod}! Tente novamente')
    else:
        print(f'--  LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}')
        for i, v in enumerate(jogadores[cod]['gols']):
            print(f'    No jogo {i + 1} fez {v} gols.')
    print('-' * 50)
print('<< VOLTE SEMPRE >>')
