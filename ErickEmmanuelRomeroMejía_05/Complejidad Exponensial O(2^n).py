print(F"Programa que ejecuta la secuencia de Fibonacci hasta 1000")
def generar_fibonacci(limite):
    secuencia = [0, 1]
    while len(secuencia) < limite:
        siguiente_valor = secuencia[-1] + secuencia[-2]
        print (f"Valor actual: {siguiente_valor}")
        secuencia.append(siguiente_valor)
    return secuencia

n = 1000
resultado = generar_fibonacci(n)
print(f"La secuencia es: {resultado}")
