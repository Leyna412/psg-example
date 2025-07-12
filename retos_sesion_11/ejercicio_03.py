# Ejercicio 3
# 1. Crear el diccionario a partir de la tupla
animales = dict((('canino', '🐶'), ('felino', '🐱'), ('aves', ['🐦', '🦅'])))

# 2. Obtener y eliminar el valor de 'aves'
aves_valor = animales.pop('aves')

# 3. Modificar el valor de 'felino' por '🐈'
animales['felino'] = '🐈'

# 4. Cambiar la clave 'canino' por 'caninos' y su valor por ['🐶', '🐕']
animales['caninos'] = ['🐶', '🐕']
del animales['canino']

# Resultados
print("Diccionario final:", animales)
print("Valor eliminado de 'aves':", aves_valor)