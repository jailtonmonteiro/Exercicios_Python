km = float(input('Digite a quantidade de KM: '))
dia = int(input('Digite a quantidade de dias: '))

valor = (dia * 60) + (km * 0.15)

print('Descritivo\n\n Custo por km: R$ 0,15\nCusto por dia: R$ 60,00\n\nValor total: R$ {:.2f}'.format(valor))