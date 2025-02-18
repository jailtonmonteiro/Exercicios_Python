from random import sample

nomeUm = input('Digite o primeiro nome: ')
nomeDois = input('Digite o segundo nome: ')
nomeTres = input('Digite o terceiro nome: ')
nomeQuatro = input('Digite o Quarto nome: ')

lista = [nomeUm, nomeDois, nomeTres, nomeQuatro]

print('Ordem de apresentação: {}'.format(sample(lista, k=4)))