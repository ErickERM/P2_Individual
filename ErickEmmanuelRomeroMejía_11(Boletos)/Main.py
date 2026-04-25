import tkinter as tk
from controller.boletos_controller import BoletosController
from vista.ventana_principal import VentanaPrincipal

def Main():

    root = tk.Tk()
    vista = VentanaPrincipal(root)
    controller = BoletosController(vista)
    
    #vista.boton_agregarNombre.config(command= controller.registrar_nombre)
    #vista.boton_contadorBoletos.config(command=controller.registrar_boletos)
    vista.boton_realizarCompra.config(command=controller.realizar_compra)

    root.mainloop()

if __name__ == "__main__":
    Main()