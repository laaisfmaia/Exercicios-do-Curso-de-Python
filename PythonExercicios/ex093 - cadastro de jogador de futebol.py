dados = dict()
gols = list()
total = 0
print(f'{"Aproveitamento do jogador":-^40}')
dados['Nome'] = input('Qual o nome do jogador? ')
qPartidas= int(input('Quantas partidas ele jogou? '))
for i in range(0, qPartidas):
     gols.append(int(input(f'Quantos gols ele fez na {i+1} partida? ')))
     total = total + gols[i]
     dados['gols'] = gols
     dados['total'] = total
print('-'*40)
for chave, valor in dados.items():
    print(f'O campo {chave} tem o valor {valor}.')
print('-'*40)
print(f'O jogador {dados["Nome"]} jogou {qPartidas} partidas.')
for i in range(0,qPartidas):
    print(f'    - Na partida {i+1} fez {dados["gols"][i]} gols.')
print(f'Foi um total de {dados["total"]} gols.')


