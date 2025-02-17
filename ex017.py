from math import pow, sqrt

oposto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto adjacente: '))

hipotenusa = pow(oposto, 2) + pow(adjacente, 2)
print('Hipotenusa: {:.2f}'.format(sqrt(hipotenusa)))