pessoa = dict()
dados = list()
somaIdades = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    somaIdades += pessoa['idade']
    pessoa['genêro'] = input('Gênero: [M/F/NB] ').upper().strip()
    while pessoa['genêro'] not in 'MFNB':
        pessoa['genêro'] = input('Gênero: [M/F/NB] ').upper().strip()
    dados.append(pessoa.copy())
    resp = input('Você quer continuar? [S/N] ').upper().strip()
    while resp not in 'SN':
        resp = input('Resposta inválida! Você quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break

print('-'*40)
print(dados)
print(f'Foram cadastradas {len(dados)} pessoas;')
print(f'   - As mulheres cadastradas foram: ', end='')
for i in range(0, len(dados)):
    if dados[i]['genêro'] == 'F':
        print(dados[i]['nome'], end=' ')
print()
media = somaIdades/(len(dados))
print(f'   - A média de idade do grupo é {media:.2f} anos;')
print(f'   - As pessoas com idade maior que a média são:')
for pes in dados:
    if pes['idade'] > media:
        print('  ', end='')
        for chave, valor in pes.items():
            print(f'* {chave} = {valor};', end=' ')
        print()
