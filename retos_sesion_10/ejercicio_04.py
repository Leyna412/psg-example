# EJERCICIO 4 
jane = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
john = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}

# Intersección (qué tienen en común)
comunes = jane & john
print("Postres en común:", comunes)  # {'Lemon Pie', 'Tarta de Manzana'}

# Unión (todos los postres únicos)
todos_postres = jane | john
print("Todos los postres:", todos_postres)  # 7 elementos

# Cálculo de porcentaje
porcentaje = (len(comunes) / len(todos_postres)) * 100

# Comparación
if porcentaje > 50:
    print(f"Resultado: Compatibles ({porcentaje:.0f}% de coincidencia)")
else:
    print(f"Resultado: Deben replantear ({porcentaje:.0f}% de coincidencia)")