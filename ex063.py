from math import sqrt

n = int(input('Digite a quantidade de elementos da sequência: '))
count = 0
aurea = 1.61803398875

while count < n:
    seq = int(((aurea**count) - ((1-aurea)**count)) / sqrt(5))
    count += 1
    print('{}'.format(seq), end='')
    print(' -> ' if count < n else '', end='')
print(' -> FIM')