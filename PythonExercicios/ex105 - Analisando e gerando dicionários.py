def notas(*num, sit=False):
    """
    Função que recebe várias notas e calcula a nota maior, a menor,
    a média das notas e a situação do aluno.
    :param num: valor das notas; pode ter várias notas
    :param sit: (opcional) Situação da média do aluno; se está Boa (média>=7); Razoável (6<=média<7) ou Ruim (média<6)
    :return: dict com esses valores
    """
    dic = dict()
    dic['Quantidade de notas'] = len(num)
    dic['Maior nota'] = max(num)
    dic['Menor nota'] = min(num)
    dic['Média'] = sum(num)/len(num)
    if sit:
        if dic['Média'] >= 7:
            dic['Situação'] = 'Boa'
        if 6 <= dic['Média'] < 7:
            dic['Situação'] = 'Razoável'
        if dic['Média'] < 6:
            dic['Situação'] = 'Ruim'
    return dic


r = notas(6.1, 6.5,10, sit=True)
print(r)
help(notas)
