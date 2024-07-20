#Actividad Práctica - 1B - Python Unidad 1
# 1) Escribe un programa que pida el nombre del usuario y muestre por consola 
# un texto: “Hola nombreUsuario”
nombre_usuario = input("Ingresá tu nombre de usuario: ")
print("Hola",nombre_usuario,sep=" ")

# 2) Escribe un programa que pida un número, luego pida otro número y
# muestre por consola el resultado de sumar dichos números.
num_1 = int(input("Ingresá un número: "))
num_2 = int(input("Ingresá el siguiente número: "))
resultado = num_1 + num_2

print("Resultado:",resultado,sep=" ")

# 3) Crear un programa que pida el nombre, el apellido, edad del usuario y luego
# muestre por consola los datos ingresados
nombre = input("Ingresá tu nombre: ")
apellido = input("Ahora ingresa tu apellido: ")
edad = int(input("Por último, ingresa tu edad: "))

print("Hola",nombre,apellido,"tenés",edad,"años.",sep=" ")

# 4) Crear un programa que pida el nombre, número de comisión, asignatura,
# docente y si el usuario estuvo presente, luego que muestre los datos por
# consola con las leyendas pertinentes.
nombre = input("Ingresá tu nombre: ")
num_comision = int(input("Ingresá el número de tu comisión: "))
asignatura = input("Ingresá la asignatura: ")
docente = input("Ingresá el nombre del docente: ")
presente = input("¿El usuario estuvo presente? (Sí/No): ")

print("=== DATOS ===")
print("\nNombre:",nombre,"\nComisión:",num_comision,"\nAsignatura:",asignatura,"\nDocente:",docente,"\nPresente:",presente,sep=" ")

# 5) Crear un programa que pida el lado de un cuadrado y calcule la superficie.
lado = int(input("Ingresá la longitud del lado del cuadrado: "))
resultado = lado ** 2

print("La superficie del cuadrado es de",resultado,sep=" ")

# 6) Crear un programa que pida los lados de un rectángulo y calcule la superficie.
base = int(input("Ingresá la longitud de la base del rectángulo: "))
altura = int(input("Ingresá la longitud de la altura del rectángulo: "))
resultado = (base * altura)

print("La superficie del rectángulo es de",resultado,sep=" ")

# 7) Crear un programa que calcule la superficie de un triángulo.
base = int(input("Ingresá la longitud de la base del triángulo: "))
altura = int(input("Ingresá la longitud de la altura del triángulo: "))
resultado = (base * altura) / 2

print("La superficie del triángulo es de",resultado,sep=" ")

# 8) Crear un programa que permite ingresar el nombre de un producto, el precio y que calcule el IVA.
producto = input("Ingresá el nombre del producto: ")
precio = float(input("Ingresá el precio del producto: "))
iva = precio * 1.21

print("El precio final del producto es:",iva,sep=" ")

# 9) Crear un programa que calcule el promedio de un alumno, ingresando su
# nombre apellido, 3 notas, que muestre al final las leyendas pertinentes.
nombre_apellido = input("Ingresá el nombre y apellido del alumno: ")
calificacion_1 = float(input("Ingresá la primera calificación del alumno: "))
calificacion_2 = float(input("Ingresá la segunda calificación del alumno: "))
calificacion_3 = float(input("Ingresá la tercera calificación del alumno: "))
promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

print("La calificación promedio del alumno",nombre_apellido,"es de",promedio,sep=" ")

# 10) Crear un programa en el cual pida al usuario el nombre y la edad y muestre
# por consola la edad que tendra dentro de 10 años.
nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))
futuro = edad + 10

print(nombre,"tendrá",futuro,"años dentro de 10 años.",sep=" ")
