# Listas - part2

# teste = list()
# teste.append('Renan')
# teste.append(18)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
tot_maior = tot_menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        tot_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        tot_menor += 1
print(f'Temos {tot_maior} maiores e {tot_menor} menores de idade.')
