soma = 0
for i in range(1, 7):
    n = int(input('Escreva o {}° número: '.format(i)))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos números pares é {}'.format(soma))
