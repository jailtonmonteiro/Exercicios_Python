largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

print('Será necessário {} l para pintar a area de {} m²'.format((area/2), area))