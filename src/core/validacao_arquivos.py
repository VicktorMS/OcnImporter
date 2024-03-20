#from sensores_formatos import sensores_formatos
from pathlib import Path

sensores_formatos = {
    "MIROS": "mir_gz",
    "YOUNG": "yng_gz",
}
def verificar_se_formato_e_valido(nome_do_arquivo):
    nome = Path(nome_do_arquivo)
    formato_arquivo = Path(nome_do_arquivo).suffix
    formato_arquivo = formato_arquivo.lstrip(".")

    if formato_arquivo in sensores_formatos.values():
        return True

    return False


