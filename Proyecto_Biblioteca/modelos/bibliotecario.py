from modelos.usuario import Usuario
from modelos.biblioteca import Biblioteca

class Bibliotecario(Usuario):
    def __init__(self,nombre,identificador,area):
        super().__init__(nombre,identificador,"Bibliotecario")
        self._area = area

    def obtener_area(self):
        return self._area
        
    def registrar_libro(self,biblioteca,libro):
        biblioteca.agregar_libros(libro)
        print(f"{self.getNombre()} registro el libro {libro.getTitulo()}")