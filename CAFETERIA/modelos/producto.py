class Producto:
    def __init__(self, nombre, precio, categoria):
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria

    def getNombre(self):
        return self.__nombre

    def getPrecio(self):
        return self.__precio

    def getCategoria(self):
        return self.__categoria

    def __str__(self):
        return f"{self.__nombre} - ${self.__precio:.2f} [{self.__categoria}]"
