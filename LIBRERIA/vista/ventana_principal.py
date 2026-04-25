import tkinter as tk

class VentanaPrincipal():

    def __init__(self, root):

        self.root = root
        self.root.title ="Sistema de Biblioteca"

        #Titulo principal
        tk.Label(root, text="Registro de Libros", font=("Arial", 14)).pack(pady=10)

        #Sección de datos
        frame_datos = tk.Frame(root)
        frame_datos.pack(pady=5)
        
        #Titulo
        tk.Label(frame_datos, text="Titulo del libro").grid(row = 0, column = 0)
        self.entrada_titulo = tk.Entry(frame_datos)
        self.entrada_titulo.grid(row = 0, column = 1)

        #Autor
        tk.Label(frame_datos, text="Nombre del autor").grid(row=1, column=0)
        self.entrada_autor = tk.Entry(frame_datos)
        self.entrada_autor.grid(row=1, column=1)

        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        #Botones
        self.boton_agregar = tk.Button(frame_botones, text= "Guardar libro")
        self.boton_agregar.grid(row = 0, column = 0, padx=5)

        self.boton_listar_libros = tk.Button(frame_botones, text= "Mostrar libro")
        self.boton_listar_libros.grid(row = 0, column= 1, padx= 5)

        self.boton_eliminar_libros = tk.Button(frame_botones, text= "Eliminar libro")
        self.boton_eliminar_libros.grid(row= 0, column= 2, padx= 5)

        #Lista
        self.lista_libros = tk.Listbox(root, width=50)
        self.lista_libros.pack()

    def limpiarCampos(self):
        self.entrada_titulo.delete(0, tk.END)
        self.entrada_autor.delete(0, tk.END)