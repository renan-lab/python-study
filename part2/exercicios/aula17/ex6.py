cont = 0
expressao = str(input('Digite uma expressão: '))
for char in expressao:
    if char in '()':
        cont += 1
if cont % 2 == 0:
    print('A expressão está correta')
else:
    print('A expressão está incorreta')
