#Desafío - Número secreto - Python Unidad 2
numero_secreto = int( (3) ** 6 + ((8)**2 + 82) )
print(
"""
+================================+
|    ¡Bienvenido a mi juego!    |
|   Introduce un número entero  |
|    y adivina qué número he    |
|        elegido para ti.       |
|  ¿Cuál es el número secreto?  |
+================================+
""")
numero = int(input("¡Adelante! ¡Ingresá un número!: "))
intentos = 1
while numero != numero_secreto:
    if numero < 0:
        print("\n=== INTENTO:",intentos,"===")
        print("¡El número secreto no es negativo!")
    elif numero >= 1000:
        print("\n=== INTENTO:",intentos,"===")
        print("¡El número secreto no es mayor a mil!")
    elif numero > numero_secreto:
        print("\n=== INTENTO:",intentos,"===")
        print("¡Te pasaste del número secreto! ¡Vuelve a intentarlo!")
    elif numero < numero_secreto:
        print("\n=== INTENTO:",intentos,"===")
        print("¡Estás lejos del número secreto! ¡Vuelve a intentarlo!")
    intentos = intentos + 1
    print("...")
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!\n\n")
    numero = int(input("¡Adelante! ¡Ingresá un número!: "))
print("\n=== COMPLETADO EN",intentos,"INTENTOS ===","\n¡Felicitaciones! ¡Te libraste de mi bucle!",sep=" ")
