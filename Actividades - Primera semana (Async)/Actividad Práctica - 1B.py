#Actividad Práctica - 1B - Python Unidad 1
# 1) Escribe un programa que pida el nombre del usuario y muestre por consola 
# un texto: “Hola nombreUsuario”
print("\n 1) Programa que pida el nombre del usuario y muestre por consola 'Hola <usuario>'\n")
nombre_usuario = input("Ingresa tu nombre de usuario: ")
print("Hola",nombre_usuario,sep=" ")

# 2) Escribe un programa que pida un número, luego pida otro número y
# muestre por consola el resultado de sumar dichos números.
print("\n 2) Programa que pida un número, luego pida otro número y muestre por consola el resultado de sumar dichos números\n")
num_1 = int(input("Ingresa un número: "))
num_2 = int(input("Ingresa el siguiente número: "))
resultado = num_1 + num_2

print("Resultado:",resultado,sep=" ")

# 3) Crear un programa que pida el nombre, el apellido, edad del usuario y luego
# muestre por consola los datos ingresados
print("\n 3) Programa que pida el nombre, el apellido, edad del usuario y luego muestre por consola los datos ingresados\n")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ahora ingresa tu apellido: ")
edad = int(input("Por último, ingresa tu edad: "))

print("Hola",nombre,apellido,"tenés",edad,"años.",sep=" ")

# 4) Crear un programa que pida el nombre, número de comisión, asignatura,
# docente y si el usuario estuvo presente, luego que muestre los datos por
# consola con las leyendas pertinentes.
print("\n 4) Programa que pida el nombre, número de comisión, asignatura, docente y si el usuario estuvo presente, luego que muestre los datos por consola\n")
nombre = input("Ingresa tu nombre: ")
num_comision = int(input("Ingresa el número de tu comisión: "))
asignatura = input("Ingresa la asignatura: ")
docente = input("Ingresa el nombre del docente: ")
presente = input("¿El usuario estuvo presente? (Sí/No): ")

print("=== DATOS ===")
print("\nNombre:",nombre,"\nComisión:",num_comision,"\nAsignatura:",asignatura,"\nDocente:",docente,"\nPresente:",presente,sep=" ")

# 5) Crear un programa que pida el lado de un cuadrado y calcule la superficie.
print("\n 5) Programa que pida el lado de un cuadrado y calcule la superficie\n")
lado = int(input("Ingresa la longitud del lado del cuadrado: "))
resultado = lado ** 2

print("La superficie del cuadrado es de",resultado,sep=" ")

# 6) Crear un programa que pida los lados de un rectángulo y calcule la superficie.
print("\n 6) Programa que pida los lados de un rectángulo y calcule la superficie\n")
base = int(input("Ingresa la longitud de la base del rectángulo: "))
altura = int(input("Ingresa la longitud de la altura del rectángulo: "))
resultado = (base * altura)

print("La superficie del rectángulo es de",resultado,sep=" ")

# 7) Crear un programa que calcule la superficie de un triángulo.
print("\n 7) Programa que calcule la superficie de un triángulo\n")
base = int(input("Ingresa la longitud de la base del triángulo: "))
altura = int(input("Ingresa la longitud de la altura del triángulo: "))
resultado = (base * altura) / 2

print("La superficie del triángulo es de",resultado,sep=" ")

# 8) Crear un programa que permite ingresar el nombre de un producto, el precio y que calcule el IVA.
print("\n 8) Programa que permite ingresar el nombre de un producto, el precio y que calcule el IVA.\n")
producto = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio del producto: "))
iva = precio * 1.21

print("El precio final del producto es:",iva,sep=" ")

# 9) Crear un programa que calcule el promedio de un alumno, ingresando su
# nombre apellido, 3 notas, que muestre al final las leyendas pertinentes.
print("\n 9) Programa que calcule el promedio de un alumno, ingresando su nombre apellido, 3 notas, que muestre al final las leyendas pertinentes.\n")
nombre_apellido = input("Ingresa el nombre y apellido del alumno: ")
calificacion_1 = float(input("Ingresa la primera calificación del alumno: "))
calificacion_2 = float(input("Ingresa la segunda calificación del alumno: "))
calificacion_3 = float(input("Ingresa la tercera calificación del alumno: "))
promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

print("La calificación promedio del alumno",nombre_apellido,"es de",promedio,sep=" ")

# 10) Crear un programa en el cual pida al usuario el nombre y la edad y muestre
# por consola la edad que tendra dentro de 10 años.
print("\n 10) Programa el cual pida al usuario el nombre y la edad y muestre por consola la edad que tendra dentro de 10 años.\n")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
futuro = edad + 10

print(nombre,"tendrá",futuro,"años dentro de 10 años.",sep=" ")
