nome = input('Qual o seu nome completo? ')
print('Seu primeiro nome é: {}'.format(nome.split()[0]))
ind = len(nome.split()) - 1
print('Seu último nome é: {}'.format(nome.split()[ind]))