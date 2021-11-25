matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Escreva o valor da posição a{i+1}{j+1}= '))
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2:
            soma3 += matriz[i][j]
        if i == 1:
            if j == 0:
                maior = matriz[i][j]
            else:
                if matriz[i][j] > maior:
                    maior = matriz[i][j]
print('-'*30)
print('MATRIZ: ')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^4}]', end='')
    print()
print('-'*30)
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {maior}.')

