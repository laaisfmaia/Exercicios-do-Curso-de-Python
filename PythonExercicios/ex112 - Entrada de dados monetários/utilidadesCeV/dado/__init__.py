def leiaDinheiro(strg):
    valido = False
    while not valido:
        n = input(strg).replace(',','.').strip()
        if n.isalpha():
            print('\033[0;31mErro! Digite um valor monetário válido.\033[m')
        else:
            valido = True
            return float(n)



