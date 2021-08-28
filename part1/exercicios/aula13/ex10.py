maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c+1)))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))
