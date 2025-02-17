from math import radians, cos, sin, tan

angulo = float(input('Digite o ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Seno: {:.3f}\nCosseno:{:.3f}\nTangente: {:.3f}'.format(seno, cosseno, tangente))