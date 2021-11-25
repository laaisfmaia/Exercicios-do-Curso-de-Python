lista = []
listaPar = []
listaImp = []
while True:
    num = int(input('Escreva um número: '))
    lista.append(num)
    """if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImp.append(num)"""
    resp = input('Você quer continuar? [S/N] ').upper().strip()
    while resp not in 'NS':
        resp = input('Opção inválida. Você quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break

for valores in lista:
    if valores % 2 == 0:
        listaPar.append(valores)
    else:
        listaImp.append(valores)

print('-'*50)
print(f'A lista completa é: {lista}')
print(f'A lista dos números pares é: {listaPar}')
print(f'A lista dos números ímpares é: {listaImp}')
