# EJERCICIO #3
# 1. Crear una lista de 10 nombres
nombres = ["María", "José", "Carlos", "Ana", "Luis", 
           "Laura", "Pedro", "Sofía", "Juan", "Diana"]

# 2. Obtener una sublista del índice 5 al 9 con saltos de 2 en 2
sublista = nombres[5:10:2]  # [5:9] no incluye el 9, por eso usamos 10
# También se puede omitir el 10: nombres[5::2]

# 3. Buscar si "José" está en la lista original
existe_jose = "José" in nombres

# 4. Ordenar la sublista alfabéticamente (A-Z)
sublista_ordenada_az = sorted(sublista)

# 5. Ordenar la lista original alfabéticamente descendente (Z-A)
nombres_ordenados_za = sorted(nombres, reverse=True)

# Mostrar resultados
print("Lista original:", nombres)
print("\nSublista [5:9] con saltos de 2:", sublista)
print("¿Existe 'José' en la lista original?", existe_jose)
print("Sublista ordenada A-Z:", sublista_ordenada_az)
print("Lista original ordenada Z-A:", nombres_ordenados_za)