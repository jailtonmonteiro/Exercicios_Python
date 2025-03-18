from random import randint
from time import sleep
from operator import itemgetter

jogada = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6),
}

print('='*30)
print('Valores Sorteados: ')
print('='*30)

for k, v in jogada.items():
    print(f'O {k} tirou {v} no dado')
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)

print('='*30)
print('Ranking dos Jogadores')
print('='*30)

for i, j in enumerate(ranking):
    print(f'{i+1}° lugar: {j[0]} com {j[1]}')
    sleep(0.3)