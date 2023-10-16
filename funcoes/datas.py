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
    try:
        data, hora = data_string.split('-')
        dia, mes, ano = map(int, data.split('/'))
        hora, minuto = map(int, hora.split(':'))

        if len(data) == 10 and len(hora) == 5:
            if 1 <= mes <= 12 and 1 <= dia <= 31 and 0 <= ano and 0 <= hora <= 23 and 0 <= minuto <= 59:
                return True

        return False

    except (ValueError, IndexError):
        return False

def calcular_porcentagem_tempo_decorrido(data_inicial, data_final):
    data_inicial = converter_string_para_data(data_inicial)
    data_final = converter_string_para_data(data_final)

    if data_inicial is not None and data_final is not None:
        data_atual = datetime.now()

        if data_inicial <= data_atual <= data_final:
            tempo_decorrido = data_atual - data_inicial
            duracao_total = data_final - data_inicial
            porcentagem_tempo_decorrido = (tempo_decorrido.total_seconds() / duracao_total.total_seconds()) * 100.00

            return round(porcentagem_tempo_decorrido, 2)
        else:
            return None
    else:
        return None
    
def verificar_data_dentro_intervalo(data_inicial, data_final):
    try:
        # Converter as datas iniciais e finais em objetos datetime
        data_inicial = datetime.strptime(data_inicial, "%d/%m/%Y-%H:%M")
        data_final = datetime.strptime(data_final, "%d/%m/%Y-%H:%M")

        # Obter a data e hora atual
        data_atual = datetime.now()

        # Verificar se a data atual está dentro do intervalo entre a data inicial e a data final
        if data_inicial <= data_atual <= data_final:
            return True
        else:
            return False
    except ValueError:
        return False