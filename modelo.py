'''
Para dejar un registro de lo que se hace cada día de laboratorio/oficina.
'''
__author__ = "Gabriel Molina"
__maintainer__ = "Gabriel Molina"
__email__ = "g-abox@hotmail.com"
__copyright__ = "Copyright 2023/06"
__version__ = "alfa-01"

import logging
import time
import os

def hora() -> str:
    '''
    !!!!!!!!! DEPRECATED !!!!!!!!
    Imprime hora y fecha para logs.
    '''
    h = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return h


class LogsRegistro:
    def __init__(self):
        ruta_main = os.path.dirname(__file__)
        archivo = os.path.join(ruta_main, 'registro_trabajo.log')
        logging.basicConfig(
            filename=archivo,
            level=logging.INFO,
            format='%(asctime)s hs. %(message)s',
            encoding='utf-8'
        )        
        logging.info(f"Inicio app {__version__}")


    def entrada_log(self, mensaje:str):
        salto = 40
        linea = ""
        h = int(time.strftime("%H", time.localtime(time.time())))
        if h < 12:
            tipo_m = "| Espectativas:"
        else:
            tipo_m = "| Acontecido:"
        log = "hs. app" + __version__ + tipo_m + mensaje
        logging.info(log)
    
    
    def log_advertencia(self, mensaje:str):
        log = hora() + " hs.| AVISO: " + mensaje
        logging.warning(log)


def obs_hora():
    '''Esto usa la hora del sistema para formatear el mendaje'''
    h = int(time.strftime("%H", time.localtime(time.time())))
    if h < 12:
        tipo_m = "| Espectativas:"
    else:
        tipo_m = "| Acontecido:"


if __name__ == "__main__":
    print("")
    print("|||||||||||||| <Aplicación personal para registro de trabajo> ||||||||||||||")
    print("\t Version del programa:", __version__)
    print("\t",__copyright__)
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("")
