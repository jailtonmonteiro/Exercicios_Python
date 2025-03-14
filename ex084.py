dado = list()
pessoas = list()
maior = menor = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))

    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
            nomeMaior = dado[0]
        if dado[1] < menor:
            menor = dado[1]
            nomeMenor = dado[0]
    pessoas.append(dado[:])
    dado.clear()
    op = str(input('Quer continuar? [S/N]: '))
    if op in 'nN':
        break


print('='*35)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'Maior peso foi do {nomeMaior}: {maior:.1f} Kg')
print(f'Menor peso foi do {nomeMenor}: {menor:.1f} Kg')