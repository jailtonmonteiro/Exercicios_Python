extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))

    if num >= 0 and num <= 20:
        print('Digitou {}'.format(extenso[num]))
        op = str(input('Quer continuar? S/N: '))
        if op in 'nN':
            break