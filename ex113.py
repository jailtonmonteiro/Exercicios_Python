def leiaInt(msg):
    while True:
        try:
            nint = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mErro: Entrada de dados interrompida.\033[m')
            return ''
        else:
            return nint
        

def leiaFloat(msg):
    while True:
        try:
            nfloat = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número float válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro: Entrada de dados interrompida.\033[m')
            return ''
        else:
            return nfloat


nint = leiaInt('Digite um inteiro: ')
print(f'Você digitou: {nint}')
nfloat = leiaFloat('Digite um float: ')
print(f'Você digitou: {nfloat}')