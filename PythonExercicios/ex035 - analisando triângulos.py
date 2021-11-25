a = int(input('Escreva o comprimento da reta A: '))
b = int(input('Escreva o comprimento da reta B: '))
c = int(input('Escreva o comprimento da reta C: '))

if ((a > abs(b - c)) and (a < (b + c))) and ((b > abs(a - c)) and (b < (a + c))) and ( (c > abs(a - b)) and (c < (a + b))) :
    print('É possível formar um triângulo com as retas {}, {} e {}.'.format(a,b,c))
else:
    print('NÃO é possível formar um triângulo com as retas {}, {} e {}.'.format(a,b,c))
