def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'Erro: {entrada} inválida')
        else:
            valido = True
            return float(entrada)