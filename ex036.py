casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
anos = int(input('Digite a quantidade de anos para pagar: '))

parcela = casa / (anos * 12)
percent = salario * 0.3

if percent >= parcela:
    print('Financiamento Aprovado')
    print('Casa R$: {:.2f}\nParcela R$: {:.2f}\nQuantidade de Parcelas: {}'.format(casa, parcela, (anos * 12)))
else:
    print('Financiamento Reprovado')
    print('Casa R$: {:.2f}\nParcela esperada R$: {:.2f}\nPercentual Atual R$: {:.2f}'.format(casa, parcela, percent))