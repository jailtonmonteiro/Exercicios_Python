from random import randint
from time import sleep

maior = 0
numeros = []

def maior(tam):
    for i in range(0, tam):
        numeros.append(randint(0, 100))
    
    print(numeros)
    for j in range(0, tam):
        if j == 0:
            maior = numeros[j]
        elif numeros[j] > maior:
            maior = numeros[j]
    print(f'O maior número da lista é: {maior}')

while True:
    tam = int(input('Digite o tamanho da lista: '))
    print('-='*20)
    maior(tam)
    numeros.clear()
    sair = str(input('Gerar nova [S/N]: ')).strip()
    if sair in 'nN':
        break
    
    print('-='*20)