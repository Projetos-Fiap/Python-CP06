import os
clear = lambda: os.system('cls')

# Cadastrar novo suprimento
def cadastrar_suprimento(suprimentos, estoque):
    print('\n')
    print('============================')
    print('||  CADASTRAR SUPRIMENTO  ||')
    print('============================')
    suprimento = input('DIGITE O NOME DO SUPRIMENTO: ')
    valor = float(input('DIGITE O VALOR DO SUPRIMENTO: '))
    if( valor <= 0):
        print("VALOR INVÁLIDO! TENTE NOVAMENTE")
    else:
        cnpjFornecedor = input('DIGITE O CNPJ DO FORNECEDOR: ')
        novo_suprimento = {"suprimento": suprimento, "valor": valor, "CNPJ_FORNECEDOR": cnpjFornecedor}
        novo_item_estoque = {"suprimento": suprimento, "valor": valor, "CNPJ_FORNECEDOR": cnpjFornecedor, "quantidade": 0}
        suprimentos.append(novo_suprimento)
        estoque.append(novo_item_estoque)
        clear()
        print('SUPRIMENTO CADASTRADO COM SUCESSO!')

# Mostra na tela menu para comprar suprimentos
def mostra_menu_comprar_suprimentos(suprimentos):
    print('\n')
    print('============================')
    print('||    MENU SUPRIMENTOS    ||')
    print('============================')
    mostrar_suprimentos(suprimentos)
    print('\n===========OPÇÕES============')
    print('1. COMPRAR SUPRIMENTO')
    print('2. CADASTRAR NOVO SUPRIMENTO')
    print('0. VOLTAR')

# Mostra na tela todos os suprimentos
def mostrar_suprimentos(suprimentos):
        for i, suprimento in enumerate(suprimentos, start=1):
            print(f"{i}. {suprimento['suprimento']} ", end='')
            print('R$ %.2f' % suprimento['valor'], end='')
            print(f", FORNECEDOR: {suprimento['CNPJ_FORNECEDOR']}")

# Mostra na tela a lista de todos os suprimentos no carrinho
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
            print(f"{item['quantidade']} * {item['suprimento']['suprimento']} =", end = " ")
            print('R$ %.2f' % valorTotalItem)
        print(f'VALOR TOTAL CARRINHO:', end = " ")
        print('R$ %.2f' % valorTotalCarrinho)
        print('==========================')
        print()

# Mostra na tela o menu que pergunta ao usuário se ele quer continuar comprando
def mostrar_menu_continuar_comprando():
    print('================================')
    print('||    CONTINUAR COMPRANDO?    ||')
    print('================================')
    print('1. SIM')
    print('2. FINALIZAR COMPRA')
    print('0. ESVAZIAR CARRINHO')

# Fluxo de comprar suprimento
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
        qtdSuprimento = int(input('QUANTAS UNIDADES DESSE SUPRIMENTO DESEJA ADICIONAR AO CARRINHO? '))
        print('\n\n')
        if( qtdSuprimento <= 0):
            print("QUANTIDADE INVÁLIDA! TENTE NOVAMENTE")
        else:
            itemCarrinho = {
                "suprimento": suprimentos[indiceEstoque-1],
                "quantidade": qtdSuprimento,
                "indiceEstoque": indiceEstoque-1
            }
            carrinho.append(itemCarrinho)
            clear()
            mostrar_carrinho(carrinho)
            mostrar_menu_continuar_comprando()
            continuar = input('DIGITE A OPÇÃO DESEJADA: ')

            match continuar:
                case "1":
                    clear()
                    continue
                case "2":
                    descricao = input("ADICIONE UMA DESCRIÇÃO À SUA COMPRA: ")
                    adiciona_carrinho_ao_estoque(carrinho, estoque)
                    registra_compra(carrinho, compras, estoque, descricao)
                    clear()
                    print("COMPRA REALIZADA COM SUCESSO!")
                    print("ITEMS ADICIONADOS AO ESTOQUE!")
                    print("NOVO REGISTRO DE ENTRADA DE ESTOQUE CRIADO!")
                    break
                case "0":
                    clear()
                    carrinho = []
                    print('CARRINHO ESVAZIADO!')
                    continue
                case _: 
                    print("\n\n\nOPÇÃO INVÁLIDA!, TENTE NOVAMENTE:\n")
                    continue

# Adiciona ao estoque todos os itens que estavam no carrinho
def adiciona_carrinho_ao_estoque(carrinho, estoque):
    for item in carrinho:
        estoque[item['indiceEstoque']]['quantidade'] += int(item['quantidade'])

# Adiciona um registro de compra
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

# Converte um objeto do tipo datetime para string no formato usado para registrar a data da saída
def converte_data_em_string(data):
    return f"{data.hour}:{data.minute} - {data.day}/{data.month}/{data.year}"
    