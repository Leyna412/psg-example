# Ejercicio 2
# Listas originales
deportiva = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
formal = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

print(deportiva)
print(formal)

# Convertir a conjuntos
prendas_deportivas = set(deportiva)
prendas_formales = set(formal)

# Aplicar operador |= (unión y asignación)
prendas_deportivas |= prendas_formales  # Equivalente a prendas_deportivas = prendas_deportivas | prendas_formales

print("Prendas combinadas:", prendas_deportivas)