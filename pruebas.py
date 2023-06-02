import time
# algoritmo para salto de lineas
mensaje = "gggggggggggggggg"

salto = 3
linea = ""
salida = ""
for i in mensaje:
    linea = linea + i
    if len(linea) == 3:
        salida = salida + linea + "\n"
        linea = ""
print(salida)


def hora() -> str:
    '''
    para que el programa sepa la hora 
    '''
    h = time.strftime("%H", time.localtime(time.time()))
    h = int(h)
    return h

print(hora(), type(hora()))