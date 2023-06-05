import time

from  modelo import HoFe
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