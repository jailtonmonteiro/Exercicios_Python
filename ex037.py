numero = int(input('Digite um numero inteiro: '))
op = int(input("""
               Selecione a conversão\n\n
               1 - Binário
               2 - Octal
               3 - Hexadecimal
               """))

if op == 1:
    print('Binario: {}'.format(bin(numero)[2:]))
elif op == 2:
    print('Octal: {}'.format(oct(numero)[2:]))
else:
    print('Hexadecimal: {}'.format(hex(numero)[2:]))