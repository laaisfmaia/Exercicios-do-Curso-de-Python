print('--- Sequência de Fibonacci ---')
n = int(input('Digite a quantidade de termos que você deseja ver da sequência de Fibonacci: '))

termo1 = 0
termo2 = 1
print(termo1, termo2, end=' ')
cont = 3
while cont <= n:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    cont += 1
    print(termo3, end=' ')
