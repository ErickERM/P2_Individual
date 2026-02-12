A=int(input(f"Dame un primer número entero "))
B=int(input(f"Dame un segundo número entero "))
C=int(input(f"Dame un tercer número entero "))
sum=A+B+C
prom=sum/3
if A>=B and A>=C:
    print(f"{A} es el número mayor")
if B>=C and B>=A:
    print(f"{B} es el número mayor")
if C>=A and C>=B:
    print(f"{C} es el número mayor")
print (f"El resultado de la suma es {sum}")
print (f"El resultado del promedio es {prom}")