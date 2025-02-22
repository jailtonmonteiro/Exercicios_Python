from random import randint

velocidade = randint(1, 200)

if(velocidade > 80):
    multa = (velocidade - 80) * 7.00
    print('Velocidade lida: {} Km/h\n Valor da multa: R$ {:.2f}'.format(velocidade, multa))
else:
    print('Velocidade lida: {} Km/h'.format(velocidade))