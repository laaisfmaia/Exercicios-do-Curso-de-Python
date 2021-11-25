valor = float(input('Qual é o valor do produto? R$'))
print('='*50)
n = int(input('Qual vai ser a condição de pagamento? \n[1] - para pagar à vista no dinheiro/cheque;\n[2] - para pagar à vista no cartão;\n[3] - para pagar de 2x no cartão;\n[4] - para pagar de 3x ou mais no cartão.\nDigite: '))

if n == 1:
    desc = valor - (10/100*valor)
    print('Você recebeu 10% de desconto! O produto sairá por apenas R${:.2f}'.format(desc))
elif n == 2:
    desc = valor - (5/ 100 * valor)
    print('Você recebeu 5% de desconto! O produto sairá por apenas R${:.2f}'.format(desc))
elif n == 3:
    parcela = valor/2
    print('Você pagará 2 parcelas de R${:.2f} sem juros. E o produto sairá por R${:.2f}'.format(parcela,valor))
elif n == 4:
    valor = valor + (20 / 100 * valor)
    totalparcelas = int(input('Deseja dividir em quantas parcelas? '))
    parcela = valor/totalparcelas
    print('Você pagará {} parcelas de R${:.2f} com jurso de 20%. E o produto sairá por R${:.2f}'.format(totalparcelas,parcela, valor))
else:
    print('Opção inválida de pagamento! Tente novamente.')
