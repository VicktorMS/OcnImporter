# import de outros modulos
from src.core.import_list_converter import convert_string_array_to_import_data_list
import tests.constants.data_entry_constants as test_data
from src.core.import_data_processor import search_files_for_import_data

if __name__ == "__main__":

    lista_de_perdas = convert_string_array_to_import_data_list(test_data.IMPORT_LIST_JSON_EXAMPLE1)
    search_files_for_import_data(lista_de_perdas, test_data.SOURCE_DIRECTORY_EXAMPLE)

    ##TODO: Criar arquivo de configuração que contenha um dicionario como nome-formato do sensores
