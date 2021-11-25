largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))
area = largura*altura
LitrosTinta = area/2
print('A área dessa parede é de {} m^2 e será necessário {} Litros de tinta para pinta-lá.'.format(area,LitrosTinta))
