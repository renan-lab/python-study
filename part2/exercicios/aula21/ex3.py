def ficha(n='<desconhecido>', g=0):
    return f'O jogador {n} fez {g} gol(s) no campeonato'


print('-' * 30)
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(nome, gols))
