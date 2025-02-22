from random import randint

numero = randint(0, 10)

print('Numero: {}'.format(numero))
print('Par' if numero % 2 == 0 else 'Ímpar')