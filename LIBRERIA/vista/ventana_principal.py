import tkinter as tk

class VentanaPrincipal():

    def __init__(self, root):

        self.root = root
        self.root.title ="Sistema de Biblioteca"
        
        #Titulo
        tk.Label(root, text="Titulo del libro").pack()
        self.entrada_titulo = tk.Entry(root)
        self.entrada_titulo.pack()

        #Autor
        tk.Label(root, text="Nombre del autor").pack()
        self.entrada_autor = tk.Entry(root)
        self.entrada_autor.pack()

        #Botones
        self.boton_agregar = tk.Button(root, text= "Agregar libro")
        self.boton_agregar.pack()

        self.boton_listar_libros = tk.Button(root, text= "Listar libro")
        self.boton_listar_libros.pack()

        #Lista
        self.lista_libros = tk.Listbox(root, width=50)
        self.lista_libros.pack()