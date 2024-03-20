from src.utils.conversor_de_formatos import nome_do_sensor_para_formato
from datetime import datetime


class DataProcessor:

    # Processa informacoes sobre perdas de um array do pyPerdas
    def extract_dataloss_from_rawdata_array(self, rawdata_array):
        dataloss_array = []
        for rawdata in rawdata_array:
            dataloss_array.append(self.extract_dataloss_info(rawdata))
        return self.remove_perdas_duplicadas(dataloss_array)

    def remove_perdas_duplicadas(self, perdas_array):
        perdas_filtradas = []
        datas_iniciais_unicas = set()
        datas_finais_unicas = set()

        for perda in perdas_array:
            data_inicial = perda["data_inicial"]
            data_final = perda["data_final"]

            if (data_final not in datas_finais_unicas) and (data_inicial not in datas_iniciais_unicas):
                datas_finais_unicas.add(data_final)
                datas_iniciais_unicas.add(data_inicial)
                perdas_filtradas.append(perda)

        return perdas_filtradas

    def extract_dataloss_info(self, rawdata):
        parts_dataloss = rawdata.split()

        time_period = parts_dataloss[2].split("->")

        sensor = parts_dataloss[0].split('][')
        part_initial_date = parts_dataloss[1]

        start_datetime = f"{part_initial_date} {time_period[0]}"
        end_datetime = f"{time_period[1]} {parts_dataloss[3]}"

        param_e_ucd = sensor[0].lstrip('[')
        sensor_name = sensor[1].rstrip(':').replace(']', '')

        data_inicial = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M')
        data_final = datetime.strptime(end_datetime, '%Y-%m-%d %H:%M')

        dataloss_dict = {
            "ucd_param": param_e_ucd,
            "sensor": sensor_name,
            "formato": nome_do_sensor_para_formato(sensor_name),
            "data_inicial": data_inicial,
            "data_final": data_final,
        }

        """
        Exemplo de Retorno
        {
            'ucd_param': 'BRM_1_ANNANERY', 
            'sensor': 'YOUNG', 
            'formato': 'yng_gz',
            'data_inicial': datetime.datetime(2023, 12, 15, 17, 0), 
            'data_final': datetime.datetime(2023, 12, 15, 17, 0)
         }
         """
        return dataloss_dict