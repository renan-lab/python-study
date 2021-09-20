vlrs = [[], []]
for c in range(0, 7):
    vlr = int(input(f'Digite o {c + 1}º valor: '))
    if vlr % 2 == 0:
        vlrs[0].append(vlr)
    else:
        vlrs[1].append(vlr)
vlrs[0].sort()
vlrs[1].sort()
print('-=' * 40)
print(f'Os valores pares digitados foram: {vlrs[0]}')
print(f'Os valores ímpares digitados foram: {vlrs[1]}')
