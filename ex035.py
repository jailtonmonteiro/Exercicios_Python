a = int(input('Digite o lado a: '))
b = int(input('Digite o lado b: '))
c = int(input('Digite o lado c: '))

if((a + b) > c and (a + c) > b and (b + c) > a):
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')