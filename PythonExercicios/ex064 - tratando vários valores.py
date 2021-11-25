soma = n = quantn = 0
while n != 999:
    soma += n
    n = int(input('Escreva um número inteiro [digite 999 para parar]: '))
    quantn += 1
print('A soma dos {} números digitados é {}'.format(quantn-1, soma))
