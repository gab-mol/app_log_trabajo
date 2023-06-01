
from tkinter import Tk

import vista


class Controlador:
    '''
    Instancia la clase importada de la vista
    '''
    def __init__(self, main):
        self.root_mainloop=main
        self.objeto_vista=vista.Ventana(self.root_mainloop)

if __name__=="__main__":
    main=Tk()
    aplicacion=Controlador(main)
    main.mainloop()