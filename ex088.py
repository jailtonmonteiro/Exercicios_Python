from random import randint
from time import sleep

quantidade = 0
cont = 0
palpite = []

print('-'*30)
print('{:^30}'.format('PALPITES MEGA SENA'))
print('-'*30)

quantidade = int(input('Quantos jogos deseja? '))

while cont < quantidade:
    while len(palpite) < 6:
        x = randint(1, 60)
        if x not in palpite:
            palpite.append(x)
    print(f'Jogo {cont+1}: {sorted(palpite)}')
    palpite.clear()
    cont += 1
    sleep(1)    