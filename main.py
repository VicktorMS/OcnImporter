# import de outros modulos
from src.core.import_list_converter import convert_string_array_to_import_data_list
import tests.data_entry_example as test_data
from src.core.manipulacao_arquivos import procurar_arquivo_da_perda_em_diretorio, copiar_dado_para_diretorio_destino


if __name__ == "__main__":

    lista_de_perdas = convert_string_array_to_import_data_list(test_data.IMPORT_LIST_JSON_EXAMPLE1)
    procurar_arquivo_da_perda_em_diretorio(lista_de_perdas, test_data.SOURCE_DIRECTORY_EXAMPLE)

    ##TODO: Refatorar Classe em data_processor
    ##TODO: Refatorar nomencalturar em inglês
    ##TODO: Criar arquivo de configuração que contenha um dicionario como nome-formato do sensores
