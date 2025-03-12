valores = list()

while True:
    val = int(input('Digite um valor inteiro: '))
    if val in valores:
        print('Valor já existente!')
    else:
        valores.append(val)
        print('Valor adicionado com sucesso!')
    
    op = str(input('Quer continuar? S/N: '))
    if op in 'nN':
        break

print('Valores ordenados: {}'.format(sorted(valores)))