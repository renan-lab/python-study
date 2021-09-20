def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor fatorial de um número n
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print('-' * 30)
print(fatorial(5, True))
# help(fatorial)
