#num = int(input('Digite um número: '))
#div = 0

#for c in range(2, num):
# if num % c == 0:
#   div += 1
#
#if div > 0 or num == 1:
#   print('{} não é um número primo.'.format(num))
#else:
#   print('{} é um número primo.'.format(num))

#código melhorado:
num = int(input('Digite um número: '))

div = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m', end='')
        div += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n\033[0;0mO número {} foi divisível {} vezes'.format(num, div))
if div == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
