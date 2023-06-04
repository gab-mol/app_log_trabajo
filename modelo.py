'''
Para dejar un registro de lo que se hace cada día de laboratorio/oficina.
'''
__author__ = "Gabriel Molina"
__maintainer__ = "Gabriel Molina"
__email__ = "g-abox@hotmail.com"
__copyright__ = "Copyright 2023/06"
__version__ = "alfa-02"

import time
import os

class HoFe:
    '''
    Hora y fecha.
    '''
    def hora() -> str:
        hora = time.strftime("%H:%M:%S hs.", time.localtime(time.time()))
        return hora
    
    def h():
        h = int(time.strftime("%H", time.localtime(time.time())))
        return h
    
    def fecha() -> str:
        fecha = time.strftime("%d-%m-%Y", time.localtime(time.time()))
        return fecha


def ver_ult_lin():
    '''Esta funcion verifica si el ultimo log es '''
    with open('registro_trabajo.txt', 'r') as archivo:
        ultima_linea = None
        for linea in archivo:
            ultima_linea = linea
    return ultima_linea


def formateador(mensaje_m:str, salto:int) -> str:
    '''Inserta los saltos de linea'''
    linea = ""
    log = ""
    for i in mensaje_m:
        linea = linea + i
        if len(linea) == salto:
            log = log + "\t" + linea + "\n"
            linea = ""
        
    return log

class LogsRegistro:
    def __init__(self):
        ruta_main = os.path.dirname(__file__)
        self.archivo = os.path.join(ruta_main, 'registro_trabajo.txt')
        
        # la fecha y la version solo se imprime a la mañana
        if ver_ult_lin()=='#-fin-log-#':
            with open(self.archivo , 'a') as archivo:
                archivo.write(f'\n{HoFe.fecha()} | App: {__version__}\n')


    def entrada_log(self, mensaje:str):
        salto = 64
        
        # modifica cabecera y final segun am o pm
        if HoFe.h() < 14:
            mensaje_m = f'{HoFe.hora()} | Espectativas:' + mensaje
            print(mensaje_m)
            log = formateador(mensaje_m, salto)
            with open(self.archivo , 'a') as archivo:
                print("esto es lo que se guarda:\n")
                print(log)
                archivo.write(f'{log}\n')
        else:
            mensaje_m = f'{HoFe.hora()} | Acontecido:' + mensaje
            log = formateador(mensaje_m, salto)
            with open(self.archivo , 'a') as archivo:
                print("esto es lo que se guarda:\n")
                print(log)
                archivo.write(f'\t{log}\n--{HoFe.fecha()}--\n#-fin-log-#')
    
# NO ESTOY PUDIENDO HACER UN SALTO DE LINEA QUE NO CORTE LA ULTIMA LINEA

if __name__ == "__main__":
    print("")
    print("|||||||||||||| <Aplicación personal para registro de trabajo> ||||||||||||||")
    print("\t Version del programa:", __version__)
    print("\t",__copyright__)
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("")

