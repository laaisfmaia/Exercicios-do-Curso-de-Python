pares = list()
impares = list()
completo = [[], []]
for i in range(1, 8):
    num = int(input(f'Escreva o {i}° valor: '))
    if num % 2 == 0:
       completo[0].append(num)
    else:
        completo[1].append(num)
print('-'*50)
completo[0].sort()
completo[1].sort()
print(f'Os valores pares adicionados são: {completo[0]}')
print(f'Os valores ÍMPARES adicionados são: {completo[1]}')