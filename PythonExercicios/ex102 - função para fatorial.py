def fatorial(num, show=False):
    """
    Função que retorna o fatorial do número.
    :param num: número para fazer a fatoração
    :param show: (opcional) True para retornar a expressão do fatorial e False para não retornar.
    :return: valor do fatorial
    """
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
        if show and i != 1:
            print(f'{i} x ', end='')
        if i == 1:
            print(f'1 = ', end='')
    return fat


print(fatorial(5, show=True))