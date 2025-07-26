print("Verificador de múltiplos de 7 (Ingrese 0 para salir)")

while True:  # Ciclo infinito
    # Entrada de datos
    numero = input("\nIngrese un número entero: ")
    
    # Verificar si es un número válido
    if not numero.lstrip('-').isdigit():
        print("Error: Debe ingresar un número entero válido")
        continue
    
    numero = int(numero)
    
    # Condición de salida
    if numero == 0:
        print("Programa terminado.")
        break
    
    # Verificar si es múltiplo de 7
    if numero % 7 == 0:
        print(f"El número {numero} SÍ es múltiplo de 7")
    else:
        print(f"El número {numero} NO es múltiplo de 7")