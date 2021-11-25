n1 = float(input('Escreva o 1° número: '))
n2 = float(input('Escreva o 2° número: '))
n3 = float(input('Escreva o 3° número: '))

if (n1 > n2) and (n1 > n3):
    print('O número maior é {}'.format(n1))
    if n2 > n3:
        print('O número menor é {} '.format(n3))
    else:
        print('O número menor é {}'.format(n2))

if (n2 > n1) and (n2 > n3):
    print('O número maior é {}'.format(n2))
    if n1 > n3:
        print('O número menor é {} '.format(n3))
    else:
        print('O número menor é {}'.format(n1))

if (n3 > n1) and (n3 > n2):
    print('O número maior é {}'.format(n3))
    if n2 > n1:
        print('O número menor é {} '.format(n1))
    else:
        print('O número menor é {}'.format(n2))