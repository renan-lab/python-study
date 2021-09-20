def aumentar(p, n, cif=False):
    n /= 100
    p += p * n
    if cif:
        return moeda(p)
    else:
        return p


def diminuir(p, n, cif=False):
    n /= 100
    p -= p * n
    if cif:
        return moeda(p)
    else:
        return p


def dobro(p, cif=False):
    if cif:
        return moeda(p * 2)
    else:
        return p * 2


def metade(p, cif=False):
    if cif:
        return moeda(p / 2)
    else:
        return p / 2


def moeda(p):
    return f'R${p:.2f}'.replace('.', ',')


def resumo(p, aument, reduc):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}\n'
          f'Dobro do preço: \t{dobro(p, cif=True)}\n'
          f'Metade do preço: \t{metade(p,cif=True)}\n'
          f'{aument}% de aumento: \t{aumentar(p, aument, cif=True)}\n'
          f'{reduc}% de redução: \t{diminuir(p, reduc, cif=True)}')
    print('-' * 30)
