import time

import modelo
# algoritmo para salto de lineas
mensaje = "12345123451234512345-12345fff"

salto = 5
linea = ""
mens_csalt = ""
j = 0
print("trunc:",int(len(mensaje)/salto))
nlinenteras = int(len(mensaje)/salto)
for i in mensaje:
    linea = linea + i
    print(i)
    if j < nlinenteras:
        mens_csalt = mens_csalt + linea + "\n"
        print("corte", j)
        linea = ""
        j = j+ 1
    else:
        mens_csalt=mens_csalt+i
print(mens_csalt)


def hora() -> str:
    '''
    para que el programa sepa la hora 
    '''
    h = time.strftime("%H", time.localtime(time.time()))
    h = int(h)
    return h

print(hora(), type(hora()))
print(f'\t{hora()}|app v.: {modelo.__version__}| Espectativas:\n')


# lee ultima linea
with open('registro_trabajo.txt', 'r') as archivo:
    ultima_linea = None
    for linea in archivo:
        ultima_linea = linea
