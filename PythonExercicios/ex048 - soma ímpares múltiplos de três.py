soma = 0
for i in range(1,501):
    if (i % 3 == 0) and (i % 2 != 0):
        soma = soma + i
print('A soma dos números ímpares múltiplos de três e que se encontram no intervalo de 1 a 500 é {}.'.format(soma))

