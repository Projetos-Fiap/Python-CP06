import os
# Defininfo função que limpa a tela do terminal
limpa_a_tela = lambda: os.system('cls')

# Mostra na tela todas as saídas
def listar_saidas(saidas):
    if len(saidas) == 0:
        print('\n\n >>NENHUMA SAÍDA REGISTRADA<<')
    else:
        print('\n')
        print("======================================")
        print("||        REGISTRO DE SAíDAS        ||")
        print("======================================")
        for saida in saidas:
            print()
            print(f"Data: {saida['data']}\n")
            print(f"Descrição: {saida['descricao']}")
            for item in saida['itens']:
                valorItem = item['valor'] * float(item['quantidade'])
                print(f"{item['quantidade']} * {item['suprimento']} = ", end = "")
                print("R$ %.2f" % valorItem)
            print("------------------------------------")

# Mostra na tela o menu de saídas  
def mostra_menu_saidas():
    print('\n')
    print('============================')
    print('||     MENU DE SAÍDAS     ||')
    print('============================')
    print('1. LISTAR SAIDAS')
    print('2. CADASTRAR SAIDAS')
    print('0. VOLTAR') 

# Fluxo de cadastrar uma saída
def cadastrar_saida(saidas, estoque):
    carrinhoDeSaida = []
    while True:
        ver_estoque_total(estoque)
        mostrar_carrinho_saidas(carrinhoDeSaida)
        indiceEstoque = int(input('QUAL SUPRIMENTO DESEJA CADASTRAR NA SAIDA? '))
        qtdSuprimento = int(input('QUANTAS UNIDADES DESSE SUPRIMENTO DESEJA CADASTRAR NA SAIDA? '))
        if(qtdSuprimento <= 0 or qtdSuprimento > estoque[indiceEstoque-1]['quantidade']):
            print("QUANTIDADE INVÁLIDA! TENTE NOVAMENTE")
        else:
            print('\n\n')
            itemCarrinho = {
                "suprimento": estoque[indiceEstoque-1],
                "quantidade": qtdSuprimento,
                "indiceEstoque": indiceEstoque-1
            }
            carrinhoDeSaida.append(itemCarrinho)
            limpa_a_tela()
            mostrar_carrinho_saidas(carrinhoDeSaida)
            mostrar_menu_continuar_retirando()
            continuar = input('DIGITE A OPÇÃO DESEJADA: ')

            match continuar:
                case "1":
                    limpa_a_tela()
                    continue
                case "2":
                    descricao = input("ADICIONE UMA DESCRIÇÃO À SAÍDA: ")
                    deduz_carrinho_do_estoque(estoque, carrinhoDeSaida)
                    registra_saida(carrinhoDeSaida, saidas, estoque, descricao)
                    limpa_a_tela()
                    print("SAÍDA CADASTRADA COM SUCESSO!")
                    print("ITENS DEDUZIDOS DO ESTOQUE!")
                    break
                case "0":
                    limpa_a_tela()
                    carrinhoDeSaida = []
                    print('CARRINHO ESVAZIADO!')
                    continue
                case _: 
                    print("\n\n\nOPÇÃO INVÁLIDA!, TENTE NOVAMENTE:\n")
                    continue


# Adiciona uma saída ao registro de saidas
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

# Converte um objeto do tipo datetime para string no formato usado para registrar a data da saída
def converte_data_em_string(data):
    return f"{data.hour}:{data.minute} - {data.day}/{data.month}/{data.year}"

# Deduz do estoque todos os itens que estavam no carrinho de saída
def deduz_carrinho_do_estoque(estoque, carrinho):
    for item in carrinho:
        estoque[item['indiceEstoque']]['quantidade'] -= item['quantidade']

# Mostra na tela o estoque filtrando apenas os itens em que quantidade != 0
def ver_estoque_total(estoque):
    print('\n')
    print("================================")
    print("||          ESTOQUE           ||")
    print("================================")
    valorTotalEstoque = 0
    for i, item in enumerate(estoque, start=1):
        if(item['quantidade'] == 0):
            continue
        valorItem = item['valor'] * float(item['quantidade'])
        valorTotalEstoque += valorItem
        print(f"{i}. {item['suprimento']}: ")
        print(f"QUANTIDADE EM ESTOQUE: {item['quantidade']} CNPJ DO FORNECEDOR: {item['CNPJ_FORNECEDOR']}  VALOR ACUMULADO:", end=' ')
        print('R$ %.2f\n' % valorItem)
        
    print('')
    print('VALOR TOTAL ACUMULDO NO ESTOQUE: R$ %.2f' % valorTotalEstoque)
    print('-----------------------------------')

# Mostra na tela todos os itens do carrinho da saídas
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
            print(f"{item['quantidade']} * {item['suprimento']['suprimento']} =", end = " ")
            print('R$ %.2f' % valorTotalItem)
        print(f'VALOR TOTAL CARRINHO:', end = " ")
        print('R$ %.2f' % valorTotalCarrinho)

# Mostra na tela o menu que pergunta se o usuário quer adicionar mais items ao carrinho de saídas
def mostrar_menu_continuar_retirando():
    print('=========================================')
    print('||    CONTINUAR CADASTRANDO SAÍDAS?    ||')
    print('=========================================')
    print('1. SIM')
    print('2. FINALIZAR REGISTRO DE SAÍDA')
    print('0. ESVAZIAR CARRINHO')