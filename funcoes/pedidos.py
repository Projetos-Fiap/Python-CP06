import os
clear = lambda: os.system('cls')

# Mostra na tela o menu que pergunta ao usuário se ele quer continuar comprando
def mostrar_menu_continuar_comprando():
    print('================================')
    print('||    CONTINUAR COMPRANDO?    ||')
    print('================================')
    print('1. SIM')
    print('2. FINALIZAR COMPRA')
    print('0. ESVAZIAR CARRINHO')


def mostra_menu_pedidos(pedidosDb):
    print('\n')
    print('============================')
    print('||      MENU PEDIDOS      ||')
    print('============================')
    print('1. FAZER PEDIDO')
    print('2. LISTAR PEDIDOS')
    print('0. VOLTAR')

def mostrar_opcoes_pedidos(pedidos):
        for i, pedido in enumerate(pedidos, start=1):
            print(f"{i}. {pedido['pedido']} ", end='')
            print('R$ %.2f' % pedido['valor'], end='')
            print(f", FORNECEDOR: {pedido['CNPJ_FORNECEDOR']}")