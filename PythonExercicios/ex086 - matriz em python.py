matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Escreva o valor da posição a{i+1}{j+1}= '))
print('-'*30)
print('MATRIZ: ')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^3}]',end='')
    print()