import random

lista = ['Par', 'Ímpar']
print('====== Jogo de Ímpar ou Par ======')
perdeu = False
cont = 0

while True:
    opPC = random.choice(lista)
    numPC = random.randint(0, 10)
    opVocê = int(input('Digite\n[1] - para escolher PAR ou\n[2] - para escolher ÍMPAR\nSua escolha: '))
    if opVocê == 1:
        opVocê = lista[0]
    if opVocê == 2:
        opVocê = lista[1]
    numVocê = int(input('Escolha um número de 0 a 10: '))
    somaMaos = numPC + numVocê
    print('')
    print(f'Mão do PC: {opPC} e {numPC}\nSua mão: {opVocê} e {numVocê}')
    print(f'Soma das mãos: {somaMaos}')
    print('-' * 40)
    if opVocê == opPC:
        print('EMPATE!!')
    else:
        if somaMaos % 2 == 0:
            if opVocê == 'Par':
                print('Você VENCEU!')
                cont += 1
            elif opPC == 'Par':
                print('Você PERDEU!')
                perdeu = True
        if somaMaos % 2 != 0:
            if opVocê == 'Ímpar':
                print('Você VENCEU!')
                cont += 1
            elif opPC == 'Ímpar':
                print('Você PERDEU!')
                perdeu = True
    if perdeu:
        print(f'FIM DO JOGO! Você teve {cont} vitórias.')
        break
    print('-'*40)
