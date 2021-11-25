print('=== Tabuada ===')

while True:
    n = int(input('Você quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for i in range(0, 11):
        print(f'{n:2} x {i:<2} = {n * i} ')
    print('-'*40)

print('Tabuada encerrada.')