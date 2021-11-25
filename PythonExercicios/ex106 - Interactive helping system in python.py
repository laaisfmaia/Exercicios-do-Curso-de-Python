def titulo(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))


def ajuda(a):
    msg = f'Acessando o manual do comando {a}'
    print(f'\033[30;44m{"-"*(len(msg)+4)}')
    print(f'  {msg}')
    print(f'{"-"* (len(msg)+4)}')
    print('\033[m')
    print('\033[7;40m')
    help(a)
    print('\033[m')


while True:
    print(f'\033[42m{"-" * 35}')
    print(f'{"Sistema de ajuda PyHELP":^35}')
    print(f'{"-" * 35}')
    print('\033[m')
    f = input('Digite a Função ou Biblioteca: ')
    if f.upper() == 'FIM':
        break
    else:
        print(ajuda(f))
