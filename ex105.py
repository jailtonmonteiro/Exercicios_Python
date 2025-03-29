def notas(*nota, situacao=False):
    '''
    => Função para analisar notas e situação de alunos
    :param nota: Pode receber 1 ou mais notas com valores inteiros e flutuantes
    :param situacao: Booleano opcional, que vai indicar se o dicionário recebe ou não a situação da turma. BOA, REGULAR e RUIM
    :return: Retorna um dicionário com informações referente as notas passadas.
    '''

    turma = dict()
    turma["maior"] = max(nota)
    turma["menor"] = min(nota)
    turma["total"] = len(nota)
    turma["media"] = sum(nota)/len(nota)

    if situacao:
        if turma["media"] >= 7:
            turma["situacao"] = 'BOA'
        elif turma["media"] >= 5:
            turma["situacao"] = 'REGULAR'
        elif turma["media"] < 5:
            turma["situacao"] = 'RUIM'

    return turma

resp = notas(8, 5, 7, 8.7, 2, 3.1, 2.7, situacao=True)
print(resp)