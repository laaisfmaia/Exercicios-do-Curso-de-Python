peso = float(input('Qual é o seu peso em kg? '))
alt = float(input('Qual a sua altura em metros? '))

imc = peso / alt**2
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está na faixa de obesidade.')
else:
    print('Você está na faixa de obesidade mórbita.')
