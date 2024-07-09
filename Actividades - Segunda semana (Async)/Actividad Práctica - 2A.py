#Actividad Práctica - 2A - Python Unidad 2
# 1) Crear un programa que pida al usuario un número, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años”
print("\n 1) Programa que pida al usuario un número, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años”\n")

valor = int(input("Ingresá un número: "))
if valor == 18:
    print("Usted tiene 18 años")

# 2) Crear un programa que pida al usuario un número y pueda calcular si es o
# no mayor de edad. Si es mayor de 18 se mostrará el mensaje “MAYOR” caso
# contrario “MENOR”.
print("\n 2) Programa que pida al usuario un número y pueda calcular si es o no mayor de edad. Si es mayor de 18 se mostrará el mensaje “MAYOR” caso contrario “MENOR”.\n")

edad = int(input("Ingresá tu edad: "))
if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")

# 3) Crear un programa que a partir del ingreso de la altura de un
# basquetbolista determinar si es pivot o no. Para serlo el mismo deberá
# medir más de 1.80 metros
print("\n 3) Programa que a partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir más de 1.80 metros\n")

altura = int(input("Ingresá la altura del jugador (en centímetros): "))
if altura >= 180:
    print("El basquetbolista es pivot.")
else:
    print("El basquetbolista no es pivot.")

# 4) Crear un programa que se ingrese la edad del usuario en número y pueda
# calcular si es adolescente (edad entre 13 y 17 años)
print("\n 4) Programa que se ingrese la edad del usuario en número y pueda calcular si es adolescente (edad entre 13 y 17 años)\n")

edad = int(input("Ingresá tu edad: "))
if edad >= 13 and edad <= 17:
    print("Sos un adolescente.")
elif edad <= 12:
    print("Aún no sos adolescente.")
else:
    print("Ya pasaste por la adolescencia.")

# 5) Crear un programa que al ingresar un número puede calcular si es mayor,
# niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
# adolescente (edad entre 13 y 17 años) de edad.
print("\n 5) Programa que al ingresar un número puede calcular si es mayor, niño/a (menor de 10) o pre-adolescente (edad entre 10 y 13 años) adolescente (edad entre 13 y 17 años) de edad.\n")

edad = int(input("Ingresá tu edad: "))
if edad <= 9:
    print("Sos un niño.")
elif edad >= 10 and edad <= 12:
    print("Sos un pre-adolescente.")
elif edad >= 13 and edad <= 17:
    print("Sos un adolescente.")
else:
    print("Ya sos mayor de edad.")

# Agrego los print() con las consignas de cada actividad para que sea más cómodo la lectura al ejecutar el código en la terminal.