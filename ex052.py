numero = int(input('Digite um número '))
total = 0

for x in range(1, numero + 1):
    if numero % x == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(x), end='')

print('\n\033[m Número {} divisível {} vezes'.format(numero, total))
if total == 2:
    print('Numero Primo')
else:
    print('Não é primo')