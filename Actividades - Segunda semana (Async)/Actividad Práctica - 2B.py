#Actividad Práctica - 2B - Python Unidad 2
# 1) Crear un programa que pueda sumar los números pares comprendidos
# entre el 1 y el 10.
num = 1
num_par = 0

while num <= 10:
    print(num)
    num = num + 1
    if num % 2 == 0:
        num_par = num_par + 1
print("Números pares:",num_par)

# 2) Crear un programa que solicite al usuario que ingrese una contraseña
# mediante prompt.
# Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no
# coincidir, volver a solicitarla hasta que coincidan.
clave = input("Ingresá la contraseña: ")
while clave != "utn750":
    print("Contraseña incorrecta. Acceso denegado.")
    clave = input("Ingresá la contraseña: ")
print("Contraseña correcta. Accediendo...")

# 3) Crear un programa que solicite al usuario que ingrese un número.
# Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no
# coincidir con el rango, volverlo a solicitar hasta que la condición se cumpla.
num = int(input("Ingresá un número entre 0 y 9: "))
while num < 0 or num > 10:
    print("Número inválido. El número ingresado debe estar entre 0 y 9.")
    num = int(input("Ingresá un número entre 0 y 9: "))
print("Número válido.")

# 4) Crear un programa que solicite al usuario que ingrese una letra. Se deberá
# validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas).
# En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que
# la condición se cumpla
letra = input("Ingresá una letra ('U', 'T' o 'N'): ")
while letra != "U" and letra != "T" and letra != "N":
    print("Letra inválida. Por favor ingresa una de las letras entre paréntesis: ")
    letra = input("Ingresá una letra: ")
print("Letra válida.")

# 5) Crear un programa que solicite 5 números mediante prompt. Calcular la
#suma acumulada y el promedio de los números ingresados.
total = 0
num_1 = float(input("Ingresá el primer número: "))
total = num_1
print(num_1,"+...")
num_2 = float(input("Ingresá el segundo número: "))
total = num_1 + num_2
print(num_1,"+",num_2,"+...")
num_3 = float(input("Ingresá el tercer número: "))
total = num_1 + num_2 + num_3
print(num_1,"+",num_2,"+",num_3,"+...")
num_4 = float(input("Ingresá el cuarto número: "))
total = num_1 + num_2 + num_3 + num_4
print(num_1,"+",num_2,"+",num_3,"+",num_4,"+...")
num_5 = float(input("Ingresá el quinto número: "))
total = num_1 + num_2 + num_3 + num_4 + num_5
promedio = total / 5
print(num_1,"+",num_2,"+",num_3,"+",num_4,"+",num_5)

print("\n=== TOTAL ===","\nSuma de los números:",total,"\n\n=== PROMEDIO ===","\nPromedio de los precios:",promedio,"\n")
