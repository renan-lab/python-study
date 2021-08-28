num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
cont = 0
print('Os 10 primeiros termos da PA são: ', end='')
while cont < 10:
    print(num, end=' --> ')
    num += razao
    cont += 1
print('FIM')
