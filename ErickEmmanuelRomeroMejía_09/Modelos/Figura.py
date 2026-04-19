from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}\n Área: {self.area():.2f}\n Perímetro: {self.perimetro():.2f}"