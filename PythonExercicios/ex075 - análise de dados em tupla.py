cont = 0

valores = (int(input('Escreva o 1° valor: ')), int(input('Escreva o 2° valor: ')),
             int(input('Escreva o 3° valor: ')), int(input('Escreva o 4° valor: ')))
print(f'Tupla: {valores}')
print(f'O número 9 aparece {valores.count(9)} vezes.')
print('Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(f'{n}', end=' ')
if 3 in valores:
    print(f'\nO número 3 foi digitado na {valores.index(3) + 1}° posição')
else:
    print('\nO valor 3 não foi digitado em nenhuma posição.')

