import math
catOp = float(input('Escreva o cateto oposto: '))
catAdj = float(input('Escreva o cateto adjacente: '))
hip = math.hypot(catOp,catAdj)
#hip = (catOp**2 + catAdj**2)**(1/2)
print('A hipotenusa desse triangulo retângulo é {:.2f}'.format(hip))