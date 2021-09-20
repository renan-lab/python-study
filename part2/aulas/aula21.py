# Funções - part2

# help(print)
# print(input.__doc__)

def contador(i, f, p):
    """
    -> Realiza uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('FIM!')


# help(contador)

def somar(a=0, b=0, c=0):
    """
    -> Realiza a soma de três valores e exibe o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    # print(f'A soma vale {s}')
    return s


r1 = somar(3, 2, 5)
r2 = somar(3, 2)
r3 = somar(3)
print(f'Os resultados foram {r1}, {r2} e {r3}')
