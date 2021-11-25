import moeda

n = float(input('Digite um preço: R$'))
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'Aumentando 10% de {n} temos {moeda.aumentar(n,10)}')
print(f'Diminuindo 20% de {n} temos {moeda.diminuir(n,20)}')
