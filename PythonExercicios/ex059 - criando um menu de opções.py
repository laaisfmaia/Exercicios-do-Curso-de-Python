n1 = float(input('Escreva o 1° valor: '))
n2 = float(input('Escreva o 2° valor: '))
print('-'*35)
maior = 0
op = 0

while op != 5:
    op = int(input('Digite:\n[1] - para SOMAR;\n[2] - para MULTIPLICAR;\n[3] - para receber o MAIOR;\n[4] - para digitar NOVOS números;\n[5] - para SAIR do programa;\nSua opção: '))
    if op == 1:
        print('A soma de {:.2f} e {} é: {:.2f}'.format(n1, n2, n1+n2))
    if op == 2:
        print('A multiplicação de {:.2f} e {:.2f} é: {:.2f}'.format(n1, n2, n1*n2))
    if op == 3:
        if n1 > n2:
            maior = n1
        elif n1 == n2:
            print('Os dois números são iguais')
        else:
            maior = n2
        print('O maior número entre {:.2f} e {:.2f} é: {:.2f}'.format(n1, n2, maior))
    if op == 4:
        n1 = float(input('Escreva o 1° valor: '))
        n2 = float(input('Escreva o 2° valor: '))
    else:
        print('Opção inválida!')
    print('-' * 35)
print('Saindo...')