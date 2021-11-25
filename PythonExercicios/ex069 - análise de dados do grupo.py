maior18 = hom = mul20 = 0
while True:
    print('-'*30)
    print('   CADASTRE UMA PESSOA   ')
    print('-' * 30)
    idade = int(input('Escreva a idade: '))
    gen = input('Escreva o gênero: [F/M/NB] ').strip().upper()
    resp = ' '
    while resp not in 'SN':
        resp = input('Você quer continuar? [S/N]').strip().upper()
    if idade >= 18:
        maior18 += 1
    if gen == 'M':
        hom += 1
    if gen == 'F' and idade < 20:
        mul20 += 1
    if resp == 'N':
        break

print('- -'*15)
print('Fim do cadastro.')
print(f'Existem {maior18} pessoas cadastradas que são maiores de 18 anos.')
print(f'Foram cadastrados {hom} homens.')
print(f'Existem {mul20} mulheres cadastradas que são menores de 20 anos.')
