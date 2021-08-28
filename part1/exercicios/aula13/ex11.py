maior_idade = 0
soma_idade = 0
nome_velho  = ''
qtd_f = 0
for c in range(0, 4):
    print('-'*5 + ' Dados da {}ª pessoa '.format(c+1) + 5*'-')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [m/f]: ')).lower()

    soma_idade += idade

    if c == 0 and sexo == 'm':
        maior_idade = idade
        nome_velho = nome
    if sexo == 'm' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    if sexo == 'f' and idade < 20:
        qtd_f += 1

media_idade = soma_idade / 4

print('\nA média de idade é de {} anos'.format(media_idade))
print('{} é o homem mais velho com {} anos'.format(nome_velho, maior_idade))
print('{} mulher(es) tem menos de 20 anos'.format(qtd_f))
