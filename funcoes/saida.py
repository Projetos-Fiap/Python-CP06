# Menu Estoque -> Saídas
def listar_saidas(saidas):
    if len(saidas) == 0:
        print('\n\n >>NENHUMA SAÍDA REGISTRADA<<')
    else:
        print("SAÍDAS REGISTRADAS:")
        for saida in saidas:
            print(f"Descrição: {saida['descricao']}")
            print(f"Quantidade: {saida['quantidade']}")
            print(f"Data: {saida['data']}\n")

def cadastrar_saida(saidas, estoque):
    carrinhoDeSaida = []
    while True:
        ver_estoque_total()
        mostrar_carrinho_saidas(carrinho)
        indiceEstoque = int(input('QUAL SUPRIMENTO DESEJA CADASTRAR NA SAIDA? '))
        qtdSuprimento = input('QUANTAS UNIDADES DESSE SUPRIMENTO DESEJA CADASTRAR NA SAIDA? ')
        print('\n\n')
        itemCarrinho = {
            "suprimento": estoque[indiceEstoque-1],
            "quantidade": qtdSuprimento,
            "indiceEstoque": indiceEstoque-1
        }
        carrinhoDeSaida.append(itemCarrinho)
        mostrar_carrinho_saidas(carrinhoDeSaida)
        mostrar_menu_continuar_retirando()
        continuar = input('DIGITE A OPÇÃO DESEJADA: ')

        match continuar:
            case "1":
                continue
            case "2":
                break
            case "0":
                carrinho = []
                print('CARRINHO ESVAZIADO!')
                continue
            case _: 
                print("\n\n\nOPÇÃO INVÁLIDA!, TENTE NOVAMENTE:\n")
                continue
    descricao = input("ADICIONE UMA DESCRIÇÃO À SUA COMPRA: ")
    deduz_carrinho_do_estoque(estoque, carrinhoDeSaida)
    registra_saida(carrinhoDeSaida, saidas, estoque, descricao)

def registra_saida(carrinho, saidas, estoque, descricao):
    from datetime import datetime
    itens = []
    for item in carrinho:
        itens.append({
            "suprimento": item['suprimento']['suprimento'],
            "valor": estoque[item['indiceEstoque']]['valor'],
            "CNPJ_FORNECEDOR": estoque[item['indiceEstoque']]['CNPJ_FORNECEDOR'],
            "quantidade": item['quantidade'],
            }
        )
    saida = {
        "itens": itens,
        "data": converte_data_em_string(datetime.now()),
        "descricao": descricao
    }
    saidas.append(saida)

def converte_data_em_string(data):
    return f"{data.hour}:{data.minute} - {data.day}/{data.month}/{data.year}"

def deduz_carrinho_do_estoque(estoque, carrinho):
    for item in carrinho:
        estoque[item['indiceEstoque']]['quantidade'] -= item['quantidade']


# Menu Estoque -> Ver Estoque
def ver_estoque_total(estoque):
    print('\n')
    print("================================")
    print("||          ESTOQUE           ||")
    print("================================")
    valorTotalEstoque = 0
    for i, item in enumerate(estoque, start=1):
        valorItem = item['valor'] * float(item['quantidade'])
        valorTotalEstoque += valorItem
        print(f"{i}. {item['suprimento']}: ")
        print(f"QUANTIDADE EM ESTOQUE: {item['quantidade']} CNPJ DO FORNECEDOR: {item['CNPJ_FORNECEDOR']}  VALOR ACUMULADO:", end=' ')
        print('R$ %.2f\n' % valorItem)
        
    print('')
    print('VALOR TOTAL ACUMULDO NO ESTOQUE: R$ %.2f' % valorTotalEstoque)
    print('-----------------------------------')


def mostrar_carrinho_saidas(carrinho):
    if carrinho == []:
        print('>>CARRINHO VAZIO!<<')
    else:
        print('==========================')
        print('||    CARRINHO ATUAL    ||')
        print('==========================')
        valorTotalCarrinho = 0
        for item in carrinho:
            valorTotalItem = item['suprimento']['valor']*float(item['quantidade'])
            valorTotalCarrinho += valorTotalItem
            print(f"{item['quantidade']}* {item['suprimento']['suprimento']} =", end = " ")
            print('R$ %.2f' % valorTotalItem)
        print(f'VALOR TOTAL CARRINHO:', end = " ")
        print('R$ %.2f' % valorTotalCarrinho)

def mostrar_menu_continuar_retirando():
    print('=========================================')
    print('||    CONTINUAR CADASTRANDO SAÍDAS?    ||')
    print('=========================================')
    print('1. SIM')
    print('2. FINALIZAR COMPRA')
    print('0. ESVAZIAR CARRINHO')