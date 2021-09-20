dados = dict()
pessoas = list()
soma_idade = 0
resp = 's'
while resp in 'Ss':
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F] ')).strip()[0]
    while dados['sexo'] not in 'MmFf':
        print('ERRO! Digite apenas M ou F')
        dados['sexo'] = str(input('Sexo [M/F] ')).strip()[0]
    dados['idade'] = int(input('Idade: '))
    soma_idade += dados['idade']
    pessoas.append(dados.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        print('ERRO! Digite apenas S ou N')
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
print('-=' * 30)
media_idade = soma_idade / len(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media_idade:.2f} anos')
print('- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print('\n- Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > media_idade:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
