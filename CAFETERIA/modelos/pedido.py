class Pedido:
    def __init__(self, cliente, fecha):
        self.__cliente = cliente
        self.__fecha = fecha
        self.__productos = []  # lista de (Producto, cantidad)

    def agregarProducto(self, producto, cantidad=1):
        self.__productos.append((producto, cantidad))

    def getCliente(self):
        return self.__cliente

    def getFecha(self):
        return self.__fecha

    def calcularTotal(self):
        subtotal = sum(p.getPrecio() * cant for p, cant in self.__productos)
        if self.__cliente.esFrecuente():
            return self.__cliente.aplicarDescuento(subtotal)  # el cliente calcula su propio descuento
        return subtotal

    def __str__(self):
        return f"{self.__cliente} -- Fecha: {self.__fecha} -- Total: ${self.calcularTotal():.2f}"
