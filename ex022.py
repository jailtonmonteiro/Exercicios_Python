nome = 'Jailton Monteiro da Silva'

print('Maiúsculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras(sem espaços): {}'.format(len(nome) - nome.count(' ')))

separado = nome.split();

print('Quantidade de letras primeiro nome: {}'.format(len(separado[0])))
