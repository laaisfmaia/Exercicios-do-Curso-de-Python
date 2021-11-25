num = int(input('Escreva um número de 0 a 9999: '))
uni = num % 10
dez = (num//10) % 10
cen = (num//100) % 10
milh = (num//1000) % 10
print('Unidade: {} '.format(uni))
print('Dezena: {} '.format(dez))
print('Centena: {} '.format(cen))
print('Milhar: {} '.format(milh))