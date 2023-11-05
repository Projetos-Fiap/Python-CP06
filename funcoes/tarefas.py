import funcoes.crudBanco as crudBanco
import funcoes.datas as datas

limpa_a_tela = lambda: os.system('cls')

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

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
        complitudeReal = input('DIGITE A COMPLITUDE REAL (de 0.00 a 100.00): ')
        
        if (not datas.validar_formato_data(dataInicial)):
            print('DATA INVÁLIDA! TENTE NOVAMENTE!')
            continue
            

        if (not datas.validar_formato_data(dataFinal)):
            print('DATA INVÁLIDA! TENTE NOVAMENTE!')
            continue


        nova_tarefa = {"id": len(tarefas), "dataInicial": dataInicial, "dataFinal": dataFinal, "responsavel": responsavel, "descricao": descricao, "complitudeReal": complitudeReal, "PlanoParaComplitude": ""}
        tarefas.append(nova_tarefa)
        crudBanco.sobrescreve_tarefas(tarefas)

        print('TAREFA CADASTRADA COM SUCESSO!')
        break

def calcular_complitude_planejada(tarefa):
    dataInicial = tarefa['dataInicial']
    dataFinal = tarefa['dataFinal']
    planejado = datas.calcular_porcentagem_tempo_decorrido(dataInicial, dataFinal)
    return planejado
    
def atualizar_complitude_real(tarefas):
    while True:
        idTarefa = input('DIGITE O ID DA TAREFA: ')
        if not idTarefa.isdigit():
            print('ID INVÁLIDO! TENTE NOVAMENTE!')
            continue
        elif int(idTarefa) > len(tarefas) - 1:
            print('ID INVÁLIDO! TENTE NOVAMENTE!')
            continue
        else:
            tarefa = tarefas[int(idTarefa)]
            complitudeReal = input('DIGITE A COMPLITUDE REAL (de 0.00 a 100.00): ')
            if is_float(complitudeReal) == False:
                print('COMPLITUDE REAL INVÁLIDA! TENTE NOVAMENTE!')
                continue
            elif (float(complitudeReal) < 0.00 or float(complitudeReal) > 100.00):
                print('COMPLITUDE REAL INVÁLIDA! TENTE NOVAMENTE!')
                continue
            else:
                tarefa['complitudeReal'] = float(complitudeReal)
                tarefas[tarefa['id']] = tarefa
                print('COMPLITUDE REAL ATUALIZADA COM SUCESSO!')
                break

def ordena_tarefas_por_dataInicial(tarefas):
    tarefasClone = tarefas[:]
    tarefasClone.sort(key=lambda tarefa: tarefa['dataInicial'])
    return tarefasClone

def filtrar_tarefas_nao_iniciadas(tarefas):
    tarefasClone = tarefas[:]
    tarefasClone = list(filter(lambda tarefa: not datas.verificar_data_passada(tarefa['dataInicial']), tarefasClone))
    return tarefasClone

def filtrar_tarefas_em_andamento(tarefas):
    tarefasClone = tarefas[:]
    tarefasClone = list(filter(lambda tarefa: tarefa['complitudeReal'] != '100.00' and datas.verificar_data_passada(tarefa['dataInicial']) , tarefasClone))
    return tarefasClone

def filtrar_tarefas_concluidas(tarefas):
    tarefasClone = tarefas[:]
    tarefasClone = list(filter(lambda tarefa: tarefa['complitudeReal'] == '100.00', tarefasClone))
    return tarefasClone

def filtrar_tarefas_atrasadas(tarefas):
    tarefasClone = tarefas[:]
    tarefasClone = list(filter(lambda tarefa: float(tarefa['complitudeReal']) < calcular_complitude_planejada(tarefa), tarefasClone))
    return tarefasClone

def mostra_tarefas(tarefas):
    for tarefa in tarefas:
        print(f"ID: {tarefa['id']}\nDATA INICIAL: {tarefa['dataInicial']} | DATA FINAL: {tarefa['dataFinal']}\nRESPONSÁVEL: {tarefa['responsavel']}\nDESCRIÇÃO: {tarefa['descricao']}\nCOMPLITUDE REAL: {tarefa['complitudeReal']} | COMPLITUDE PLANEJADA: {calcular_complitude_planejada(tarefa)}\nPLANO PARA COMPLITUDE: {tarefa['PlanoParaComplitude']}")
        print('-----------------------------------')

def insere_plano_para_complitude(tarefas):
    while True: 
        idTarefa = input('DIGITE O ID DA TAREFA: ')
        if not idTarefa.isdigit():
            print('ID INVÁLIDO! TENTE NOVAMENTE!')
            continue
        elif int(idTarefa) > len(tarefas) - 1:
            print('ID INVÁLIDO! TENTE NOVAMENTE!')
            continue
        else:
            tarefa = tarefas[int(idTarefa)]

            planoParaComplitude = input('DIGITE OPLANO PARA COMPLITUDE: (Minimo 10 caracteres): ')
            if (len(planoParaComplitude) < 10):
                print('PLANO PARA COMPLITUDE INVÁLIDO! TENTE NOVAMENTE!')
                continue
            else:
                tarefa['PlanoParaComplitude'] = planoParaComplitude
                tarefas[tarefa['id']] = tarefa
                print('PLANO PARA COMPLITUDE INSERIDO COM SUCESSO!')
                break

def mostra_menu_tarefas():
    print('\n')
    print('===========================')
    print('||    MENU DE TAREFAS    ||')
    print('===========================')
    print('1. CADASTRAR TAREFA')  
    print('2. ATUALIZAR COMPLITUDE REAL')
    print('3. MOSTRAR TAREFAS')
    print('0. VOLTAR')

def menu_tarefas_em_andamento():
    print('\n')
    print('===========================')
    print('|| TAREFAS EM ANDAMENTO  ||')
    print('===========================')

def menu_tarefas_concluidas():
    print('\n')
    print('===========================')
    print('||  TAREFAS CONCLUÍDAS   ||')
    print('===========================')

def menu_tarefas_nao_iniciadas():
    print('\n')
    print('===========================')
    print('|| TAREFAS NÃO INICIADAS ||')
    print('===========================')

def menu_tarefas_atrasadas():
    print('\n')
    print('===========================')
    print('||   TAREFAS ATRASADAS   ||')
    print('===========================')

def mostra_menu_tarefas():
    print('\n')
    print('===========================')
    print('||    MENU DE TAREFAS    ||')
    print('===========================')
    print('1. CADASTRAR TAREFA')  
    print('2. ATUALIZAR COMPLITUDE REAL')
    print('3. MOSTRAR TODAS AS TAREFAS')
    print('4. MOSTRAR TAREFAS EM ANDAMENTO')
    print('5. MOSTRAR TAREFAS CONCLUÍDAS')
    print('6. MOSTRAR TAREFAS NÃO INICIADAS')
    print('7. MOSTRAR TAREFAS ATRASADAS')
    print('8. INSERIR PLANO PARA COMPLITUDE')
    print('0. VOLTAR')
        