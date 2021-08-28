import random
from time import sleep

print('Opções de jogada:\n'
      '[0] Pedra\n'
      '[1] Papel\n'
      '[2] Tesoura')
opcao = int(input('Informe a jogada: '))

if opcao == 0:
    jogada = 'pedra'
elif opcao == 1:
    jogada = 'papel'
elif opcao == 2:
    jogada = 'tesoura'
else:
    print('Opção inválida!')
    exit()

jogada_comp = random.choice(['pedra', 'papel', 'tesoura'])

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(jogada_comp.upper()))
print('Você jogou {}'.format(jogada.upper()))
print('-=' * 11)

if jogada == 'pedra' and jogada_comp == 'tesoura':
    print('Parabéns, você ganhou!')
elif jogada == 'tesoura' and jogada_comp == 'pedra':
    print('Que pena, você perdeu.')
elif jogada == 'papel' and jogada_comp == 'pedra':
    print('Parabéns, você ganhou!')
elif jogada == 'pedra' and jogada_comp == 'papel':
    print('Que pena, você perdeu.')
elif jogada == 'papel' and jogada_comp == 'tesoura':
    print('Que pena, você perdeu.')
elif jogada == 'tesoura' and jogada_comp == 'papel':
    print('Parabéns, você ganhou!')
else:
    print('Empate!')
