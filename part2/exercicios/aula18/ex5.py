from random import randint
from time import sleep
lista = list()
jogos = list()
cont = 0
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
while len(jogos) < qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print(f'{f" SORTEANDO {qtd} JOGOS ":=^35}')
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {l}')
print(f'{" < BOA SORTE! > ":=^35}')
