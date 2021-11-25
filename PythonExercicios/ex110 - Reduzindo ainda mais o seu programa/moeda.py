def aumentar(valor=0, porc=0, fmt = False):
    """
    Função que aumenta o valor por uma porcentagem dada.
    :param valor: valor que se quer aumentar
    :param porc: porcentagem
    :param fmt: formatação da moeda
    :return: o valor acrescido da porcentagem
    """
    num = valor + (porc/100)*valor
    if fmt:
        return moeda(num)
    else:
        return num


def diminuir(valor=0, porc=0, fmt=False):
    """
    Função que reduz o valor por uma porcentagem dada.
    :param valor: valor que se quer diminuir
    :param porc: porcentagem
    :param fmt: formatação da moeda
    :return: o valor reduzido da porcentagem
    """
    num = valor - (porc / 100) * valor
    if fmt:
        return moeda(num)
    else:
        return num


def dobro(valor=0, fmt=False):
    """
    Função que dobra o valor
    :param valor: valor que se quer dobrar
    :param fmt: formatação da moeda
    :return: valor dobrado
    """
    num = valor*2
    if fmt:
        return moeda(num)
    else:
        return num


def metade(valor=0, fmt=False):
    """
    Função que dobra o valor
    :param valor: valor que se quer dobrar
    :param fmt: formatação da moeda
    :return: valor dobrado
    """
    num = valor / 2
    if fmt:
        return moeda(num)
    else:
        return num


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, porcAum=10, porcDim=10):
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-'*35)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor,fmt=True)}')
    print(f'Metade do preço: \t{metade(valor,fmt=True)}')
    print(f'{porcAum}% de aumento: \t{aumentar(valor,porcAum,fmt=True)}')
    print(f'{porcDim}% de redução: \t{diminuir(valor,porcDim,fmt=True)}')

