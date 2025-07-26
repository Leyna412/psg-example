# Programa para imprimir los primeros 20 números de la sucesión de Lucas

# Inicializamos los primeros dos términos
a, b = 2, 1

print("Los primeros 20 números de la sucesión de Lucas son:")

# Usamos un bucle for para iterar 20 veces
for i in range(20):
    print(a, end=" ")
    # Calculamos el siguiente término
    a, b = b, a + b