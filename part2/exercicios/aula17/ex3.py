vlrs = list()
maior = menor = 0
for c in range(0, 5):
    vlr = int(input('Digite um valor: '))
    if c == 0 or vlr > vlrs[-1]:
        vlrs.append(vlr)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(vlrs):
            if vlr <= vlrs[pos]:
                vlrs.insert(pos, vlr)
                print(f'Adiconado na posição {pos} da lista')
                break
            pos += 1
print('-=' * 40)
print(f'Os valores digitados em ordem foram {vlrs}')
