valor = float(input('Digite o valor do produto: '))
opcao = int(input("""
Selecione a Forma de Pagamento:
                  
[1] - Dinheiro/Cheque
[2] - Cartão
                """))

if opcao == 1:
    print('Desconto adicionado!')
    print('Novo Valor R$ {:.2f}'.format(valor - (valor*0.10)))
elif opcao == 2:
    parcelas = int(input('Digite a quantidade de vezes: '))

    if parcelas == 1:
        print('Desconto adicionado!')
        print('Novo Valor R$ {:.2f}'.format(valor - (valor*0.05)))
    elif parcelas == 2:
        print('Pagmento em {} de R$ {:.2f}'.format(parcelas, (valor/parcelas)))
    elif parcelas >= 3:
        juros = valor + (valor * 0.20)
        print('Juros calculados, novo valor R$ {:.2f}'.format(juros))
        print('Pagmento em {} de R$ {:.2f}'.format(parcelas, (juros/parcelas)))