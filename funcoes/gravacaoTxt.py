from datetime import datetime
def gravar_saida_txt(string):
    data = datetime.now().strftime('%d%m%Y-%Hh%Mm%S')
    with open(f"saidas/{data}.txt", 'w', encoding='utf-8') as arquivo:
     arquivo.write(string)
     print(f"ARQUIVO {data}.txt GRAVADO COM SUCESSO!")

def menu_deseja_gravar_saida():
    print("DESEJA GRAVAR A SAÍDA EM UM ARQUIVO DE TEXTO?")
    print("1. SIM")
    print("2. NÃO")
    opcao = input("DIGITE A OPÇÃO DESEJADA: ")
    return opcao