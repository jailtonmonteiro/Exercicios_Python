import ex109m as moeda

val = float(input('Digite o valor R$: '))

print(f'Aumentar 10%: {moeda.aumentar(val)}')
print(f'Diminuir 5%: {moeda.diminuir(val)}')
print(f'Dobro: {moeda.dobro(val, True)}')
print(f'Metade: {moeda.metade(val, True)}')
