print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)
num = int(input('Digite a quantidade de termos que deseja mostrar: '))
t1 = 0
t2 = 1
cont = 2
print('{} --> {}'.format(t1, t2), end='')
while cont < num:
    t3 = t1 + t2
    print(' --> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' --> FIM')
