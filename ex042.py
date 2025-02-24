a = int(input('Digite o lado A: '))
b = int(input('Digite o lado B: '))
c = int(input('Digite o lado C: '))

if a == b and b == c:
    print('Triângulo Equilátero')
elif a != b and b != c:
    print('Triângulo Escaleno')
else:
    print('Triângulo Isósceles')