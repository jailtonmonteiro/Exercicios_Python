import datetime

anoNascimento = int(input('Insira o ano de nascimento: '))

atual = datetime.date.today()

if atual.year - anoNascimento > 18:
    print('Já passou da hora do alistamento militar obrigatório!')
    print('Tempo de atraso: {} anos'.format(atual.year-anoNascimento-18))
elif atual.year - anoNascimento < 18:
    print('Ainda falta um tempo para o seu alistamento militar obrigatório')
    print('Faltam {} anos'.format(18 - (atual.year - anoNascimento)))
elif atual.year - anoNascimento == 18:
    print('Está na hora de fazer o alistamento militar obrigatório')