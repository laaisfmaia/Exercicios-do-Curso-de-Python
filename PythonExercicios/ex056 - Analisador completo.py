soma = 0
sMMenos20 = 0
idadevelho = 0
for i in range(1, 5):
    nome = input('Escreva o nome da {}° pessoa: '.format(i))
    idade = int(input('Escreva a sua idade: '))
    gen = input('Escreva seu gênero: [F/M/NB] ').upper()
    print('='*30)
    soma = soma + idade
    if gen == 'F' and idade < 20:
        sMMenos20 = sMMenos20 + 1
    if gen == 'M':
        if i == 1:
            velhoNome = nome
            idadevelho = idade
        else:
            if idade > idadevelho:
                idadevelho = idade
                velhoNome = nome

media = soma/4
print('='*50)
print('A média de idade do grupo é {:.1f} anos'.format(media))
print('No grupo existem {} mulheres com menos de 20 anos.'.format(sMMenos20))
print('O homem mais velho é o {} e tem {} anos'.format(velhoNome,idadevelho))

