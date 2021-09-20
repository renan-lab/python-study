dados = list()
pessoas = list()
resp = 's'
maior = menor = 0
while resp in 'Ss':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (Kg): ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
print('-=' * 40)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[:][1] == menor:
        print(f'[{p[0]}]', end=' ')
