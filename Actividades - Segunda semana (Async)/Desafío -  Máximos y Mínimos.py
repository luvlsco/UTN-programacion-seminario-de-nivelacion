# Desafío - Desafío Máximos y Mínimos - Python Unidad 2
contador = 0
max_num = 0
min_num = float('inf')

while(contador < 4):
    num = int(input("Ingresá un número: "))
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
    
    contador = contador + 1

print("Números ingresados:",contador)
print("El valor máximo es:",max_num)
print("El valor mínimo es:",min_num)

# ¿Qué sucede si ingresamos números consecutivos como 1,2,3,4?
# Al ingresar números consecutivos el programa tomara el valor más alto y el más bajo.
# Ejemplo: 1, 2, 3, 4 > min_num == 1, max_num == 4
#
# Y si se ingresan números negativos, el programa seguira funcionando como en el primer ejemplo
# Ejemplo 2: 1, 2, 3, 4 > min_num == -4, máx_num == 0 (Si solo se ingresan números negativos el valor máximo siempre va a ser "0")
