import moeda

n = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n,fmt=True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, fmt=True)}')
print(f'Aumentando 10% de {moeda.moeda(n)} temos {moeda.aumentar(n,10,fmt=True)}')
print(f'Diminuindo 20% de {moeda.moeda(n)} temos {moeda.diminuir(n,20,fmt=True)}')
