'''
Vista aplicacion logs de trabajo.
'''

from tkinter import Label, Entry, StringVar, Button, Text, END

import modelo

class Ventana:
    def __init__(
            self,
            root_mainloop
        ):
        self.root = root_mainloop
        self.registro = modelo.LogsRegistro()
        self.instruc_princ = Label(
            master=self.root,
            text=f"Version del programa: {modelo.__version__} \n INGRESAR LOG: "
        )
        self.instruc_princ.pack()

        def obtener_texto():
            texto = self.caja_mensaje.get("1.0", END)
            self.registro.entrada_log(texto)

        # Entrada de mensaje
        self.caja_mensaje = Text(
            master = self.root,
            height=10, 
            width=40
        )
        self.caja_mensaje.pack()

        boton = Button(
            self.root, 
            text="Guardar registro", 
            command=obtener_texto)
        boton.pack()
    
