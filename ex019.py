from random import choice

nomeUm = input('Digite o primeiro nome: ')
nomeDois = input('Digite o segundo nome: ')
nomeTres = input('Digite o terceiro nome: ')
nomeQuatro = input('Digite o Quarto nome: ')

lista = [nomeUm, nomeDois, nomeTres, nomeQuatro]

print('O escolhido foi {}'.format(choice(lista)))