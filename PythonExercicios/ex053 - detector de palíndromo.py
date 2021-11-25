print('==== Detector de Palíndromo ====')
frase = input('Escreva uma frase: ').strip().lower().replace(' ', '')

tamFrase = len(frase)
s = 0
for i in range(0, tamFrase):
    ult = tamFrase - i
    if frase[i] != frase[ult-1]:
        s = s + 1
if s == 0:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase NÃO é um palíndromo.')






