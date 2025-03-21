pessoa = {}
pessoas = []
soma = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['sexo'] = str(input('Sexo F/M: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    adicionar = str(input('Quer continuar S/N: '))
    if adicionar in 'nN':
        break

print('=-='*10)

print(f'Foram cadastradas {len(pessoas)} pessoas')
for j in pessoas:
    soma += j['idade']

print(f'A média de idade é {soma/len(pessoas)} anos')

print('A mulheres cadastradas são ',end='')
for j in pessoas:
    if j['sexo'] == 'F':
        print(f'{j["nome"]}', end=', ')

print('\nLista de pessoas com idade acima da média: ')
for j in pessoas:
    if j['idade'] >= (soma/len(pessoas)):
        for k, v in j.items():
            print(f' => {k} = {v};',end=' ')
        print()
        