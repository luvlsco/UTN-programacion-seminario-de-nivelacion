# Desafío - While Reality Show - Python Unidad 2

#==========================================#
# Enunciado:
# De los 3 Jugadores de un Reality Show, se registra:
# Nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos.

# Informar:
# a) Nombre del candidato con más votos
# b) Nombre y edad del candidato con menos votos
# c) El promedio de edades de los candidatos
# d) Total de votos emitidos.
# Todos los datos se ingresan mediante input()
#==========================================#


# Variables:
# <j> Son los jugadores a registrar (van a ser 3)
# <j(número)_n> Nombre del jugador (número: 1, 2 o 3)
# <j(número)_e> Edad del jugador (número: 1, 2 o 3)

# Jugadores
j = 0 
while j < 3:
    j1_n = input("\n\n=== JUGADORES ===\n\nIngresá el nombre del primer jugador: ")
    j1_e = int(input("Ingresá la edad del primer jugador: "))
    while j1_e < 25: # Solo se aceptan jugadores de 25 años o más
        print("\nLos jugadores deben tener 25 años o más.")
        j1_e = int(input("Ingresá la edad del primer jugador: "))
    j = j + 1 # Se agrega un jugador

    j2_n = input("\nIngresá el nombre del segundo jugador: ")
    j2_e = int(input("Ingresá la edad del segundo jugador: "))
    while j2_e < 25:
        print("\nLos jugadores deben tener 25 años o más.")
        j2_e = int(input("Ingresá la edad del segundo jugador: "))
    j = j + 1 # Se agrega otro jugador

    j3_n = input("\nIngresá el nombre del tercer jugador: ")
    j3_e = int(input("Ingresá la edad del tercer jugador: "))
    while j3_e < 25:
        print("\nLos jugadores deben tener 25 años o más.")
        j3_e = int(input("Ingresá la edad del tercer jugador: "))
    j = j + 1 # Se agrega el último jugador

# Variables:
# <e> Son las etapas de votación, una etapa para cada jugador.
# <j(número)_v> Votos para el jugador (número: 1, 2 o 3)

# Etapa de votos
e = 0
while e < 3:
    j1_v = int(input("\n\n=== VOTACIÓN ===\n\nIngresá los votos para el primer jugador: "))
    while j1_v < 0: # Solo votos que no sean negativos
        print("\nLos votos  ingresados no pueden ser negativos.")
        j1_v = int(input("Ingresá los votos para el primer jugador: "))
    e = e + 1 # Una vez dada la votación se suma una etapa y pasa al siguiente jugador

    j2_v = int(input("Ingresá los votos para el segundo jugador: "))
    while j2_v < 0:
        print("\nLos votos ingresados no pueden ser negativos.")
        j2_v = int(input("Ingresá los votos para el segundo jugador: "))
    e = e + 1

    j3_v = int(input("Ingresá los votos para el tercer jugador: "))
    while j3_v < 0:
        print("\nLos votos ingresados no pueden ser negativos.")
        j3_v = int(input("Ingresá los votos para el tercer jugador: "))
    e = e + 1 # Última etapa

# Variables:
# <v> Son los votos totales (se suman los votos de todos los jugadores)
# <p> Es el promedio de edad entre los tres jugadores.
 
v = j1_v + j2_v + j3_v
p = int((j1_e + j2_e + j3_e) / 3)

# Variables:
# <x> Es el nombre del jugador con más votos.
# <a> Es el nombre del jugador con menos votos.
# <b> Es la edad del jugador con menos votos.
x = j1_v
if j2_v > x:
    x = j2_v
if j3_v > x:
    x = j3_v
if x == j1_v:
    x = j1_n
elif x == j2_v:
    x = j2_n
elif x == j3_v:
    x = j3_n

a = j1_v
if j2_v < a:
    a = j2_v
if j3_v < a:
    a = j3_v
if a == j1_v:
    a = j1_n
elif a == j2_v:
    a = j2_n
elif a == j3_v:
    a = j3_n

b = a
if a == j1_n:
    b = j1_e
elif a == j2_n:
    b = j2_e
elif a == j3_n:
    b = j3_e

# Informar:
# a) Nombre del candidato con más votos
# b) Nombre y edad del candidato con menos votos
# c) El promedio de edades de los candidatos
# d) Total de votos emitidos.

print("\n\n=== RESULTADOS ===\n")
print("a) Jugador con más votos:",x)
print("b) Jugador con menos votos:",a,"\n   Edad del jugador con menos votos:",b)
print("c) Promedio de edades de los jugadores:",p)
print("d) Total de votos:",v)
