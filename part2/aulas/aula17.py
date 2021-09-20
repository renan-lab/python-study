# Listas

# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# if 5 in num:
#     num.remove(5)
# else:
#     print('Número 4 não encontrado')
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# for pos, valor in enumerate(valores):
#     print(f'Na posição {pos} foi encontrado o valor {valor}!')
# print('Fim da lista')

a = [2, 3, 4, 7]
# a = b --> ligação de listas
b = a[:]  # lista b recebendo todos os valores da lista a sem fazer ligação
b[2] = 8
print(f'Lista A: {a}\n'
      f'Lista B: {b}')
