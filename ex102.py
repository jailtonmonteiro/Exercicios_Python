def fatorial(n, show=False):
    '''
    => Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n.
    '''

    fatorial = 1
    contador = n
    while contador > 0:
        fatorial *= contador
        if show == True:
            print(' {} '.format(contador), end='')
            print(' x ' if contador > 1 else ' = ', end='')
        contador -= 1
    print(f'{fatorial}')
    

n = int(input('Digite o numero: '))
show = str(input('Mostrar calculo [S/N]: '))[0]
if show in 'sS':
    fatorial(n, True)
else:
    fatorial(n)