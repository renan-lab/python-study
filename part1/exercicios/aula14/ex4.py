cont = num = int(input('Digite um número: '))
r = 1
while cont > 1:
    r *= cont
    cont -= 1
print('{}! = {}'.format(num, r))
