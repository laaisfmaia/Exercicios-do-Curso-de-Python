listagem = ('Lápis', 1.75, 'Borracha', 2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor','4.20')
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<32}R$', end='')
    else:
        print(f'{listagem[i]:>6}')
print('-'*40)