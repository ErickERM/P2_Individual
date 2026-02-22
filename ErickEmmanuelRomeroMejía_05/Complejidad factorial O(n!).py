print (f"Programa que ejecuta el problema del viajero con 3 caminos")
lista = [1, 2, 3]
pasos = 0
for i in lista:
    for j in lista:
        for k in lista:
            if i != j and i != k and j != k:
                pasos += 1
                print(f"Permutación {pasos}: {i, j, k}")
print(f"\nPara {len(lista)} elementos, hubo {pasos} combinaciones")