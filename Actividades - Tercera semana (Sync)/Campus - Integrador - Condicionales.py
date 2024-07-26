# Campus - Integrador - Condicionales

# Ferrete Lámparas:
# En una ferretería se quiere implementar un sistema que permita a los 
# usuarios saber cuánto deberán pagar por la compra de lámparas de bajo 
# consumo. Se tiene en cuenta que todas las lámparas cuestan $800.

# A partir de la cantidad y marca de las lámparas compradas 
# (solo se puede comprar una marca por vez) se aplicará el siguiente descuento:

# ● Si compra 6 o más lámparas bajo consumo tiene un descuento del 50%.

# ● Si compra 5 lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento
# del 40% y si es de otra marca el descuento es del 30%.

# ● Si compra 4 lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se 
# hace un descuento del 25% y si es de otra marca el descuento es del 20%.

# ● Si compra 3 lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 
# 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.

# Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.

# Mostrar por pantalla: 
# Marca, cantidad de lámparas, total a pagar sin descuento, el descuento 
# obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.
cantidad_lamparas = int(input("Ingresá la cantidad de lámparas que vas a comprar: "))
marca = input("Ingresá la marca de las lámparas (ArgentinaLuz/FelipeLamparas o cualquier otra marca): ")
precio_base = 800
descuento = 0
descuento_adicional = 0

if cantidad_lamparas >= 6:
    descuento = 100 - 50

if cantidad_lamparas == 5:
    if marca == "ArgentinaLuz":
        descuento = 100 - 40
    else:
        descuento = 100 - 30

if cantidad_lamparas == 4:
    if marca == "ArgentinaLuz":
        descuento = 100 - 25
    elif marca == "FelipeLamparas":
        descuento = 100 - 20

if cantidad_lamparas == 3:
    if marca == "ArgentinaLuz":
        descuento = 100 - 15
    elif marca == "FelipeLamparas":
        descuento = 100 - 10
    else:
        descuento = 100 - 5



descuento_total = descuento / 100
precio_total = precio_base * cantidad_lamparas
precio_total_descuento = precio_total * descuento_total

if precio_total_descuento > 4000:
    descuento_adicional = 5
    descuento_total = (descuento - descuento_adicional) / 100
    precio_total_descuento = precio_total * descuento_total

print(f"Marca de las lámparas: {marca}")
print(f"Cantidad de lámparas: {cantidad_lamparas}")
print(f"Precio total por las lámparas: ${precio_total}")

descuento_obtenido = 100 - descuento
if descuento != 0 and descuento_adicional == 0:
    print(f"Descuento obtenido: {descuento_obtenido}%")
    print(f"Total a pagar con descuento: ${precio_total_descuento}")
if descuento != 0 and descuento_adicional == 5:
    print(f"Descuento obtenido: {descuento_obtenido}%")
    print(f"Descuento adicional: {descuento_adicional}%")
    print(f"Total a pagar con descuento: ${precio_total_descuento}")