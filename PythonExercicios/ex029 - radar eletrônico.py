vel = float(input('Qual a velocidade atual do carro? [km/h] '))
if vel > 80:
    multa = (vel-80)*7
    print('Você foi multado! A multa será no valor de R${:.2f} '.format(multa))
else:
    print('A velocidade está dentro da faixa permitida.')