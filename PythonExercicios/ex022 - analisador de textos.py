nome = input('Qual é o seu nome completo? ').strip()
print('NOME EM MAIÚSCULA: {} '.format(nome.upper()))
print('nome em minúscula: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(len(nome.split()[0])))