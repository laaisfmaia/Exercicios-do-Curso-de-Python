lista = []
for i in range(1, 6):
    num = int(input(f'Escreva o {i}° número: '))
    if i == 1 or num > lista[-1]: #lista[-1] é o último elemento
        lista.append(num)
        print(f'O número {num} foi adicionado no final da lista!')
    else:
        posição = 0
        while posição < len(lista):
            if num <= lista[posição]:
                lista.insert(posição, num)
                print(f'O número {num} foi adicionado na posição {posição}')
                break
            posição += 1
print('-'*54)
print(f'Os valores digitados em ordem foram: {lista}')