total = 0
granos = 1
cuadrante = 1

for cuadro in range(64):
    total += granos
    print (f"Cuadrante No.{cuadrante} : {granos}")
    granos *= 2
    cuadrante += 1

print(f"Total de granos: {total}")