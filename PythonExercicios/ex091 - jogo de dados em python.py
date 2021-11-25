from random import randint
from time import sleep
from operator import itemgetter

print('-' * 30)
print(f'{"JOGO DE DADOS":^30}')
print('-' * 30)
jogadas = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
for chave, valor in jogadas.items():
    print(f'O {chave} tirou o número: {valor}')
    sleep(1)
print('-' * 30)

ranking = list()
print(f'{"Ranking dos jogadores":^30}')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for i in range(0, len(jogadas)):
    print(f'{i+1}° lugar: {ranking[i][0]}')
    sleep(1)

