import numpy as np

#Leer csv
datosJugadores = np.genfromtxt(
    "jugadores_futbol.csv",
    delimiter=",",
    dtype = None,
    encoding = "utf-8",
    names=True
)

print(datosJugadores)

#Top % de goleadores

jugadoresOrdenados = np.sort(
    datosJugadores,
    order ="Goles"
)

top5 = jugadoresOrdenados[-5:]

print(f"\nTop 5 goleadores: {top5}")

#Promedio de edad

promedioEdad = np.mean(datosJugadores["Edad"])
print(f"\nPromedio Edad: {promedioEdad}")

#10 jugadores más casos

jugadoresCaros = np.sort(
    datosJugadores,
    order ="ValorMercado"
)

topCaros = jugadoresCaros[-10:]

print(f"\nTop 10 caros: {topCaros}")

np.savetxt(
    "JugadoresMasCaros.csv",
    topCaros,
    delimiter="|",
    fmt="%s",
    header="ID,JUGADOR,EQUIPO,POSICIÓN,EDAD,PARTIDOS,GOLES,ASISTENCIA,VALORMERCADO"
)

#Ejercicio:
#Total de goles
sumGoles = np.sum(datosJugadores["Goles"])

print(f"\nSuma de Goles: {sumGoles}")

#Promedio de goles
promedioGol = np.mean(datosJugadores["Goles"])

print(f"\nPromedio Gol: {promedioGol}")

#Máxima cantidad de goles
MaxGoles = np.max(datosJugadores["Goles"])

print(f"\nMax Goles: {MaxGoles}")