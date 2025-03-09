soma = 0
cont = 0

while True:
    num = int(input('Digite um numero (999 para sair): '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print('Digitados: {}\nSoma: {}'.format(cont, soma))