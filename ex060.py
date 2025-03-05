numero = int(input('Digite o numero para ver o fatorial: '))
fatorial = numero

while numero > 1:
    fatorial = fatorial * (numero - 1)
    numero -= 1

print('Fatorial = {}'.format(fatorial))