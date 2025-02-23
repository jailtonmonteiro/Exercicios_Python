a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))

menor = a

if(b < a and b < c):
    menor = b
if(c < a and c < b):
    menor = c

maior = a

if(b > a and b > c):
    maior = b
if(c > a and c > b):
    maior = c

print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
