from datetime import datetime, timedelta
from src.core.constants import (
    SENSOR_PARAM_UCD,
    SENSOR_NAME,
    SENSOR_FORMAT,
    START_DATE,
    END_DATE,
)


def comparar_lista_de_perda_com_lista_de_dados(lista_de_perdas, lista_de_dados):
    dados_encontrados = []
    for perda in lista_de_perdas:
        data_inicial_perda = perda[START_DATE]
        data_final_perda = perda[END_DATE]

        # Verifica se a perda tem um intervalo de datas
        if data_inicial_perda < data_final_perda:
            range_da_perda = calcular_intervalo_entre_datas(data_inicial_perda, data_final_perda)
        else:
            range_da_perda = [data_inicial_perda]  # Se não houver intervalo, usamos apenas a data inicial

        for data_perda in range_da_perda:
            for dado in lista_de_dados:
                if data_perda == dado["data"]:
                    dados_encontrados.append(dado)
    print(dados_encontrados)
    return dados_encontrados


def calcular_intervalo_entre_datas(data_inicial, data_final):
    horarios = []
    data_atual = data_inicial
    intervalo_minutos = 60

    while data_atual <= data_final:
        horarios.append(data_atual)
        data_atual += timedelta(minutes=intervalo_minutos)

    return horarios

