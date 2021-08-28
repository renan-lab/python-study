c = 1
r = 's'
while r in 'Ss':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] '))
print('FIM')
print('*-'*20)
n = 1
qtd_par = qtd_impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            qtd_par += 1
        else:
            qtd_impar += 1
print('Qtd pares: {} | Qtd ímpares: {}'.format(qtd_par, qtd_impar))
print('FIM')
