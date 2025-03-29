def jogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


n = str(input('Digite um nome: ')).strip()
g = str(input('Digite os gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    jogador(gols=g)
else:
    jogador(n, g)