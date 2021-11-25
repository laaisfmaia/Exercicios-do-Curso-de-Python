exp = input('Digite uma expressão: ')
pilha = []
for i in exp:
    if i in '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está VÁLIDA!')
else:
    print(f'Sua expressão está INVÁLIDA.')
