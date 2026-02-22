print(f"Programa para realizar una suma de los elementos en una lista")
def sumar_todo(lista):
    total = 0
    for numero in lista:
        total += numero
    return total
print(f"El resultado de la lista es {sumar_todo([1, 5, 7, 3, 9])}")
