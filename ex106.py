def ajuda(comando):
    return help(comando)


def titulo(msg):
    tam = len(msg)+4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)


while True:
    titulo('SISTEMA DE AJUDA PYTHON')
    cmd = str(input('Digite a Função ou Biblioteca: '))
    if cmd == '':
        print('Digite algum valor.')
    elif cmd.upper() in 'FIM':
        break
    else:
        ajuda(cmd)
titulo('APLICAÇÃO FINALIZADA')