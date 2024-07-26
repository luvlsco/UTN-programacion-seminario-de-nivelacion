# Ejercicios iniciales - Integradores - Entradas y Salidas

# 1) Agencia de viaje:
# Para saber el costo de un viaje necesitamos el siguiente algoritmo, sabiendo
# que el precio por kilo de pasajero es 1000 pesos. Se ingresan todos los datos
# por PROMPT los datos a solicitar de dos personas son: nombre, edad y peso

# Se pide  armar el siguiente mensaje:

# "Hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente, sumados da 140 kilos,
# el promedio de edad es 33 y su viaje vale 140000 pesos "
pasajero_1 = input("Ingresá el nombre del primer pasajero: ")
edad_1 = int(input("Ingresá la edad del primer pasajero: "))
peso_1 = int(input("Ingresá el peso del primer pasajero: "))


pasajero_2 = input("Ingresá el nombre del segundo pasajero: ")
edad_2 = int(input("Ingresá la edad del segundo pasajero: "))
peso_2 = int(input("Ingresá el peso del segundo pasajero: "))

peso_total = peso_1 + peso_2
precio = peso_total * 1000
edad_promedio = int(edad_1 + edad_2) / 2

print(f"Hola {pasajero_1} y {pasajero_2}, sus pesos son {peso_1} y {peso_2} kilos respectivamente, sumados da {peso_total} kilos")
print(f"el promedio de edad es {edad_promedio} y su viaje vale {precio} pesos.")

# 2) Empresa de Camiones:

# Para el departamento de logística:
# A) Es necesario saber la cantidad de camiones que harían falta para transportar los materiales que se utilizarán
# para la construcción de un edificio. Para ello, se ingresa la cantidad de toneladas necesarias
# de materiales a transportar. El programa deberá informar la cantidad de camiones, sabiendo que cada 
# uno de ellos puede transportar por viaje 3500kg.
cantidad_materiales = int(input("Ingresá la cantidad de toneladas de material a transportar: "))
capacidad_camiones = 3.5 #3500kg = 3.5t
camiones = (cantidad_materiales / capacidad_camiones)
camiones_enteros = int(camiones)
if camiones > camiones_enteros:
    camiones = camiones_enteros + 1
print(f"Se necesitaran {camiones} camiones, para transportar {cantidad_materiales} toneladas de material.")

# B) A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones
# para llegar al destino de la obra, necesitamos que el programa informe cual
# es el tiempo (en horas) que tardará cada uno de los camiones, si sabemos que cada camión puede 
# ir a una velocidad máxima y constante de 90 km/h.
kilometros = int(input("Ingresá los kilómetros a recorrer: "))
velocidad_camiones = 90
horas = int(kilometros / velocidad_camiones)
print(f"Los camiones tardaran en llegar al destino alrededor de {horas} horas.")