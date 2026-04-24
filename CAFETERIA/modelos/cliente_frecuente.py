from modelos.cliente import Cliente

class ClienteFrecuente(Cliente):
    def __init__(self, nombre, identificador, descuento=0.10):
        super().__init__(nombre, identificador)
        self.__descuento = descuento

    def getDescuento(self):
        return self.__descuento

    def esFrecuente(self):
        return True
    
    def aplicarDescuento(self, subtotal):
        return subtotal * (1 - self.__descuento)

    def __str__(self):
        return f"{super().__str__()} | Descuento: {self.__descuento * 100:.0f}%"
