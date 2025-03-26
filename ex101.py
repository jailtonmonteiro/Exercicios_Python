def voto(nascimento=0):
    from datetime import date

    anoAtual = date.today().year
    idade = anoAtual - nascimento
    
    if idade > 18:
        return f'{idade} anos: VOTO OBRIGATÓRIO'
    elif idade > 16:
        return f'{idade} anos: VOTO OPCIONAL'
    else:
        return f'{idade} anos: VOTO NEGADO'
    


print('=-='*15)
nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))