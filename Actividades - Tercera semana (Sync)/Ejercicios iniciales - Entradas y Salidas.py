# Ejercicios iniciales - Entradas y Salidas

# 1) Escribir un programa que muestre por pantalla “bienvenidos a la utn”.
print("bienvenidos a la utn")

# 2) Escribir un programa que pregunte el nombre del usuario en la consola(usando input) y después de
# que el usuario lo introduzca muestre por pantalla la cadena ”<nombre>”, donde 
# <nombre> es el nombre que el usuario haya introducido.
nombre = input("Ingresá tu nombre: ")
print(nombre)

# 3) Se deberá obtener tanto el nombre como la edad usando input y luego mostrar los datos concatenados con print.
# Ej: "Usted se llama José y su edad es 66 años"
nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))
print("Usted se llama",nombre,"y su edad es",edad,"años.")

# 4) Tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y operador_b), 
# transformarlos en números enteros, realizar la operación suma y luego mostrar el resultado de la misma utilizando print.
# Ej: "El resultado de la suma es: 755"
operador_a = int(input("Ingresá un número: "))
operador_b = int(input("Ingresá otro número: "))
print("El resultado de la suma es:",operador_a + operador_b)

# 5) Se deberá crear un programa que muestre cada operación (suma, resta, multiplicación, y división), tenemos
# que obtener los valores (por input) que el usuario nos ingrese (operador_a y operador_b),
# transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado de la misma utilizando print.
# Ej: "El resultado de la …… es: 755"
operador_a = int(input("Ingresá un número: "))
operador_b = int(input("Ingresá otro número: "))
print("El resultado de la suma es:",operador_a + operador_b)
print("El resultado de la resta es:",operador_a - operador_b)
print("El resultado de la multiplicación es:",operador_a * operador_b)
print("El resultado de la división es:",operador_a / operador_b)

# 6) Tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y operador_b),
# transformarlos en números enteros, realizar la operación que nos permita obtener el
# resto de una división y luego mostrar el resultado de la misma utilizando print.
# Ej: "El resto de dividir 7 por 2 es: 1"
operador_a = int(input("Ingresá un número: "))
operador_b = int(input("Ingresá otro número: "))
resto = operador_a % operador_b
print(f"El resto de dividir {operador_a} por {operador_b} es: {resto}")

# 7) Tenemos que obtener el sueldo (por input) que el usuario nos ingrese ,
# transformarlo en número entero y mostrar el importe de sueldo actualizado
# con el incremento del 15% utilizando print
sueldo = int(input("Ingresá tu sueldo: "))
importe = sueldo * 1.15
print(f"Importe de sueldo actualizado: {importe}")

# 8) Tenemos que obtener los valores (por input) que el usuario nos ingrese (sueldo e incremento),
# transformarlos en números enteros y mostrar el importe de sueldo actualizado con
# el incremento porcentual utilizando print.
sueldo = int(input("Ingresá tu sueldo: "))
incremento = int(input("Ingresá el porcentaje del incremento: "))
resultado = sueldo * (1 + (incremento / 100))
print(f"Importe de sueldo actualizado: {resultado}")

# 9) Tenemos que crear un programa que deberá obtener el importe que ingrese el usuario
# por consola(input), transformar en número y mostrar el importe actualizado 
# con un descuento del 20% utilizando print.
importe = int(input("Ingresá tu importe: "))
descuento = sueldo * 0.80
print(f"Importe actualizado: {descuento}")

# 10) Tenemos que crear un programa que deberán obtener el importe y el descuento
# que ingrese el usuario por consola, transformarlos en números y mostrar el
# importe actualizado con el descuento utilizando print.
importe = int(input("Ingresá tu importe: "))
descuento = int(input("Ingresá el porcentaje del descuento: "))
resultado = importe * (1 - (descuento / 100))
print(f"Importe actualizado: {resultado}")