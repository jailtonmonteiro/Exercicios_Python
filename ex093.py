jogador = {}
gols = []

jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
jogador['jogos'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for i in range(0, jogador['jogos']):
    gols.append(int(input(f'Quantos gols no {i+1}° jogo: ')))

jogador['gols'] = gols
jogador['total'] = sum(gols)

print('=-='*15)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=-='*15)
print(f'Jogador {jogador["nome"]} jogou {jogador["jogos"]} partidas.')
for p, g in enumerate(jogador['gols']):
    print(f'=> Na partida {p}, fez {g} gols')

print(f'Somando um total de {jogador["total"]} gols')