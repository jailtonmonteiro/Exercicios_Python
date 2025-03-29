import ex107m as moeda

val = float(input('Digite o valor R$: '))
print(f'Aumentar: {moeda.aumentar(val):.2f}')
print(f'Diminuir: {moeda.diminuir(val):.2f}')
print(f'Dobro: {moeda.dobro(val):.2f}')
print(f'Metade: {moeda.metade(val):.2f}')