from datetime import date

somaMaior = 0
somaMenor = 0

for i in range(1, 8):
    ano = int(input('Em que ano a {}°pessoa nasceu? '.format(i)))
    idade = date.today().year - ano
    if idade >= 21:
        somaMaior = somaMaior + 1
    else:
        somaMenor = somaMenor + 1
print('')
print('{} pessoas dessa lista já atingiram a maior idade.'.format(somaMaior))
print('{} pessoas dessa lista ainda são menores de idade.'.format(somaMenor))
