class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidad = True

    def prestar(self):
        if (self.disponibilidad):
            self.disponibilidad = False
            return True
        return False

    def devolver(self):
        self.disponibilidad = True