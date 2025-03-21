jogador = dict()
gols = list()
atletas = list()

while True:
    jogador["nome"] = str(input('Nome do jogador: ')).strip().capitalize()
    jogador["jogos"] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

    for i in range(0, jogador["jogos"]):
        gols.append(int(input(f'Quantos gols no {i+1}° jogo: ')))

    jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)
    gols.clear()

    atletas.append(jogador.copy())

    adicionar = str(input('Quer continuar S/N: '))
    if adicionar in 'nN':
        break

print('-='*30)
print('cod ',end=' ')
for j in jogador.keys():
    print(f'{j:<15}', end='')
print()
print('--'*30)

for k, v in enumerate(atletas):
    print(f'{k:>3}', end=' ')
    for a in v.values():
        print(f'{str(a):<15}', end='')
    print()

busca = 0
while True:
    busca = int(input('Selecione um jogador [999 para sair]: '))
    if busca == 999:
        print('Aplicação Finalizada')
        break
    if busca >= len(atletas):
        print('Código não encontrado')
    else:
        print(f'Histórico de jogador {atletas[busca]["nome"]}: ')
        for p, g in enumerate(atletas[busca]["gols"]):
            print(f'=> Na partida {p}, fez {g} gols')