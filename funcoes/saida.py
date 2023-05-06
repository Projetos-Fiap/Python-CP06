# Menu Estoque -> Saídas
def listar_saidas(saidas):
    if len(saidas) == 0:
        print('\n\n >>NENHUMA SAÍDA REGISTRADA<<')
    else:
        print("SAÍDAS REGISTRADAS:")
        for saida in saidas:
            print(f"Descrição: {saida['descricao']}")
            print(f"Quantidade: {saida['quantidade']}")
            print(f"Data: {saida['data']}\n")
