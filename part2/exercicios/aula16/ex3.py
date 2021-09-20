from random import randint
num_random = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for num in num_random:
    print(num, end=' ')
print(f'\nO maior valor sorteado foi {max(num_random)}\n'
      f'O menor valor sorteado foi {min(num_random)}')
