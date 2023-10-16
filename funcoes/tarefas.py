from datas import *

def cadastrar_tarefa(tarefas):
    while True:
        print('\n')
        print('============================')
        print('||    CADASTRAR TAREFA     ||')
        print('============================')
        dataInicial = input('DIGITE A DATA INICIAL (FORMATO DD/MM/YYYY-HH:MM): ')
        dataFinal = input('DIGITE A DATA FINAL (FORMATO DD/MM/YYYY-HH:MM):: ')
        responsavel = input('DIGITE O NOME DO RESPONSÁVEL: ')
        descricao = input('DIGITE A DESCRIÇÃO DA TAREFA: ')
        complitudeReal = input('DIGITE A COMPLITUDE REAL: ')
        
        if (validar_formato_data(dataInicial)):
            dataInicial = converter_string_para_data(dataInicial)
        else:
            print('DATA INVÁLIDA! TENTE NOVAMENTE!')
            continue

        if (validar_formato_data(dataFinal)):
            dataFinal = converter_string_para_data(dataFinal)
        else:
            print('DATA INVÁLIDA! TENTE NOVAMENTE!')
            continue


        nova_tarefa = {"id": len(tarefas), "dataInicial": dataInicial, "dataFinal": dataFinal, "responsavel": responsavel, "descricao": descricao, "complitudeReal": complitudeReal, "PlanoParaComplitude": ""}
        tarefas.append(nova_tarefa)

        print('TAREFA CADASTRADA COM SUCESSO!')

def calcular_complitude_real(tarefa)

