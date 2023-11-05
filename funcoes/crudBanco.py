import json

def sobrescreve_compras(compras):

    with open('./bases/compras.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(compras, arquivo)

def sobrescreve_produtos(produtos):
    with open('./bases/produtos.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(produtos, arquivo)

def sobrescreve_pedidos(pedidos):
    with open('./bases/pedidos.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(pedidos, arquivo)

def sobrescreve_vendas(vendas):
    with open('./bases/vendas.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(vendas, arquivo)

def sobrescreve_estoque(estoque):    
    with open('./bases/estoque.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(estoque, arquivo)

def sobrescreve_fornecedores(fornecedores):
    with open('./bases/fornecedores.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(fornecedores, arquivo)

def sobrescreve_suprimentos(suprimentos):
    with open('./bases/suprimentos.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(suprimentos, arquivo)

def sobrecreve_opcoes(opcoes):
    with open('./bases/opcoes.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(opcoes, arquivo)

def sobrescreve_tarefas(tarefas):
    with open('./bases/tarefas.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(tarefas, arquivo)

def sobrecreve_saidas(saidas):
    with open('./bases/saidas.json', 'w') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(saidas, arquivo)

def carrega_compras():
    try:
        with open('./bases/compras.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            print(arquivo)
            compras = json.load(arquivo)
            return compras
    except FileNotFoundError:
        return ['arquivo n encontrado'] 
    
def carrega_produtos():
    try:
        with open('./bases/produtos.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            produtos = json.load(arquivo)
            return produtos
    except FileNotFoundError:
        return []
    
def carrega_pedidos():
    try:
        with open('./bases/pedidos.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            pedidos = json.load(arquivo)
            return pedidos
    except FileNotFoundError:
        return []   
    
def carrega_vendas():
    try:
        with open('./bases/vendas.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            vendas = json.load(arquivo)
            return vendas
    except FileNotFoundError:
        return []
    
def carrega_estoque():
    try:
        with open('./bases/estoque.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            estoque = json.load(arquivo)
            return estoque
    except FileNotFoundError:
        return []       
    
def carrega_fornecedores():
    try:
        with open('./bases/fornecedores.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            fornecedores = json.load(arquivo)
            return fornecedores
    except FileNotFoundError:
        return []
    
def carrega_suprimentos():
    try:
        with open('./bases/suprimentos.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            suprimentos = json.load(arquivo)
            return suprimentos
    except FileNotFoundError:
        return []
    
def carrega_opcoes():
    try:
        with open('./bases/opcoes.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            opcoes = json.load(arquivo)
            return opcoes
    except FileNotFoundError:
        return []
    
def carrega_tarefas():
    try:
        with open('./bases/tarefas.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            tarefas = json.load(arquivo)
            return tarefas
    except FileNotFoundError:
        return []

def carrega_saidas():
    try:
        with open('./bases/saidas.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            saidas = json.load(arquivo)
            return saidas
    except FileNotFoundError:
        return []