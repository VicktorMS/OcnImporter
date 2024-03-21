from src.utils.conversor_de_formatos import nome_do_sensor_para_formato
from datetime import datetime


class DataProcessor:

    # Processa informacoes sobre perdas de um array do pyPerdas
    def convert_string_array_to_import_data_list(self, string_array):
        import_data_list = []
        for string in string_array:
            import_data = self.extract_import_data_from_string(string)
            import_data_list.append(import_data)
        return self.remove_duplicate_import_data(import_data_list)

    def remove_duplicate_import_data(self, import_data_array):
        filtered_import_data = []
        unique_start_dates = set()
        unique_end_dates = set()

        for import_data in import_data_array:
            start_date = import_data["data_inicial"]
            end_date = import_data["data_final"]

            if (end_date not in unique_end_dates) and (start_date not in unique_start_dates):
                unique_end_dates.add(end_date)
                unique_start_dates.add(start_date)
                filtered_import_data.append(import_data)

        return filtered_import_data

    def extract_import_data_from_string(self, raw_data):
        parts_import_data = raw_data.split()

        time_period = parts_import_data[2].split("->")

        sensor = parts_import_data[0].split('][')
        part_initial_date = parts_import_data[1]

        start_datetime = f"{part_initial_date} {time_period[0]}"
        end_datetime = f"{time_period[1]} {parts_import_data[3]}"

        param_and_ucd = sensor[0].lstrip('[')
        sensor_name = sensor[1].rstrip(':').replace(']', '')

        start_date = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M')
        end_date = datetime.strptime(end_datetime, '%Y-%m-%d %H:%M')

        import_data_dict = {
            "ucd_param": param_and_ucd,
            "sensor": sensor_name,
            "formato": nome_do_sensor_para_formato(sensor_name),
            "data_inicial": start_date,
            "data_final": end_date,
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
        return import_data_dict