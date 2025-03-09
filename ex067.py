cont = 0

while True:
    num = int(input('Digite um numero para ver a tabuada: '))
    print('='*50)
    if num < 0:
        print('Calculadora encerrada')
        break
    else:
        for x in range(11):
            print('{} x {} = {}'.format(num, x, num * x))
    print('='*50)