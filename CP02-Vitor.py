# oi vitor tudo bom
# vou colar até onde eu fiz aqui
# e comentar algumas coisas q vc precisa fazer
# obrigado boa sorte deus abençoe

estoque = [
    {"suprimento": "ROLHAS", "valor": 3.0, "CNPJ_FORNECEDOR": "60.718.835/0001-03", "quantidade": 1},
    {"suprimento": "GARRAFAS", "valor": 5.0, "CNPJ_FORNECEDOR": "60.718.835/0001-03", "quantidade": 1},
    {"suprimento": "CAIXAS", "valor": 4.0, "CNPJ_FORNECEDOR": "49.548.348/0001-07", "quantidade": 1},
    {"suprimento": "RÓTULOS", "valor": 2.0, "CNPJ_FORNECEDOR": "49.548.348/0001-07", "quantidade": 1}
]

# Lista de suprimentos
suprimentos = [
    {"suprimento": "ROLHAS", "valor": 3.0, "cnpj_fornecedor": "60.718.835/0001-03"},
    {"suprimento": "GARRAFAS", "valor": 5.0, "cnpj_fornecedor": "60.718.835/0001-03"},
    {"suprimento": "CAIXAS", "valor": 4.0, "cnpj_fornecedor": "49.548.348/0001-07"},
    {"suprimento": "RÓTULOS", "valor": 2.0, "cnpj_fornecedor": "49.548.348/0001-07"}
]    
    
# Lista de fornecedores
fornecedores = [
    {"fornecedor": "FULANO", "cnpj": "60.718.835/0001-03"},
    {"fornecedor": "CICLANO", "cnpj": "49.548.348/0001-07"}
]
def mostra_menu_comprar_suprimentos():
    print("\n")
    print("============================")
    print("||    MENU SUPRIMENTOS    ||")
    print("============================")
    for i, suprimento in enumerate(suprimentos, start=1):
        print(f"{i}. FORNECEDOR {suprimento['suprimento']}, CNPJ {suprimento['valor']}, FORNECEDOR {suprimento['cnpj_fornecedor']}")
    print("========================")
    print("1. COMPRAR SUPRIMENTO")
    print("2. CADASTRAR NOVO SUPRIMENTO")
    print("0. VOLTAR")


# Menu Principal
def mostra_menu_principal():
    print("\n")
    print("==========================")
    print("||    MENU PRINCIPAL    ||")
    print("==========================")
    print("1. COMPRAS")
    print("2. ESTOQUE")

# Menu de Compras
def mostra_menu_compras():
    print("\n")
    print("===========================")
    print("||    MENU DE COMPRAS    ||")
    print("===========================")
    print("1. LISTA DE FORNECEDORES")
    print("2. SUPRIMENTOS") # aqui mostra os suprimentos mas tem q criar uma nova função p comprar eles, informar quantidade no ato de compra
    print("3. VER TODAS AS COMPRAS") # nao fiz essa parte, tem q criar uma lista que adicione as compras dessa linha de cima
    print("0. VOLTAR")

# Menu de Estoque
def mostra_menu_estoque():
    print("\n")
    print("===========================")
    print("||    MENU DE ESTOQUE    ||")
    print("===========================")
    print("1. ENTRADAS")  ## fazer (tem um esqueleto ja)
    print("2. SAÍDAS") ## fazer (tem um esqueleto ja) 
    print("3. VER ESTOQUE") ## fazer (tem um esqueleto ja)
    print("0. VOLTAR") 


# Menu Compras -> Lista de Fornecedores
def mostra_listar_fornecedores():
    print("\n")
    print("========================")
    print("||    FORNECEDORES    ||")
    print("========================")
    for i, fornecedor in enumerate(fornecedores, start=1):
        print(f"{i}. FORNECEDOR {fornecedor['fornecedor']}, CNPJ {fornecedor['cnpj']}")
    print("========================")
    print("9. CADASTRAR NOVO FORNECEDOR") 
    print("0. VOLTAR")

    
# Cadastrar novo fornecedor (e adicionar à lista)
def cadastrar_fornecedor():
    print("\n")
    print("============================")
    print("||  CADASTRAR FORNECEDOR  ||")
    print("============================")
    fornecedor = input("DIGITE O NOME DO FORNECEDOR: ")
    cnpj = input("Digite o CNPJ do fornecedor: ")
    novo_fornecedor = {"fornecedor": fornecedor, "cnpj": cnpj}
    fornecedores.append(novo_fornecedor)
    print("\n")
    print("FORNECEDOR CADASTRADO COM SUCESSO!")
    
# Menu Compras -> Comprar Suprimentos
def comprar_suprimentos(compras):
    print("\n")
    print("===============================")
    print("||    COMPRAR SUPRIMENTOS    ||")
    print("===============================")
    for i, suprimento in enumerate(suprimentos, start=1):
        print(f"{i}.{suprimento['suprimento']}, VALOR {suprimento['valor']}")
    print("9. CADASTRAR NOVO PRODUTO")
    print("0. VOLTAR")

# Cadastrar novo produto (e adicionar à lista)
def cadastrar_suprimento():
    print("\n")
    print("============================")
    print("||  CADASTRAR SUPRIMENTO  ||")
    print("============================")
    suprimento = input("DIGITE O NOME DO SUPRIMENTO: ")
    valor = input("DIGITE O VALOR DO SUPRIMENTO: ")
    cnpjFornecedor = input("DIGITE O CNPJ DO FORNECEDOR: ")
    novo_suprimento = {"suprimento": suprimento, "valor": valor, "cnpj_fornecedor": cnpjFornecedor}
    suprimentos.append(novo_suprimento)
    print("\n")
    print("SUPRIMENTO CADASTRADO COM SUCESSO!")

# Menu Compras -> Ver todas as compras
def ver_compras(compras):
    if len(compras) == 0:
        print("\n\n>>NENHUMA COMPRA REALIZADA.<<")
    else:
        print("COMPRAS REALIZADAS:")
        for compra in compras:
            print(f"DESCRIÇÃO: {compra['descricao']}")
            print(f"QUANTIDADE: {compra['quantidade']}")
            print(f"VALOR: R${compra['valor']}")
            print("")

# Menu Estoque -> Entradas
def listar_entradas(entradas):
    if len(entradas) == 0:
        print("\n\n >>NENHUMA ENTRADA REGISTRADA.<<")
    else:
        print("ENTRADAS REGISTRADAS:")
        for entrada in entradas:
            print(f"Descrição: {entrada['descricao']}")
            print(f"Quantidade: {entrada['quantidade']}")
            print(f"Data: {entrada['data']}")
            print("")

# Menu Estoque -> Saídas
def listar_saidas(saidas):
    if len(saidas) == 0:
        print("\n\n >>NENHUMA SAÍDA REGISTRADA<<")
    else:
        print("SAÍDAS REGISTRADAS:")
        for saida in saidas:
            print(f"Descrição: {saida['descricao']}")
            print(f"Quantidade: {saida['quantidade']}")
            print(f"Data: {saida['data']}")
            print("")

# Menu Estoque -> Ver Estoque
def ver_estoque_total(entradas, saidas):
    estoque = 0
    for entrada in entradas:
        estoque += entrada['quantidade']
    for saida in saidas:
        estoque -= saida['quantidade']

    print(f"Estoque total: {estoque}")

########### DEFINIÇÃO DO PROGRAMA ###############

compras = []
entradas = []
saidas = []

while True:
    mostra_menu_principal()
    entrada = input("DIGITE A OPÇÃO DESEJADA: ") 
    match entrada:
        case "1":
            while True: 
                mostra_menu_compras()
                opcaoCompra = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoCompra:
                    case "1":
                        while True:
                            mostra_listar_fornecedores()
                            opcaoFornecedor = input('DIGITE A OPÇÃO DESEJADA: ')
                            match opcaoFornecedor:
                                case "9":
                                    cadastrar_fornecedor()
                                    continue
                                case "0":
                                    break
                                case _:
                                    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                                    continue
                    case "2":
                        while True:
                            mostra_menu_comprar_suprimentos()
                            opcaoSuprimento = input('DIGITE A OPÇÃO DESEJADA: ')
                            match opcaoSuprimento:
                                case "1":
                                    break
                                case "2":
                                    cadastrar_suprimento()
                                    continue
                                case "0":
                                    break
                                case _:
                                    break
                    case "3":
                        ver_compras(compras)
                        continue
                    case "0":
                        break
                    case _ :
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
            continue
        case "2":
            while True:
                mostra_menu_estoque()
                opcaoEstoque = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoEstoque:
                    case "1":
                        listar_entradas(entradas)
                        continue
                    case "2":
                        listar_saidas(saidas)
                        continue
                    case "3":
                        ver_estoque_total(entradas, saidas)
                        continue
                    case "0":
                        break
                    case _:
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
            continue
        case _:
            break


        

