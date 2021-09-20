# Dicionários

# pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 18}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# pessoas['peso'] = '52'
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = list()
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{v}', end=' ')
    print()
