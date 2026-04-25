from modelos.cliente import Cliente
from modelos.cliente_frecuente import ClienteFrecuente
from modelos.producto import Producto
from modelos.pedido import Pedido
from modelos.cafeteria import Cafeteria

cafeteria1 = Cafeteria("Café del Centro")

producto1 = Producto("Café Americano", 35.00, "Bebidas")
producto2 = Producto("Capuchino", 55.00, "Bebidas")
producto3 = Producto("Croissant", 45.00, "Panadería")
producto4 = Producto("Sándwich Club", 90.00, "Alimentos")

cafeteria1.agregar_producto(Producto("Café Americano", 35.00, "Bebidas"))
cafeteria1.agregar_producto(Producto("Capuchino", 55.00, "Bebidas"))
cafeteria1.agregar_producto(Producto("Croissant", 45.00, "Panadería"))
cafeteria1.agregar_producto(Producto("Sándwich Club", 90.00, "Alimentos"))

cafeteria1.listar_productos()

cliente1 = Cliente("Erick Mejía", "14991")
clienteFrecuente1 = ClienteFrecuente("Aixia Garcia", "12345")

pedido1 = Pedido(cliente1, "24-04-2026")
pedido1.agregarProducto(cafeteria1.productos[1], 1)
pedido1.agregarProducto(cafeteria1.productos[2], 2) 

pedido2 = Pedido(clienteFrecuente1, "24-04-2026")
pedido2.agregarProducto(cafeteria1.productos[0], 2)
pedido2.agregarProducto(cafeteria1.productos[3], 1) 

cafeteria1.agregar_pedido(pedido1)
cafeteria1.agregar_pedido(pedido2)

cafeteria1.listar_pedidos()
