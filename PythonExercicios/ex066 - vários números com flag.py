soma = qNum = 0
while True:
    n = int(input('Escreva um número inteiro [Digite 999 para parar]: '))
    if n == 999:
        break
    soma += n
    qNum += 1

print(f'Foram digitados {qNum} números e a soma deles foi {soma}')
