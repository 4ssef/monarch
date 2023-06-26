"""
Este módulo contiene las funciones principales para garantizar
una mayor portabilidad en los scripts principales.

"""

import subprocess

# concatena el comando completo para ejecutar un .bat con parámetros
def run_batch(path_to_batch, *params):
    command = str(path_to_batch)
    
    # concatena los parámetros en un string final
    for parameter in params:
        command = command + ' ' + parameter
    
    return subprocess.call(command)