def leiaInt(msg):
    while True:
        ok = False
        valor = 0
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
