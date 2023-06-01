'''
Para dejar un registro de lo que se hace cada día de laboratorio/oficina.
'''
__author__ = "Gabriel Molina"
__maintainer__ = "Gabriel Molina"
__email__ = "g-abox@hotmail.com"
__copyright__ = "Copyright 2023/06"
__version__ = "alfa-00"

import logging
import time
import os

def hora() -> str:
    '''
    Imprime hora y fecha para logs.
    '''
    h = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return h


class LogsRegistro:
    def __init__(self):
        ruta_main = os.path.dirname(__file__)
        archivo = os.path.join(ruta_main, 'registro_trabajo.log')
        logging.basicConfig(filename=archivo, level="INFO")
        logging.info(f"Inicio app {__version__} > {hora()}" + "<")

    @staticmethod
    def ruta_registro() -> str:
        pass

    def log_mañana(self, mensaje:str):
        log = hora() + " hs.| Espectativas: " + mensaje
        logging.info(log)
    
    def log_tarde(self, mensaje:str):
        log = hora() + " hs.| Acontecido: " + mensaje
        logging.info(log)
    
    def log_advertencia(self, mensaje:str):
        log = hora() + " hs.| AVISO: " + mensaje
        logging.warning(log)



if __name__ == "__main__":
    print("")
    print("|||||||||||||| <Aplicación personal para registro de trabajo> ||||||||||||||")
    print("\t Version del programa:", __version__)
    print("\t",__copyright__)
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("")
