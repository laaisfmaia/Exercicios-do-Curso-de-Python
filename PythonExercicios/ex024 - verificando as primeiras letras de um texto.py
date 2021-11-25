cidade = input('Escreva o nome da cidade: ').strip()
PrimNome = cidade.upper().split()
print('Essa cidade começa com a palavra "Santo"? {} '.format('SANTO' in PrimNome[0]))