from random import randint

computador = randint(0, 10)
usuario = 11  #Força um resultado falso para inicialização do while
palpite = 1

while usuario != computador:
    usuario = int(input('Digite o numero para tentar acertar: '))
    if usuario == computador:
        print('Você acertou!\nNúmero sorteado é {}'.format(computador))
        print('{} Palpites foram necessários'.format(palpite))
        palpite += 1
    else:
        print('Você errou!\nTente novamente')
        palpite += 1