import os
import shutil
from pathlib import Path
from utils.validacao_arquivos import verificar_se_formato_e_valido
from datetime import datetime, timedelta



def procurar_arquivo_da_perda_em_diretorio(lista_de_perdas, diretorio_de_busca):
    if os.path.exists(diretorio_de_busca):
        lista_de_dados = []
        arquivos_em_hist = os.listdir(diretorio_de_busca)

        for arquivo in arquivos_em_hist:
           if verificar_se_formato_e_valido(arquivo):
               filtrar_nome_do_arquivo(arquivo)

        comparar_lista_de_perda_com_lista_de_arquivos(lista_de_perdas, lista_de_dados)


def comparar_lista_de_perda_com_lista_de_arquivos(lista_de_perdas, lista_de_dados):
    for perda in lista_de_perdas:
        data_inicial_perda = perda["data_inicial"]
        #data_final = perda["data_inicial"]

        #TODO: Elaborar funcao que crie um range de data inicial ate a data final

        correspondente = False
        for dado in lista_de_dados:
            data_dado = dado["data"]
            #TODO: Funcao para comparar data do dado e data da perda
            comparar_data_da_perda_com_data_do_dado(data_inicial_perda, data_dado)

def comparar_data_da_perda_com_data_do_dado(data_perda, data_arquivo):
    #TODO: Terminar de Implementar
    return None


def filtrar_nome_do_arquivo(nome_arquivo):
    if nome_arquivo:
        #Exemplo de nome do Arquivo: 23701_2023-12-19-23-00.yng_gz
        nome_arquivo_separado = nome_arquivo.split(".")

        codigo_e_data = nome_arquivo_separado[0].split("_")
        data = datetime.strptime(codigo_e_data[1], '%Y-%m-%d-%H-%M')

        #Exemplo Resultado em Array ['23701_2023', '12', '19', '23', '00.yng_gz']
        nome_arquivo_dict = {
            "codigo":          codigo_e_data[0],
            "formato":         nome_arquivo_separado[1],
            "nome_do_arquivo": nome_arquivo,
            "data": data
        }

        return nome_arquivo_dict
    else:
        return None


def copiar_dado_para_diretorio_destino(caminho_do_dado, diretorio_destino):
    shutil.copy(caminho_do_dado, diretorio_destino)
