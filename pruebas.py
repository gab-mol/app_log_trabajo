import time
import subprocess

from  modelo import HoFe, RUTA_REGISTRO
# algoritmo para salto de lineas
mensaje = "123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345-12345fff"

salto = 19
linea = ""
nlinea = 0
mens_csalt = ""
nlinenteras = int(len(mensaje)/salto)
ultima =""
print(nlinenteras)
for i in mensaje:
    linea = linea + i
    print(nlinea, nlinenteras, "|", len(linea))
    if len(linea) == salto:
        print("nlinea, nlinenteras, |, len(linea")
        print("if")
        mens_csalt = mens_csalt + "\t" + linea + "\n"
        linea = ""
        nlinea = nlinea + 1
    if nlinea >= nlinenteras:
        print("> nlinenteras")
        ultima = ultima + i
mens_csalt = mens_csalt + "\t" + ultima
print(mens_csalt)


print(f'\t{"mens"}\n--{HoFe.fecha()}--\n#-fin-log-#')



def hora() -> str:
    '''
    para que el programa sepa la hora 
    '''
    h = time.strftime("%H", time.localtime(time.time()))
    h = int(h)
    return h

#print(hora(), type(hora()))
#print(f'\t{hora()}|app v.: {modelo.__version__}| Espectativas:\n')


# lee ultima linea
with open('registro_trabajo.txt', 'r') as archivo:
    ultima_linea = None
    for linea in archivo:
        ultima_linea = linea

print('\n\t-\n')



def formateador(mensaje_m:str, salto:int) -> str:
    '''Inserta los saltos de linea. OBSOLETA'''
    linea = ""
    log = ""
    ultima =""
    nlinea = 0

    # n de lineas completas. (la última suele no serlo!)
    nlinenteras = int(len(mensaje_m)/salto)
    
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

def fom(mensaje_m: str, salto: int) -> str:
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

def abrir_registro():
    subprocess.run(['notepad.exe', RUTA_REGISTRO])

abrir_registro()