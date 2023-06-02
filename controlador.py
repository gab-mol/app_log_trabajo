
from tkinter import Tk

import vista
from modelo import __version__, __copyright__


class Controlador:
    '''
    Instancia la clase importada de la vista
    '''
    def __init__(self, main):
        self.root_mainloop=main
        self.objeto_vista=vista.Ventana(self.root_mainloop)

if __name__=="__main__":
    print("")
    print("|||||||||||||| <Aplicación personal para registro de trabajo> ||||||||||||||")
    print("\t Version del programa:", __version__)
    print("\t",__copyright__)
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("")
    main=Tk()
    aplicacion=Controlador(main)
    main.mainloop()