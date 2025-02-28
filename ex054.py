from datetime import date

atual = date.today()
maior = 0
menor = 0

for x in range(7):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(x+1)))

    if atual.year - ano > 18:
        maior += 1
    else:
        menor += 1

print('Menor de idade: {}\nMaior de idade: {}'.format(menor, maior))