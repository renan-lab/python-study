from datetime import date
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = ano_atual - ano_nasc
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['contratacao'] + 35 - ano_nasc
print('-=' * 30)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
