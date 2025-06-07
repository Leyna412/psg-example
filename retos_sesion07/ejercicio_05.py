# Solicitar la cadena al usuario
texto = input("Ingresa una frase o palabra: ")

# Convertir a minúsculas y eliminar espacios
limpio = texto.lower().replace(" ", "")

# Invertir la cadena
invertido = limpio[::-1]

# Comparar si es igual al revés
es_palindromo = limpio == invertido

# Mostrar resultado
print("¿Es palíndromo?", es_palindromo)