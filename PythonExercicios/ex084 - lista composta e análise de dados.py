dados = []
lista = []
maior = menor = 0
print(f'{" CADASTRO DE NOME E PESO ":=^40}')
while True:
    dados.append(input('Nome: '))
    dados.append((float(input('Peso [Kg] : '))))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    resp = input('Você quer continuar? [S/N]').upper().strip()
    while resp not in 'SN':
        resp = input('Você quer continuar? [S/N]').upper().strip()
    if resp == 'N':
        break

print('-'*50)
print(lista)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {maior:.1f}kg. E foi o peso de ', end='')
for i in lista:
    if i[1] == maior:
        print(f'{i[0]}; ', end='')
print('')
print(f'O menor peso foi de {menor:.1f}kg. E foi o peso de ', end='')
for i in lista:
    if i[1] == menor:
        print(f'{i[0]}; ', end='')