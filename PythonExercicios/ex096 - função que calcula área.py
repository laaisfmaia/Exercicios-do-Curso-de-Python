def area(largura,comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m^2.')


print('-'*40)
print(f'{"Controle de Terrenos":^40}')
print('-'*40)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

