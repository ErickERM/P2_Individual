print(f"Ordenamiento de una lista comparando cada número de una lista")
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
numeros = [64, 34, 25, 12, 22]
print(numeros)
print(ordenamiento_burbuja(numeros))