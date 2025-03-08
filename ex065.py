continua = 'S'
cont = 0
soma = 0
maior = 0
menor = 0

while continua == 'S':
    numero = int(input('Digite um numero: '))
    if cont == 0:
        maior = numero
        menor = numero
    else:
        if numero >= maior:
            maior = numero
        if numero <= menor:
            menor = numero
    cont += 1
    soma += numero
    continua = str(input('Quer continuar(s/n)? ')).upper().strip()

print('Maior = {} Menor = {}'.format(maior, menor))
print('Digitados = {}\nMédia = {:.2f}'.format(cont, soma/cont))