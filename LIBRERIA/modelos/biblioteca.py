class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def obtenerListadoDeLibros(self):
        return self.libros
    
    def eliminarLibro(self, libro):
        self.libros.remove(libro)