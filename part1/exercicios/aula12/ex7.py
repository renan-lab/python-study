peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif imc < 25:
    status = 'PESO IDEAL'
elif imc < 30:
    status = 'SOBREPESO'
elif imc < 40:
    status = 'OBESIDADE'
else:
    status = 'OBESIDADE MÓRBIDA'

print('Você está em {}'.format(status))
