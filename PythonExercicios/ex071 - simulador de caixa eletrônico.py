print('-' * 30)
print('       CAIXA ELETRÔNICO   ')
print('-' * 30)
valor = int(input('Qual vai ser o valor sacado? R$'))

while True:
    notas50 = valor// 50
    resto = valor % 50
    notas20 = resto// 20
    resto = resto % 20
    notas10 = resto// 10
    resto = resto % 10
    notas1 = resto // 1
    resto = resto % 1
    if notas50 != 0:
        print(f'Total de {notas50} cédulas de R$50')
    if notas20 != 0:
        print(f'Total de {notas20} cédulas de R$20')
    if notas10 != 0:
        print(f'Total de {notas10} cédulas de R$10')
    if notas1 != 0:
        print(f'Total de {notas1} cédulas de R$1')
    if resto == 0:
        break
print('-' * 30)
print('Volte sempre!')






""" if valor % 50 == 0:
        qNotas = valor//50
        ced = 50
        resto = 0
    if valor % 20 == 0:
        qNotas = valor // 20
        ced = 20
        resto = 0
    if valor % 10 == 0:
        qNotas = valor // 10
        ced = 10
        resto = 0
    if valor % 1 == 0:
        qNotas = valor
        ced = 1
        resto = 0"""


    #