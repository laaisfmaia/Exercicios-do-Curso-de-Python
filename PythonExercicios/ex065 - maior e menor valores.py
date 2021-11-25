resp = 'S'
soma = qNum = maior = menor = 0
while resp == 'S':
    n = int(input('Escreva um número: '))
    soma += n
    qNum += 1
    resp = input('Você quer continar? [S/N] ').upper().strip()
    print('-'*30)
    if qNum == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('Você digitou {} números e a média desses números digitados é {:.2f}'.format(qNum,soma/qNum))
print('O maior número digitado é {} e o menor valor é {}'.format(maior, menor))
