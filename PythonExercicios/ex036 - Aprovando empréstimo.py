print('='*30)
print('CÁLCULO DE EMPRÉSTIMO BANCÁRIO')
print('='*30)
casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o valor do seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar o empréstimo? '))

prestação = casa/(12*anos)
print('Para pagar um casa de R${:.2f} em {} anos a prestação será de RS{:.2f}'.format(casa,anos,prestação))
if prestação > (30/100*salario):
    print('Empréstimo negado! Valor da prestação excede 30% do seu salário.')
else:
    print('Parabéns! Empréstimo concedido.')