opcao = 0
while opcao != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    opcao = int(input('Escolha uma opção:\n'
          '[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa\n'
          'Sua opção: '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    if opcao == 2:
        print('{} x {] = {}'.format(n1, n2, n1*n2))
    if opcao == 3:
        if n1 > n2:
            print('O {} é maior que o {}'.format(n1, n2))
        else:
            print('O {} é maior que o {}'.format(n2, n1))
