from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim <= 0 or inicio > fim:
        fim -= 1
        passo *= -1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
contador(
    inicio=int(input('Início: ')),
    fim=int(input('Fim: ')),
    passo=int(input('Passo: '))
)
