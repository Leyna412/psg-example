# EJERCICIO #4 - VERSIÓN CORREGIDA

# Listas iniciales
productos = ["Chocolatina Jet", "Bon Bon Bum", "Oreo", "Chizitos", "Gomitas Trululu"]
precios = [1500, 500, 2000, 1200, 800]

print("\n--- PROCESO INICIAL ---")
print("Productos iniciales:", productos)
print("Precios iniciales:", precios)

# 1. Agregar 2 productos nuevos al final de las listas
productos.append("Mentitas")
productos.append("Galletas Festival")
precios.append(600)
precios.append(1800)

print("\n--- PASO 1: Después de agregar 2 productos ---")
print("Productos actualizados:", productos)
print("Precios actualizados:", precios)

# 2. Eliminar el producto "Bon Bon Bum" y su precio
indice_bonbum = productos.index("Bon Bon Bum")
producto_eliminado = productos.pop(indice_bonbum)
precio_eliminado = precios.pop(indice_bonbum)

print("\n--- PASO 2: Después de eliminar 'Bon Bon Bum' ---")
print(f"Se eliminó: {producto_eliminado} (${precio_eliminado})")
print("Productos restantes:", productos)
print("Precios restantes:", precios)

# 3. Obtener precios de "Oreo" y "Chizitos"
indice_oreo = productos.index("Oreo")
indice_chizitos = productos.index("Chizitos")
precio_oreo = precios[indice_oreo]
precio_chizitos = precios[indice_chizitos]

print("\n--- PASO 3: Precios específicos ---")
print(f"Precio de Oreo: ${precio_oreo}")
print(f"Precio de Chizitos: ${precio_chizitos}")

# 4. Encontrar producto más caro y más barato
precio_maximo = max(precios)
precio_minimo = min(precios)
indice_caro = precios.index(precio_maximo)
indice_barato = precios.index(precio_minimo)
producto_caro = productos[indice_caro]
producto_barato = productos[indice_barato]

print("\n--- PASO 4: Productos extremos ---")
print(f"Producto más caro: {producto_caro} (${precio_maximo})")
print(f"Producto más barato: {producto_barato} (${precio_minimo})")

# 5. Calcular cantidad total de productos
total_productos = len(productos)

# 6. Calcular costo total de todos los productos
costo_total = sum(precios)

print("\n--- PASO 5: Totales ---")
print(f"Cantidad total de productos: {total_productos}")
print(f"Costo total de inventario: ${costo_total}")

# 7. Ordenar productos y precios del más barato al más caro
# Primero emparejamos productos con precios y luego ordenamos
productos_con_precios = list(zip(productos, precios))
productos_ordenados = [producto for producto, precio in sorted(productos_con_precios, key=lambda x: x[1])]
precios_ordenados = [precio for producto, precio in sorted(productos_con_precios, key=lambda x: x[1])]

print("\n--- PASO 6: Listas ordenadas ---")
print("Productos ordenados por precio:", productos_ordenados)
print("Precios ordenados:", precios_ordenados)

# 8. Eliminar todos los productos de las listas
productos.clear()
precios.clear()

print("\n--- PASO 7: Después de limpiar las listas ---")
print("Productos finales:", productos)
print("Precios finales:", precios)