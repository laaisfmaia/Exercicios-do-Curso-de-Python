valores = []
maior = menor = 0
for i in range(0, 5):
    valores.append(int(input(f'Escreva o {i+1}° valor: ')))
    if i == 0:
        maior = valores[i]
        menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]
print('-'*30)
print(f'Você digitou os valores: {valores}')
print(f'O MAIOR valor digitado foi {maior} na posição ', end='')
for ind, num in enumerate(valores):
    if num == maior:
        print(f'{ind}...', end='')
print('')
print(f'O MENOR valor digitado foi {menor} na posição ', end='')
for ind, num in enumerate(valores):
    if num == menor:
        print(f'{ind}...', end='')

#print(f'O MAIOR valor digitado foi {max(valores)} e ele está na {valores.index(max(valores))+1}° posição.')
#print(f'O MENOR valor digitado foi {min(valores)} e ele está na {valores.index(min(valores))+1}° posição.')