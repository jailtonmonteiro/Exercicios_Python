lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90,
         )

titulo = 'listagem de preços'
print('='*40)
print('{:-^40}'.format(titulo.upper()))
print('='*40)
for i in range(0, len(lista), 2):
    print('{:.<30}R${: >8.2f}'.format(lista[i], lista[i+1]))
print('='*40)