estudiantes = [('Miguel', 51), ('Daniel', 80), ('Virginia', 90), ('Franco', 40), ('Flabio', 30)]

print("Felicitaciones a los siguientes estudiantes por aprobar el curso:")

for nombre, nota in estudiantes:
    if nota >= 51:
        print(f"¡Felicidades {nombre}! Has aprobado con {nota} puntos.")
    else:
        print(f"Lo siento {nombre}, no has aprobado. Tu nota fue {nota}.")
        