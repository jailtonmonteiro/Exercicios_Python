maisDezoito = 0
qtdHomens = 0
mulheresVinte = 0

while True:
    nome = str(input('\n\nDigite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o Sexo F/M: ')).strip()

    if idade > 18:
        maisDezoito += 1
    if sexo in 'mM':
        qtdHomens += 1
    if sexo in 'fF' and idade < 20:
        mulheresVinte += 1
    
    cadastro = str(input('\nQuer continuar? S/N: ')).strip().upper()
    print('='*30)

    if cadastro == 'N':
        break

print('Foram cadastrados {} homens'.format(qtdHomens))
print('{} Pessoas tem mais de 18 anos'.format(maisDezoito))
print('{} Mulheres tem menos de 20 anos'.format(mulheresVinte))