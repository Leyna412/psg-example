# Tamaño del tablero
tamaño = 8

# Imprimir el tablero de ajedrez
for fila in range(tamaño):
    for columna in range(tamaño):
        if (fila + columna) % 2 == 0:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()  # Salto de línea al final de cada fila