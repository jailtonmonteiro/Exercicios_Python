frase = str(input('Digite a frase: ')).strip()

print('A letra "A" aparece {} vezes'.format(frase.upper().count('A')))
print('A primeira ocorrência da letra "A" ocorre na posição {}'.format(frase.upper().find('A')+1))
print('A ultima ocorrência da letra "A" ocorre na posição: {}'.format(frase.upper().rfind('A')+1))