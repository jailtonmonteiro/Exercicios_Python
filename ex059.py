repeat = 1

while repeat == 1:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))

    op = int(input('''
            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa
             '''))
    
    if op == 1:
        print('A soma entre {} e {} é igual a {}'.format(num1, num2,num1+num2))
    if op == 2:
        print('A multiplicação entre {} e {} é {}'.format(num1, num2, num1*num2))
    if op == 3:
        if num1 > num2:
            print('Maior: {}'.format(num1))
        elif num2 > num1:
            print('Maior: {}'.format(num2))
        else:
            print('Os numeros são iguais')
    if op == 4:
        repeat = 1
    if op == 5:        
        exit()