contagem = []

expressao = str(input('Digite a expressão: '))

for simb in expressao:
    if simb == '(':
        contagem.append('(')
    elif simb == ')':
        if len(contagem) > 0:
            contagem.pop()
        else:
            contagem.append(')')
            break

if len(contagem) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')