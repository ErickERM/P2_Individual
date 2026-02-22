print(f"Programa que dado un número lo divide hasta el minimo posible")
L=int(input(f"Asigna un número "))
pasos = 0
while L > 1:
    L = L // 2
    pasos += 1
    print(f"Para {pasos} el valor es {L}")
print(f"Terminado en {pasos} pasos.")