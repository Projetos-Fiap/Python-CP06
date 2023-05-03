# CP02 - Python - Turma 1ESPW
# Membros do grupo: André Lambert (RM99148), Alessandra Vaiano (RM551497), 
# Bryan William (RM551305), Lucas Feijó (RM99727) e Vitor Maia (RM99658).


# Função para listar Menu com duas opções, COMPRAS e ESTOQUE
def exibir_menu():
    print("----- Menu principal: -----")
    print("1. COMPRAS")
    print("2. ESTOQUE")

# Função para listar Menu de Compras
    # Fornecedores com CNPJ
    # Comprar suprimentos, com descrição, qtd e valores
    # Poder ver todas as compras
def exibir_menu_compras():
    print("----- Menu de Compras: -----")
    print("1. Lista de Fornecedores")
    print("2. Comprar suprimentos")
    print("3. Ver todas as compras feitas")

# Função para listar Menu de Estoque
    # Entradas, saídas e estoque 
def exibir_menu_estoque():
    print("----- Menu de Estoque: -----")
    print("1. Listar entradas")
    print("2. Listar saídas")
    print("3. Ver estoque total")    

# Função para listar Fornecedores
def listar_fornecedores():
    fornecedores = [
        {"nome": "Fornecedor A", "CNPJ": "1234567890"},
        {"nome": "Fornecedor B", "CNPJ": "0987654321"},
        {"nome": "Fornecedor C", "CNPJ": "5678901234"}
    ]

    print("Lista de Fornecedores:")
    for fornecedor in fornecedores:
        print(f"{fornecedor['nome']} - CNPJ: {fornecedor['cnpj']}")

# Função para submenu de comprar suprimentos
def comprar_suprimentos(compras):
    descricao = input("Digite a descrição do suprimento: ")
    quantidade = int(input("Digite a quantidade: "))
    valor = float(input("Digite o valor: "))

    compra = {
        "descricao": descricao,
        "quantidade": quantidade,
        "valor": valor
    }

    compras.append(compra)
    print("Compra realizada com sucesso!")

# Função para submenu de ver compras 
def ver_compras(compras):
    if len(compras) == 0:
        print("Nenhuma compra realizada.")
    else:
        print("Compras realizadas:")
        for compra in compras:
            print(f"Descrição: {compra['descricao']}")
            print(f"Quantidade: {compra['quantidade']}")
            print(f"Valor: R${compra['valor']}")
            print("")

# Função para submenu de entradas
def listar_entradas(entradas):
    if len(entradas) == 0:
        print("Nenhuma entrada registrada.")
    else:
        print("Entradas registradas:")
        for entrada in entradas:
            print(f"Descrição: {entrada['descricao']}")
            print(f"Quantidade: {entrada['quantidade']}")
            print(f"Data: {entrada['data']}")
            print("")

# Função para submenu de saídas
def listar_saidas(saidas):
    if len(saidas) == 0:
        print("Nenhuma saída registrada.")
    else:
        print("Saídas registradas:")
        for saida in saidas:
            print(f"Descrição: {saida['descricao']}")
            print(f"Quantidade: {saida['quantidade']}")
            print(f"Data: {saida['data']}")
            print("")

# Função para submenu de estoque
def ver_estoque_total(entradas, saidas):
    estoque = 0
    for entrada in entradas:
        estoque += entrada['quantidade']
    for saida in saidas:
        estoque -= saida['quantidade']

    print(f"Estoque total: {estoque}")

########### Rodar o programa ###############

def main():
    compras = []
    entradas = []
    saidas = []

    while True:
        exibir_menu()
        opcao_menu = int(input("Digite a opção desejada: "))

        if opcao_menu == 1:
            exibir_menu_compras()
            opcao_compras = int(input("Digite a
