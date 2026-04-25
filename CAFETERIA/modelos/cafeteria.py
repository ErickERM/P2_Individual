class Cafeteria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.pedidos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def listar_productos(self):
        print(f"\nMenú de {self.nombre} ")
        for producto in self.productos:
            print(f"  {producto}")
        print("\n")

    def listar_pedidos(self):
        print(f"\nPedidos de {self.nombre}")
        for pedido in self.pedidos:
            print(f"  {pedido}")
        print("\n")
