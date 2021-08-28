while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 35)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 35)
print('Programa tabuada encerrado.')
