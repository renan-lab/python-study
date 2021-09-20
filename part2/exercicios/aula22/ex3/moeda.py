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
