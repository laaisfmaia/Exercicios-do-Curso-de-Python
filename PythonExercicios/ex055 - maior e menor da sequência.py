maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa em kg? '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < maior:
            menor = peso
print('')
print('O maior peso é {}kg'.format(maior))
print('O menor peso é {}kg'.format(menor))

