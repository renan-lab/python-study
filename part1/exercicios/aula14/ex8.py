cont = num = soma = 0
num = int(input('Digite um número (999 para parar): '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número (999 para parar): '))
print('Soma de todos os números digitados: {}\nQtd de números digitados: {}'.format(soma, cont))
