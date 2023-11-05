def string_menu_estoque():
    string = "\n"
    string += "===========================\n"
    string += "||    MENU DE ESTOQUE    ||\n"
    string += "===========================\n"
    string += "1. MOSTRAR ENTRADAS\n"
    string += "2. MENU SAÍDAS\n"
    string += "3. MOSTRAR ESTOQUE\n"
    string += "0. VOLTAR\n"
    return string

def string_mostra_estoque(estoque):
    string = ""
    string += "\n"
    string += "================================\n"
    string += "||          ESTOQUE           ||\n"
    string += "================================\n"
    valorTotalEstoque = 0
    for item in estoque:
        valorItem = item['valor'] * float(item['quantidade'])
        valorTotalEstoque += valorItem
        if(item['quantidade'] == 0):
            string += f"(EM FALTA) {item['suprimento']}: \n"
            string += f"QUANTIDADE EM ESTOQUE: {item['quantidade']} CNPJ DO FORNECEDOR: {item['CNPJ_FORNECEDOR']}  VALOR ACUMULADO: "
            string += 'R$ %.2f\n' % valorItem 
        else: 
            string += f"{item['suprimento']}: \n"
            string += f"QUANTIDADE EM ESTOQUE: {item['quantidade']} CNPJ DO FORNECEDOR: {item['CNPJ_FORNECEDOR']}  VALOR ACUMULADO: "
            string += 'R$ %.2f\n' % valorItem
        
    string += '\n'
    string += 'VALOR TOTAL ACUMULADO NO ESTOQUE: R$ %.2f\n' % valorTotalEstoque
    string += '-----------------------------------\n'
    return string

# Mostra na tela o menu de estoque
def mostra_menu_estoque():
    # print('\n')
    # print('===========================')
    # print('||    MENU DE ESTOQUE    ||')
    # print('===========================')
    # print('1. MOSTRAR ENTRADAS')  
    # print('2. MENU SAÍDAS')
    # print('3. MOSTRAR ESTOQUE')
    # print('0. VOLTAR') 
    print(string_menu_estoque())

# Mostra na tela o estoque
def mostra_estoque(estoque):
    # print('\n')
    # print("================================")
    # print("||          ESTOQUE           ||")
    # print("================================")
    # valorTotalEstoque = 0
    # for item in estoque:
    #     valorItem = item['valor'] * float(item['quantidade'])
    #     valorTotalEstoque += valorItem
    #     if(item['quantidade'] == 0):
    #         print(f"(EM FALTA) {item['suprimento']}: ")
    #         print(f"QUANTIDADE EM ESTOQUE: {item['quantidade']} CNPJ DO FORNECEDOR: {item['CNPJ_FORNECEDOR']}  VALOR ACUMULADO:", end=' ')
    #         print('R$ %.2f\n' % valorItem) 
    #     else: 
    #         print(f"{item['suprimento']}: ")
    #         print(f"QUANTIDADE EM ESTOQUE: {item['quantidade']} CNPJ DO FORNECEDOR: {item['CNPJ_FORNECEDOR']}  VALOR ACUMULADO:", end=' ')
    #         print('R$ %.2f\n' % valorItem)
        
    # print('')
    # print('VALOR TOTAL ACUMULADO NO ESTOQUE: R$ %.2f' % valorTotalEstoque)
    # print('-----------------------------------')
    print(string_mostra_estoque(estoque))





