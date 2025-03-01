lista = [0, 0, 0, 0, 0]

for x in range(0, 5, 1):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(x+1)))
    lista[x] = peso

maior = lista[0]
menor = lista[0]

for peso in lista:
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('Pesos digitados: {}'.format(lista))
print('Maior: {}\nMenor: {}'.format(maior, menor))