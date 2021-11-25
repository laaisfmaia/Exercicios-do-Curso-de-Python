from datetime import date

ano = int(input('Qual o ano de nascimento do atleta? '))
idade = date.today().year - ano
print('A idade do atleta é {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: Atleta MIRIM.')
elif idade <= 14:
    print('Classificação: Atleta INFANTIL.')
elif idade <= 19:
    print('Classificação: Atleta JÚNIOR.')
elif idade <= 20:
    print('Classificação: Atleta SÊNIOR.')
else:
    print('Classificação: Atleta MASTER.')
