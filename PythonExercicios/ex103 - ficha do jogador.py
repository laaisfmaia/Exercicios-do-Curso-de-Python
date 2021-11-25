def ficha(nome='<Não especificado>', gols=0):
    if nome == '':
        nome = '<Não especificado>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


n = input('Nome do jogador: ')
g = input('Número de gols: ')
print(ficha(n, g))
