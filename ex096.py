def area(largura, comprimento):
    areaTerreno = largura * comprimento
    print(f'\nA área do terreno é {areaTerreno:.2f} m²\n')


print('\nAREA DO TERRENO\n')
largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))
area(largura, comprimento)