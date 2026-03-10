from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.gestorPrestamos import GestorPrestamos

libro1= Libro("Peppa Pig","Bucanero", "12345")
usuario1= Usuario("Valeria", "2521578")

gestor = GestorPrestamos()
mensaje = gestor.realizar_prestamo(libro1, usuario1, "2026-03-07")

print(mensaje)

print (libro1.disponibilidad)

gestor.listar_prestamos()