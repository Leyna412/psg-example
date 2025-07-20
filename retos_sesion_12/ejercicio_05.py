# Lista para almacenar contactos válidos
contactos = []

def validar_contacto(nombre, telefono):
    """Función para validar los datos del contacto"""
    # Validar nombre (no vacío y solo letras y espacios)
    if not nombre or not nombre.replace(" ", "").isalpha():
        return False
    
    # Validar teléfono (exactamente 11 dígitos)
    if not telefono.isdigit() or len(telefono) != 11:
        return False
    
    return True

# Interfaz de usuario
print("=== GESTIÓN DE CONTACTOS ===")
while True:
    print("\n1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    # Estructura de control para manejar las opciones
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ").strip()
        telefono = input("Ingrese el teléfono (11 dígitos con código de país): ").strip()
        
        if validar_contacto(nombre, telefono):
            contactos.append({"nombre": nombre, "telefono": telefono})
            print("✅ Contacto guardado correctamente")
        else:
            print("❌ Datos incorrectos. El nombre debe contener solo letras y el teléfono 11 dígitos")
    
    elif opcion == "2":
        print("\n=== LISTA DE CONTACTOS ===")
        if not contactos:
            print("No hay contactos guardados")
        else:
            for i, contacto in enumerate(contactos, 1):
                print(f"{i}. {contacto['nombre']}: {contacto['telefono']}")
    
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Por favor seleccione 1, 2 o 3")