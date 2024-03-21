import unittest
from datetime import datetime, timedelta
from src.core.import_data_comparison import calculate_date_range, compare_import_data_list_with_files_list
from tests.data_entry_example import SOURCE_DIRECTORY_FILE_LIST_EXAMPLE, IMPORT_LIST_DICTIONARY_LIST_EXAMPLE


class TestComparadorDadoEPerda(unittest.TestCase):
    def setUp(self):
        self.source_directory_files_list = SOURCE_DIRECTORY_FILE_LIST_EXAMPLE
        self.import_list = IMPORT_LIST_DICTIONARY_LIST_EXAMPLE

    def test_calcular_intervalo_entre_datas(self):
        data_inicial = datetime(2023, 12, 20, 16, 00)
        data_final = datetime(2023, 12, 21, 13, 00)
        intervalo_de_datas = calculate_date_range(data_inicial, data_final)

        # Gere uma lista de datas esperadas
        datas_esperadas = [data_inicial + timedelta(hours=i) for i in range(0, 22)]

        self.assertEqual(intervalo_de_datas, datas_esperadas, "O intervalo de datas não é o esperado")

    def test_comparacao_de_perdas_e_dados(self):
        # Executar a função que será testada
        resultado = compare_import_data_list_with_files_list(self.import_list, self.source_directory_files_list)

        # Verificar se o resultado está correto
        self.assertEqual(len(resultado), 3)  # Deve haver apenas um dado encontrado
        self.assertEqual(resultado[0]["data"], self.import_list[0]["data_inicial"])
        self.assertEqual(resultado[2]["data"], self.import_list[1]["data_inicial"])



if __name__ == '__main__':
    unittest.main()