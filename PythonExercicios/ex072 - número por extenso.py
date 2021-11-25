NumExtenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    resp = 'S'
    n = int(input('Escreva um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {NumExtenso[n]}')
        resp = input('Você quer continuar? [S/N] ').upper().strip()
    else:
        print('Tente novamente. Escreva um número entre 0 e 20: ')
    if resp == 'N':
        break





