import numpy as np
print("\nAlgoritmo de calculo de duracion de luz verde en semaforos para mejorar el flujo vehicular en intersecciones.")
# Sustituto de input dada en autos que se encuentran en cada via  perpendicular cercana a la interseccion por lapso de tiempo (sea segundos, minutos o cualquier fraccion deseada).
# Debi recurrir a datos simbolicos debido a la no disponibilidad de sensores.
datosS1 = np.array([1, 2, 3, 40, 41, 42, 42, 50, 60, 70])
datosS2 = np.array([70, 60, 50, 43, 42, 41, 40, 3, 2, 1])
# Tiempo maximo y minimo de duracion de cualquiera de los dos semaforos de la interseccion.
maxtime = 90
mintime = 28
# Tolerancia ajustable para la precision de los lapsos de cambio, entre mas pequeña, mas tiempo se pierde en el cambio de flujo de la interseccion.
tolerancia = 10
# Promedio entre el tiempo minimo y maximo de duracion de luz verde de ambos semaforos.
promedio = int((maxtime+mintime)/2)
# Se muestra en pantalla el promedio dado, previamente estandarizado a entero, (Solo para diagnostico).
print("\nDuracion de luz verde en ambos semaforos a igual flujo: "+str(promedio))
# Aqui se observan los tiempos estimados de cada semaforo para optimizar el flujo de automoviles(Tamaño fijo 10 por limitados datos, se coloca un while infinito para garantizar su ejecucion ininterrumpida en produccion).
for cont in range(0, 10):
    # El numero de la iteraccion contada en input del sensor (Solo para diagnostico).
    print("\nInput de Sensores N° "+str(cont+1)+"\n")
    if datosS1[cont] > datosS2[cont]:
        # Si el Flujo es mucho mayor en el semaforo 1 que en el semaforo 2.
        temp = datosS1[cont]/datosS2[cont]
        if temp > 2:
            semaforo1 = maxtime
            semaforo2 = mintime
            print("Tiempo semaforo 1: "+str(semaforo1))
            print("Tiempo semaforo 2: "+str(semaforo2))
        else:
            # Ajuste fino del tiempo en base al espacio entre flujos iguales y flujos extremos.
            semaforo1 = int(temp*promedio)
            semaforo2 = int(promedio/temp)
            if semaforo1 > maxtime:
                semaforo1 -= tolerancia
            elif semaforo2 < mintime:
                semaforo2 += tolerancia

            print("Tiempo semaforo 1: "+str(semaforo1))
            print("Tiempo semaforo 2: "+str(semaforo2))
    else:
        # Si el Flujo es mucho mayor en el semaforo 2 que en el semaforo 1.
        temp = datosS2[cont]/datosS1[cont]
        if temp > 2:
            semaforo1 = mintime
            semaforo2 = maxtime
            print("Tiempo semaforo 1: "+str(semaforo1))
            print("Tiempo semaforo 2: "+str(semaforo2))
        else:
            # Ajuste fino del tiempo en base al espacio entre flujos iguales y flujos extremos.
            semaforo2 = int(temp*promedio)
            semaforo1 = int(promedio/temp)
            if semaforo2 > maxtime:
                semaforo2 -= tolerancia
            elif semaforo1 < mintime:
                semaforo1 += tolerancia
            semaforo1 = int(temp*promedio)
            semaforo2 = int(temp*promedio)
            print("Tiempo semaforo 1: "+str(semaforo1))
            print("Tiempo semaforo 2: "+str(semaforo2))
