# EJERCICIO #4

# Listas iniciales
productos = ["Chocolatina Jet", "Bon Bon Bum", "Oreo", "Chizitos", "Gomitas Trululu"]
precios = [1500, 500, 2000, 1200, 800]

# 1. Agregar 2 productos nuevos al final de las listas
productos.append("Mentitas")
productos.append("Galletas Festival")
precios.append(600)
precios.append(1800)

# 2. Eliminar el producto "Bon Bon Bum" y su precio
indice = productos.index("Bon Bon Bum")
productos.pop(indice)
precios.pop(indice)

# 3. Precio de "Oreo" y "Chizitos"
precio_oreo = precios[productos.index("Oreo")]
precio_chizitos = precios[productos.index("Chizitos")]

# 4. Producto más caro y más barato
producto_mas_caro = productos[precios.index(max(precios))]
producto_mas_barato = productos[precios.index(min(precios))]

# 5. Cantidad total de productos
total_productos = len(productos)

# 6. Costo total de todos los productos
costo_total = sum(precios)

# 7. Ordenar productos y precios del más barato al más caro
productos_ordenados = [x for _, x in sorted(zip(precios, productos))]
precios_ordenados = sorted(precios)

# 8. Eliminar todos los productos de las listas
productos.clear()
precios.clear()

# Mostrar resultados
print("Operaciones completadas:")
print("\n1. Después de agregar y eliminar:")
print("Productos:", productos)
print("Precios:", precios)

print("\n2. Precios específicos:")
print(f"Oreo cuesta: ${precio_oreo}")
print(f"Chizitos cuesta: ${precio_chizitos}")

print("\n3. Productos extremos:")
print(f"Producto más caro: {producto_mas_caro} (${max(precios)})")
print(f"Producto más barato: {producto_mas_barato} (${min(precios)})")

print("\n4. Totales:")
print(f"Total de productos: {total_productos}")
print(f"Costo total de todos los productos: ${costo_total}")

print("\n5. Listas ordenadas (barato a caro):")
print("Productos ordenados:", productos_ordenados)
print("Precios ordenados:", precios_ordenados)

print("\n6. Después de eliminar todo:")
print("Productos:", productos)
print("Precios:", precios)