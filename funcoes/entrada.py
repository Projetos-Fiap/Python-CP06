# Mostra todas as entradas na tela
def listar_entradas(entradas):
    if len(entradas) == 0:
        print('\n\n >>NENHUMA ENTRADA REGISTRADA.<<')
    else:
        print('\n')
        print("=================================")
        print("||    Histórico de entradas    ||")
        print("=================================")
        for entrada in entradas:
            print('')
            print(f"DATA     : {entrada['data']}")
            print(f"DESCRICAO: {entrada['descricao']}")
            print("ITENS:")
            for item in entrada['itens']:
                print(f"{item['quantidade']} * {item['suprimento']}")
            print('')
            print('-----------------------------------')