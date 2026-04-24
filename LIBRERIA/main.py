import tkinter as tk
from vista.ventana_principal import VentanaPrincipal
from controller.biblioteca_controller import BibliotecaController

def main():

    root = tk.Tk()
    vista = VentanaPrincipal(root)
    controller = BibliotecaController(vista)
    
    vista.boton_agregar.config(command= controller.agregar_libro)
    vista.boton_listar_libros.config(command=controller.mostrarLibros)

    root.mainloop()

if __name__ == "__main__":
    main()