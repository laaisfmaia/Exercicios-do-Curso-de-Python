dist = float(input('Qual a distância em km? '))
if dist <= 200:
    preço = 0.50*dist
    print('O preço da passagem é R${:.2f}'.format(preço))
else:
    preço = 0.45*dist
    print('O preço da passagem é de R${:.2f}'.format(preço))