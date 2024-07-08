# A) Ingresár tres precios de productos y mostrar la suma de los mismos.
producto_1 = int(input("Ingresá el precio del primer producto: "))
producto_2 = int(input("Ingresá el precio del segundo producto: "))
producto_3 = int(input("Ingresá el precio del tercer producto: "))

total = producto_1 + producto_2 + producto_3

print("\n=== PRECIOS ===","\nPrecio del primer producto:",producto_1,"\nPrecio del segundo producto:",producto_2,"\nPrecio del tercer producto:",producto_3,"\n\n=== TOTAL ===","\nSuma de los precios:",total,"\n",sep=" ")

# B) Ingresár tres precios de productos y mostrar el promedio de los mismos.
producto_1 = int(input("Ingresá el precio del primer producto: "))
producto_2 = int(input("Ingresá el precio del segundo producto: "))
producto_3 = int(input("Ingresá el precio del tercer producto: "))

promedio = (producto_1 + producto_2 + producto_3) / 3

print("\n=== PRECIOS ===","\nPrecio del primer producto:",producto_1,"\nPrecio del segundo producto:",producto_2,"\nPrecio del tercer producto:",producto_3,"\n\n=== PROMEDIO ===","\nPromedio de los precios:",promedio,"\n",sep=" ")

# C) ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
producto_1 = int(input("Ingresá el precio del primer producto: "))
producto_2 = int(input("Ingresá el precio del segundo producto: "))
producto_3 = int(input("Ingresá el precio del tercer producto: "))

iva = (producto_1 + producto_2 + producto_3) * 1.21

print("\n=== PRECIOS ===","\nPrecio del primer producto:",producto_1,"\nPrecio del segundo producto:",producto_2,"\nPrecio del tercer producto:",producto_3,"\n\n=== TOTAL ===","\nSuma de los precios (+21% IVA):",total,"\n",sep=" ")
