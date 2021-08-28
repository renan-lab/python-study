num = int(input('Digite um número: '))

opcao = int(input('Escolha uma opção:\n'
                  '[1] - Converter para \033[32mBINÁRIO\n'
                  '\033[0;0m[2] - Converter para \033[33mOCTAL\n'
                  '\033[0;0m[3] - Converter para \033[36mHEXADECIMAL\n\033[0;0m'))

if opcao == 1:
    print('O número {} em BINÁRIO é {}'.format(num, bin(num)[2:])) # [2:] divide a string e mostra somente a partir da 3ª posição.
elif opcao == 2:
    print('O número {} em OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
