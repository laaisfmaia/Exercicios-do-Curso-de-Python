from lib.Interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)



while True:
    resp = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resp == 1:
        cabeçalho('Opção 1')
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('Opção 2')
    elif resp == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('\033[31mErro! Digite uma opção válida\033[m')
    sleep(2)