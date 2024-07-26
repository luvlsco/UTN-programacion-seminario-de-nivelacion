# Ejercicios iniciales - Condicionales

# 1) A partir del ingreso de una edad, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años”.
edad = int(input("Ingresá tu edad: "))
if edad == 18:
    print("Usted tiene 18 años.")

# 2) A partir del ingreso de una edad, determinar si la persona es mayor de edad. Si es mayor o igual que 18
# se mostrará el mensaje “UD ES MAYOR DE EDAD”.
edad = int(input("Ingresá tu edad: "))
if edad >= 18:
    print("Usted es mayor de edad.")

# 3) A partir del ingreso de una edad, determinar si la persona es mayor de edad o no. Si es mayor de 18 se
# mostrará el mensaje “UD ES MAYOR DE EDAD” caso contrario “UD ES MENOR DE EDAD”.
edad = int(input("Ingresá tu edad: "))
if edad >= 18:
    print("Usted es mayor de edad.")
elif edad < 18:
    print("Usted es menor de edad.")

# 4) A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo
# deberá medir más de 1.80 metros.
altura = int(input("Ingresá la altura del basquetbolista (En centímetros): "))
if altura >= 180:
    print("El jugador es pivot.")
elif altura < 180:
    print("El jugador no es pivot.")

# 5) Pedirle al usuario su edad, determinar si el usuario es adolescente.
edad = int(input("Ingresá tu edad: "))
if edad >= 13 and edad <= 17:
    print("Sos un adolescente.")

# 6) Pedirle al usuario su edad, determinar si el usuario NO es adolescente.
edad = int(input("Ingresá tu edad: "))
if edad <= 13 and edad >= 17:
    print("Ya pasaste por la adolescencia.")

# 7) Pedirle al usuario su edad, determinar si es mayor (18 años o más), niño/a (menor de 10), pre-
# adolescente (edad entre 10 y 13 años inclusive) o adolescente (edad entre 13 y 17 años).
edad = int(input("Ingresá tu edad: "))
if edad <= 9:
    print("Sos un niño.")
elif edad >= 10 and edad <= 12:
    print("Sos un pre-adolescente.")
elif edad >= 13 and edad <= 17:
    print("Sos un adolescente.")
else:
    print("Ya sos mayor de edad.")

# 8) A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá
# determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# ● Menos de 160 cm: Base
# ● Entre 160 cm y 179 cm: Escolta
# ● Entre 180 cm y 199 cm: Alero
# ● 200 cm o más: Ala-Pívot o Pívot
altura = int(input("Ingresá la altura del basquetbolista (En centímetros): "))
if altura <= 159:
    print("El basquetbolista jugará de base.")
elif altura >= 160 and altura <= 179:
    print("El basquetbolista jugará de escolta.")
elif altura >= 180 and altura <= 199:
    print("El basquetbolista jugará de alero.")
else:
    print("El basquetbolista jugará de ala-pivot.")

# 9) Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde
# los dieciocho (18) años están habilitados a votar. A partir del ingreso de la edad del usuario y el estado
# si es naturalizado o nativo), se deberá informar si es o no posible que la persona concurra a votar en
# base a la información suministrada.
edad = int(input("Ingresá tu edad: "))
estado = input("Ingresá tu estado (nativo/naturalizado): ")
if (estado == "nativo" and edad >= 16) or (estado == "naturalizado" and edad >= 18):
    print("Usted puede ir a votar.")
else:
    print("Usted no puede ir a votar.")

# 10) Ingresar el sueldo, estado civil (casado o soltero) y cantidad de hijos de un empleado. Determinar si el
# empleado debe o no pagar el impuesto a las ganancias. El mismo no se pagará si el empleado es
# casado con hijos y sus ingresos son menores a $2.200.000.
sueldo = int(input("Ingresá tu sueldo: "))
estado = input("Ingresá tu estado civil (casado/soltero): ")
hijos = int(input("Ingresá cuantos hijos tenés: "))
if (estado == "casado" and hijos >= 1 and sueldo <= 2200000):
    print("Usted no tiene que pagar impuesto a las ganancias.")
else:
    print("Usted tiene que pagar impuesto a las ganancias.")

# 11) Mostrar un número aleatorio entre el 1 y el 10 inclusive.
from random import randint
numero_aleatorio = randint(1, 10)
print(numero_aleatorio)

# 12) Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# ● 6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
# ● 4 y 5 ---> Aprobado, la nota es ...
# ● 1, 2 y 3 ---> Desaprobado, la nota es ...
from random import randint
nota = randint(1, 10)
print(nota)
if nota >= 6 and nota <= 10:
    print(f"Promoción directa, la nota es: {nota}")
elif nota >= 4 and nota <= 5:
    print(f"Aprobado, la nota es: {nota}")
elif nota >= 1 and nota <= 3:
    print(f"Desaprobado, la nota es: {nota}")