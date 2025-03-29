def exibir(formatado):
    '''
    => Formata o valor como monetário BRL
    :param formatado: Valor bruto que recebe
    :return: Valor retornado com as devidas formatações
    '''
    return f'R$ {formatado:.2f}'


def aumentar(valor, show=False):
    '''
    => Aumentar o valor passado em 10
    :param valor: valor inserido
    :return: retornar o valor atualizado
    '''
    valor += (valor*0.10)
    return valor if show == False else exibir(valor)


def diminuir(valor, show=False):
    '''
    => Diminuir o valor passado em 5
    :param valor: valor inserido
    :return: retornar o valor atualizado
    '''
    valor -= (valor*0.05)
    return valor if show == False else exibir(valor)


def dobro(valor, show=False):
    '''
    => Dobra o valor passado
    :param valor: valor inserido
    :return: retornar o valor atualizado
    '''
    valor *= 2
    return valor if show == False else exibir(valor)


def metade(valor, show=False):
    '''
    => Divide o valor passado em 2
    :param valor: valor inserido
    :return: retornar o valor atualizado
    '''
    valor = valor/2
    return valor if show == False else exibir(valor)