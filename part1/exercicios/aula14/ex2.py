from random import randint

random_num = randint(0, 10)
print('*-' * 25)
print('TENTE ADIVINHAR O NÚMERO SORTEADO ENTRE 0 E 10')
print('*-' * 25)
cont = 0
num = int(input('Adivinhe o número: '))
while num != random_num:
    cont += 1
    if num > random_num:
        print('Menos...')
    if num < random_num:
        print('Mais...')
    num = int(input('Tente novamente: '))
print('Parabéns você acertou o número sorteado após {} tentativas'.format(cont))
