resp = 's'
menor = maior = soma = cont = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    soma += num
    resp = str(input('Deseja continuar inserindo novos números? [S/N] '))
print('Quantidade de valores digitados: {} e a média entre todos os valores: {:.2f}'
      '\nMaior valor: {}\nMenor valor: {}'.format(cont, soma / cont, maior, menor))
