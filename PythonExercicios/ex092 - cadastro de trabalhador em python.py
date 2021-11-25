from datetime import date
print(f'{"CÁLCULO DE APOSENTADORIA":^40}')
dados = dict()
dados['Nome'] = input('Nome: ')
ano = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - ano
dados['CTPS'] = int(input('N° da carteira de trabalho: [0 se não tem] '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Qual é o salário: R$'))
    dados['Aposentadoria'] = (dados['Ano de contratação'] + 35) - ano
print('-'*50)
for chaves, valores in dados.items():
    print(f'{chaves} tem o valor {valores}')
