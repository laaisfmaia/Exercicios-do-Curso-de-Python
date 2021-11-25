from datetime import date
ano = int(input('Qual o ano de nascimento do jovem? '))
idade = date.today().year - ano
print('Quem nasceu em {} tem {} anos.'.format(ano,idade))
if idade < 18:
    sobra = 18 - idade
    print('Ele tem menos de 18 anos e vai se alistar no serviço militar daqui a {} anos.'.format(sobra))
elif idade == 18:
    print('Ele tem 18 anos e está na hora de se alistar!')
else:
    excedido = idade - 18
    print('Ele já excedeu o tempo de alistamento em {} anos!'.format(excedido))