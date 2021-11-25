import requests

try:
    resp = requests.get('http://pudim.com.br/')
except:
    print(f'\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print(f'\033[33mConsegui acessar o site Pudim com sucesso!\033[m')