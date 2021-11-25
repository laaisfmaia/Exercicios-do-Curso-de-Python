palavras = ('Python', 'Laranja', 'Ferro', 'Bola', 'Natal', 'alegria')

for p in palavras:
    print(f'\nA palavra {p.upper()} tem as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
