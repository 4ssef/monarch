"""
Este script se encarga de registrar/crear una aplicación nueva en portal.azure.com
cumpliendo las características necesarias para crear una cuenta publicadora.

Dentro del directorio 'myinfo.la', en el apartado de 'App registrations' es en donde
se crean manualmente las cuentas nuevas de los clientes, es decir, la cuenta 'prodynamics19@myinfo.la',
'prodynamics20@myinfo.la' ... 'prodynamicsn@myinfo.la', por lo que, este script se encarga de automatizar
esa parte con el uso de la herramienta 'Azure CLI', cuyo lugar de descarga oficial es:

https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli

Entonces, ya que Azure CLI utiliza la variable de entorno 'az', se puede ejecutar desde cualquier línea de comandos,
por lo que en este script, se utilizará la librería 'subprocess' para llamar a los .bat encargados de las tareas.

---------------------------------------------------------------
Este script retorna las variables de entorno:
1. CLIENT_ID
---------------------------------------------------------------

"""

import os
from shutil import which
from dotenv import load_dotenv
from pathlib import Path
import json
from lib.funcs import run_batch

load_dotenv()

PROJECT_PATH = Path(__file__).resolve().parent
LIB_PATH = Path.joinpath(PROJECT_PATH, 'lib')

# verifica si Azure CLI está instalado
try:
	os.system(f"echo Azure CLI installation found at {which('az')}")
except:
	os.system("echo Azure CLI is not installed. Please download at https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli")
	exit()

APP_NAME = input("New Azure AD application name: ")

params = {
	'app_name': APP_NAME
}

# ---------------------------------------------------------------
# Registra la aplicación en Azure AD (register_azure_app.bat)
# ---------------------------------------------------------------
path_to_batch = Path.joinpath(LIB_PATH, 'register_azure_app.bat')
run_batch(path_to_batch, params['app_name'])

# ---------------------------------------------------------------
# Obtiene el appId (el client ID) y la crea como variable de 
# entorno llamada CLIENT_ID
# ---------------------------------------------------------------
client_id = json.load(open('app_details.json'))['appId']
os.environ['CLIENT_ID'] = client_id
os.remove('app_details.json')

# ---------------------------------------------------------------
# Agrega los permisos de /lib/cons y los concede via administrador
# a la aplicación registrada en el paso anterior (add_permissions_to_app.bat)
# ---------------------------------------------------------------
path_to_batch = Path.joinpath(LIB_PATH, 'add_permissions_to_app.bat')
run_batch(path_to_batch, client_id)