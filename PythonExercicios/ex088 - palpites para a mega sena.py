from random import randint
from time import sleep

print('-'*30)
print(F'{"JOGOS NA MEGA SENA":^30}')
print('-'*30)

n = 0
lista = list()
temp = list()
quantJogos = int(input('Quantos jogos você quer gerar? '))
print(f'----- Sorteando {quantJogos} jogos ------')
print()

for i in range(0, quantJogos):
    lista.append(temp[:])
    n = 0
    while n < 6:
        numJogos = randint(1, 60)
        if numJogos not in lista[i]:
            lista[i].append(numJogos)
            n += 1
    lista[i].sort()
    print(f'Jogo {i+1}: {lista[i]}')
    sleep(0.5)

print(f'{" Boa sorte!! ":-^30}')