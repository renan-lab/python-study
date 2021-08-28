from datetime import date

current_year = date.today().year
age = current_year - (int(input('Digite o ano de nascimento: ')))
print('O atleta tem {} anos'.format(age))

if age <= 9:
    classif = 'MIRIM'
elif age <= 14:
    classif = 'INFANTIL'
elif age <= 19:
    classif = 'JÚNIOR'
elif age <= 25:
    classif = 'SÊNIOR'
else:
    classif = 'MASTER'

print('Classificação: {}'.format(classif))
