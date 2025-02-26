soma = 0
for x in range(6):
    numero = int(input('Digite o valor inteiro: '))
    if(numero % 2 == 0):
        soma += numero
print('Soma dos pares: {}'.format(soma))