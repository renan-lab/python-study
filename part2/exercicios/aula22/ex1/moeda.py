def aumentar(p, n):
    n /= 100
    p += p * n
    return p


def diminuir(p, n):
    n /= 100
    p -= p * n
    return p


def dobro(p):
    return p * 2


def metade(p):
    return p / 2
