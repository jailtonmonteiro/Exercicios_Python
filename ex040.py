nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Média: {:.1f}\nReprovado!'.format(media))
elif media >= 5.0 and media < 7.0:
    print('Média: {:.1f}\nRecuperação!'.format(media))
elif media >= 7.0:
    print('Média: {:.1f}\nAprovado!'.format(media))