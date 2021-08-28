print('-' * 5 + ' PROGRESSÃO ARITMÉTICA ' + '-' * 5)
n1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = n1 + (10 - 1) * razao

print('Os 10 termos são: ', end='')
for c in range(n1, decimo + razao, razao):
    print(c, end=' --> ')
print('FIM')
