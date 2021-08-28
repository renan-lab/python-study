num = int(input('Digite o número para gerar a tabuada: '))

print('-'*14)
print('Tabuada do {}'.format(num))
print('-'*14)
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))
