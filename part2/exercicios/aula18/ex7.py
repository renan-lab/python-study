tabela = list()
resp = 's'
maior = 0
print(f'{" TOP 5 BRASILEIRÃO ":=^35}')
for c in range(0, 5):
    time = str(input('Time: '))
    for t in tabela:
        if time in t:
            time = str(input('Time já inserido. Digite outro: '))
            break
    pont = int(input('Pontos: '))
    pos = 0
    time_inserido = False
    while pos < len(tabela):
        if pont >= tabela[pos][1]:
            tabela.insert(pos, [time, pont])
            time_inserido = True
            break
        pos += 1
    if not time_inserido:
        tabela.append([time, pont])
print('-=' * 30)
print(f'{"POS.":<8}{"TIME":<15}{"PONTOS":>10}')
print('-' * 35)
for i, t in enumerate(tabela):
    print(f'{i + 1:<8}{t[0]:<15}{t[1]:>10}')
print('-' * 35)
