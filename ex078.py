valores = list()
for x in range(0, 5):
    val = int(input('Digite o {}° valor: '.format(x+1)))
    valores.append(val)
    if x == 0:
        maior = valores[x]
        menor = valores[x]
        imenor = imaior = x
    if valores[x] > maior:
        maior = valores[x]
        imaior = x
    if valores[x] < menor:
        menor = valores[x]
        imenor = x


print(valores)
print('='*20)
print('Menor valor: {}'.format(menor))
print('Indice menor: {}'.format(imenor))
print('Maior valor: {}'.format(maior))
print('Indice maior: {}'.format(imaior))