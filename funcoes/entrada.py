def string_lista_entradas(entradas):
    string = ""
    if len(entradas) == 0:
        string += "\n\n>>NENHUMA ENTRADA REGISTRADA.<<"
    else:
        string += '\n'
        string += "=================================\n"
        string += "||    Histórico de entradas    ||\n"
        string += "=================================\n"
        for entrada in entradas:
            string += '\n'
            string += f"DATA     : {entrada['data']}\n"
            string += f"DESCRICAO: {entrada['descricao']}\n"
            string += "ITENS:\n"
            for item in entrada['itens']:
                string += f"{item['quantidade']} * {item['suprimento']}\n"
            string += '\n'
            string += '-----------------------------------\n'
    return string

# Mostra todas as entradas na tela
def listar_entradas(entradas):
    # if len(entradas) == 0:
    #     print('\n\n >>NENHUMA ENTRADA REGISTRADA.<<')
    # else:
    #     print('\n')
    #     print("=================================")
    #     print("||    Histórico de entradas    ||")
    #     print("=================================")
    #     for entrada in entradas:
    #         print('')
    #         print(f"DATA     : {entrada['data']}")
    #         print(f"DESCRICAO: {entrada['descricao']}")
    #         print("ITENS:")
    #         for item in entrada['itens']:
    #             print(f"{item['quantidade']} * {item['suprimento']}")
    #         print('')
    #         print('-----------------------------------')
    print(string_lista_entradas(entradas))