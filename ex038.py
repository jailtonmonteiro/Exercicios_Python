one = int(input('Digite o primeiro valor inteiro: '))
duo = int(input('Digite o segundo valor inteiro: '))

if one > duo:
    print('O primeiro valor é maior')
elif duo > one:
    print('O segundo valor é maior')
elif one == duo:
    print('Não existe valor maior, os dois são iguais')