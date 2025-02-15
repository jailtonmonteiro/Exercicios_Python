entrada = input('Digite o valor: ')

print('{}'.format(type(entrada)))
print('Numero: {}\nAlfabeto: {}\nAlfanumérico: {}\nMaiúsculo: {}\n'.format(entrada.isnumeric(), entrada.isalpha(), entrada.isalnum(), entrada.isupper()))