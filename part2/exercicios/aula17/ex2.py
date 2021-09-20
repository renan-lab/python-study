resp = 's'
vlrs = list()
while resp in 'Ss':
    vlr = (int(input('Digite um valor: ')))
    if vlr in vlrs:
        print('Valor duplicado! Não vou adicionar...')
    else:
        vlrs.append(vlr)
        print('Valor adicionado com sucesso')
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
print('-=' * 30)
vlrs.sort()
print(f'Você digitou os valores {vlrs}')
