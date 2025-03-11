clubes = ('Palmeiras', 'Botafogo', 'Red Bull Bragantino', 'Flamengo', 'Grêmio', 'Atlético Mineiro', 'Fluminense', 'São Paulo', 'Athletico Paranaense', 'Internacional', 'Fortaleza', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Bahia', 'Vasco da Gama', 'Goiás', 'Coritiba', 'América Mineiro', 'Santos')

print('='*35)
print('\nBrasileiro 2023\n')
print('='*35)

for z5 in range (0, 5):
    print('{}° Lugar: {}'.format(z5+1, clubes[z5]))
print('#'*35)
for z4 in range(16, 20):
    print('{}° Lugar: {}'.format(z4+1, clubes[z4]))
print('#'*35)
ordem = sorted(clubes)
for o in range(len(clubes)):
    print('{}'.format(ordem[o]))
print('#'*35)
print('O Flamengo está na {}° colocação'.format(clubes.index('Flamengo')+1))