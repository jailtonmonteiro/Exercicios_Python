valores = []

for x in range(0,5):
    val = int(input('Digite um valor: '))
    if x == 0 or val > valores[-1]:
        valores.append(val)
    else:
        pos = 0
        while pos < len(valores):
            if val <= valores[pos]:
                valores.insert(pos, val)
                break
            pos += 1
print(valores)