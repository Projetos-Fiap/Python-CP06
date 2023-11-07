import os
clear = lambda: os.system('cls')
from datetime import datetime, timedelta
import funcoes.crudBanco as crudBanco



# Mostra na tela o menu que pergunta ao usuário se ele quer continuar comprando
def mostrar_menu_continuar_comprando():
    print('================================')
    print('||    CONTINUAR COMPRANDO?    ||')
    print('================================')
    print('1. SIM')
    print('2. FINALIZAR COMPRA')
    print('0. ESVAZIAR CARRINHO')

def mostra_menu_pedidos():
    print('\n')
    print('============================')
    print('||      MENU PEDIDOS      ||')
    print('============================')
    print('1. FAZER PEDIDO')
    print('2. LISTAR PEDIDOS')
    print('0. VOLTAR')

def mostra_opcoes_pedidos(pedidos):
        for i, pedido in enumerate(pedidos, start=1):
            print(f"{i}. {pedido['opcaoPedido']} ", end='')
            print('R$ %.2f' % pedido['valor'], end='')
            print('')

def mostra_menu_realizar_pedido(pedidos):
        print('\n')
        print('============================')
        print('||      MENU PEDIDOS      ||')
        print('============================')
        mostra_opcoes_pedidos(pedidos)

def mostra_carrinho(carrinho, pedidos):
    if carrinho == []:
        print('>>> Carrinho Vazio <<<')
    else:
        print('==========================')
        print('||        Carrinho      ||')
        print('==========================')
        custoCarrinho = calcula_custo_carrinho(carrinho, pedidos)
        custoFrete =  calcula_frete_carrinho(carrinho, pedidos)
        custoTotal = custoCarrinho + custoFrete
        for item in carrinho:
            print(f"{item['quantidade']} x {pedidos[item['idOpcaoPedido']]['opcaoPedido']}")
        print('CUSTO DO CARRINHO R$ %.2f' % custoCarrinho)
        print('CUSTO DO FRETE    R$ %.2f' % custoFrete)
        print('CUSTO TOTAL       R$ %.2f' % custoTotal)

        print('\n')

def conta_garrafas_carrinho(carrinho):
    qtdGarrafas = 0
    for item in carrinho:
        if item['idOpcaoPedido'] == 1:
            qtdGarrafas += item['quantidade']
            continue
        
        if item['idOpcaoPedido'] == 4:
            qtdGarrafas += item['quantidade'] * 6
            continue

        if item['idOpcaoPedido'] == 5:
            qtdGarrafas += item['quantidade'] * 12
            continue
    return qtdGarrafas
        
        
def calcula_frete_carrinho(carrinho, opcoesPedidos):
    custoCarrinho = calcula_custo_carrinho(carrinho, opcoesPedidos)
    qtdGarrafas = conta_garrafas_carrinho(carrinho)
    frete = 10.0
    frete += custoCarrinho * 0.1
    frete += qtdGarrafas*10.0
    return frete


def calcula_custo_carrinho(carrinho, opcoesPedidos):
    somaCarrinho = 0
    for item in carrinho:
        somaCarrinho += opcoesPedidos[item['idOpcaoPedido']]['valor'] * item['quantidade']

    return somaCarrinho

def calcula_data_entrega():
    return datetime.now() + timedelta(days=7)

def transforma_carrinho_em_carrinho_de_saidas(carrinho, estoque):
    qtdGarrafas = conta_garrafas_carrinho(carrinho)
    carrinhoSaida = []

    #Adiciona garrafas
    itemGarrafa = {
        "suprimento": estoque[1],
        "quantidade": qtdGarrafas,
        "indiceEstoque": 1
    }

    carrinhoSaida.append(itemGarrafa)

    #Adiciona suprimentos que nao são garrafas
    for item in carrinho:
        if item['idOpcaoPedido'] == 1 or item['idOpcaoPedido'] == 4 or item['idOpcaoPedido'] == 5:
            continue

        novoItem = {
                "suprimento": estoque[item['idOpcaoPedido']],
                "quantidade": item['quantidade'],
                "indiceEstoque": item['idOpcaoPedido']
            }
        carrinhoSaida.append(novoItem)

    return carrinhoSaida

def converte_data_em_string(data):
    return f"{data.hour}:{data.minute} - {data.day}/{data.month}/{data.year}"

def registra_pedido(carrinho, pedidos, estoque, descricao, frete, valorCarrinho):
    itens = []
    for item in carrinho:
        itens.append({
            "suprimento": item['suprimento']['suprimento'],
            "valor": estoque[item['indiceEstoque']]['valor'],
            "CNPJ_FORNECEDOR": estoque[item['indiceEstoque']]['CNPJ_FORNECEDOR'],
            "quantidade": item['quantidade'],
            }
        )
    pedido = {
        "itens": itens,
        "frete": frete,
        "valorTotal": valorCarrinho + frete,
        "dataPedido": converte_data_em_string(datetime.now()),
        "dataEntrega": converte_data_em_string(calcula_data_entrega()),
        "descricao": descricao
    }
    pedidos.append(pedido)
    crudBanco.sobrescreve_pedidos(pedidos)

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


def string_lista_pedidos(pedidos):
    string = ""
    if len(pedidos) == 0:
        string += "\n\n>>NENHUM PEDIDO REGISTRADO.<<"
    else:
        string += '\n'
        string += "======================================\n"
        string += "||        REGISTRO DE PEDIDOS        ||\n"
        string += "======================================\n"
        for pedido in pedidos:
            string += '\n'
            string += f"Data do pedido: {pedido['dataPedido']}\n"
            string += f"Data de entrega: {pedido['dataEntrega']}\n"
            string += "Frete: R$ %.2f\n" % pedido['frete']
            string += "Total pedido: R$ %.2f\n" % pedido['valorTotal']
            string += f"Descrição: {pedido['descricao']}\n"
            for item in pedido['itens']:
                valorItem = item['valor'] * float(item['quantidade'])
                string += f"{item['quantidade']} * {item['suprimento']} = "
                string += "R$ %.2f\n" % valorItem
            string += "------------------------------------\n"
    return string
# Mostra na tela todas as saídas
def listar_pedidos(pedidos):
    # if len(pedidos) == 0:
    #     print('\n\n >>NENHUM PEDIDO REGISTRADO<<')
    # else:
    #     print('\n')
    #     print("======================================")
    #     print("||        REGISTRO DE PEDIDOS        ||")
    #     print("======================================")
    #     for pedido in pedidos:
    #         print()
    #         print(f"Data do pedido: {pedido['dataPedido']}")
    #         print(f"Data de entrega: {pedido['dataEntrega']}\n")
    #         print("Frete: R$ %.2f" % pedido['frete'])
    #         print("Total pedido: R$ %.2f" % pedido['valorTotal'])
    #         print(f"Descrição: {pedido['descricao']}\n")
    #         for item in pedido['itens']:
    #             valorItem = item['valor'] * float(item['quantidade'])
    #             print(f"{item['quantidade']} * {item['suprimento']} = ", end = "")
    #             print("R$ %.2f" % valorItem)
    #         print("------------------------------------")
    print(string_lista_pedidos(pedidos))