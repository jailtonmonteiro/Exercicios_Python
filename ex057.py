sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo F/M: ')).strip().upper()
    print(sexo)

if sexo == 'F':
    print('Sexo Feminino')
elif sexo == 'M':
    print('Sexo Masculino')