# Ejercicio 1
# Solicitar al usuario un número entero
numero = int(input("Ingrese un número entero: "))

# Verificar si es múltiplo de 5 usando operador ternario
resultado = "es múltiplo de 5" if numero % 5 == 0 else "no es múltiplo de 5"

# Mostrar el resultado
print(f"El número {numero} {resultado}")