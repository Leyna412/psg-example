# Tupla con las notas del estudiante
notas = (10, 61, 0, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)

# Calcular el promedio usando sum() y len()
promedio = sum(notas) / len(notas)

# Determinar si aprobó (promedio >= 51)
aprobado = promedio >= 51

# Imprimir resultados
print(f"Notas del semestre: {notas}")
print(f"Promedio: {promedio:.2f}")  # Mostramos con 2 decimales
print(f"¿Aprobó el semestre? {'Sí' if aprobado else 'No'}")