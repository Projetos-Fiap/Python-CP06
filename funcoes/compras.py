def string_menu_compras():
    string = "\n"
    string += "===========================\n"
    string += "||    MENU DE COMPRAS    ||\n"
    string += "===========================\n"
    string += "1. MENU DE FORNECEDORES\n"
    string += "2. MENU DE COMPRAS\n"
    string += "3. VER TODAS AS COMPRAS\n"
    string += "0. VOLTAR\n"
    return string

def string_ver_compras(compras):
    string = ""
    if len(compras) == 0:
        string += "\n\n>>NENHUMA COMPRA REALIZADA.<<"
    else:
        string += '\n'
        string += "================================\n"
        string += "||    Histórico de compras    ||\n"
        string += "================================\n"
        for compra in compras:
            valorTotalCompra = 0
            string += '\n'
            string += f"DATA     : {compra['data']}\n"
            string += f"DESCRICAO: {compra['descricao']}\n"
            string += "ITENS:\n"
            for item in compra['itens']:
                valorTotalItem = item['valor'] * float(item['quantidade'])
                valorTotalCompra += valorTotalItem
                string += f"{item['quantidade']} * {item['suprimento']} = "
                string += 'R$ %.2f\n' % valorTotalItem
            string += '\n'
            string += 'VALOR TOTAL DA COMPRA: R$ %.2f\n' % valorTotalCompra
            string += '-----------------------------------\n'
    return string

# Menu de Compras
def mostra_menu_compras():
    # print("\n")
    # print("===========================")
    # print("||    MENU DE COMPRAS    ||")
    # print("===========================")
    # print("1. MENU DE FORNECEDORES")
    # print("2. MENU DE COMPRAS") # aqui mostra os suprimentos mas tem q criar uma nova função p comprar eles, informar quantidade no ato de compra
    # print("3. VER TODAS AS COMPRAS") # nao fiz essa parte, tem q criar uma lista que adicione as compras dessa linha de cima
    # print("0. VOLTAR")
    print(string_menu_compras())


# Mostra na tela todas as compras
def ver_compras(compras):
    # if len(compras) == 0:
    #     print("\n\n>>NENHUMA COMPRA REALIZADA.<<")
    # else:
    #     print('\n')
    #     print("================================")
    #     print("||    Histórico de compras    ||")
    #     print("================================")
    #     for compra in compras:
    #         valorTotalCompra = 0
    #         print('')
    #         print(f"DATA     : {compra['data']}")
    #         print(f"DESCRICAO: {compra['descricao']}")
    #         print("ITENS:")
    #         for item in compra['itens']:
    #             valorTotalItem = item['valor'] * float(item['quantidade'])
    #             valorTotalCompra += valorTotalItem
    #             print(f"{item['quantidade']} * {item['suprimento']} =", end= " ")
    #             print('R$ %.2f' % valorTotalItem)
    #         print('')
    #         print('VALOR TOTAL DA COMPRA: R$ %.2f' % valorTotalCompra)
    #         print('-----------------------------------')
    print(string_ver_compras(compras))    