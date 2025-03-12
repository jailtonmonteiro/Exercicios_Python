print('Digite os numeros: ')

numeros = (int(input('a: ')), int(input('b: ')), int(input('c: ')), int(input('d: ')))
print(numeros)
nove = 0

for x in numeros:
    if x == 9:
        nove += 1

print('Número 9 apareceu {} vez(es)'.format(nove))

if 3 in numeros:
    print('Número 3 foi o {}° digitado'.format(numeros.index(3)+1))
else:   
    print('Não foi digitado nenhum número 3')
        
print('Números pares: ', end=' ')

for p in numeros:
    if p % 2 == 0:
        print(p, end=' ')