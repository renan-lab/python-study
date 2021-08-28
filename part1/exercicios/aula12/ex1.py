vlr_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário: R$'))
qtd_mes = int(input('Digite a quantidade de anos de financiamento: ')) * 12

vlr_prest = vlr_casa / qtd_mes

if vlr_prest > (salario * 0.3):
    print('Empréstimo' + '\033[31m negado.' + '\033[0;0m Valor da parcela excede 30% do salário.')
else:
    print('Empréstimo' +  '\033[32m aprovado.' + '\033[0;0m Valor da parcela: R${:.2f}'.format(vlr_prest))
