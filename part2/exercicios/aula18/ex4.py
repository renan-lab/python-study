matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_3col = maior_2line = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        if c == 2:
            soma_3col += matriz[l][c]
        if l == 1 and c == 0 or matriz[1][c] > maior_2line:
            maior_2line = matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares digitados é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_3col}')
print(f'O maior valor da seguna linha é {maior_2line}')
