def contador(inicio, fim, passo):
    for i in range(inicio, fim, passo):
        print(i, end=' ')
    print()


def primeiraContagem():
    for j in range(1, 11, 1):
        print(j, end=' ')


def segundaContagem():
    for k in range(10, 0, -2):
        print(k, end=' ')


print(f'{"CONTADORES":^14}\n\n')

inicio = int(input('Digite o inicio da contagem: '))
fim = int(input('Digite o fim da contagem: '))
passo = int(input('Digite o passo da contagem: '))

print('\n1 até 10, de 1 em 1: ',end='')
primeiraContagem()
print('\n10 até 0, de 2 em 2: ',end='')
segundaContagem()
print('\nContagem Personalizada: ',end='')
contador(inicio, fim, passo)