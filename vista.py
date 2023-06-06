'''
Vista aplicacion logs de trabajo.
'''

from tkinter import Label, Entry, StringVar, Button, Text, END
import subprocess

import modelo

class Ventana:
    def __init__(
            self,
            root_mainloop
        ):
        self.root = root_mainloop
        self.registro = modelo.LogsRegistro()
        self.root.geometry("425x240")
        self.root.title("Registro Diario")
        self.instruc_princ = Label(
            master=self.root,
            text=f"Version del programa: {modelo.__version__} \n INGRESAR LOG: "
        )
        self.instruc_princ.grid(row=0, columnspan=3, column=0, padx=10)

        def obtener_texto():
            texto = self.caja_mensaje.get("1.0", END)
            self.registro.entrada_log(texto)
            aviso_lab.config(text="--guardado--")

        def abrir_registro():
            subprocess.run(['notepad.exe', modelo.RUTA_REGISTRO])
            
        # Entrada de mensaje
        self.caja_mensaje = Text(
            master = self.root,
            height=10, 
            width=50
        )
        self.caja_mensaje.grid(row=1, columnspan=3, column=0, padx=10)

        aviso_lab = Label(master=self.root, text="     ", padx=10)
        aviso_lab.grid(row=2, column=1)

        boton_g = Button(
            self.root, 
            text="Guardar registro", 
            command=obtener_texto)
        boton_g.grid(row=2,column=0, sticky="w", padx=10, pady=5)
        
        boton_l = Button(
            self.root, 
            text="Ver registro", 
            command=abrir_registro)
        boton_l.grid(row=2, column=2, sticky="e", padx=10, pady=5)
    
