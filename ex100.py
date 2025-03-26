from random import randint

def sorteia():
    for i in range(0, 5):
        numeros.append(randint(0, 100))
    print(f'Lista: {numeros}')


def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'Soma de pares: {soma}')


while True:
    numeros = list()
    print('-='*20)
    sorteia()
    somaPar(numeros)
    numeros.clear()
    continua = str(input('Quer continuar [S/N]: '))
    if continua in 'nN':
        break
    print('-='*20)
    soma = 0