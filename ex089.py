aluno = []
alunos = []

while True:
    aluno.append(str(input('Digite o nome: ')).strip().upper())
    notaA = float(input('Digite a primeira nota: '))
    notaB = float(input('Digite a segunda nota: '))
    media = (notaA+notaB)/2
    aluno.append(media)

    alunos.append(aluno[:])
    aluno.clear()

    parar = str(input('Quer continuar? [S/N]: '))
    if parar in 'nN':
        break

print('='*20)
print('{:^20}'.format('LISTA DE NOTAS'))
print('='*20)
print('{:<5}{:<10}{:>5}'.format('N°','NOME','MÉDIA'))
print('-'*20)

for x in range(0, len(alunos)):
    print('{:<5}{:<10}{:>5.1f}'.format(x, alunos[x][0], alunos[x][1]))
print('='*20)