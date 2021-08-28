from random import randint
cont = 0
print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
while True:
    valor = int(input('Digite um valor: '))
    jogada = str(input('Par ou ímpar? [P/I] ')).strip()[0]
    while jogada not in 'PpIi':
        jogada = str(input('Par ou ímpar? [P/I] ')).strip()[0]
    valor_comp = randint(1, 10)
    r = valor + valor_comp
    print('-' * 50)
    print(f'Você jogou {valor} e o computador {valor_comp}. Total de {r} ', end='')
    if r % 2 == 0:
        print('DEU PAR')
        print('-' * 50)
        if jogada in 'Pp':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('-=' * 15)
            cont += 1
        else:
            print('Você PERDEU!')
            print('-=' * 15)
            break
    else:
        print('DEU ÍMPAR')
        print('-' * 50)
        if jogada in 'Ii':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('-=' * 15)
            cont += 1
        else:
            print('Você PERDEU!')
            print('-=' * 15)
            break
print(f'GAME OVER! Você venceu {cont} vezes.')
