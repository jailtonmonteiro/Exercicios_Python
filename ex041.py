from datetime import date

atual = date.today()
anoNascimento = int(input('Digite o ano de nascimento: '))
idade = atual.year - anoNascimento

if idade > 25:
    print('Idade {} anos\nAtleta MASTER'.format(idade))
elif idade > 19:
    print('Idade {} anos\nAtleta SÊNIOR'.format(idade))
elif idade > 14:
    print('Idade {} anos\nAtleta JÚNIOR'.format(idade))
elif idade > 9:
    print('Idade {} anos\nAtleta INFANTIL'.format(idade))
else:
    print('Idade {} anos\nAtleta MIRIM'.format(idade))