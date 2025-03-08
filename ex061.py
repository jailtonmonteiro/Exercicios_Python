primeiroTermo = int(input('Digite o Primeiro termo: '))
razao = int(input('Digite a Razao: '))
qtd = 0

print('PA {} = '.format(primeiroTermo))
while qtd < 10:
    termo = primeiroTermo + qtd * razao
    print(' {} '.format(termo), end='')
    print(' -> ' if qtd < 10-1 else ' -> FIM ', end='')
    qtd += 1