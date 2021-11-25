import random
from time import sleep
lista = ('Tesoura', 'Papel', 'Pedra')
escPC = random.randint(0, 2)
print('Vamos jogar PEDRA, PAPEL, TESOURA!!')
print('='*35)
escVocê = int(input('Digite:\n[0] para escolher TESOURA;\n[1] para escolher PAPEL ou\n[2] para escolher PEDRA.\nSua escolha: '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('POO!')
print('='*65)
if escPC == 0:
    if escVocê == 0:
        print('O computador também escolheu {} e você escolheu {}. Deu EMPATE.'.format(lista[escPC],lista[escVocê]))
    elif escVocê == 1:
        print('O computador escolheu {} e você escolheu {}. Você PERDEU!'.format(lista[escPC],lista[escVocê]))
    elif escVocê == 2:
        print('O computador escolheu {} e você escolheu {}. Você VENCEU!'.format(lista[escPC],lista[escVocê]))
elif escPC == 1:
    if escVocê == 1:
        print('O computador também escolheu {}. Deu EMPATE.'.format(lista[escPC]))
    elif escVocê == 2:
        print('O computador escolheu {} e você escolheu {}. Você PERDEU!'.format(lista[escPC],lista[escVocê]))
    elif escVocê == 0:
        print('O computador escolheu {} e você escolheu {}. Você VENCEU!'.format(lista[escPC],lista[escVocê]))
elif escPC == 2:
    if escVocê == 2:
        print('O computador também escolheu {}. Deu EMPATE.'.format(lista[escPC]))
    elif escVocê == 0:
        print('O computador escolheu {} e você escolheu {}. Você PERDEU!'.format(lista[escPC],lista[escVocê]))
    elif escVocê == 1:
        print('O computador escolheu {} e você escolheu {}. Você VENCEU!'.format(lista[escPC],lista[escVocê]))
    else:
        print('Jogada inválida!')

