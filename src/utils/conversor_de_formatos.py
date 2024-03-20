#from sensores_formatos import sensores_formatos
sensores_formatos = {
    "MIROS": "mir_gz",
    "YOUNG": "yng_gz",
}


def nome_do_sensor_para_formato(nome_sensor):
    try:
        return sensores_formatos[nome_sensor]
    except KeyError:
        print(f"O sensor '{nome_sensor}' não foi encontrado no dicionário.")
        return None


def formato_para_nome_do_sensor(formato):
    for nome_sensor, formato_sensor in sensores_formatos.items():
        if formato_sensor == formato:
            print(f"O formato '{formato}' não foi encontrado no dicionário.")
            return nome_sensor
    return None
