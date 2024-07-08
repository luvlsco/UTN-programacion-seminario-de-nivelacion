#Actividad Práctica - 1A - Python Unidad 1
# 1) Escribe un programa muestre por consola “Hola UTN”.
print("Hola UTN")

# 2) Escribe un programa que muestre por consola el resultado de sumar 3 + 5.
print(3 + 5)

# 3) Escribe un programa que muestre por consola el resultado de restar 10-5.
print(10 - 5)

# 4) Escribe un programa que muestre por consola el resultado de restar 10-15
print(10 - 15)

# 5) Escribe un programa que muestre por consola el resultado de multiplicar 4*10
print(4 * 10)

# 6) Escribe un programa que muestre por consola el resultado de dividir 10/2
print(10 / 2)

# 7) Escribe un programa que muestre por consola el resultado de dividir 10/0
print(10 / 0)

# Al ejecutar el ejercicio 7 (línea 15), Python dara el error "ZeroDivisionError: division by zero"
# porque en matemáticas la división por cero no está definida.

# 8) Escribe un programa que muestre por consola el resultado de la siguiente
# operación (10+3) * (6+6), ¿qué sucede si realizas la misma operación pero sin
# los paréntesis?
print((10+3) * (6+6)) #Resultado: 156

# Python sigue las reglas de prioridad en operadores matemáticos, a la primera línea le dará 
# prioridad al paréntesis, pero a la siguiente línea le dará prioridad a la multiplicación, dando así un resultado diferente.
print(10 + 3 * 6 + 6) #Resultado: 34

# 9) Escribe un programa que muestre por consola el resultado de la siguiente operación 10%2
print(10 % 2)

#10) Escribe un programa que muestre por consola la siguiente operación 10%3
print(10 % 3)

#11) Crear un programa (suma, resta, multiplicación, y división),
# se deberá generar dos variables del tipo “variableA” y “variableB”,
# asignarles un valor del tipo número a cada una de ellas.
# El programa deberá mostrar por consola el resultado de realizar las 4
# operaciones aritméticas mencionadas entre ellas.
variableA = 100
variableB = 50
print(variableA + variableB) #Resultado: 150
print(variableA - variableB) #Resultado: 50
print(variableA * variableB) #Resultado: 5000
print(variableA / variableB) #Resultado: 2
