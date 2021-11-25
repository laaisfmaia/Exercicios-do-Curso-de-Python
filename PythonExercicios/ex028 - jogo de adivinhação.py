import random

num = random.randint(0,5)
escolha = int(input('Qual o número entre 0 e 5 que eu pensei? '))
if num == escolha:
    print('Parábens, você acertou!!')
else:
    print('Vish, você errou! O número que eu pensei foi {}'.format(num))
