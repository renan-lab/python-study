from datetime import date

ano_atual = date.today().year

qtd_maior = 0
for c in range(0, 7):
    ano_nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c+1)))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        qtd_maior += 1

print('Quantidade de pessoas maior de idade: {}\n'
      'Quantidade de pesssoas menor de idade: {}'.format(qtd_maior, 7 - qtd_maior))
