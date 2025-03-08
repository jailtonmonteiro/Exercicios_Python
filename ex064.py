cont = 0
soma = 0
while cont != 999:
    cond = int(input('Digite um numero ou 999 para sair: '))
    if cond == 999:
        break
    else:
        cont += 1
        soma += cond

print('Digitados: {}\nSoma: {}'.format(cont, soma))