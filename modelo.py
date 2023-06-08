'''
Para dejar un registro de lo que se hace cada día de laboratorio/oficina.
'''

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

__author__ = "Gabriel Molina"
__maintainer__ = "Gabriel Molina"
__email__ = "g-abox@hotmail.com"
__version__ = "Beta-03"
__copyright__ = f"Copyright {HoFe.fecha()}"

global RUTA_REGISTRO, HCORTE
RUTA_REGISTRO = os.path.join(os.path.dirname(__file__), 'registro_trabajo.txt')
HCORTE = 12

def ver_ult_lin():
    '''Esta funcion verifica si el ultimo log es "self.divisor"'''
    ultima_linea = None
    try:
        with open('registro_trabajo.txt', 'r', encoding="utf-8") as archivo:
            for linea in archivo:
                ultima_linea = linea
        return ultima_linea
    except:
        with open('registro_trabajo.txt', 'a', encoding="utf-8") as archivo:
            archivo.write(f"===   REGISTRO ACTIVIDAD   === \n\t-Creado: {HoFe.fecha()}\n\t v.: {__version__}\n")
        return ultima_linea

def finlog(intvar):
    if HoFe.h() < HCORTE:
        intvar.set(value=0)
    else:
        intvar.set(value=1)
    return intvar


def formateador(mensaje_m:str, salto:int) -> str:
    '''
    OBSOLETO>>> Inserta los saltos de linea. Este algoritmo es mío,
    sin embargo, es ineficiente y además corta mal las palabras,
    y duplica caracteres. <<<<OBSOLETO.
    '''
    linea = ""
    log = ""
    ultima =""
    nlinea = 0

    # n de lineas completas. (la última suele no serlo!)
    #nlinenteras = int(len(mensaje_m)/salto)
    nlinenteras = len(mensaje_m) // salto

    # bucle recorre el mensaje y corta en lineas
    # ! -> para no cortar última linea: segundo if
    for i in mensaje_m:
        linea = linea + i
        if len(linea) == salto:
            log = log + "\t" + linea + "\n"
            linea = ""
            nlinea = nlinea + 1
        if nlinea >= nlinenteras:
            ultima = ultima + i
    log = log + "\t" + ultima

    return log

def formateador_opt(mensaje_m: str, salto: int) -> str:
    '''Había olvidado que los str son inmutables...
    >Es mejor usar usar listas para esto.
    > "//" es un operador que devuelve el resul entero de
    la dividisión. Esto lo generó chatGPT:'''
    lineas = []
    linea_actual = ""
    
    for palabra in mensaje_m.split():
        if len(linea_actual) + len(palabra) + 1 <= salto:
            linea_actual += palabra + " "
        else:
            lineas.append("\t" + linea_actual.strip())
            linea_actual = palabra + " "
    
    if linea_actual:
        lineas.append("\t" + linea_actual.strip())
    
    log = "\n".join(lineas)
    return log


class LogsRegistro:
    '''Metodos de registro y su configuración'''
    def __init__(self):
        self.archivo = RUTA_REGISTRO
        self.divisor = '-\n'
        self.final = "\n#-fin-log-#\n"
        self.h_corte = HCORTE
        self.salto = 80
        # la fecha y la version solo se imprime a la mañana
        ult = ver_ult_lin()
        if not ult == self.divisor:
            with open(self.archivo , 'a', encoding="utf-8") as archivo:
                archivo.write(f'\n{HoFe.fecha()} | v.: {__version__}\n{self.divisor}')


    def entrada_log(self, mensaje:str, checkbotv:int):        
        # modifica cabecera y final segun am o pm
        if HoFe.h() < self.h_corte:
            mensaje_m = f'{HoFe.hora()} | Mañana: ' + mensaje
            print(mensaje_m)
            log = formateador_opt(mensaje_m, self.salto)
            with open(self.archivo , 'a', encoding="utf-8") as archivo:
                print("esto es lo que se guarda:\n")
                print(log)
                archivo.write(f'{log}\n' + self.divisor)
        else:
            mensaje_m = f'{HoFe.hora()} | Tarde: ' + mensaje
            log = formateador_opt(mensaje_m, self.salto)
            with open(self.archivo , 'a', encoding="utf-8") as archivo:
                print("esto es lo que se guarda:\n")
                print(log)
                if checkbotv == 1:
                    archivo.write(f'{log}\n\t--{HoFe.fecha()}--{self.final}')
                else:
                    archivo.write(f'{log}\n' + self.divisor)
    

if __name__ == "__main__":
    print("")
    print("|||||||||||||| <Aplicación personal para registro de trabajo> ||||||||||||||")
    print("\t Version del programa:", __version__)
    print("\t",__copyright__)
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("")

