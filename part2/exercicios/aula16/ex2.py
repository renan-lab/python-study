times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Atlético-GO', 'Ceará SC',
         'Athletico-PR', 'Internacional', 'Santos', 'São Paulo', 'Juventude', 'Cuiabá', 'Bahia', 'Fluminense',
         'América-MG', 'Grêmio', 'Sport Recife', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[16:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
