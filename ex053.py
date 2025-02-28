frase = str(input('Digite a frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)

invertido = ''

for l in range(len(junto) -1, -1, -1):
    invertido += junto[l]

if junto == invertido:
    print('A frase "{}" é um palindromo'.format(frase))
    print('Original: {}\nInverido: {}'.format(junto, invertido))
else:
    print('A frase "{}" não é um palindromo'.format(frase))
    print('Original: {}\nInverido: {}'.format(junto, invertido))