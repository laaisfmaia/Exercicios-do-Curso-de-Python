sal = float(input('Qual é o seu salário? R$'))
if sal > 1250.00:
    sal = sal + (10/100*sal)
    print('Você recebeu um aumento de 10%! Seu novo salário é R${:.2f}'.format(sal))
else:
    sal = sal + (15/100*sal)
    print('Você recebeu um aumento de 15%! Seu novo salário é R${:.2f}'.format(sal))
