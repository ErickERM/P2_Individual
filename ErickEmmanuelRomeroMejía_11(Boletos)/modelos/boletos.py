class Boletos:

    def __init__(self):
        self.registros = []

    def agregarRegistro(self, registro):
        self.registros.append(registro)

    def obtenerRegistros(self):
        return self.registros
    