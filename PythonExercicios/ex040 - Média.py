nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))

media = (nota1 + nota2)/2
print('Tirando {} e {}, a média do aluno será de {:.1f}'.format(nota1,nota2,media))
if media < 5:
    print('@ alun@ foi REPROVADO.')
elif 5 <= media <= 6.9:
    print('@ alun@ está de RECUPERAÇÃO.')
else:
    print('@ alun@ foi APROVADO.')