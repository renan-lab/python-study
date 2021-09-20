def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


print('Controle de terrenos')
print('-' * 20)
area(
    larg=float(input('Largura (m): ')),
    comp=float(input('Comprimento (m): '))
)
