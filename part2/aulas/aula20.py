# Funções

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)
print()
soma(b=4, a=5)


def soma(*num):
    s = 0
    for n in num:
        s += n
    print(s)


soma(2, 4, 5)
soma(2, 4)
soma(1, 2, 3, 4, 5)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


vlrs = [6, 3, 9, 1, 0, 2]
dobra(vlrs)
print(vlrs)
