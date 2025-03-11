from random import randint

numeros = (randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999))

for n in range(len(numeros)):
    if n == 0:
        menor = numeros[n]
        maior = numeros[n]
    if menor > numeros[n]:
        menor = numeros[n]
    if maior < numeros[n]:
        maior = numeros[n]

for p in range(len(numeros)):
    print('{}'.format(numeros[p]), end=' ')

print('\nMaior: {}'.format(maior))
print('Menor: {}'.format(menor))