soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print('A soma de todos os números ímpares múltiplos de 3 no intervalo de 1 a 500 é {}'.format(soma))
