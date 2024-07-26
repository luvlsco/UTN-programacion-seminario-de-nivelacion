# Ejercicios iniciales - Bucles

# 1) Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
numero = 1
while numero <= 10:
    print(numero)
    numero += 1

# 2) Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
numero = 10
while numero >= 1:
    print(numero)
    numero -= 1

# 3) Mostrar la suma de los números desde el 1 hasta el 10.
numero = 1
acumulador = 0
while numero <= 10:
    acumulador = acumulador + numero
    numero += 1
print(f"Suma de los números del 1 al 10: {acumulador}")

# 4) Mostrar la suma de los números pares desde el 1 hasta el 10.
numero = 2
acumulador = 0
while numero <= 10:
    acumulador = acumulador + numero
    numero += 2
print(f"Suma de los números pares del 1 al 10: {acumulador}")

# 5) Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio.
# Mostrar por pantalla.
numeros = 0
acumulador = 0
while numeros < 5:
    numeros_ingresados = int(input("Ingresá un número: "))
    acumulador = acumulador + numeros_ingresados
    numeros += 1
promedio = acumulador / 5
print(f"Suma de los números ingresados: {acumulador}")
print(f"Promedio de los números ingresados: {promedio}")

# 6) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma
# de los números ingresados y el promedio de los mismos.
acumulador = 0
numeros = 0
while True:
    numero = int(input("Ingresá un número: "))
    respuesta = input("¿Ingresar otro número? (si/no): ")
    if respuesta == "no":
        break
    else:
        acumulador = acumulador + numero
        numeros += 1
promedio = acumulador / numeros
print(f"Suma de los números ingresados: {acumulador}")
print(f"Promedio de los números ingresados: {promedio}")

# 7) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los
# números positivos y el producto de los negativos.
acumulador = 0
producto_negativo = 1
contador_negativo = 0
while True:
    numero = int(input("Ingresá un número: "))
    if numero > 0:
        acumulador = acumulador + numero
    elif numero < 0:
        producto_negativo = producto_negativo * numero
        contador_negativo += 1

    respuesta = input("¿Ingresar otro número? (si/no): ")
    if respuesta == "no":
        break

print(f"Suma de los números positivos ingresados: {acumulador}")
if contador_negativo == 0:
    print("No se ingresaron números negativos.")
else:
    print(f"Producto de los números negativos ingresados: {producto_negativo}")

# 8) Ingresar 10 números enteros. Determinar el máximo y el mínimo.
contador = 0
maximo = 0
minimo = 0

while contador < 5:
    numero = int(input("Ingresá un número: "))
    if numero > maximo or contador == 0:
        maximo = numero
    if numero < minimo or contador == 0:
        minimo = numero
   
    contador += 1
print(maximo, minimo)

# 9) Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos
# indeterminados.
clave = "utn"

clave_usuario = input("Ingresá una clave: ")
while clave_usuario != clave:
    clave_usuario = input("Ingresá una clave: ")

print("Clave correcta, ingresando...")

# 10) Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.
clave = "utn"
intentos = 3

while intentos > 0:
    clave_usuario = input("Ingresá una clave: ")
    if clave_usuario == clave:
        print("Clave correcta, ingresando...")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Clave incorrecta, quedan {intentos} intentos.")
        else:
            print("No quedan intentos disponibles.")

# 11) Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
while True:
    nota = int(input("Ingresá una nota: "))
    if nota > 0 and nota <= 10:
        break

print(nota)

# 12) Solicitarle al usuario el ingreso de un color primario. Validar que el mismo sea Rojo, Verde o Azul.
while True:
    color = input("Ingresá el nombre de un color primario: ")
    if color == "Rojo" or color == "Verde" or color == "Azul":
        break
    else:
        print("Color inválido. Por favor, ingresa Rojo, Verde o Azul.")