valor = 0
valores = [[], []]

for c in range(0, 7):
    valor = int(input('Digite o {}° valor: '.format(c+1)))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

print(f'Valores pares: {valores[0]}')
print(f'Valors impares: {valores[1]}')