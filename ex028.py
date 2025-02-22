from random import randint;
numero = randint(0, 5)

tentativa = int(input('Digite o seu numero: '))

print('O computador escolheu {}'.format(numero))
print('Você acertou' if numero == tentativa else 'Você errou!')