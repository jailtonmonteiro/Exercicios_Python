from math import pow

peso = float(input('Digite o seu peso: '))
altura = int(input('Digite a altura em cm: '))

altura = altura/100

imc = peso / (altura * altura)

print('IMC: {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade I!')
else:
    print('Obesidade Mórbida')