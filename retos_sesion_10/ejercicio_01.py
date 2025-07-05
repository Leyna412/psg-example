# Ejercicio #1

cadena = "📎📐📏✏️🖊️🖋️📎📌📏📇🗂️📁📌🗃️✏️📂🖇️"
print(cadena)

# Convertir la cadena en un conjunto para eliminar duplicados
elementos_unicos = set(cadena)

# Volver a unir los elementos en una cadena (sin orden específico)
cadena_sin_repetir = "".join(elementos_unicos)

print(cadena_sin_repetir)