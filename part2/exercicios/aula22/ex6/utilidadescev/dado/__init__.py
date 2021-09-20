def leiaDinheiro(msg):
    valido = False
    vlr = 0
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == "":
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            vlr = float(entrada)
            valido = True
    return vlr
