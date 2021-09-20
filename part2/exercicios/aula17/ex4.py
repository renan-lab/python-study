resp = 's'
num = list()
while resp in 'Ss':
    num.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip()[0]
print('-=' * 40)
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
