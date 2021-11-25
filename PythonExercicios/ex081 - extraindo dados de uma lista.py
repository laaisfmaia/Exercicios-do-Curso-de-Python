lista = []
cont = 0
while True:
    num = int(input('Escreva um número: '))
    lista.append(num)
    cont += 1
    resp = input('Você deseja continuar? [S/N] ').upper().strip()
    while resp not in 'SN':
        resp = input('Opção inválida. Você deseja continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('-'*50)
print(f'A lista digitada foi: {lista}')
print(f'Foram digitados {cont} números nessa lista.')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é da forma: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
