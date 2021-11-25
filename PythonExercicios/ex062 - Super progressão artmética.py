print('=== Cálculo da Progressão Aritmética ===')
a1 = int(input('Escreva o primeiro termo da PA: '))
r = int(input('Escreva a razão da PA: '))

print('-'*40)
print('Os 10 primeiros termos dessa PA são: ')
n = 1
resp = 10
while resp != 0:
    n = 1
    while n <= resp:
        an = a1 + (n - 1) * r
        n += 1
        print(an, end=' ')
    print('')
    acres = int(input('Você quer mostrar mais quantos termos? '))
    resp += acres
    if acres == 0:
        break