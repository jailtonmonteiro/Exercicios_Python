from random import randint

vitorias = 0

while True:
    op = str(input('\nPar ou Impar P/I: ')).upper().strip()
    num = int(input('Digite um numero: '))

    com = randint(0, 10)
    soma = num + com

    if soma % 2 == 0 and op == 'P':
        print('Você = {}\nComputador = {}'.format(num, com))
        print('Você ganhou!')
        vitorias += 1
    elif soma % 2 != 0 and op == 'I':
        print('Você = {}\nComputador = {}'.format(num, com))
        print('Você ganhou!')
        vitorias += 1
    else:
        print('Você = {}\nComputador = {}'.format(num, com))
        print('Você perdeu')
        break