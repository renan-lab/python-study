nome = str(input('Qual é seu nome? '))

if nome == 'Renan':
    print('Que nome bonito!')
elif nome in 'Pedro Maria Paulo':
    print('Seu nome é bem popular')
elif nome == 'Ana' or nome == 'Cláudia' or nome == "Jéssica" or nome == 'Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')

print('Tenha um bom dia, {}!'.format(nome))
