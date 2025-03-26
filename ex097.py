def escreva(palavra):
    tam = int(len(palavra)+4)
    print('~'*tam)
    print(f'  {palavra}')
    print('~'*tam)


print('TEXTO FORMATADO\n')
texto = str(input('Digite o texto: ')).strip().upper()
escreva(texto)