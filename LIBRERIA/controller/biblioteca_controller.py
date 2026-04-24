from modelos.biblioteca import Biblioteca
from modelos.libro import Libro
from tkinter import messagebox

class BibliotecaController:
    def __init__(self, vista):
        self.vista = vista
        self.biblioteca = Biblioteca()

    def agregar_libro(self):
        titulo = self.vista.entrada_titulo.get()
        autor = self.vista.entrada_autor.get()

        if (titulo == "" or autor ==""):
            messagebox.showwarning("Error", "Los campos son obligatorios")
        else:
            libro = Libro(titulo, autor)
            self.biblioteca.agregarLibro(libro)

            messagebox.showinfo("Éxito", " Libro agregado")

    def mostrarLibros(self):
        self.vista.lista_libros.delete(0, "end")

        for libro in self.biblioteca.obtenerListadoDeLibros():
            self.vista.lista_libros.insert("end", str(libro))