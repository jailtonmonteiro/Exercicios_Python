valor = int(input('Valor de Saque: '))

cinquenta = 0
vinte = 0
dez = 0
um = 0

while valor > 0:
    if valor > 50:
        valor -= 50
        cinquenta += 1
    elif valor > 20:
        valor -= 20
        vinte += 1
    elif valor > 10:
        valor -= 10
        dez += 1
    elif valor > 0:
        valor -= 1
        um += 1

print('='*30)

print('Quantidades de notas utilizadas: ')
print('R$ 50.00 = {}\nR$ 20.00 = {}\nR$ 10.00 = {}\nR$ 1.00 = {}\n'.format(cinquenta, vinte, dez, um))

print('='*30)
