from random import randint

numAleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram:')
for pos, numero in enumerate(numAleatorios):
    print(f'{numero}', end=' ')

print('')
print(f'O maior número sorteado é: {max(numAleatorios)}\nE o menor número é: {min(numAleatorios)} ')



