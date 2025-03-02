
somaIdade = 0
mediaIdade = 0
maiorIdadeH = 0
nomeVelho = ''
totalMulher = 0

for p in range(1, 5):
    print('{} ª Pessoa'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()
    somaIdade += idade
    if p == 1 and sexo == 'M':
        maiorIdadeH = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maiorIdadeH:
        maiorIdadeH = idade
        nomeVelho = nome
    if sexo == 'F' and idade < 20:
        totalMulher += 1

mediaIdade = somaIdade/4
print('\nMédia de idade: {}'.format(mediaIdade))
print('\nHomem mais velho: {}\nIdade: {}'.format(nomeVelho, maiorIdadeH))
print('\nTotal de mulher com menos de 20 anos: {}'.format(totalMulher))
