valores = []
impares = []
pares = []

while True:
    val = int(input('Digite um valor: '))
    valores.append(val)
    op = str(input('Quer continuar? S/N: '))
    if op in 'nN':
        break

for i in range(len(valores)):
    if valores[i] % 2 == 0:
        pares.append(valores[i])
    else:
        impares.append(valores[i])

print('Digitados: {}'.format(valores))
print('Pares: {}'.format(pares))
print('Impares: {}'.format(impares))