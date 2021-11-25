gen = input('Qual é o seu gênero? [M/F/NB] ').upper().strip()

while gen != 'M' and gen != 'F' and gen != 'NB':
    print('Digite novamente. Opção inválida.')
    gen = input('Qual é o seu gênero? [M/F/NB] ').upper()

if gen == 'M':
    print('Seu gênero é masculino.'.format(gen))
if gen == 'F':
    print('Seu gênero é feminino.'.format(gen))
if gen == 'NB':
    print('Você é uma pessoa não binária.'.format(gen))
