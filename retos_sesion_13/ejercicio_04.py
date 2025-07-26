# Estructura de control SECUENCIAL (inicio del programa)
print("Verificador de Palíndromos")
print("Ingrese una frase o escriba 'salir' para terminar")

# Estructura de control REPETITIVA (ciclo infinito)
while True:
    # Entrada de datos (estructura SECUENCIAL)
    frase = input("\nFrase: ").strip().lower()  # Convierte a minúsculas y elimina espacios
    
    # Estructura de control SELECTIVA (condicional para salir)
    if "salir" in frase:
        print("Programa terminado.")
        break  # Rompe el ciclo
    
    # Procesamiento para verificar palíndromo
    frase_limpia = ""
    # Estructura REPETITIVA (for para filtrar letras)
    for letra in frase:
        if letra.isalpha():  # Solo considera letras (ignora espacios, números y símbolos)
            frase_limpia += letra
    
    # Estructura SELECTIVA (verifica si es palíndromo)
    if frase_limpia == frase_limpia[::-1]:  # Compara la cadena original con su inversa
        print(f"'{frase}' **SÍ** es un palíndromo")
    else:
        print(f"'{frase}' **NO** es un palíndromo")