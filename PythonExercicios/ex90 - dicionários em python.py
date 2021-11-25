dados = {}
dados['Nome'] = input('Nome: ')
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))

if dados['Média'] >= 7:
    dados['Situação'] = 'APROVADO'
elif 5 <= dados['Média'] < 7:
    dados['Situação'] = 'RECUPERAÇÃO'
else:
    dados['Situação'] = 'REPROVADO'
print('-'*30)
for chaves, valores in dados.items():
    print(f'{chaves} é igual a {valores}')