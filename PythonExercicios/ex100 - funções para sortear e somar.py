def sorteio(lista):
    from random import randint
    from time import sleep
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
        print(num, end=' ')
        sleep(0.5)
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for valores in lista:
        if valores % 2 == 0:
            soma += valores
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = list()
sorteio(números)
somaPar(números)






