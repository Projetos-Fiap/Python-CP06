import funcoes.compras as compras
import funcoes.entrada as entrada
import funcoes.estoque as estoque
import funcoes.fornecedor as fornecedor
import funcoes.saida as saida
import funcoes.suprimento as suprimento

# Tabela de compras
comprasDB = [
    {
        "itens": [
            {"suprimento": "ROLHAS", "valor": 3.0, "CNPJ_FORNECEDOR": "60.718.835/0001-03", "quantidade": 2},
            {"suprimento": "GARRAFAS", "valor": 5.0, "CNPJ_FORNECEDOR": "60.718.835/0001-03", "quantidade": 2},
            {"suprimento": "CAIXAS", "valor": 4.0, "CNPJ_FORNECEDOR": "49.548.348/0001-07", "quantidade": 1},
            {"suprimento": "RÓTULOS", "valor": 2.0, "CNPJ_FORNECEDOR": "49.548.348/0001-07", "quantidade": 1}
        ],
        "data": "02:43 - 6/5/2023",
        "descricao": "Compra inicial"
    }  
]
# Tabela de saídas
saidasDB = [
    {
        "itens:": [
            {"suprimento": "ROLHAS", "quantidade": 1},
            {"suprimento": "GARRAFAS", "quantidade": 1},
        ],
        "data": "02:48 - 06/05/2023",
        "descricao": "Saída inicial"
    }
]
# Tabela de estoque
estoqueDB = [
    {"suprimento": "ROLHAS", "valor": 3.0, "CNPJ_FORNECEDOR": "60.718.835/0001-03", "quantidade": 1},
    {"suprimento": "GARRAFAS", "valor": 5.0, "CNPJ_FORNECEDOR": "60.718.835/0001-03", "quantidade": 1},
    {"suprimento": "CAIXAS", "valor": 4.0, "CNPJ_FORNECEDOR": "49.548.348/0001-07", "quantidade": 1},
    {"suprimento": "RÓTULOS", "valor": 2.0, "CNPJ_FORNECEDOR": "49.548.348/0001-07", "quantidade": 1}
]
# Tabela de suprimentos
suprimentosDB = [
    {"suprimento": "ROLHAS", "valor": 3.0, "cnpj_fornecedor": "60.718.835/0001-03"},
    {"suprimento": "GARRAFAS", "valor": 5.0, "cnpj_fornecedor": "60.718.835/0001-03"},
    {"suprimento": "CAIXAS", "valor": 4.0, "cnpj_fornecedor": "49.548.348/0001-07"},
    {"suprimento": "RÓTULOS", "valor": 2.0, "cnpj_fornecedor": "49.548.348/0001-07"}
]     
# Tabela de fornecedores
fornecedoresDB = [
    {"fornecedor": "FULANO", "cnpj": "60.718.835/0001-03"},
    {"fornecedor": "CICLANO", "cnpj": "49.548.348/0001-07"}
]

# Menu Principal
def mostra_menu_principal():
    print("\n")
    print("==========================")
    print("||    MENU PRINCIPAL    ||")
    print("==========================")
    print("1. COMPRAS")
    print("2. ESTOQUE")

########### DEFINIÇÃO DO PROGRAMA ###############

while True:
    mostra_menu_principal()
    opcaoMenuPrincipal = input("DIGITE A OPÇÃO DESEJADA: ") 
    match opcaoMenuPrincipal:
        case "1":
            while True: 
                compras.mostra_menu_compras()
                opcaoCompra = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoCompra:
                    case "1":
                        while True:
                            fornecedor.mostra_listar_fornecedores(fornecedoresDB)
                            opcaoFornecedor = input('DIGITE A OPÇÃO DESEJADA: ')
                            match opcaoFornecedor:
                                case "9":
                                    fornecedor.cadastrar_fornecedor(fornecedoresDB)
                                    continue
                                case "0":
                                    break
                                case _:
                                    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                                    continue
                    case "2":
                        while True:
                            suprimento.mostra_menu_comprar_suprimentos(suprimentosDB)
                            opcaoSuprimento = input('DIGITE A OPÇÃO DESEJADA: ')
                            match opcaoSuprimento:
                                case "1":
                                    suprimento.comprar_suprimento(suprimentosDB, estoqueDB, comprasDB)
                                    continue
                                case "2":
                                    suprimento.cadastrar_suprimento(suprimentosDB, estoqueDB)
                                    continue
                                case "0":
                                    break
                                case _:
                                    break
                    case "3":
                        compras.ver_compras(comprasDB)
                        continue
                    case "0":
                        break
                    case _ :
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
            continue
        case "2":
            while True:
                estoque.mostra_menu_estoque()
                opcaoEstoque = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoEstoque:
                    case "1":
                        entrada.listar_entradas(comprasDB)
                        continue
                    case "2":
                        saida.listar_saidas(saidasDB)
                        continue
                    case "3":
                        estoque.ver_estoque_total(estoqueDB)
                        continue
                    case "0":
                        break
                    case _:
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
            continue
        case _:
            break


        

