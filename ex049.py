numero = int(input('Digite um número para ver atabuada: '))

for x in range(1, 11, 1):
    print('{} x {} = {}'.format(numero, x, numero * x))