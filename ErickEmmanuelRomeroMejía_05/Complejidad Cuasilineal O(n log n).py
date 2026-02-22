print(f"Programa que ordena una lista")
def ordenar_datos(lista):
    lista.sort()
    return lista

datos = [5, 2, 9, 1, 5, 6]
print(f"Lista inicial: {datos}")
print(f"Lista ordenada de forma eficiente: {ordenar_datos(datos)}")