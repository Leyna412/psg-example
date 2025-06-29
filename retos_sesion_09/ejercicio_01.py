# EJERCICIO #1

# Crear la lista con los elementos
lista_mixta = [3.14, 2.71, 1.618, 0.577, 1.414,  # 5 flotantes
               42, 7, 100, 256, 1024]            # 5 enteros

# Mostrar todos los elementos con sus tipos usando índices
print("Elementos de la lista y sus tipos:")
for i in range(len(lista_mixta)):
    elemento = lista_mixta[i]
    tipo = type(elemento).__name__
    print(f"Índice {i}: {elemento} - Tipo: {tipo}")