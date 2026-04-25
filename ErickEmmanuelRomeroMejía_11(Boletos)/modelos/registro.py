class Registro:

    def __init__(self, nombre, boletos):
        self.nombre = nombre
        self.boletos = boletos

    def __str__(self):
        return f"{self.nombre} compró {self.boletos} boleto(s)"