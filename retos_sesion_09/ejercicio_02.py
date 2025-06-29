# EJERCICIO #2

lista_original = [5, 4, 3, 2, 2, 2, 0, 0, 1, 2]

# 1. Invertimos la lista
lista_invertida = lista_original[::-1]  # [2, 1, 0, 0, 2, 2, 2, 3, 4, 5]

# 2. Tomamos elementos cada 3 posiciones
sublista_saltos_3 = lista_invertida[::3]  # [2, 0, 2, 4]

print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)
print("Sublista inversa con saltos de 3:", sublista_saltos_3)