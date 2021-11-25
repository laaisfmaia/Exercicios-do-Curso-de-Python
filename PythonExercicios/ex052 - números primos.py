num = int(input('Escreva um número inteiro: '))
ndiv = 0
for i in range(1,num+1):
    ndiv = ndiv + (num % i == 0)
if ndiv == 2:
    print('O número {} é um número primo.'.format(num))
else:
    print('O número {} NÃO é um número primo.'.format(num))
