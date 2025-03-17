aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 7 and aluno['media'] >= 3:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('='*20)
print(f'Nome: {aluno['nome']}')
print(f'Média: {aluno['media']}')
print(f'Situação: {aluno['situação']}')