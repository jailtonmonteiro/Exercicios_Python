from random import randint

while True:
    op = str(input('\nPar ou Impar P/I: ')).upper().strip()
    num = int(input('Digite um numero: '))

    com = randint(0, 10)
    soma = num + com

    if soma % 2 == 0 and op == 'P':
        print('Você = {}\nComputador = {}'.format(num, com))
        print('Você ganhou!')
    elif soma % 2 != 0 and op == 'I':
        print('Você = {}\nComputador = {}'.format(num, com))
        print('Você ganhou!')
    else:
        print('Você = {}\nComputador = {}'.format(num, com))
        print('Você perdeu')
        break