import random

a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
alunos = [a1,a2,a4,a3]
print('O aluno escolhido aleatoriamente foi {}'.format(random.choice(alunos)))
