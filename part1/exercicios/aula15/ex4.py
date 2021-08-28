maior_18 = cont_m = f_menor_20 = 0
print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: ')).strip()[0]
    if idade > 18:
        maior_18 += 1
    if sexo in 'Mm':
        cont_m += 1
    if idade < 20 and sexo in 'Ff':
        f_menor_20 += 1
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Ao todo temos {cont_m} homens cadastrados')
print(f'E temos {f_menor_20} mulheres com menos de 20 anos')
