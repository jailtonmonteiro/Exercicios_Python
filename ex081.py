valores = []

while True:
    val = int(input('Digite um valor: '))
    valores.append(val)
    op = str(input('Quer continuar? S/N: '))
    if op in 'nN':
        break

print('Foram digitados {} valores'.format(len(valores)))
valores.sort(reverse=True)
print('{}'.format(valores))
if 5 in valores:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')