print('-' * 30)
print('   CADASTRO DE PRODUTOS   ')
print('-' * 30)
total = maior1000 = menor = cont = 0
nomeMenor = ''
while True:
    nome = input('Nome do Produto: ')
    preço = float(input('Preço do Produto: R$'))
    total += preço
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Você quer continuar? [S/N] ').strip().upper()
    if preço > 1000:
        maior1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        nomeMenor = nome
    if resp == 'N':
        break

print('- -'*15)
print('Fim do cadastro.')
print(f'O preço total gasto na compra foi R${total:.2f}')
print(f'Existem {maior1000} produtos com o preço maior que R$1000.00')
print(f'O produto mais barato é {nomeMenor}')
