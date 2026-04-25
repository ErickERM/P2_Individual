import tkinter as tk

class VentanaPrincipal():

    def __init__(self, root):
        self.root = root
        self.root.title("Compra de boletos")  # ← era = en lugar de ()

        tk.Label(root, text="Compra tus boletos", font=("Arial", 14)).pack(pady=10)

        frame_datos = tk.Frame(root)
        frame_datos.pack(pady=5)

        tk.Label(frame_datos, text="Nombre del usuario").grid(row=0, column=0)
        self.entrada_nombre = tk.Entry(frame_datos)
        self.entrada_nombre.grid(row=0, column=1)

        tk.Label(frame_datos, text="Cantidad de boletos").grid(row=1, column=0)
        self.entrada_boletos = tk.Entry(frame_datos)
        self.entrada_boletos.grid(row=1, column=1)

        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        #self.boton_agregarNombre = tk.Button(frame_botones, text="Registrar nombre")
        #self.boton_agregarNombre.grid(row=0, column=0, padx=5)

        #self.boton_contadorBoletos = tk.Button(frame_botones, text="Guardar cantidad")
        #self.boton_contadorBoletos.grid(row=0, column=1, padx=5)

        self.boton_realizarCompra = tk.Button(frame_botones, text="Comprar")
        self.boton_realizarCompra.grid(row=0, column=2, padx=5)

        self.lista_datos = tk.Listbox(root, width=50)
        self.lista_datos.pack(pady=5)

    def limpiarCampos(self):
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_boletos.delete(0, tk.END)