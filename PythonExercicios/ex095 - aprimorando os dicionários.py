dados = dict()
partidas = list()
time = list()
#gols = list()
print(f'{"Aproveitamento do jogador":-^40}')
while True:
    dados.clear()
    partidas.clear()
    dados['Nome'] = input('Qual o nome do jogador? ')
    qPartidas= int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for i in range(0, qPartidas):
         partidas.append(int(input(f'Quantos gols {dados["Nome"]} fez na {i+1}° partida? ')))
         dados['gols'] = partidas[:]
         dados['total'] = sum(partidas)
    time.append(dados.copy())
    resp = input('Você quer continuar? [S/N] ').upper().strip()
    while resp not in 'SN':
        resp = input('Resposta inválida! Você quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break
    print('-'*40)
print('-'*40)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for chave, valor in enumerate(time):
    print(f'{chave:>3} ', end='')
    for d in valor.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    cod = int(input('Mostrar dados de qual jogador? Digite o código correspondente. '))
    if cod == 999:
        break
    if cod >= len(time):
        print(f'ERRO. Não existe jogador com o código {cod}. Digite 999 para sair')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[cod]["Nome"]} ---')
        for i in range(0, len(time[cod]["gols"])):
            print(f'   No jogo {i+1} fez {time[cod]["gols"][i]} gols.')
    print('-'*40)
print('Fim do programa.')