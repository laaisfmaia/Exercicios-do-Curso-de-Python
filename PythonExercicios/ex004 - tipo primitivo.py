a = input('Digite algo: ')
print('Seu tipo é: {}\nÉ alfa númerico? {}\nÉ composto por letras? {}\n  '.format(type(a), a.isalnum(),a.isalpha()))
