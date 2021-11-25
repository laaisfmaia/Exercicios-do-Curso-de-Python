def aumentar(valor, porc):
    """
    Função que aumenta o valor por uma porcentagem dada.
    :param valor: valor que se quer aumentar
    :param porc: porcentagem
    :return: o valor acrescido da porcentagem
    """
    num = valor + (porc/100)*valor
    return num


def diminuir(valor, porc):
    """
    Função que reduz o valor por uma porcentagem dada.
    :param valor: valor que se quer diminuir
    :param porc: porcentagem
    :return: o valor reduzido da porcentagem
    """
    num = valor - (porc / 100) * valor
    return num


def dobro(valor):
    """
    Função que dobra o valor
    :param valor: valor que se quer dobrar
    :return: valor dobrado
    """
    num = valor*2
    return num


def metade(valor):
    """
    Função que dobra o valor
    :param valor: valor que se quer dobrar
    :return: valor dobrado
    """
    num = valor / 2
    return num

