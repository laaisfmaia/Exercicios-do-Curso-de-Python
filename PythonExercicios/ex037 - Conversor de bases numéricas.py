num = int(input('Escreva o número que você deseja converter: '))
op = int(
    input('Qual será a base de conversão? \nDigite: \n[1] - para BINÁRIO\n[2] - para OCTAL\n[3] - para HEXADECIMAL\nSua opção: '))

if op == 1:
    print('O número {} na representação binário é {}'.format(num, format(num, 'b')))
elif op == 2:
    print('O número {} na representação octal é {}'.format(num, format(num, 'o')))
elif op == 3:
    print('O número {} na representação hexadecimal é {}'.format(num, format(num,'x')))
else:
    print('Opção inválida!')
