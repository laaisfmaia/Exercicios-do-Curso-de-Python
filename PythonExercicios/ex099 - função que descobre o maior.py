def maior(*números):
    maior = 0
    from time import sleep
    print('-'*50)
    print('Analisando os valores passados...')
    for i, valor in enumerate(números):
        print(valor, end=' ')
        sleep(0.2)
        if i == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    print()
    print(f'Foram informados {len(números)} números ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
