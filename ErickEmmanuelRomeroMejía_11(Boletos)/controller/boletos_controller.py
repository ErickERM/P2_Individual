from modelos.boletos import Boletos
from modelos.registro import Registro
from tkinter import messagebox

class BoletosController:
    def __init__(self, vista):
        self.vista = vista
        self.boletos = Boletos()
        self.nombre_temp = ""

    #def registrar_nombre(self):
        #nombre = self.vista.entrada_nombre.get()

        #if nombre == "":
            #messagebox.showwarning("Error", "El nombre es obligatorio")
        #else:
            #self.nombre_temp = nombre
            #messagebox.showinfo("Éxito", f"Nombre '{nombre}' registrado")

    #def registrar_boletos(self):
        #cantidad = self.vista.entrada_boletos.get()

        #if cantidad == "":
            #messagebox.showwarning("Error", "Ingresa la cantidad de boletos")
        #elif not cantidad.isdigit():
            #messagebox.showwarning("Error", "La cantidad debe ser un número entero")
        #else:
            #messagebox.showinfo("Éxito", f"Cantidad '{cantidad}' guardada")

    def realizar_compra(self):
        nombre = self.vista.entrada_nombre.get()
        cantidad = self.vista.entrada_boletos.get()

        cantidad = self.vista.entrada_boletos.get()
        cantidad = self.vista.entrada_boletos.get()

        if nombre == "" or cantidad == "":
            messagebox.showwarning("Error", "Completa nombre y cantidad antes de comprar")
            return

        if not cantidad.isdigit():
            messagebox.showwarning("Error", "La cantidad debe ser un número entero")
            return

        registro = Registro(nombre, cantidad)
        self.boletos.agregarRegistro(registro)

        self.vista.lista_datos.delete(0, "end")
        for r in self.boletos.obtenerRegistros():
            self.vista.lista_datos.insert("end", str(r))

        messagebox.showinfo("Compra realizada", str(registro))
        self.vista.limpiarCampos()