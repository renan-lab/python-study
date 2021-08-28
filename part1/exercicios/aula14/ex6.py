num = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
total = cont = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print(num, end=' - ')
        num += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Digite o número de termos que deseja mostrar a mais: '))
print('Progressão finalizada com {} termos mostrados'.format(cont))
