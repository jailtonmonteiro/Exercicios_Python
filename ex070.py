barato = 0
nomeBarato = ''
total = 0
maisMil = 0
cont = 1

while True:
    nome = str(input('\nDigite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preco R$: '))

    total += preco

    if cont == 1:
        barato = preco
        nomeBarato = nome
    if preco < barato:
        barato = preco
        nomeBarato = nome
    if preco > 1000.00:
        maisMil += 1

    print('='*40)
    continua = str(input('Quer continuar? S/N: ')).upper().strip()

    if continua == 'N':
        break
    
    cont += 1

print('='*40)
print('\nTotal da compra R$: {:.2f}'.format(total))
print('{} produto(s) custam mais de R$ 1000.00'.format(maisMil))
print('Produto mais barato: {}\nR$ {:.2F}'.format(nomeBarato, barato))
print('='*40)