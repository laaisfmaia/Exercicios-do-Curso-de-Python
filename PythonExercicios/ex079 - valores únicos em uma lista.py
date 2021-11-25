valores = []
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado. Não é possível adicionar')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso.')
    resp = input('Quer continuar? [S/N] ').upper().strip()
    while resp != 'S' and resp != 'N':
        resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break
valores.sort()
print(f'A lista ficou com esses valores: {valores}')