def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    
    Parámetros:
    calificaciones (list): Lista de números representando calificaciones
    
    Retorna:
    float: El promedio de las calificaciones
    """
    if not calificaciones:  # Si la lista está vacía
        return 0
    return sum(calificaciones) / len(calificaciones)

# Lista de calificaciones proporcionada
calificaciones = [50, 75, 80, 91, 70]

# Llamar a la función e imprimir el resultado
promedio = calcular_promedio(calificaciones)
print(f"El promedio de las calificaciones es: {promedio}")