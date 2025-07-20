# Solicitar datos al cliente
print("=== SISTEMA DE DESCUENTOS ===")
edad = int(input("Ingrese su edad: "))
monto_compra = float(input("Ingrese el monto total de su compra: $"))

# Aplicar estructura condicional para determinar el descuento
if edad > 60 and monto_compra > 1000:
    descuento = 20
elif 18 <= edad <= 60 and monto_compra > 500:
    descuento = 10
else:
    descuento = 2

# Calcular el monto con descuento
monto_descuento = monto_compra * (descuento / 100)
total_pagar = monto_compra - monto_descuento

# Mostrar resultados
print("\n=== RESUMEN DE COMPRA ===")
print(f"Edad del cliente: {edad} años")
print(f"Monto de compra: ${monto_compra:.2f}")
print(f"Descuento aplicado: {descuento}%")
print(f"Monto descontado: ${monto_descuento:.2f}")
print(f"Total a pagar: ${total_pagar:.2f}")