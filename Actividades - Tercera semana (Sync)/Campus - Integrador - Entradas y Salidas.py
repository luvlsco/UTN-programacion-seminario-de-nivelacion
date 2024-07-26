# Campus - Integrador - Entradas y Salidas

# La juguetería "El Mundo de Charly" nos encarga un
# programa para conocer qué cantidad de materiales 
# se necesita para la fabricación de distintos juguetes.

# Medidas:
# AB = Diágonal mayor
# DC = Diágonal menor
# BD y BC = lados menores
# AD y AC = lados mayores

# El usuario ingresará las medidas  BC, CD y AD.

# Detalles de construcción:
# Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico
# y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.

# El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo 
# papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.

# Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción 
# en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.

lado_menor = int(input("Ingresá las medidas (en centímetros) de uno de los lados menores: ")) # (BC/BD)
diagonal_menor = int(input("Ingresá las medidas (en centímetros) de la diagonal menor: ")) # (CD/DC)
lado_mayor = int(input("Ingresá las medidas (en centímetros) de uno de los lados mayores: ")) # (AD/AC)
cometas_pendientes = 10

# Metros de varillas
perimetro_cometa = (lado_menor * 2) + (lado_mayor * 2)
metros_varillas = perimetro_cometa * cometas_pendientes / 100 # 100cm = 1m


# Metros de papel
diagonal_mayor = int(((lado_mayor - lado_menor)**2 + diagonal_menor**2) ** 0.5)
# El usuario no ingresa una diagonal mayor, se usa esta fórmula para obtenerla.

area_cometa = (diagonal_menor * diagonal_mayor) / 2 # Fórmula para obtener el área del cometa.
area_cola = area_cometa * 1.10 # Se agrega un +10% adicional para la cola.
area_total = area_cometa + area_cola # Total de centímetros cuadrados para un cometa.

metros_papel = (area_total * cometas_pendientes) / 10000 # Fórmula de los metros cuadrados necesarios para diez cometas.

print(f"Para la construcción de diez cometas se necesitan {metros_varillas} metros de varillas y {metros_papel} metros cuadrados de papel de alta resistencia.")