vlrs = list()
for c in range(0, 5):
    vlrs.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-' * 40)
print(f'Você digitou os valores {vlrs}')
print(f'O maior valor digitado foi {max(vlrs)} nas posições ', end='')
for pos, vlr in enumerate(vlrs):
    if vlr == max(vlrs):
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {min(vlrs)} nas posições ', end='')
for pos, vlr in enumerate(vlrs):
    if vlr == min(vlrs):
        print(f'{pos}...', end=' ')
