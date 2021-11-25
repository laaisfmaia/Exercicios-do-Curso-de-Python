import math
ang = float(input('Escreva o ângulo em graus: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo {} rad tem:\no SENO: {:.3f};\no COSSENO: {:.3f}\ne a TANGENTE: {:.4f}'.format(ang,seno,cos,tan))
