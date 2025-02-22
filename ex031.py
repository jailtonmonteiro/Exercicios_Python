from random import randint

distancia = randint(0, 500)

if(distancia > 200):
    valor = distancia*0.45
    print('Corrida: {} Km\nValor R$: {:.2f}'.format(distancia, valor))
else:
    valor = distancia*0.50
    print('Corrida: {} Km\nValor R$: {:.2f}'.format(distancia, valor))