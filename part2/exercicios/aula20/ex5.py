from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lst.append(randint(1, 10))
        print(lst[c], end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lst):
    s = 0
    for n in lst:
        if n % 2 == 0:
            s += n
    print(f'Somando todos os valores pares de {lst}, temos {s}')


lista = list()
sorteia(lista)
somaPar(lista)
