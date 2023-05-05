# CP02 - Python - Turma 1ESPW
# Membros do grupo: André Lambert (RM99148), Alessandra Vaiano (RM551497), 
# Bryan William (RM551305), Lucas Feijó (RM99727) e Vitor Maia (RM99658).


# Menu Principal
def menu_principal():
    print("\n")
    print("==========================")
    print("||    MENU PRINCIPAL    ||")
    print("==========================")
    print("1. COMPRAS")
    print("2. ESTOQUE")

# Menu de Compras
def menu_compras():
    print("\n")
    print("===========================")
    print("||    MENU DE COMPRAS    ||")
    print("===========================")
    print("1. LISTA DE FORNECEDORES")
    print("2. COMPRAR SUPRIMENTOS")
    print("3. VER TODAS AS COMPRAS")
    print("0. VOLTAR")

# Menu de Estoque
def menu_estoque():
    print("\n")
    print("===========================")
    print("||    MENU DE ESTOQUE    ||")
    print("===========================")
    print("1. ENTRADAS") 
    print("2. SAÍDAS")
    print("3. VER ESTOQUE")
    print("0. VOLTAR") 

# Lista de fornecedores
fornecedores = [
    {"fornecedor": "FULANO", "cnpj": "60.718.835/0001-03"},
    {"fornecedor": "CICLANO", "cnpj": "49.548.348/0001-07"}
]

# Menu Compras -> Lista de Fornecedores
def listar_fornecedores():
    print("\n")
    print("========================")
    print("||    FORNECEDORES    ||")
    print("========================")
    for i, fornecedor in enumerate(fornecedores, start=1):
        print(f"{i}. FORNECEDOR {fornecedor['fornecedor']}, CNPJ {fornecedor['cnpj']}")
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
    listar_fornecedores()
    
# Lista de suprimentos
suprimentos = [
    {"suprimento": "ROLHAS", "valor": "R$ 3"},
    {"suprimento": "GARRAFAS", "valor": "R$ 5"},
    {"suprimento": "CAIXAS", "valor": "R$ 4"},
    {"suprimento": "RÓTULOS", "valor": "R$ 2"}
]    
    
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
    valor = input("Digite o CNPJ do fornecedor: ")
    novo_suprimento = {"suprimento": suprimento, "valor": valor}
    suprimento.append(novo_suprimento)
    print("\n")
    print("SUPRIMENTO CADASTRADO COM SUCESSO!")
    comprar_suprimentos()

# Menu Compras -> Ver todas as compras
def ver_compras(compras):
    if len(compras) == 0:
        print("NENHUMA COMPRA REALIZADA.")
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
        print("NENHUMA ENTRADA REGISTRADA.")
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
        print("NENHUMA SAÍDA REGISTRADA")
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

menu_principal()

opcao_menu = int(input("DIGITE A OPÇÃO DESEJADA: "))

if opcao_menu == 1:
    menu_compras()
    opcao_compras = int(input("DIGITE A OPÇÃO DESEJADA: "))

    if opcao_compras == 1:
        listar_fornecedores()
        opcao_fornecedores = int(input("DIGITE A OPÇÃO DESEJADA: "))
        
        if opcao_fornecedores == 9:
            cadastrar_fornecedor()
        elif opcao_fornecedores == 0:
            menu_compras()
        else:
            print("OPÇÃO INVÁLIDA.")
        
    elif opcao_compras == 2:
        comprar_suprimentos(compras)
    elif opcao_compras == 3:
        ver_compras(compras)
    elif opcao_compras == 0:
        menu_principal()
    else:
        print("OPÇÃO INVÁLIDA.")

elif opcao_menu == 2:
    menu_estoque()
    opcao_estoque = int(input("DIGITE A OPÇÃO DESEJADA: "))

    if opcao_estoque == 1:
        listar_entradas(entradas)
    elif opcao_estoque == 2:
        listar_saidas(saidas)
    elif opcao_estoque == 3:
        ver_estoque_total(entradas, saidas)
    elif opcao_estoque == 0:
        menu_principal()
    else:
        print("OPÇÃO INVÁLIDA.")

else:
    print("OPÇÃO INVÁLIDA.")
        

