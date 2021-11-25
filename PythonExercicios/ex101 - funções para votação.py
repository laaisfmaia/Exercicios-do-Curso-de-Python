def voto(ano=0):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com idade {idade} anos: NÃO VOTA.'
    elif idade > 65 or 16 <= idade < 18:
        return f'Com idade {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com idade {idade} anos: VOTO OBRIGÁTORIO.'


resp = int(input('Em que ano você nasceu? '))
print(voto(resp))

