# Ejercicios iniciales - Integradores - Bucles

# 1) Permitir que el usuario ingrese todos los números que desee. Los mismos deben estar
# comprendidos entre -10000 y 10000, y deben ser distintos de 0. Determinar:

# A) La suma acumulada de los números negativos.
# B) La suma acumulada de los números positivos.

# C) La cantidad de números negativos ingresados.
# D) El promedio de los números positivos.

# E) El número positivo más grande.
# F) El porcentaje de números negativos ingresados, respecto del total de ingresos.
acumulador_positivo = 0
positivos_ingresados = 0

acumulador_negativo = 0
negativos_ingresados = 0

contador_negativo = 0
positivo_maximo = 0

total_ingresados = 0

while True:
    numero = int(input("Ingresá un número: "))
    
    if numero > 0:
        acumulador_positivo += numero
        positivos_ingresados += 1
        if positivo_maximo == 0 or numero > positivo_maximo:
            positivo_maximo = numero
    elif numero < 0:
        acumulador_negativo += numero
        negativos_ingresados += 1
    
    total_ingresados += 1
    
    respuesta = input("¿Ingresar otro número? (si/no): ")
    if respuesta == "no":
        break

promedio_positivo = acumulador_positivo / positivos_ingresados
porcentaje_negativos = (negativos_ingresados / total_ingresados) * 100

print(f"Suma de los números positivos ingresados: {acumulador_positivo}")
print(f"Promedio de los números positivos ingresados: {promedio_positivo}")
print(f"Suma de los números negativos ingresados: {acumulador_negativo}")
print(f"Cantidad de números negativos ingresados: {negativos_ingresados}")
print(f"El número positivo más grande es: {positivo_maximo}")
print(f"Porcentaje de números negativos respecto del total: {porcentaje_negativos}%")

# 2) De los jugadores participantes en un torneo de ajedrez, se registra:

# ● nombre
# ● la edad (mayor de 10 años)
# ● la cantidad de partidas ganadas (no menor a cero) que obtuvieron en el torneo.

# Informar:
# a. Nombre del jugador con más partidas ganadas.
# b. Nombre y edad del jugador con menos partidas ganadas.
# c. El promedio de edades de los jugadores.
# d. El total de partidas ganadas.
jugadores = 0
jugador_mas_partidas = ""
jugador_menos_partidas = ""
edad_jugador_menos_partidas = 0

total_edades = 0
total_partidas_ganadas = 0

min_partidas = 0
max_partidas = 0
bandera = 1

while True:
    nombre = input("Ingresá el nombre del jugador: ")
    
    edad = int(input("Ingresá la edad del jugador (mayor de 10 años): "))
    while edad <= 10:
        edad = int(input("Edad inválida. Ingresá la edad del jugador (mayor de 10 años): "))
    
    partidas_ganadas = int(input("Ingresá la cantidad de partidas ganadas del jugador (no menor a cero): "))
    while partidas_ganadas < 0:
        partidas_ganadas = int(input("Partidas inválidas. Ingresá la cantidad de partidas ganadas del jugador (no menor a cero): "))

    if partidas_ganadas > max_partidas or bandera == 1:
        max_partidas = partidas_ganadas
        jugador_mas_partidas = nombre

    if partidas_ganadas < min_partidas or bandera == 1:
        min_partidas = partidas_ganadas
        jugador_menos_partidas = nombre
        edad_jugador_menos_partidas = edad
        bandera = 0

    jugadores += 1
    total_edades += edad
    total_partidas_ganadas += partidas_ganadas

    continuar = input("¿Ingresar otro jugador? (si/no): ")
    if continuar == "no":
        break

promedio_edades = total_edades / jugadores
print(f"Nombre del jugador con más partidas ganadas: {jugador_mas_partidas}")

print(f"Nombre del jugador con menos partidas ganadas: {jugador_menos_partidas}")
print(f"Edad del jugador con menos partidas ganadas: {edad_jugador_menos_partidas}")

print(f"Promedio de edades de los jugadores: {promedio_edades}")
print(f"Total de partidas ganadas: {total_partidas_ganadas}")

# 3) Validaciones.
# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar
# la carga y validación de datos para luego mostrarlos por pantalla.
# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
apellido = input("Ingresá tu apellido: ")

edad = int(input("Ingresá tu edad: "))
while edad < 18 or edad > 90:
    edad = int(input("Edad inválida. Ingresá tu edad: "))

estado = input("Ingresá tu estado civil (Soltero, Casado, Divorciado, Viudo): ")
while estado != "soltero" and estado != "casado" and estado != "divorciado" and estado != "viudo":
    estado = input("Estado inválido. Ingresá tu estado civil (Soltero, Casado, Divorciado, Viudo): ")

legajo = int(input("Ingresá tu número de legajo: "))
while legajo < 1000 or legajo > 9999:
    legajo = int(input("Número de legajo inválido. Ingresá tu número de legajo: "))