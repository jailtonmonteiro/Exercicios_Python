primeiroTermo = int(input('Digite o Primeiro termo: '))
razao = int(input('Digite a Razao: '))
count = 0
qtd = 10

print('PA {} = '.format(primeiroTermo))
while count < qtd:
    termo = primeiroTermo + count * razao
    print(' {} '.format(termo), end='')
    if count < qtd - 1:
        print(' -> ', end='')
    else:
        print('-> Pausa')
        novaContagem = int(input('Quantos termos quer mostrar mais: '))
        if novaContagem != 0:
            qtd += novaContagem
        else:
            print('Fim')
    count += 1