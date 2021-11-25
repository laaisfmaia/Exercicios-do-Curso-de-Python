preço = float(input('Qual o preço do produto? '))
desc = (5/100)*preço
NovoPreço = preço - desc
print('O produto com 5% de desconto sairá por {:.2f} reais '.format(NovoPreço))
