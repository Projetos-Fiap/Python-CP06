
# Cadastrar novo produto (e adicionar à lista)
def cadastrar_suprimento(suprimentos, estoque):
    print('\n')
    print('============================')
    print('||  CADASTRAR SUPRIMENTO  ||')
    print('============================')
    suprimento = input('DIGITE O NOME DO SUPRIMENTO: ')
    valor = input('DIGITE O VALOR DO SUPRIMENTO: ')
    cnpjFornecedor = input('DIGITE O CNPJ DO FORNECEDOR: ')
    novo_suprimento = {"suprimento": suprimento, "valor": valor, "cnpj_fornecedor": cnpjFornecedor}
    novo_item_estoque = {"suprimento": suprimento, "valor": valor, "cnpj_fornecedor": cnpjFornecedor, "quantidade": 0}
    suprimentos.append(novo_suprimento)
    estoque.append(novo_item_estoque)
    print('\n')
    print('SUPRIMENTO CADASTRADO COM SUCESSO!')

def mostra_menu_comprar_suprimentos(suprimentos):
    print('\n')
    print('============================')
    print('||    MENU SUPRIMENTOS    ||')
    print('============================')
    mostrar_suprimentos(suprimentos)
    print('========================')
    print('1. COMPRAR SUPRIMENTO')
    print('2. CADASTRAR NOVO SUPRIMENTO')
    print('0. VOLTAR')

def mostrar_suprimentos(suprimentos):
        for i, suprimento in enumerate(suprimentos, start=1):
            print(f"{i}. {suprimento['suprimento']}, {suprimento['valor']}, FORNECEDOR: {suprimento['cnpj_fornecedor']}")

def mostrar_carrinho(carrinho):
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

def mostrar_menu_continuar_comprando():
    print('================================')
    print('||    CONTINUAR COMPRANDO?    ||')
    print('================================')
    print('1. SIM')
    print('2. FINALIZAR COMPRA')
    print('0. ESVAZIAR CARRINHO')

def comprar_suprimento(suprimentos, estoque, compras):
    carrinho = []
    while True:
        print('\n')
        
        print('================================')
        print('||    LISTA DE SUPRIMENTOS    ||')
        print('================================')
        mostrar_suprimentos(suprimentos)
        print('===============================')
        mostrar_carrinho(carrinho)
        indiceEstoque = int(input('QUAL SUPRIMENTO DESEJA ADICIONAR AO CARRINHO? '))
        qtdSuprimento = input('QUANTAS UNIDADES DESSE SUPRIMENTO DESEJA ADICIONAR AO CARRINHO? ')
        print('\n\n')
        itemCarrinho = {
            "suprimento": suprimentos[indiceEstoque-1],
            "quantidade": qtdSuprimento,
            "indiceEstoque": indiceEstoque-1
        }
        carrinho.append(itemCarrinho)
        mostrar_carrinho(carrinho)
        mostrar_menu_continuar_comprando()
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
    adiciona_carrinho_ao_estoque(carrinho, estoque)
    registra_compra(carrinho, compras, estoque, descricao)

def adiciona_carrinho_ao_estoque(carrinho, estoque):
    for item in carrinho:
        estoque[item['indiceEstoque']]['quantidade'] += int(item['quantidade'])

def registra_compra(carrinho, compras, estoque, descricao):
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
    compra = {
        "itens": itens,
        "data": converte_data_em_string(datetime.now()),
        "descricao": descricao
    }
    compras.append(compra)

def converte_data_em_string(data):
    return f"{data.hour}:{data.minute} - {data.day}/{data.month}/{data.year}"
    