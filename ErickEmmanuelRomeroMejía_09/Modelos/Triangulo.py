from Modelos.Figura import Figura

class triangulo(Figura):

    def __init__(self, B, H, L1, L2, L3):
        #Base y altura
        self.__B   = B
        self.__H = H
        #Lados del triangulo
        self.__L1  = L1
        self.__L2  = L2
        self.__L3  = L3

    def area(self):
        return (self.__B * self.__H) / 2

    def perimetro(self):
        return self.__L1 + self.__L2 + self.__L3