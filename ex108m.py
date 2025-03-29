def exibir(formatado):
    return f'R$ {formatado:.2f}'


def aumentar(valor):
    '''
    => Aumentar o valor passado em 10
    :param valor: valor inserido
    :return: retornar o valor atualizado
    '''
    valor += (valor*0.10)
    return exibir(valor)


def diminuir(valor):
    '''
    => Diminuir o valor passado em 5
    :param valor: valor inserido
    :return: retornar o valor atualizado
    '''
    valor -= (valor*0.05)
    return exibir(valor)


def dobro(valor):
    '''
    => Dobra o valor passado
    :param valor: valor inserido
    :return: retornar o valor atualizado
    '''
    valor *= 2
    return exibir(valor)


def metade(valor):
    '''
    => Divide o valor passado em 2
    :param valor: valor inserido
    :return: retornar o valor atualizado
    '''
    valor = valor/2
    return exibir(valor)