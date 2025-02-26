primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print('10 Termos')
for x in range(10):
    termo = primeiroTermo + x * razao
    print('{}° Termo = {}'.format(x+1, termo))