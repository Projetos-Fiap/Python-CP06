# Menu de Estoque
def mostra_menu_estoque():
    print('\n')
    print('===========================')
    print('||    MENU DE ESTOQUE    ||')
    print('===========================')
    print('1. ENTRADAS')  ## fazer (tem um esqueleto ja)
    print('2. SAÍDAS') ## fazer (tem um esqueleto ja) 
    print('3. VER ESTOQUE') ## fazer (tem um esqueleto ja)
    print('0. VOLTAR') 

# Menu Estoque -> Ver Estoque
def ver_estoque_total(estoque):
    print('\n')
    print("================================")
    print("||          ESTOQUE           ||")
    print("================================")
    valorTotalEstoque = 0
    for item in estoque:
        valorItem = item['valor'] * float(item['quantidade'])
        valorTotalEstoque += valorItem
        print(f"{item['suprimento']}: ")
        print(f"QUANTIDADE EM ESTOQUE: {item['quantidade']} CNPJ DO FORNECEDOR: {item['CNPJ_FORNECEDOR']}  VALOR ACUMULADO:", end=' ')
        print('R$ %.2f\n' % valorItem)
        
    print('')
    print('VALOR TOTAL ACUMULDO NO ESTOQUE: R$ %.2f' % valorTotalEstoque)
    print('-----------------------------------')


# {"suprimento": "RÓTULOS", "valor": 2.0, "CNPJ_FORNECEDOR": "49.548.348/0001-07", "quantidade": 1}

