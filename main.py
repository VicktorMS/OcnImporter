# import de outros modulos
from src.core.data_processor import DataProcessor
import tests.data_entry_example as test_data
from src.core.manipulacao_arquivos import procurar_arquivo_da_perda_em_diretorio, copiar_dado_para_diretorio_destino


if __name__ == "__main__":
    data_processor = DataProcessor()

    lista_de_perdas = data_processor.extract_dataloss_from_rawdata_array(test_data.IMPORT_LIST_JSON_EXAMPLE1)
    procurar_arquivo_da_perda_em_diretorio(lista_de_perdas, test_data.SOURCE_DIRECTORY_EXAMPLE)

    ##TODO: Refatorar Classe em data_processor
    ##TODO: Refatorar nomencalturar em inglês
    ##TODO: Criar arquivo de configuração que contenha um dicionario como nome-formato do sensores
