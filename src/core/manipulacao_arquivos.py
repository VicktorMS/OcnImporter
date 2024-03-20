import os
import shutil
from src.core.validacao_arquivos import verificar_se_formato_e_valido
from src.core.comparador_dado_e_perda import comparar_lista_de_perda_com_lista_de_dados
from datetime import datetime


def procurar_arquivo_da_perda_em_diretorio(lista_de_perdas, diretorio_de_busca):
    if os.path.exists(diretorio_de_busca):
        lista_de_dados = []
        arquivos_em_diretorio = os.listdir(diretorio_de_busca)

        for arquivo in arquivos_em_diretorio:
           if verificar_se_formato_e_valido(arquivo):
               lista_de_dados.append(filtrar_nome_do_arquivo(arquivo))

        comparar_lista_de_perda_com_lista_de_dados(lista_de_perdas, lista_de_dados)


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
            "data":            data
        }

        return nome_arquivo_dict
    else:
        return None


def copiar_dado_para_diretorio_destino(caminho_do_dado, diretorio_destino):
    shutil.copy(caminho_do_dado, diretorio_destino)