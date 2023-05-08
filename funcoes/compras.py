# Menu de Compras
def mostra_menu_compras():
    print("\n")
    print("===========================")
    print("||    MENU DE COMPRAS    ||")
    print("===========================")
    print("1. MENU DE FORNECEDORES")
    print("2. MENU DE SUPRIMENTOS") # aqui mostra os suprimentos mas tem q criar uma nova função p comprar eles, informar quantidade no ato de compra
    print("3. VER TODAS AS COMPRAS") # nao fiz essa parte, tem q criar uma lista que adicione as compras dessa linha de cima
    print("0. VOLTAR")

# Mostra na tela todas as compras
def ver_compras(compras):
    if len(compras) == 0:
        print("\n\n>>NENHUMA COMPRA REALIZADA.<<")
    else:
        print('\n')
        print("================================")
        print("||    Histórico de compras    ||")
        print("================================")
        for compra in compras:
            valorTotalCompra = 0
            print('')
            print(f"DATA     : {compra['data']}")
            print(f"DESCRICAO: {compra['descricao']}")
            print("ITENS:")
            for item in compra['itens']:
                valorTotalItem = item['valor'] * float(item['quantidade'])
                valorTotalCompra += valorTotalItem
                print(f"{item['quantidade']} * {item['suprimento']} =", end= " ")
                print('R$ %.2f' % valorTotalItem)
            print('')
            print('VALOR TOTAL DA COMPRA: R$ %.2f' % valorTotalCompra)
            print('-----------------------------------')
            