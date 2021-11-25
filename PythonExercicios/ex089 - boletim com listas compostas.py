dados = []
print('='*40)
print(f'{"Cadastro de Notas":^40}')
print('='*40)
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    dados.append([nome, [nota1, nota2], media])

    resp = input('Você quer continuar? [S/N] ').upper().strip()
    while resp not in 'SN':
        resp = input('Opção inválida. Você quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break

print('='*30)
print(f'{"n°":<3}{"NOME":<11} {"MÉDIA":>10}')
print('-'*25)
for i in range(0, len(dados)):
    print(f'{i:<3}{dados[i][0]:<10} {dados[i][2]:>10.1f}')
print('-'*25)
while True:
    qualAluno = int(input('Mostrar notas de qual aluno? Digite o n° correspondente ao aluno: [999 interrompe] '))
    if qualAluno == 999:
        break
    if qualAluno <= len(dados)-1:
        print(f'As notas de {dados[qualAluno][0]} são {dados[qualAluno][1]}')
print('FINALIZADO')
