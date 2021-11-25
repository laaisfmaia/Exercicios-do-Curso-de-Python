def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pela usuário.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pela usuário.')
            return 0
        else:
            return n

n = leiaInt('Digite um número inteiro: ')
p = leiaFloat('Digite um número real: ')
print(f'Você digitou o número {n} e {p}.')
