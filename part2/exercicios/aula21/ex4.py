def leiaInt(msg):
    valido = False
    vlr = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            vlr = int(n)
            valido = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if valido:
            break
    return vlr


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
