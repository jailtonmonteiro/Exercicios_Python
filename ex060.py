numero = int(input('Digite o numero para ver o fatorial: '))
contador = numero
fatorial = 1

print('Calculando {}! = '.format(numero), end='')
while contador > 0:
    fatorial *= contador
    print(' {} '.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    contador -= 1

print('{}'.format(fatorial))