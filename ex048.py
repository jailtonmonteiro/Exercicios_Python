intervalo = 500
soma = 0

for x in range(intervalo):
    if(x % 3 == 0):
        print(x)
        soma += x
print('Soma dos multiplos de 3 = {}'.format(soma))