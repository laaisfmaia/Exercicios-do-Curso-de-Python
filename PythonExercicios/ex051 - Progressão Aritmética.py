print('=== Cálculo da Progressão Aritmética ===')
a1 = int(input('Escreva o primeiro termo da PA: '))
r = int(input('Escreva a razão da PA: '))

print('Os 10 primeiros termos dessa PA são: ')
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(an, end=' ')
