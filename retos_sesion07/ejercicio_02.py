# Solicitar entrada del usuario como cadenas
a = input("Ingresa el primer número: ")
b = input("Ingresa el segundo número: ")
c = input("Ingresa el tercer número: ")

# Convertir las cadenas a enteros para realizar la resta
resultado = int(a) - int(b) - int(c)

# Mostrar el resultado como parte de una cadena
print("El resultado de la resta es: " + str(resultado))