import requests
import configparser
import os
import re

def deploy_to_pa(ruta_archivo_local):

    path = os.path.dirname(os.path.abspath(__file__))

    config_file = re.sub(r'\\', '/', path) + \
        "/config/config.ini"

    config = configparser.ConfigParser()
    config.read(config_file)

    username = config["CREDENTIALS"]["USER"]
    token = config["CREDENTIALS"]["API_TOKEN"]

    # Obtener información de la cuota de CPU
    response = requests.get(
        f'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/',
        headers={'Authorization': f'Token {token}'}
    )

    if response.status_code == 200:
        print('CPU quota info:')
        print(response.content)
    else:
        print(f'Got unexpected status code {response.status_code}: {response.content}')

    # Ruta del archivo local que deseas subir
    #ruta_archivo_local = r'C:\Users\dev-h\OneDrive\Escritorio\proyectos_python\to_zip_script\requirements.txt'

    # Ruta del archivo en PythonAnywhere donde deseas subirlo
    ruta_archivo_remoto = '/home/gcamposhyl/nombre_archivo.txt'

    # Subir el archivo local a PythonAnywhere
    with open(ruta_archivo_local, 'rb') as archivo:
        response = requests.post(
            f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path{ruta_archivo_remoto}',
            headers={'Authorization': f'Token {token}'},
            files={'content': archivo}
        )

    if response.status_code == 201:
        print('Archivo subido exitosamente a PythonAnywhere.')
    else:
        print('Error al subir el archivo a PythonAnywhere:', response.content)
