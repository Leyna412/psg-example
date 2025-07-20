print("=== CALCULADORA BÁSICA ===")
print("Ingrese la operación en formato: numero1, numero2, operación")
print("Operaciones válidas: + (suma), - (resta), * (multiplicación), / (división)\n")

# Entrada de datos
entrada = input("Operación: ").strip()

try:
    # Procesamiento de la entrada
    partes = [p.strip() for p in entrada.split(',')]
    
    # Validación de estructura básica
    if len(partes) != 3:
        raise ValueError("Formato incorrecto. Debe ser: numero1, numero2, operación")
    
    # Extracción y conversión de valores
    num1 = float(partes[0])
    num2 = float(partes[1])
    operacion = partes[2]
    
    # Realización de operación con estructura condicional
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        resultado = num1 / num2
    else:
        raise ValueError("Operación no válida. Use: +, -, *, /")
    
    # Mostrar resultado
    print("--------------")
    print(f"Resultado: {resultado}")

except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")