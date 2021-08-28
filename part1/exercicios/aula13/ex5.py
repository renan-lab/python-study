soma = 0
for c in range(0, 6):
    num = int(input('Digite o {}º número: '.format(c+1)))
    if num % 2 == 0:
        soma += num

print('A soma dos números pares digitados é {}'.format(soma))
