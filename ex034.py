salario = float(input('Digite o salário: '))

if(salario > 1250.00):
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)

print('Salário atualizado R$: {:.2f}'.format(aumento))