matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0,]]
soma = 0
somaTerceira = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite o valor [{}, {}]: '.format(l+1, c+1)))
        soma += matriz[l][c]
        if l == 1:
            maior = matriz[l][c]
        elif matriz[1][c] > maior:
            maior = matriz[l][c]

        if c == 2:
            somaTerceira += matriz[l][2]
print('=-='*10)

for l in range(0, 3):
    for c in range(0, 3):
        print('[{:^5}]'.format(matriz[l][c]), end='')
    print('')

print('=-='*10)

print(f'Soma de todos os valores: {soma}')
print(f'Soma valores terceira coluna: {somaTerceira}')
print(f'Maior valor linha 2: {maior}')
