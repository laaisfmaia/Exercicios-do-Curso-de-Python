times = ('Atlético-MG','Flamengo','Fortaleza','Bragantino','Palmeiras','Corinthias','Internacional',
         'Athletico-PR','Cuiabá','Fluminense','Atlético-GO','América-MG','São Paulo','Ceará SC',
         'Juventude','Santos','Bahia','Sport Recife','Grêmio','Chapecoense')

print('============= BRASILEIRÃO 2021 =============')
print(f'Lista de times em ORDEM DE COLOCAÇÃO:\n{times}')
print('- -'*33)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('- -'*33)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('- -'*33)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('- -'*33)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}° posição.')

"""for c, time in enumerate(times):
    if time == 'Chapecoense':
        print(f'A {time} está na {c+1}° posição.')
"""