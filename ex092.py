from datetime import date

funcionario = {}
anoAtual = date.today().year

print('**'*20)

funcionario['nome'] = str(input('Nome: ')).strip().capitalize()
nascimento = int(input('Ano de nascimento: '))
funcionario['idade'] = anoAtual - nascimento
funcionario['ctps'] = int(input('Carteira de trabalho(0 não tem): '))

if funcionario['ctps'] > 0:
    funcionario['anoContrato'] = int(input('Ano Contratação: '))
    funcionario['salario'] = float(input('Salário: R$ '))
    funcionario['aposentadoria'] = 70 - funcionario['idade']
print('**'*20)
print()

if funcionario['ctps'] >= 0:
    print('=='*20)
    print('{:^20}'.format("DADOS FUNCIONÁRIO"))
    print('=='*20)
    print(f'Nome: {funcionario["nome"]}')
    print(f'Idade: {funcionario["idade"]}')
    print(f'Carteira de trabalho te valor {funcionario["ctps"]}')
if funcionario['ctps'] > 0:
    print(f'Contradato: {funcionario["anoContrato"]}')
    print(f'Salário R$: {funcionario["salario"]}')
    print(f'Aposenta em {funcionario["aposentadoria"]} anos')

print('=='*20)
