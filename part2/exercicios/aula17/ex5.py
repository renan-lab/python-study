num = list()
pares = list()
impares = list()
resp = 's'
while resp in 'Ss':
    num.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N] ')).strip()[0]
for n in num:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-=' * 40)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
