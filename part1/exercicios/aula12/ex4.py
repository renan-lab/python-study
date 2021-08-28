from datetime import date

current_year = date.today().year
birth_year = int(input('Insira sua data de nascimento: '))

age = current_year - birth_year

if age < 18:
    years = 18 - age
    year = current_year + years
    print('Ainda faltam {} ano(s) para o alistamento'.format(years))
    print('Seu alistamento será em {}'.format(year))
elif age == 18:
    print('Você tem que se alistar agora.')
else:
    years = age - 18
    year = current_year - years
    print('Você tem que se alistar imediatamente. Você deveria ter se alistado há {} ano(s) atrás'.format(years))
    print('Seu alistamento foi em {}'.format(year))
