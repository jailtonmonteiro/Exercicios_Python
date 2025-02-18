numero = int(input('Digite um numero entre 0 e 9999: '))
num = str(numero)

print('Unidade: {}'.format(num[3]))
print('Centena: {}'.format(num[2]))
print('Dezena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))