from math import factorial

print('--- Cálculo do Fatorial ---')
num = int(input('Escreva um número: '))
print('O Fatorial de {} é:'.format(num))
fat = 1
n = num

"""f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))"""

"""for i in range(num, 1, -1):
    print('{}x'.format(i), end='')
    fat = fat * i
print('1 = {}'.format(fat))"""

while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n != 1 else ' = ', end='')
    fat = fat * n
    n -= 1
print('{}'.format(fat))
