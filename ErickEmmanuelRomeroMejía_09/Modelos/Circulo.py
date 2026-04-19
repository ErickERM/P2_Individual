import math
from Modelos.Figura import Figura

class circulo(Figura):

    def __init__(self, r):
        #Radio
        self.__r = r

    def getRadio(self):
        return self.__r

    def area(self):
        return math.pi * self.__r ** 2

    def perimetro(self):
        return 2 * math.pi * self.__r