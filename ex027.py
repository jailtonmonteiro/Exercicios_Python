nome = str(input('Nome completo: '))

separado = nome.split();
print('Primeiro nome: {}'.format(separado[0]))
print('Ultimo sobrenome: {}'.format(separado[len(separado) - 1]))