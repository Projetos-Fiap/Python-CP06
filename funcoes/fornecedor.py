# Cadastrar novo fornecedor (e adicionar à lista)
def cadastrar_fornecedor(fornecedores):
    print('\n')
    print('============================')
    print('||  CADASTRAR FORNECEDOR  ||')
    print('============================')
    fornecedor = input('DIGITE O NOME DO FORNECEDOR: ')
    cnpj = input('Digite o CNPJ do fornecedor: ')
    novo_fornecedor = {'fornecedor': fornecedor, 'cnpj': cnpj}
    fornecedores.append(novo_fornecedor)
    print('\n')
    print('FORNECEDOR CADASTRADO COM SUCESSO!')

# Menu Compras -> Lista de Fornecedores
def mostra_listar_fornecedores(fornecedores):
    print('\n')
    print('========================')
    print('||    FORNECEDORES    ||')
    print('========================')
    for i, fornecedor in enumerate(fornecedores, start=1):
        print(f"{i}. FORNECEDOR {fornecedor['fornecedor']}, CNPJ {fornecedor['cnpj']}")
    print('========================')
    print('9. CADASTRAR NOVO FORNECEDOR') 
    print('0. VOLTAR')