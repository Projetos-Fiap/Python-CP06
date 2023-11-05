import funcoes.crudBanco as crudBanco
import os
# Definindo função que limpa a tela do terminal
limpa_a_tela = lambda: os.system('cls')

def string_mostra_lista_de_fornecedores(fornecedores):
    string = "\n"
    string += "========================\n"
    string += "||    FORNECEDORES    ||\n"
    string += "========================\n"
    for i, fornecedor in enumerate(fornecedores, start=1):
        string += f"{i}. FORNECEDOR {fornecedor['fornecedor']}, CNPJ {fornecedor['cnpj']}\n"
    string += '\n============OPÇÕES============\n'
    string += '9. CADASTRAR NOVO FORNECEDOR\n' 
    string += '0. VOLTAR\n'
    return string

# Cadastrar novo fornecedor
def cadastrar_fornecedor(fornecedores):
    print('\n')
    print('============================')
    print('||  CADASTRAR FORNECEDOR  ||')
    print('============================')
    fornecedor = input('DIGITE O NOME DO FORNECEDOR: ')
    cnpj = input('Digite o CNPJ do fornecedor: ')
    novo_fornecedor = {'fornecedor': fornecedor, 'cnpj': cnpj}
    fornecedores.append(novo_fornecedor)
    crudBanco.sobrescreve_fornecedores(fornecedores)
    print('\n')
    limpa_a_tela()
    print('FORNECEDOR CADASTRADO COM SUCESSO!')

# Mostra na tela todos os fornecedores
def mostra_lista_de_fornecedores(fornecedores):
    # print('\n')
    # print('========================')
    # print('||    FORNECEDORES    ||')
    # print('========================')
    # for i, fornecedor in enumerate(fornecedores, start=1):
    #     print(f"{i}. FORNECEDOR {fornecedor['fornecedor']}, CNPJ {fornecedor['cnpj']}")
    # print('\n============OPÇÕES============')
    # print('9. CADASTRAR NOVO FORNECEDOR') 
    # print('0. VOLTAR')
    print(string_mostra_lista_de_fornecedores(fornecedores))