from Modelos.Figura import Figura

class cuadrado(Figura):

    def __init__(self, L):
        #Lado
        self.__l = L

    def getLado(self):
        return self.__l

    def area(self):
        return self.__l ** 2

    def perimetro(self):
        return 4 * self.__l