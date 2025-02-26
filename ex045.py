from random import choice

posicoes = ['pedra','papel','tesoura']
computador = choice(posicoes)

usuario = int(input("""
    Selecione a sua jogada
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura
                    
    Opção Selecionada: """)) - 1

usuario = posicoes[usuario]

print('Computador escolheu {}'.format(computador))
print('Usuário escolheu {}'.format(usuario))


if computador == 'pedra':
    if usuario == 'tesoura':
        print('Vitŕoia do computador')
    elif usuario == 'papel':
        print('Vitória do jogador')
    elif usuario == 'pedra':
        print('Empate entre os jogadores')

elif computador == 'papel':
    if usuario == 'pedra':
        print('Vitória do computador')
    elif usuario == 'tesoura':
        print('Vitória do jogador')
    elif usuario == 'papel':
        print('Empate entre os jogadores')

elif computador == 'tesoura':
    if usuario == 'papel':
        print('Vitória do computador')
    elif usuario == 'pedra':
        print('Vitória do jogador')
    elif usuario == 'tesoura':
        print('Empate entre os jogadores')

