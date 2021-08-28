print('{:=^30}'.format(' Banco RCA '))
vlr = int(input('Digite o valor a ser sacado: R$'))
while vlr <= 0:
    vlr = int(input('Valor inválido. Digite novamente: R$'))
total = vlr
tot_ced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        else:
            ced = 1
        tot_ced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO RCA! Tenha um bom dia')
