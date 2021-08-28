total = maior_mil = cont = barato = 0
nome_barato = ''
print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        maior_mil += 1
    if cont == 0:
        barato = preco
        nome_barato = nome
    if preco < barato:
        barato = preco
        nome_barato = nome
    cont += 1
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total}\n'
      f'Temos {maior_mil} produtos custando mais de R$1000.00\n'
      f'O produtos mais barato foi {nome_barato} que custa R${barato:.2f}')
