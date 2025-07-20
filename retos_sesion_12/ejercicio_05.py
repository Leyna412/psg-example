# Lista para almacenar contactos
lista_contactos = []

print("=== APLICACIÓN DE CONTACTOS ===")

# Ingreso de datos (flujo secuencial)
nombre = input("Ingrese el nombre del contacto: ").strip()
telefono = input("Ingrese el número de teléfono (11 dígitos con código de país): ").strip()

# Validaciones usando condicionales
if (nombre and  # Truthiness: nombre no vacío
    telefono.isdigit() and  # Solo dígitos
    len(telefono) == 11):  # Exactamente 11 caracteres
    
    # Guardar contacto si es válido
    lista_contactos.append({"nombre": nombre, "telefono": telefono})
    print("✅ Contacto guardado exitosamente")
else:
    print("❌ Datos incorrectos. Verifique:")
    if not nombre:
        print("- El nombre no puede estar vacío")
    if not telefono.isdigit():
        print("- El teléfono debe contener solo números")
    if len(telefono) != 11:
        print("- El teléfono debe tener exactamente 11 dígitos")

# Mostrar lista de contactos actual
print("\n=== LISTA DE CONTACTOS ===")
if lista_contactos:  # Truthiness: lista no vacía
    for contacto in lista_contactos:
        print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
else:
    print("No hay contactos registrados")