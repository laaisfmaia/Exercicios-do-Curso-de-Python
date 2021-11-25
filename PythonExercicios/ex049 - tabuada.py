num = int(input('Escolha um número para ver sua tabuada: '))
print('=' * 12)

for i in range(0, 11):
    print('{} x {} = {}'.format(num, i, num * i))
