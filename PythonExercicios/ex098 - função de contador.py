def contador(início, fim, passo):
    from time import sleep
    print('=' * 40)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    if início < fim:
        for i in range(início, fim+1, passo):
            print(i, end=' ')
            sleep(0.5)
        print('FIM')
    elif início > fim:
        for i in range(início, fim-1, -passo):
            print(i, end=' ')
            sleep(0.5)
        print('FIM')
    sleep(0.5)


contador(1,10,1)
contador(10,0,2)
print('=' * 40)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
