from datetime import datetime

def converter_string_para_data(data_string):
    try:
        data, hora = data_string.split('-')
        dia, mes, ano = map(int, data.split('/'))
        hora, minuto = map(int, hora.split(':'))
        data_e_hora = datetime(ano, mes, dia, hora, minuto)
        return data_e_hora
    except ValueError:
        return None

def primeira_data_maior(data_string1, data_string2):
    data1 = converter_string_para_data(data_string1)
    data2 = converter_string_para_data(data_string2)

    if data1 is not None and data2 is not None:
        if data1 > data2:
            return True
        else:
            return False
    else:
        return False
    
def validar_formato_data(data_string):
    data = converter_string_para_data(data_string)

    if data is not None:
        return True
    else:
        return False

def calcular_porcentagem_tempo_decorrido(data_inicial, data_final):
    data_inicial = converter_string_para_data(data_inicial)
    data_final = converter_string_para_data(data_final)

    if data_inicial is not None and data_final is not None:
        data_atual = datetime.now()

        if data_final <= data_atual:
            return 100.00


        if data_inicial <= data_atual:
            tempo_decorrido = data_atual - data_inicial
            duracao_total = data_final - data_inicial
            porcentagem_tempo_decorrido = (tempo_decorrido.total_seconds() / duracao_total.total_seconds()) * 100.00

            return round(porcentagem_tempo_decorrido, 2)
        else:
            return 0.00
    else:
        return None
    
def verificar_data_dentro_intervalo(data_inicial, data_final):
    try:
        data_inicial = datetime.strptime(data_inicial, "%d/%m/%Y-%H:%M")
        data_final = datetime.strptime(data_final, "%d/%m/%Y-%H:%M")
        data_atual = datetime.now()

        if data_inicial <= data_atual <= data_final:
            return True
        else:
            return False
    except ValueError:
        return False

def verificar_data_passada(data_string):
    data = converter_string_para_data(data_string)

    if data is not None:
        data_atual = datetime.now()

        if data < data_atual:
            return True
        else:
            return False
    else:
        return False