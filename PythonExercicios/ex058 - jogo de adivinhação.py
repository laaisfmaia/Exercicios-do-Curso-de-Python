from random import randint

escPC = randint(0, 10)
cont = 0

print('========= Jogo de adivinhação =========')
escVocê = int(input('Em qual número entre 0 e 10 eu pensei? '))

while escVocê != escPC:
    if escVocê < escPC:
        m = 'maior'
    else:
        m = 'menor'
    print('Você ERROU! É um número {}... Tente novamente!'.format(m))
    print('-'*40)
    escVocê = int(input('Em qual número entre 0 e 10 eu pensei? '))
    cont += 1

print('Você ACERTOU! Foram necessárias {} tentativas para você adivinhar.'.format(cont))